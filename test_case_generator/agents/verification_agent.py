"""
Verification Agent - Adds state verification to positive test cases

This agent:
1. Extracts state categories dynamically from functional description (GENERIC!)
2. Analyzes positive test cases to identify state changes (reads_state, writes_state)
3. Links tests that can verify each other's results
4. Generates pre/post verification steps for tests that modify state
5. Creates new state check tests if no existing test can verify a state change
"""

from typing import List, Dict, Set, Tuple, Optional
from .base import BaseAgent
from ..models.schemas import TestCase, ParsedFunctionalDescription


class VerificationAgent(BaseAgent):
    """Agent responsible for adding verification capabilities to test cases"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_categories: List[str] = []  # Dynamically extracted from functional description
        self.state_descriptions: Dict[str, str] = {}  # Category name -> description

    @property
    def name(self) -> str:
        return "Verification Agent"

    @property
    def system_prompt(self) -> str:
        return """You are an expert test analyst specializing in state verification for web application testing.

Your task is to analyze test cases and identify:
1. What application state each test READS (displays, shows, checks)
2. What application state each test WRITES (modifies, creates, deletes, updates)

Rules:
- A test that displays/views data READS state
- A test that creates/updates/deletes data WRITES state
- Login tests typically WRITE session/authentication state
- Many tests can both READ and WRITE state
- Be specific about which state categories apply
- Only include state that is directly affected by the test

Return JSON only."""

    def extract_state_categories(self, parsed_desc: ParsedFunctionalDescription) -> None:
        """
        Extract state categories dynamically from the parsed functional description.
        Uses the structured, summarized data (not the raw description).

        Args:
            parsed_desc: Parsed functional description with modules
        """
        print("    - Extracting state categories from application description...")

        # Build a concise summary from parsed modules
        module_summaries = []
        for module in parsed_desc.modules:
            summary = {
                "title": module.title,
                "items": module.mentioned_items[:10],  # Limit to top 10 items
                "workflows": module.workflows[:5],      # Limit to top 5 workflows
                "rules": module.business_rules[:5]      # Limit to top 5 rules
            }
            module_summaries.append(summary)

        # Use LLM to extract state categories from summaries
        prompt = f"""Analyze this web application and identify the key STATE CATEGORIES that can be modified or read.

Application: {parsed_desc.project_name}

Modules Summary:
{self._format_modules_for_state_extraction(module_summaries)}

Extract state categories that represent DATA that can be:
- Created, updated, deleted, or modified (WRITE operations)
- Viewed, displayed, or checked (READ operations)

Examples of state categories:
- For e-commerce: product_catalog, shopping_cart, order_status, user_profile, wishlist, inventory
- For banking: account_balance, transaction_history, loan_status, payee_list, session_status
- For social media: user_profile, posts, comments, followers, notifications, messages
- For CRM: customer_records, sales_pipeline, contact_list, activity_log

Return JSON in this format:
{{
    "state_categories": [
        {{
            "name": "snake_case_name",
            "description": "Brief description of what this state represents"
        }},
        ...
    ]
}}

Rules:
- Use snake_case for names
- Keep it to 5-15 categories (most important ones)
- Focus on DATA that changes or is displayed
- Ignore UI actions (clicks, navigation)
- Include session/authentication state if login exists"""

        try:
            result = self.call_llm_json(prompt, temperature=0.3)
            categories = result.get("state_categories", [])

            for cat in categories:
                name = cat.get("name", "")
                desc = cat.get("description", "")
                if name:
                    self.state_categories.append(name)
                    self.state_descriptions[name] = desc

            print(f"    - Extracted {len(self.state_categories)} state categories: {', '.join(self.state_categories)}")

        except Exception as e:
            print(f"    - Warning: Failed to extract state categories: {e}")
            # Fallback: use generic categories
            self.state_categories = [
                "user_profile", "session_status", "data_records",
                "form_submissions", "notifications"
            ]
            print(f"    - Using fallback state categories: {', '.join(self.state_categories)}")

    def _format_modules_for_state_extraction(self, module_summaries: List[Dict]) -> str:
        """Format module summaries for LLM prompt"""
        lines = []
        for ms in module_summaries:
            lines.append(f"• {ms['title']}")
            if ms['items']:
                lines.append(f"  Items: {', '.join(ms['items'][:5])}")
            if ms['workflows']:
                lines.append(f"  Workflows: {', '.join(ms['workflows'][:3])}")
        return "\n".join(lines)

    def run(
        self,
        test_cases: List[TestCase],
        parsed_desc: Optional[ParsedFunctionalDescription] = None
    ) -> List[TestCase]:
        """
        Process all test cases and add verification information to positive tests.

        Args:
            test_cases: List of test cases from TestGenerationAgent
            parsed_desc: Optional parsed functional description for extracting state categories

        Returns:
            List of test cases with verification information added to positive tests
        """
        # Separate positive tests (need verification) from others
        positive_tests = [tc for tc in test_cases if tc.test_type == "positive"]
        other_tests = [tc for tc in test_cases if tc.test_type != "positive"]

        if not positive_tests:
            print("    - No positive tests to process for verification")
            return test_cases

        print(f"    - Processing {len(positive_tests)} positive tests for verification")

        # Extract state categories if not already done
        if not self.state_categories and parsed_desc:
            self.extract_state_categories(parsed_desc)
        elif not self.state_categories:
            print("    - Warning: No state categories available, using generic fallback")
            self.state_categories = ["user_data", "session_status", "application_state"]

        # Step 1: Tag all positive tests with state information
        tagged_tests = self._tag_state_for_tests(positive_tests)

        # Step 2: Link tests that can verify each other
        linked_tests = self._link_verification_tests(tagged_tests)

        # Step 3: Generate pre/post verification steps
        verified_tests = self._generate_verification_steps(linked_tests)

        # Step 4: Generate missing state check tests if needed
        new_tests = self._generate_missing_state_checks(verified_tests, other_tests)

        # Combine all tests
        all_tests = verified_tests + other_tests + new_tests

        return all_tests

    def _tag_state_for_tests(self, tests: List[TestCase]) -> List[TestCase]:
        """Tag each test with reads_state and writes_state using LLM"""

        # Batch tests by module for efficiency
        module_tests: Dict[int, List[TestCase]] = {}
        for tc in tests:
            if tc.module_id not in module_tests:
                module_tests[tc.module_id] = []
            module_tests[tc.module_id].append(tc)

        # Process each module's tests
        for module_id, module_test_list in module_tests.items():
            self._tag_module_tests(module_test_list)

        return tests

    def _tag_module_tests(self, tests: List[TestCase]) -> None:
        """Tag tests for a single module using LLM"""

        if not tests:
            return

        # Build test info for LLM
        test_info = []
        for i, tc in enumerate(tests):
            test_info.append({
                "index": i,
                "title": tc.title,
                "workflow": tc.workflow,
                "steps": tc.steps,
                "expected_result": tc.expected_result
            })

        # Build state categories description
        state_cat_desc = []
        for cat in self.state_categories:
            desc = self.state_descriptions.get(cat, "")
            if desc:
                state_cat_desc.append(f"- {cat}: {desc}")
            else:
                state_cat_desc.append(f"- {cat}")
        state_categories_text = "\n".join(state_cat_desc)

        prompt = f"""Analyze these positive test cases from the "{tests[0].module_title}" module and identify what state each test reads and writes.

Tests:
{self._format_tests_for_prompt(test_info)}

For each test, return:
- reads_state: list of state categories this test READS/DISPLAYS/CHECKS
- writes_state: list of state categories this test MODIFIES/CREATES/UPDATES

Available state categories for this application:
{state_categories_text}

Return JSON in this format:
{{
    "tests": [
        {{
            "index": 0,
            "reads_state": ["category1", "category2"],
            "writes_state": ["category3"]
        }},
        ...
    ]
}}

Rules:
- Empty lists are valid if test doesn't read or write any state
- Login tests typically write session/authentication state
- Viewing/displaying data means the test READS that state
- Creating/updating/deleting data means the test WRITES that state
- A test can both READ and WRITE the same state (e.g., update profile reads current values, writes new ones)"""

        try:
            result = self.call_llm_json(prompt, temperature=0.2)
            tagged = result.get("tests", [])

            for item in tagged:
                idx = item.get("index", -1)
                if 0 <= idx < len(tests):
                    tests[idx].reads_state = item.get("reads_state", [])
                    tests[idx].writes_state = item.get("writes_state", [])

        except Exception as e:
            print(f"    - Warning: Failed to tag tests for {tests[0].module_title}: {e}")
            # Fallback: use keyword-based tagging
            for tc in tests:
                tc.reads_state, tc.writes_state = self._keyword_based_tagging(tc)

    def _format_tests_for_prompt(self, test_info: List[Dict]) -> str:
        """Format test info for LLM prompt"""
        lines = []
        for t in test_info:
            lines.append(f"[{t['index']}] {t['title']}")
            lines.append(f"    Workflow: {t['workflow']}")
            lines.append(f"    Steps: {', '.join(t['steps'][:3])}...")
            lines.append(f"    Expected: {t['expected_result']}")
            lines.append("")
        return "\n".join(lines)

    def _keyword_based_tagging(self, tc: TestCase) -> Tuple[List[str], List[str]]:
        """Fallback keyword-based state tagging using extracted state categories"""
        reads = []
        writes = []

        title_lower = tc.title.lower()
        steps_text = " ".join(tc.steps).lower()
        combined = title_lower + " " + steps_text

        # Match extracted state categories using keywords
        for state_cat in self.state_categories:
            # Split state category name into keywords (e.g., "account_balance" -> ["account", "balance"])
            keywords = state_cat.split("_")

            # Check if any keyword appears in the test
            if any(kw in combined for kw in keywords):
                # Determine if it's read or write based on action verbs
                if any(verb in combined for verb in ["view", "check", "display", "show", "see", "get", "list", "find"]):
                    reads.append(state_cat)
                if any(verb in combined for verb in ["create", "update", "edit", "change", "modify", "add", "delete", "remove", "submit", "transfer", "pay", "request"]):
                    writes.append(state_cat)

        # Special handling for session/authentication
        if any(w in combined for w in ["login", "log in", "sign in", "authenticate", "logout", "log out"]):
            # Find session-related state
            session_states = [s for s in self.state_categories if "session" in s or "auth" in s or "login" in s]
            if session_states:
                writes.append(session_states[0])
            else:
                writes.append("session_status")  # Fallback

        # Remove duplicates
        reads = list(set(reads))
        writes = list(set(writes))

        return reads, writes

    def _link_verification_tests(self, tests: List[TestCase]) -> List[TestCase]:
        """Link tests that can verify each other's state changes"""

        # Build index of tests by what state they read
        readers_by_state: Dict[str, List[TestCase]] = {}
        for tc in tests:
            for state in tc.reads_state:
                if state not in readers_by_state:
                    readers_by_state[state] = []
                readers_by_state[state].append(tc)

        # For each test that writes state, find tests that read that state
        for tc in tests:
            if not tc.writes_state:
                continue

            verification_ids = set()
            for state in tc.writes_state:
                if state in readers_by_state:
                    for reader_tc in readers_by_state[state]:
                        # Don't link to self
                        if reader_tc != tc:
                            # Use title as temporary ID (actual ID assigned later by assembler)
                            verification_ids.add(reader_tc.title)

            tc.verification_test_ids = list(verification_ids)

        return tests

    def _generate_verification_steps(self, tests: List[TestCase]) -> List[TestCase]:
        """Generate pre/post verification steps for tests that write state"""

        # Only process tests that write state
        state_changing_tests = [tc for tc in tests if tc.writes_state]

        if not state_changing_tests:
            return tests

        # Batch by module for efficiency
        module_tests: Dict[int, List[TestCase]] = {}
        for tc in state_changing_tests:
            if tc.module_id not in module_tests:
                module_tests[tc.module_id] = []
            module_tests[tc.module_id].append(tc)

        for module_id, module_test_list in module_tests.items():
            self._generate_steps_for_module(module_test_list)

        return tests

    def _generate_steps_for_module(self, tests: List[TestCase]) -> None:
        """Generate verification steps for tests in a module"""

        test_info = []
        for i, tc in enumerate(tests):
            test_info.append({
                "index": i,
                "title": tc.title,
                "steps": tc.steps,
                "writes_state": tc.writes_state,
                "expected_result": tc.expected_result
            })

        prompt = f"""Generate pre-verification and post-verification steps for these state-changing tests.

Tests:
{self._format_state_tests_for_prompt(test_info)}

For each test, generate:
- pre_verification_steps: Steps to capture/verify the INITIAL state BEFORE the test action
- post_verification_steps: Steps to verify the EXPECTED state change AFTER the test action

Examples:
- For a "Transfer $100" test that writes account_balance:
  pre_verification: ["Navigate to Accounts Overview", "Note source account balance", "Note destination account balance"]
  post_verification: ["Navigate to Accounts Overview", "Verify source balance decreased by $100", "Verify destination balance increased by $100"]

- For an "Update Profile" test that writes user_profile:
  pre_verification: ["Navigate to Profile page", "Note current profile values"]
  post_verification: ["Navigate to Profile page", "Verify profile shows updated values"]

Return JSON:
{{
    "tests": [
        {{
            "index": 0,
            "pre_verification_steps": ["step1", "step2"],
            "post_verification_steps": ["step1", "step2"]
        }},
        ...
    ]
}}

Rules:
- Keep steps concise and actionable
- Include navigation to verification page if needed
- Pre-steps should capture initial state values
- Post-steps should verify the expected change occurred
- Match the specific state being modified"""

        try:
            result = self.call_llm_json(prompt, temperature=0.3)
            verified = result.get("tests", [])

            for item in verified:
                idx = item.get("index", -1)
                if 0 <= idx < len(tests):
                    tests[idx].pre_verification_steps = item.get("pre_verification_steps", [])
                    tests[idx].post_verification_steps = item.get("post_verification_steps", [])

        except Exception as e:
            print(f"    - Warning: Failed to generate verification steps: {e}")
            # Fallback: generate generic steps
            for tc in tests:
                tc.pre_verification_steps = self._generate_generic_pre_steps(tc)
                tc.post_verification_steps = self._generate_generic_post_steps(tc)

    def _format_state_tests_for_prompt(self, test_info: List[Dict]) -> str:
        """Format state-changing tests for prompt"""
        lines = []
        for t in test_info:
            lines.append(f"[{t['index']}] {t['title']}")
            lines.append(f"    Modifies: {', '.join(t['writes_state'])}")
            lines.append(f"    Steps: {', '.join(t['steps'][:3])}...")
            lines.append(f"    Expected: {t['expected_result']}")
            lines.append("")
        return "\n".join(lines)

    def _generate_generic_pre_steps(self, tc: TestCase) -> List[str]:
        """Generate generic pre-verification steps based on state"""
        steps = []
        for state in tc.writes_state:
            if state == "account_balance":
                steps.extend(["Navigate to Accounts Overview", "Note current account balance(s)"])
            elif state == "user_profile":
                steps.extend(["Navigate to Profile/Settings", "Note current profile values"])
            elif state == "transaction_history":
                steps.extend(["Navigate to Transaction History", "Note current transaction count"])
            elif state == "session_status":
                steps.extend(["Verify user is logged out initially"])
            elif state == "loan_status":
                steps.extend(["Navigate to Loan section", "Note current loan status"])
            elif state == "account_list":
                steps.extend(["Navigate to Accounts Overview", "Note current number of accounts"])
            elif state == "payee_list":
                steps.extend(["Navigate to Payees section", "Note current payee list"])
        return steps if steps else ["Note initial application state"]

    def _generate_generic_post_steps(self, tc: TestCase) -> List[str]:
        """Generate generic post-verification steps based on state"""
        steps = []
        for state in tc.writes_state:
            if state == "account_balance":
                steps.extend(["Navigate to Accounts Overview", "Verify balance reflects the change"])
            elif state == "user_profile":
                steps.extend(["Navigate to Profile/Settings", "Verify updated values are displayed"])
            elif state == "transaction_history":
                steps.extend(["Navigate to Transaction History", "Verify new transaction appears"])
            elif state == "session_status":
                steps.extend(["Verify user session state changed as expected"])
            elif state == "loan_status":
                steps.extend(["Navigate to Loan section", "Verify loan status updated"])
            elif state == "account_list":
                steps.extend(["Navigate to Accounts Overview", "Verify account list updated"])
            elif state == "payee_list":
                steps.extend(["Navigate to Payees section", "Verify payee list updated"])
        return steps if steps else ["Verify application state changed as expected"]

    def _generate_missing_state_checks(
        self,
        positive_tests: List[TestCase],
        other_tests: List[TestCase]
    ) -> List[TestCase]:
        """Generate new state check tests for state changes that have no verifier"""

        # Collect all states written and all states read
        all_writes: Set[str] = set()
        all_reads: Set[str] = set()

        for tc in positive_tests:
            all_writes.update(tc.writes_state)
            all_reads.update(tc.reads_state)

        # Find states that are written but never read (no verification test exists)
        unverified_states = all_writes - all_reads

        if not unverified_states:
            return []

        print(f"    - Found {len(unverified_states)} states without verification tests: {unverified_states}")

        # Generate state check tests for unverified states
        new_tests = []
        for state in unverified_states:
            # Find a test that writes this state to get module info
            writer_test = next((tc for tc in positive_tests if state in tc.writes_state), None)
            if not writer_test:
                continue

            new_test = self._generate_state_check_test(state, writer_test)
            if new_test:
                new_tests.append(new_test)

        return new_tests

    def _generate_state_check_test(self, state: str, reference_test: TestCase) -> TestCase:
        """Generate a state check test for a specific state"""

        # Build test info based on state
        state_titles = {
            "account_balance": "View Account Balance",
            "user_profile": "View User Profile",
            "transaction_history": "View Transaction History",
            "loan_status": "View Loan Status",
            "account_list": "View Account List",
            "payee_list": "View Payee List",
            "bill_payment_status": "View Bill Payment Status",
            "notification_settings": "View Notification Settings",
            "password_status": "View Security Settings",
            "contact_info": "View Contact Information",
        }

        title = state_titles.get(state, f"View {state.replace('_', ' ').title()}")

        # Generate basic steps
        steps = [
            f"Navigate to the {state.replace('_', ' ')} section",
            f"Verify {state.replace('_', ' ')} is displayed correctly",
            "Note the current values for verification purposes"
        ]

        return TestCase(
            id="",  # Will be assigned by assembler
            title=title,
            module_id=reference_test.module_id,
            module_title=reference_test.module_title,
            workflow=f"State verification for {state.replace('_', ' ')}",
            test_type="positive",
            priority="Medium",
            preconditions="User is logged in",
            steps=steps,
            expected_result=f"The {state.replace('_', ' ')} is displayed with correct current values",
            reads_state=[state],
            writes_state=[],
            verification_test_ids=[],
            pre_verification_steps=[],
            post_verification_steps=[]
        )

    def update_verification_ids(self, test_cases: List[TestCase]) -> List[TestCase]:
        """
        Update verification_test_ids from titles to actual test IDs.
        Should be called after AssemblerAgent assigns IDs.
        """
        # Build title to ID mapping
        title_to_id: Dict[str, str] = {}
        for tc in test_cases:
            title_to_id[tc.title] = tc.id

        # Update verification_test_ids
        for tc in test_cases:
            if tc.verification_test_ids:
                updated_ids = []
                for title_or_id in tc.verification_test_ids:
                    if title_or_id in title_to_id:
                        updated_ids.append(title_to_id[title_or_id])
                    else:
                        # Already an ID or not found
                        updated_ids.append(title_or_id)
                tc.verification_test_ids = updated_ids

        return test_cases

    def get_verification_summary(self, test_cases: List[TestCase]) -> Dict:
        """Generate verification coverage summary"""

        positive_tests = [tc for tc in test_cases if tc.test_type == "positive"]

        total_positive = len(positive_tests)
        tests_with_writes = len([tc for tc in positive_tests if tc.writes_state])
        tests_with_reads = len([tc for tc in positive_tests if tc.reads_state])
        tests_with_verification = len([tc for tc in positive_tests if tc.verification_test_ids])
        tests_with_pre_steps = len([tc for tc in positive_tests if tc.pre_verification_steps])
        tests_with_post_steps = len([tc for tc in positive_tests if tc.post_verification_steps])

        # Collect all unique states
        all_writes = set()
        all_reads = set()
        for tc in positive_tests:
            all_writes.update(tc.writes_state)
            all_reads.update(tc.reads_state)

        return {
            "total_positive_tests": total_positive,
            "tests_that_write_state": tests_with_writes,
            "tests_that_read_state": tests_with_reads,
            "tests_with_verification_links": tests_with_verification,
            "tests_with_pre_verification_steps": tests_with_pre_steps,
            "tests_with_post_verification_steps": tests_with_post_steps,
            "unique_states_written": list(all_writes),
            "unique_states_read": list(all_reads),
            "unverified_states": list(all_writes - all_reads)
        }
