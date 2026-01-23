from typing import List, Dict

from .base import BaseAgent
from ..models.schemas import TestCase, ModuleSummary


class VerificationFlagAgent(BaseAgent):
    """Agent responsible for flagging test cases that need post-verification"""

    @property
    def name(self) -> str:
        return "Verification Flag Agent"

    @property
    def system_prompt(self) -> str:
        return """You are an expert QA engineer who understands when test results need external verification.

Your task is to analyze test cases and determine which ones need post-verification - 
meaning the test's success should be verified by checking data in another part of the application.

NEEDS POST-VERIFICATION (needs_post_verification = true):
- Data creation: Verify new records appear in list/overview pages
- Data modification: Verify changes are reflected in display pages
- Data transfer/movement: Verify data moved from source to destination
- Submissions: Verify submission appears in history/status pages
- Any action that modifies persistent data viewable elsewhere

DOES NOT NEED POST-VERIFICATION (needs_post_verification = false):
- Login/Logout: Session state, no persistent data change
- Registration: Self-contained, success message is enough
- Read-only pages: Just displaying data, nothing to verify elsewhere
- Negative tests: Validation failures, no state change
- Edge case tests: Usually testing boundaries, not state changes
- Navigation: Just moving between pages
- Password reset requests: External verification (email), out of scope
- Search/Filter: Just filtering displayed data, no state change"""

    def run(
        self, 
        test_cases: List[TestCase], 
        module_summaries: Dict[int, ModuleSummary]
    ) -> List[TestCase]:
        """Flag test cases that need post-verification"""
        
        # Only process positive test cases - negative and edge cases don't need verification
        positive_tests = [tc for tc in test_cases if tc.test_type == "positive"]
        other_tests = [tc for tc in test_cases if tc.test_type != "positive"]
        
        if not positive_tests:
            return test_cases
        
        # Build context about modules for the LLM
        modules_context = self._build_modules_context(module_summaries)
        
        # Build test cases for analysis
        tests_for_analysis = []
        for tc in positive_tests:
            tests_for_analysis.append({
                "id": tc.id,
                "title": tc.title,
                "module": tc.module_title,
                "workflow": tc.workflow,
                "steps": tc.steps[:5],  # First 5 steps for context
                "expected_result": tc.expected_result
            })
        
        prompt = f"""Analyze these POSITIVE test cases and determine which ones need post-verification.

AVAILABLE MODULES AND THEIR CAPABILITIES:
{modules_context}

TEST CASES TO ANALYZE:
{self._format_tests(tests_for_analysis)}

For each test case, determine:
1. needs_post_verification: true/false
2. modifies_state: List of states this test modifies (use the state names from module summaries)

Return JSON:
{{
    "flagged_tests": [
        {{
            "test_id": "ACTION-001",
            "needs_post_verification": true,
            "modifies_state": ["relevant_state_name"],
            "reason": "This action modifies data which can be verified in another module"
        }},
        {{
            "test_id": "LOGIN-001",
            "needs_post_verification": false,
            "modifies_state": ["session_status"],
            "reason": "Login only affects session state, no persistent data to verify elsewhere"
        }}
    ]
}}

RULES:
1. Only flag tests that MODIFY data which can be VERIFIED in ANOTHER module
2. If a test modifies data but there's no way to verify it elsewhere, still flag it (we'll handle missing coverage later)
3. Read-only tests should NEVER be flagged
4. Login/logout/registration/password-reset should NOT be flagged
5. Include ALL test cases in the output
6. Use state names that match those defined in the module summaries"""

        try:
            result = self.call_llm_json(prompt, max_tokens=4000)
            
            # Create lookup for flagged tests
            flags = {item["test_id"]: item for item in result.get("flagged_tests", [])}
            
            # Update test cases with flags
            for tc in positive_tests:
                if tc.id in flags:
                    flag_data = flags[tc.id]
                    tc.needs_post_verification = flag_data.get("needs_post_verification", False)
                    tc.modifies_state = flag_data.get("modifies_state", [])
            
            # Combine back with other tests
            return positive_tests + other_tests
            
        except Exception as e:
            print(f"Warning: Verification flagging failed: {e}")
            return test_cases

    def _build_modules_context(self, module_summaries: Dict[int, ModuleSummary]) -> str:
        """Build a context string describing all modules"""
        lines = []
        for summary in module_summaries.values():
            lines.append(f"- {summary.module_title}:")
            lines.append(f"    Summary: {summary.summary}")
            if summary.can_verify_states:
                lines.append(f"    Can verify: {', '.join(summary.can_verify_states)}")
            if summary.action_states:
                lines.append(f"    Modifies: {', '.join(summary.action_states)}")
        return "\n".join(lines)

    def _format_tests(self, tests: List[dict]) -> str:
        """Format tests for prompt"""
        lines = []
        for t in tests:
            lines.append(f"- {t['id']}: {t['title']}")
            lines.append(f"  Module: {t['module']}, Workflow: {t['workflow']}")
            lines.append(f"  Expected: {t['expected_result'][:100]}")
        return "\n".join(lines)
