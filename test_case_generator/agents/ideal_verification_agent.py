from typing import List, Dict

from .base import BaseAgent
from ..models.schemas import TestCase, ModuleSummary, IdealVerification


class IdealVerificationAgent(BaseAgent):
    """Agent responsible for generating ideal verification scenarios for flagged test cases"""

    @property
    def name(self) -> str:
        return "Ideal Verification Agent"

    @property
    def system_prompt(self) -> str:
        return """You are an expert QA engineer who designs verification strategies for test cases.

Your task is to generate IDEAL verification scenarios - what SHOULD be checked after a test executes
to confirm the test actually succeeded.

For example, after a data submission test:
1. Check the new record appears in the list/overview page
2. Check the record details are correct
3. Check any related counters or totals are updated

These are IDEAL verifications - we'll later match them to actual test cases that exist."""

    def run(
        self,
        flagged_tests: List[TestCase],
        module_summaries: Dict[int, ModuleSummary]
    ) -> Dict[str, List[IdealVerification]]:
        """Generate ideal verifications for each flagged test case
        
        Returns:
            Dict mapping test_case_id to list of IdealVerification objects
        """
        
        # Only process tests that need verification
        tests_needing_verification = [tc for tc in flagged_tests if tc.needs_post_verification]
        
        if not tests_needing_verification:
            return {}
        
        # Build verification context from module summaries
        verification_context = self._build_verification_context(module_summaries)
        
        # Process in batches to avoid token limits
        all_verifications = {}
        batch_size = 10
        
        for i in range(0, len(tests_needing_verification), batch_size):
            batch = tests_needing_verification[i:i+batch_size]
            batch_verifications = self._generate_verifications_for_batch(batch, verification_context)
            all_verifications.update(batch_verifications)
        
        return all_verifications

    def _build_verification_context(self, module_summaries: Dict[int, ModuleSummary]) -> str:
        """Build context about what each module can verify"""
        lines = ["MODULES THAT CAN VERIFY DATA:"]
        for summary in module_summaries.values():
            if summary.can_verify_states:
                lines.append(f"- {summary.module_title}:")
                lines.append(f"    Summary: {summary.summary}")
                lines.append(f"    Can verify: {', '.join(summary.can_verify_states)}")
        return "\n".join(lines)

    def _generate_verifications_for_batch(
        self,
        test_cases: List[TestCase],
        verification_context: str
    ) -> Dict[str, List[IdealVerification]]:
        """Generate ideal verifications for a batch of test cases"""
        
        # Format test cases for prompt
        tests_text = ""
        for tc in test_cases:
            tests_text += f"""
Test ID: {tc.id}
Title: {tc.title}
Module: {tc.module_title}
Workflow: {tc.workflow}
Modifies State: {', '.join(tc.modifies_state) if tc.modifies_state else 'Unknown'}
Steps: {'; '.join(tc.steps[:5])}
Expected Result: {tc.expected_result}
---
"""

        prompt = f"""Generate IDEAL verification scenarios for each test case below.

{verification_context}

TEST CASES NEEDING VERIFICATION:
{tests_text}

For each test case, generate 1-3 ideal verifications that would confirm the test truly succeeded.
Think about: What data changed? Where can we see that change? What should we check?

Return JSON:
{{
    "test_verifications": [
        {{
            "test_id": "TEST-001",
            "ideal_verifications": [
                {{
                    "description": "Verify the created/modified record appears in the list view",
                    "target_module": "Relevant Overview/List Module",
                    "verification_action": "View the list or overview page",
                    "expected_change": "New/updated record should be visible with correct data",
                    "state_to_verify": "relevant_state_name"
                }},
                {{
                    "description": "Verify the record details are correct",
                    "target_module": "Details/View Module", 
                    "verification_action": "View the specific record details",
                    "expected_change": "All fields should show the expected values",
                    "state_to_verify": "record_details"
                }}
            ]
        }}
    ]
}}

IMPORTANT:
- target_module should be a module that CAN verify the state (from the context above)
- Be specific about what to check and what the expected outcome is
- Include ALL test cases in the output
- Only generate verifications that are actually achievable with the available modules
- If no verification is possible, return empty ideal_verifications array
- Use actual module names from the provided context, not placeholder names
- Use state names that match those in the module summaries"""

        try:
            result = self.call_llm_json(prompt, max_tokens=4000)
            
            verifications = {}
            for item in result.get("test_verifications", []):
                test_id = item.get("test_id")
                if test_id:
                    ideal_list = []
                    for v in item.get("ideal_verifications", []):
                        ideal_list.append(IdealVerification(
                            description=v.get("description", ""),
                            target_module=v.get("target_module", ""),
                            verification_action=v.get("verification_action", ""),
                            expected_change=v.get("expected_change", ""),
                            state_to_verify=v.get("state_to_verify", "")
                        ))
                    verifications[test_id] = ideal_list
            
            return verifications
            
        except Exception as e:
            print(f"Warning: Ideal verification generation failed: {e}")
            return {}
