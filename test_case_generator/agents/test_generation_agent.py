from typing import List

from .base import BaseAgent
from ..models.schemas import WorkflowChunk, TestCase


class TestGenerationAgent(BaseAgent):
    """Agent responsible for generating test cases from workflow chunks"""

    @property
    def name(self) -> str:
        return "Test Generation Agent"

    @property
    def system_prompt(self) -> str:
        return """You are an expert QA engineer specializing in test case design for web automation.

Your task is to generate comprehensive test cases that cover the functionality described.

GUIDING PRINCIPLES:
1. Cover all scenarios mentioned in the functional description
2. Tests must be executable by a browser automation tool
3. Test steps should describe actions on the current page - NOT navigation to the page

TEST TYPES:
1. POSITIVE TESTS: Verify success scenarios work as described
2. NEGATIVE TESTS: Test error conditions and validation rules mentioned
3. EDGE CASE TESTS: Boundary values, special characters, format variations if relevant

DO NOT generate tests for:
- Device-specific interactions (touch gestures, mobile-only features)
- Browser-specific features (right-click context menus, opening in new tabs)
- Network conditions (offline, slow connection, server errors)
- Stress scenarios (rapid clicking, load testing)

For each test case, provide:
- Clear, concise title
- Single precondition statement (or "None")
- Specific test steps (actions on the page, NOT navigation to the page)
- Single expected result
- Priority (High for core functionality, Medium for validations, Low for edge cases)"""

    def run(self, chunk: WorkflowChunk) -> List[TestCase]:
        """Generate test cases for a workflow chunk"""

        # Build context from chunk
        items_str = ", ".join(chunk.related_items) if chunk.related_items else "Not specified"
        rules_str = "\n".join([f"  - {r}" for r in chunk.related_rules]) if chunk.related_rules else "None"
        behaviors_str = "\n".join([f"  - {b}" for b in chunk.related_behaviors]) if chunk.related_behaviors else "None"

        prompt = f"""Generate test cases for this workflow.

Module: {chunk.module_title}
Workflow: {chunk.workflow_name}
Description: {chunk.workflow_description}

Available Items/Elements: {items_str}

Business Rules:
{rules_str}

Expected Behaviors:
{behaviors_str}

Generate test cases in this JSON format:
{{
    "test_cases": [
        {{
            "title": "Short descriptive title",
            "test_type": "positive|negative|edge_case",
            "priority": "High|Medium|Low",
            "preconditions": "Single precondition statement or None",
            "steps": ["Step 1", "Step 2", "Step 3"],
            "expected_result": "Single expected outcome"
        }}
    ]
}}

REQUIREMENTS:
1. POSITIVE tests: Cover success scenarios mentioned (e.g., login with username, login with email if mentioned)
2. NEGATIVE tests: Cover error conditions and validations mentioned in business rules
3. EDGE CASE tests: Include if relevant (boundaries, special characters, max lengths)
4. Steps should describe actions on THIS page only - do NOT include navigation steps like "Navigate to login page"
5. Tests must be executable by browser automation
6. DO NOT use specific values - use generic descriptive text instead

IMPORTANT:
- Cover different valid input variations mentioned (e.g., if "username or email" is mentioned, test both)
- Test the key error scenarios described
- Do not generate tests for touch gestures, right-click menus, network failures, or rapid clicking
- Use generic descriptive text for values, NOT specific data:
  ✓ CORRECT: "Enter a valid username", "Enter valid first name", "Enter valid email address"
  ✗ WRONG: "Enter 'John'", "Enter 'john@example.com'", "Enter '123 Main St'"
- Keep test steps natural and descriptive without hardcoded values
"""

        try:
            result = self.call_llm_json(prompt, max_tokens=4000)
            return self._parse_test_results(result, chunk)
        except Exception as e:
            print(f"Warning: Test generation failed for {chunk.workflow_name}: {e}")
            return []

    def _parse_test_results(self, result: dict, chunk: WorkflowChunk) -> List[TestCase]:
        """Parse LLM response into TestCase objects"""

        tests = []
        raw_tests = result.get("test_cases", [])

        for i, raw_test in enumerate(raw_tests):
            # Validate and normalize test_type
            test_type = raw_test.get("test_type", "positive").lower()
            if test_type not in ["positive", "negative", "edge_case"]:
                test_type = "positive"

            # Validate and normalize priority
            priority = raw_test.get("priority", "Medium")
            if priority not in ["High", "Medium", "Low"]:
                priority = "Medium"

            # Normalize preconditions
            preconditions = raw_test.get("preconditions", "None")
            if not preconditions or preconditions.lower() in ["none", "n/a", ""]:
                preconditions = "None"

            # Normalize expected_result
            expected = raw_test.get("expected_result", "")
            if isinstance(expected, list):
                expected = "; ".join(expected)

            test_case = TestCase(
                id="",  # Will be assigned by AssemblerAgent
                title=raw_test.get("title", f"Test Case {i+1}"),
                module_id=chunk.module_id,
                module_title=chunk.module_title,
                workflow=chunk.workflow_name,
                test_type=test_type,
                priority=priority,
                preconditions=preconditions,
                steps=raw_test.get("steps", []),
                expected_result=expected
            )
            tests.append(test_case)

        return tests

    def generate_for_type(
        self,
        chunk: WorkflowChunk,
        test_type: str
    ) -> List[TestCase]:
        """Generate only a specific type of test cases"""

        type_prompts = {
            "positive": "Generate positive (happy path) test cases. Cover all success scenarios mentioned in the description.",
            "negative": "Generate negative test cases for error conditions and validations mentioned in the description.",
            "edge_case": "Generate edge case tests for boundary values, special characters, or format variations if relevant."
        }

        items_str = ", ".join(chunk.related_items) if chunk.related_items else "Not specified"
        rules_str = "\n".join([f"  - {r}" for r in chunk.related_rules]) if chunk.related_rules else "None"

        prompt = f"""{type_prompts.get(test_type, type_prompts["positive"])}

Module: {chunk.module_title}
Workflow: {chunk.workflow_name}
Description: {chunk.workflow_description}

Available Items: {items_str}

Business Rules:
{rules_str}

Return JSON with test_cases array.
Steps should NOT include navigation - only actions on the current page.
Tests must be executable by browser automation (no touch gestures, right-click menus, network tests).
"""

        try:
            result = self.call_llm_json(prompt, max_tokens=4000)
            tests = self._parse_test_results(result, chunk)
            # Ensure all tests have correct type
            for test in tests:
                test.test_type = test_type
            return tests
        except Exception as e:
            print(f"Warning: {test_type} test generation failed: {e}")
            return []
