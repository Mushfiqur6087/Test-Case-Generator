from typing import List, Dict
from dataclasses import dataclass, field

from .base import BaseAgent
from ..models.schemas import TestCase


@dataclass
class ExecutionSequence:
    """Represents an execution sequence for verifying a test case"""
    source_test_id: str                     # The test that needs verification
    source_test_title: str                  # Title of the source test
    execution_order: List[Dict] = field(default_factory=list)  # Ordered list of tests to run
    manual_steps: List[str] = field(default_factory=list)      # Manual steps if no automated test
    verification_coverage: str = ""         # "full" | "partial" | "none"
    notes: str = ""                          # Additional execution notes
    
    def to_dict(self) -> dict:
        return {
            "source_test_id": self.source_test_id,
            "source_test_title": self.source_test_title,
            "execution_order": self.execution_order,
            "manual_steps": self.manual_steps,
            "verification_coverage": self.verification_coverage,
            "notes": self.notes
        }


class ExecutionPlanAgent(BaseAgent):
    """
    Agent responsible for compiling final execution plans.
    
    This is the FINAL step in the verification pipeline that:
    1. Takes all flagged tests with their matched verifications
    2. Compiles them into clear execution sequences
    3. Determines the optimal order to run verification tests
    4. Provides manual steps for gaps that can't be automated
    """

    @property
    def name(self) -> str:
        return "Execution Plan Agent"

    @property
    def system_prompt(self) -> str:
        return """You are a QA execution planner. Your job is to create clear, actionable 
execution plans that tell testers exactly what steps to follow after running a test case.

For each test that needs post-verification, you will:
1. Analyze the matched verification tests
2. Determine the optimal execution order
3. Add any necessary setup or navigation steps between tests
4. Include manual steps for verifications that couldn't be matched to existing tests

Keep execution notes concise and actionable."""

    def run(self, test_cases: List[TestCase]) -> Dict[str, ExecutionSequence]:
        """
        Generate execution plans for all tests needing post-verification.
        
        Args:
            test_cases: All test cases (flagged ones have post_verifications populated)
            
        Returns:
            Dictionary mapping test_id -> ExecutionSequence
        """
        
        # Filter to only tests that need post-verification AND have verifications
        tests_needing_plans = [
            tc for tc in test_cases 
            if tc.needs_post_verification and tc.post_verifications
        ]
        
        if not tests_needing_plans:
            return {}
        
        execution_plans: Dict[str, ExecutionSequence] = {}
        
        for tc in tests_needing_plans:
            plan = self._build_execution_plan(tc, test_cases)
            execution_plans[tc.id] = plan
        
        return execution_plans

    def _build_execution_plan(
        self, 
        source_test: TestCase,
        all_tests: List[TestCase]
    ) -> ExecutionSequence:
        """Build execution plan for a single test case"""
        
        execution_order = []
        manual_steps = []
        found_count = 0
        total_verifications = len(source_test.post_verifications)
        
        # Build lookup for test details
        test_lookup = {tc.id: tc for tc in all_tests}
        
        for pv in source_test.post_verifications:
            if pv.get('status') == 'found':
                matched_id = pv.get('matched_test_id', '')
                matched_test = test_lookup.get(matched_id)
                
                execution_order.append({
                    "step": len(execution_order) + 1,
                    "action": "execute_test",
                    "test_id": matched_id,
                    "test_title": matched_test.title if matched_test else pv.get('matched_test_title', ''),
                    "purpose": pv.get('ideal', ''),
                    "execution_note": pv.get('execution_note', ''),
                    "confidence": pv.get('confidence', 0.0)
                })
                found_count += 1
                
            elif pv.get('status') == 'partial':
                matched_id = pv.get('matched_test_id', '')
                matched_test = test_lookup.get(matched_id)
                
                execution_order.append({
                    "step": len(execution_order) + 1,
                    "action": "execute_test_partial",
                    "test_id": matched_id,
                    "test_title": matched_test.title if matched_test else pv.get('matched_test_title', ''),
                    "purpose": pv.get('ideal', ''),
                    "execution_note": pv.get('execution_note', ''),
                    "limitation": pv.get('reason', ''),
                    "confidence": pv.get('confidence', 0.0)
                })
                found_count += 0.5  # Count partial as half
                
            else:  # not_found
                manual_steps.append({
                    "purpose": pv.get('ideal', ''),
                    "suggested_step": pv.get('suggested_manual_step', ''),
                    "reason": pv.get('reason', 'No matching test case found')
                })
        
        # Determine coverage level
        if total_verifications > 0:
            coverage_ratio = found_count / total_verifications
            if coverage_ratio >= 1.0:
                coverage = "full"
            elif coverage_ratio >= 0.5:
                coverage = "partial"
            else:
                coverage = "minimal" if coverage_ratio > 0 else "none"
        else:
            coverage = "none"
        
        # Generate execution notes
        notes = self._generate_execution_notes(source_test, execution_order, manual_steps)
        
        return ExecutionSequence(
            source_test_id=source_test.id,
            source_test_title=source_test.title,
            execution_order=execution_order,
            manual_steps=manual_steps,
            verification_coverage=coverage,
            notes=notes
        )

    def _generate_execution_notes(
        self,
        source_test: TestCase,
        execution_order: List[Dict],
        manual_steps: List[Dict]
    ) -> str:
        """Generate human-readable execution notes"""
        
        if not execution_order and not manual_steps:
            return "No verification steps identified."
        
        notes_parts = []
        
        if execution_order:
            test_ids = [step['test_id'] for step in execution_order]
            notes_parts.append(f"After executing {source_test.id}, run: {' → '.join(test_ids)}")
        
        if manual_steps:
            notes_parts.append(f"Manual verification needed for {len(manual_steps)} item(s)")
        
        return "; ".join(notes_parts)

    def generate_execution_plan_summary(
        self, 
        execution_plans: Dict[str, ExecutionSequence]
    ) -> Dict:
        """Generate a summary of all execution plans"""
        
        if not execution_plans:
            return {
                "total_plans": 0,
                "coverage_distribution": {},
                "total_automated_steps": 0,
                "total_manual_steps": 0
            }
        
        coverage_dist = {"full": 0, "partial": 0, "minimal": 0, "none": 0}
        total_automated = 0
        total_manual = 0
        
        for plan in execution_plans.values():
            coverage_dist[plan.verification_coverage] = coverage_dist.get(plan.verification_coverage, 0) + 1
            total_automated += len(plan.execution_order)
            total_manual += len(plan.manual_steps)
        
        return {
            "total_plans": len(execution_plans),
            "coverage_distribution": coverage_dist,
            "total_automated_steps": total_automated,
            "total_manual_steps": total_manual,
            "automation_rate": round(
                total_automated / (total_automated + total_manual) * 100, 1
            ) if (total_automated + total_manual) > 0 else 0
        }
