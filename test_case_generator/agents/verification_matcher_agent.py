from typing import List, Dict

from .base import BaseAgent
from .rag_indexer import RAGIndexer
from ..models.schemas import TestCase, ModuleSummary, IdealVerification, VerificationMatch


class VerificationMatcherAgent(BaseAgent):
    """Agent responsible for matching ideal verifications to actual test cases using RAG"""

    @property
    def name(self) -> str:
        return "Verification Matcher Agent"

    @property
    def system_prompt(self) -> str:
        return """You are an expert at matching verification requirements to test cases.

Given an ideal verification scenario and candidate test cases from RAG search,
determine if any of the candidates can actually verify what we need.

Consider:
1. Does the test case operate on the right module/page?
2. Does it check the right data (balance, transaction, profile, etc.)?
3. Can it detect the expected change?"""

    def run(
        self,
        flagged_tests: List[TestCase],
        ideal_verifications: Dict[str, List[IdealVerification]],
        all_test_cases: List[TestCase],
        module_summaries: Dict[int, ModuleSummary],
        use_embeddings: bool = True
    ) -> List[TestCase]:
        """Match ideal verifications to actual test cases
        
        Args:
            flagged_tests: Test cases that need verification
            ideal_verifications: Dict mapping test_id to list of IdealVerification
            all_test_cases: All generated test cases to search through
            module_summaries: Module summaries for context
            use_embeddings: Whether to use embedding-based RAG
            
        Returns:
            Updated test cases with post_verifications populated
        """
        
        # Build RAG index
        print("  - Building RAG index...")
        rag = RAGIndexer(use_embeddings=use_embeddings)
        rag.build_index(all_test_cases)
        
        # Process each flagged test
        for tc in flagged_tests:
            if not tc.needs_post_verification:
                continue
            
            test_id = tc.id
            if test_id not in ideal_verifications:
                continue
            
            ideals = ideal_verifications[test_id]
            if not ideals:
                tc.verification_coverage = "none"
                tc.coverage_gaps = ["No verification scenarios identified"]
                continue
            
            # Match each ideal verification
            matches = []
            for ideal in ideals:
                match = self._match_verification(ideal, rag, all_test_cases, tc.id)
                matches.append(match.to_dict())
            
            # Store matches in test case
            tc.post_verifications = matches
            
            # Calculate coverage
            found_count = sum(1 for m in matches if m["status"] == "found")
            partial_count = sum(1 for m in matches if m["status"] == "partial")
            total = len(matches)
            
            if found_count == total:
                tc.verification_coverage = "full"
            elif found_count > 0 or partial_count > 0:
                tc.verification_coverage = "partial"
            else:
                tc.verification_coverage = "none"
            
            # Collect gaps
            tc.coverage_gaps = [
                m.get("reason", "Unknown reason")
                for m in matches 
                if m["status"] in ("not_found", "partial")
            ]
        
        return flagged_tests

    def _match_verification(
        self,
        ideal: IdealVerification,
        rag: RAGIndexer,
        all_tests: List[TestCase],
        source_test_id: str
    ) -> VerificationMatch:
        """Match a single ideal verification to test cases"""
        
        # Build search query from ideal verification
        query = f"{ideal.description} {ideal.verification_action} {ideal.target_module} {ideal.expected_change}"
        
        # Search RAG
        candidates = rag.search(
            query=query,
            top_k=5,
            module_filter=ideal.target_module if ideal.target_module else None
        )
        
        # Filter out the source test case itself
        candidates = [(tc, score) for tc, score in candidates if tc.id != source_test_id]
        
        if not candidates:
            return VerificationMatch(
                ideal_description=ideal.description,
                status="not_found",
                reason=f"No test cases found for module '{ideal.target_module}'",
                suggested_manual_step=f"Manual verification: {ideal.verification_action}. Expected: {ideal.expected_change}"
            )
        
        # Use LLM to validate the best candidates
        return self._validate_candidates(ideal, candidates[:3])

    def _validate_candidates(
        self,
        ideal: IdealVerification,
        candidates: List[tuple]
    ) -> VerificationMatch:
        """Use LLM to validate if candidates can verify the ideal scenario"""
        
        candidates_text = ""
        for tc, score in candidates:
            candidates_text += f"""
Test ID: {tc.id}
Title: {tc.title}
Module: {tc.module_title}
Steps: {'; '.join(tc.steps[:4])}
Expected: {tc.expected_result[:150]}
Similarity Score: {score:.2f}
---
"""

        prompt = f"""Determine if any of these test cases can verify the following requirement:

VERIFICATION NEEDED:
- Description: {ideal.description}
- Target Module: {ideal.target_module}
- Verification Action: {ideal.verification_action}
- Expected Change: {ideal.expected_change}
- State to Verify: {ideal.state_to_verify}

CANDIDATE TEST CASES:
{candidates_text}

Analyze each candidate and determine:
1. Can it verify the required state change?
2. Is it from the correct module?
3. Does it check the right data?

Return JSON:
{{
    "best_match": {{
        "test_id": "TEST-ID or null if none match",
        "status": "found|partial|not_found",
        "confidence": 0.0 to 1.0,
        "execution_note": "How to use this test for verification (e.g., 'Run this test after the action to verify the change')",
        "reason": "Explanation if not_found or partial",
        "suggested_manual_step": "Manual step if no automated option exists"
    }}
}}

STATUS DEFINITIONS:
- found: Test case can fully verify the requirement
- partial: Test case partially verifies but misses some aspects
- not_found: None of the candidates can verify this requirement"""

        try:
            result = self.call_llm_json(prompt, max_tokens=1000)
            match_data = result.get("best_match", {})
            
            status = match_data.get("status", "not_found")
            test_id = match_data.get("test_id")
            
            # Find the matched test case for its title
            matched_title = ""
            matched_confidence = match_data.get("confidence", 0.0)
            if test_id and test_id != "null":
                for tc, score in candidates:
                    if tc.id == test_id:
                        matched_title = tc.title
                        if matched_confidence == 0:
                            matched_confidence = score
                        break
            
            return VerificationMatch(
                ideal_description=ideal.description,
                status=status,
                matched_test_id=test_id if test_id and test_id != "null" else "",
                matched_test_title=matched_title,
                confidence=matched_confidence,
                execution_note=match_data.get("execution_note", ""),
                reason=match_data.get("reason", ""),
                suggested_manual_step=match_data.get("suggested_manual_step", "")
            )
            
        except Exception as e:
            print(f"Warning: Candidate validation failed: {e}")
            # Fallback: use best candidate by score
            if candidates:
                best_tc, best_score = candidates[0]
                return VerificationMatch(
                    ideal_description=ideal.description,
                    status="partial" if best_score > 0.5 else "not_found",
                    matched_test_id=best_tc.id if best_score > 0.3 else "",
                    matched_test_title=best_tc.title if best_score > 0.3 else "",
                    confidence=best_score,
                    execution_note=f"Execute {best_tc.id} to verify",
                    reason="LLM validation failed, using similarity score"
                )
            
            return VerificationMatch(
                ideal_description=ideal.description,
                status="not_found",
                reason="No matching test cases found"
            )
