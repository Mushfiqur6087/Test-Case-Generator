#!/usr/bin/env python3
"""
Test Case Generator - Main Entry Point

This script orchestrates the test case generation process using multiple agents.

Pipeline:
    Input → ParserAgent → NavigationAgent → ChunkerAgent → TestGenerationAgent 
    → AssemblerAgent → SummaryAgent → VerificationFlagAgent → IdealVerificationAgent 
    → VerificationMatcherAgent (RAG) → JSON Output
"""

import json
import os
from typing import Dict, Any, List

from .agents import (
    ParserAgent,
    NavigationAgent,
    ChunkerAgent,
    TestGenerationAgent,
    AssemblerAgent,
    SummaryAgent,
    VerificationFlagAgent,
    IdealVerificationAgent,
    VerificationMatcherAgent
)
from .agents.base import BaseAgent
from .models.schemas import (
    WorkflowChunk,
    TestCase,
    TestSuiteOutput,
    ModuleSummary
)


class TestCaseGenerator:
    """Main orchestrator for test case generation"""

    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4o",
        provider: str = "openai",
        debug: bool = False,
        debug_file: str = "debug_log.txt"
    ):
        self.api_key = api_key
        self.model = model
        self.provider = provider
        self.debug = debug
        self.debug_file = debug_file

        # Initialize debug session once (handles file clearing and header)
        if debug:
            BaseAgent.reset_debug_state()
            BaseAgent.init_debug_session(debug_file, model)

        # Initialize agents with debug settings
        self.parser_agent = ParserAgent(
            api_key=api_key, model=model, provider=provider, debug=debug, debug_file=debug_file
        )
        self.navigation_agent = NavigationAgent(
            api_key=api_key, model=model, provider=provider, debug=debug, debug_file=debug_file
        )
        self.chunker_agent = ChunkerAgent(
            api_key=api_key, model=model, provider=provider, debug=debug, debug_file=debug_file
        )
        self.test_gen_agent = TestGenerationAgent(
            api_key=api_key, model=model, provider=provider, debug=debug, debug_file=debug_file
        )
        self.assembler_agent = AssemblerAgent(
            api_key=api_key, model=model, provider=provider, debug=debug, debug_file=debug_file
        )
        # New verification pipeline agents
        self.summary_agent = SummaryAgent(
            api_key=api_key, model=model, provider=provider, debug=debug, debug_file=debug_file
        )
        self.verification_flag_agent = VerificationFlagAgent(
            api_key=api_key, model=model, provider=provider, debug=debug, debug_file=debug_file
        )
        self.ideal_verification_agent = IdealVerificationAgent(
            api_key=api_key, model=model, provider=provider, debug=debug, debug_file=debug_file
        )
        self.verification_matcher_agent = VerificationMatcherAgent(
            api_key=api_key, model=model, provider=provider, debug=debug, debug_file=debug_file
        )

    def generate(
        self,
        functional_desc_path: str,
        credentials_path: str = None,
        output_dir: str = "output"
    ) -> TestSuiteOutput:
        """
        Generate test cases from functional description.

        Args:
            functional_desc_path: Path to functional_desc.json
            credentials_path: Optional path to credentials.json
            output_dir: Directory to save output files

        Returns:
            TestSuiteOutput with navigation graph and test cases
        """

        print("=" * 60)
        print("TEST CASE GENERATOR")
        print("=" * 60)
        if self.debug:
            print(f"Debug mode: ON (logging to {self.debug_file})")

        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        # Load inputs
        print("\n[1/10] Loading input files...")
        functional_desc = self._load_json(functional_desc_path)
        if credentials_path:
            _ = self._load_json(credentials_path)  # For future use with test data
            print(f"  - Loaded: {functional_desc_path}, {credentials_path}")
        else:
            print(f"  - Loaded: {functional_desc_path}")

        # Step 1: Parse functional description
        print("\n[2/10] Parsing functional description...")
        parsed_desc = self.parser_agent.run(functional_desc)
        print(f"  - Project: {parsed_desc.project_name}")
        print(f"  - Modules found: {len(parsed_desc.modules)}")
        for m in parsed_desc.modules:
            print(f"    • {m.title}: {len(m.workflows)} workflows, {len(m.mentioned_items)} items")

        # Step 2: Build navigation graph
        print("\n[3/10] Building navigation graph...")
        nav_graph = self.navigation_agent.run(parsed_desc)
        print(f"  - Login module ID: {nav_graph.login_module_id}")
        print(f"  - Page nodes: {len(nav_graph.nodes)}")

        # Step 3: Split modules into workflow chunks
        print("\n[4/10] Splitting modules into workflow chunks...")
        all_chunks: List[WorkflowChunk] = []

        for module in parsed_desc.modules:
            chunks = self.chunker_agent.run(module)
            all_chunks.extend(chunks)
            print(f"  - {module.title}: {len(chunks)} chunk(s)")
            for chunk in chunks:
                print(f"    • {chunk.workflow_name}")

        # Step 4: Generate test cases for each chunk
        print("\n[5/10] Generating test cases...")
        all_tests: List[TestCase] = []

        for chunk in all_chunks:
            print(f"  - Generating tests for: {chunk.module_title} / {chunk.workflow_name}")
            tests = self.test_gen_agent.run(chunk)
            print(f"    • Generated {len(tests)} test cases")
            all_tests.extend(tests)

        # Step 5: Assemble and assign IDs
        print("\n[6/10] Assembling test cases...")
        output = self.assembler_agent.run(
            test_cases=all_tests,
            nav_graph=nav_graph,
            project_name=parsed_desc.project_name,
            base_url=parsed_desc.base_url
        )
        print(f"  - Assembled {len(output.test_cases)} unique test cases")

        # Step 6: Generate module summaries
        print("\n[7/10] Generating module summaries...")
        module_summaries = self.summary_agent.run(parsed_desc.modules)
        output.module_summaries = module_summaries
        print(f"  - Generated summaries for {len(module_summaries)} modules")
        for ms in module_summaries.values():
            verify_str = f", can verify: {', '.join(ms.can_verify_states)}" if ms.can_verify_states else ""
            action_str = f", modifies: {', '.join(ms.action_states)}" if ms.action_states else ""
            print(f"    • {ms.module_title}{verify_str}{action_str}")

        # Step 7: Flag tests needing post-verification
        print("\n[8/10] Flagging tests for post-verification...")
        flagged_tests = self.verification_flag_agent.run(output.test_cases, module_summaries)
        flagged_count = sum(1 for tc in flagged_tests if tc.needs_post_verification)
        print(f"  - Flagged {flagged_count} tests as needing post-verification")
        
        # Step 8: Generate ideal verification scenarios
        print("\n[9/10] Generating ideal verification scenarios...")
        ideal_verifications = self.ideal_verification_agent.run(flagged_tests, module_summaries)
        total_ideals = sum(len(v) for v in ideal_verifications.values())
        print(f"  - Generated {total_ideals} ideal verification scenarios for {len(ideal_verifications)} tests")

        # Step 9: Match verifications to actual test cases using RAG
        print("\n[10/10] Matching verifications with RAG...")
        final_tests = self.verification_matcher_agent.run(
            flagged_tests=flagged_tests,
            ideal_verifications=ideal_verifications,
            all_test_cases=output.test_cases,
            module_summaries=module_summaries,
            use_embeddings=True  # Use sentence-transformers if available
        )
        output.test_cases = final_tests

        # Update summary with verification coverage
        output.summary = self._generate_enhanced_summary(output.test_cases, module_summaries)

        # Generate navigation graph image
        print("\n  Generating navigation graph image...")
        graph_image_path = os.path.join(output_dir, "navigation_graph.png")
        generated_path = self.navigation_agent.generate_graph_image(
            nav_graph=output.navigation_graph,
            output_path=graph_image_path,
            title=f"{parsed_desc.project_name} - Navigation Graph"
        )
        if generated_path:
            output.navigation_graph.graph_image_path = generated_path
            print(f"  - Graph image saved to: {generated_path}")
        else:
            print("  - Graph image generation skipped")

        # Validate
        issues = self.assembler_agent.validate(output.test_cases)
        if issues:
            print(f"  - Validation issues: {len(issues)}")
            for issue in issues[:5]:
                print(f"    ! {issue}")

        # Export JSON
        json_path = os.path.join(output_dir, "test-cases.json")
        self.assembler_agent.export_json(output, json_path)
        print(f"\n  Output saved to: {json_path}")

        # Print summary
        self._print_summary(output)

        return output

    def _generate_enhanced_summary(
        self, 
        test_cases: List[TestCase],
        module_summaries: Dict[int, ModuleSummary]
    ) -> Dict:
        """Generate enhanced summary with verification coverage"""
        summary = {
            "total_tests": len(test_cases),
            "by_type": {"positive": 0, "negative": 0, "edge_case": 0},
            "by_priority": {"High": 0, "Medium": 0, "Low": 0},
            "by_module": {},
            "post_verification": {
                "tests_needing_verification": 0,
                "full_coverage": 0,
                "partial_coverage": 0,
                "no_coverage": 0,
                "coverage_gaps": []
            }
        }
        
        all_gaps = set()
        
        for tc in test_cases:
            # Count by type
            if tc.test_type in summary["by_type"]:
                summary["by_type"][tc.test_type] += 1
            
            # Count by priority
            if tc.priority in summary["by_priority"]:
                summary["by_priority"][tc.priority] += 1
            
            # Count by module
            if tc.module_title not in summary["by_module"]:
                summary["by_module"][tc.module_title] = 0
            summary["by_module"][tc.module_title] += 1
            
            # Count verification coverage
            if tc.needs_post_verification:
                summary["post_verification"]["tests_needing_verification"] += 1
                if tc.verification_coverage == "full":
                    summary["post_verification"]["full_coverage"] += 1
                elif tc.verification_coverage == "partial":
                    summary["post_verification"]["partial_coverage"] += 1
                else:
                    summary["post_verification"]["no_coverage"] += 1
                
                # Collect gaps
                for gap in tc.coverage_gaps:
                    all_gaps.add(gap)
        
        summary["post_verification"]["coverage_gaps"] = list(all_gaps)[:10]  # Top 10 gaps
        
        return summary

    def _load_json(self, path: str) -> Dict[str, Any]:
        """Load JSON file"""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _print_summary(self, output: TestSuiteOutput):
        """Print summary statistics"""
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)

        summary = output.summary
        print(f"Total Test Cases: {summary.get('total_tests', 0)}")

        print(f"\nBy Type:")
        for t, count in summary.get('by_type', {}).items():
            print(f"  - {t}: {count}")

        print(f"\nBy Priority:")
        for p, count in summary.get('by_priority', {}).items():
            print(f"  - {p}: {count}")

        print(f"\nBy Module:")
        for m, count in summary.get('by_module', {}).items():
            print(f"  - {m}: {count}")

        # Print post-verification coverage
        post_verif = summary.get('post_verification', {})
        if post_verif:
            print(f"\nPost-Verification Coverage:")
            print(f"  - Tests needing verification: {post_verif.get('tests_needing_verification', 0)}")
            print(f"  - Full coverage: {post_verif.get('full_coverage', 0)}")
            print(f"  - Partial coverage: {post_verif.get('partial_coverage', 0)}")
            print(f"  - No coverage: {post_verif.get('no_coverage', 0)}")
            gaps = post_verif.get('coverage_gaps', [])
            if gaps:
                print(f"  - Coverage gaps ({len(gaps)}):")
                for gap in gaps[:5]:
                    gap_text = gap[:80] + "..." if len(gap) > 80 else gap
                    print(f"    ! {gap_text}")

        print(f"\nNavigation Graph:")
        print(f"  - Total nodes: {len(output.navigation_graph.nodes)}")
        if output.navigation_graph.graph_image_path:
            print(f"  - Graph image: {output.navigation_graph.graph_image_path}")
        for node in output.navigation_graph.nodes.values():
            tc_count = len(node.test_case_ids)
            print(f"  - {node.title}: {tc_count} test cases, connects to {len(node.connected_to)} pages")


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description="Test Case Generator")
    parser.add_argument(
        "--generate",
        action="store_true",
        help="Generate test cases using the LLM"
    )
    parser.add_argument(
        "--input",
        type=str,
        required=False,
        help="Path to functional description JSON"
    )
    parser.add_argument(
        "--credentials",
        type=str,
        default=None,
        help="Path to credentials JSON (optional)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output",
        help="Output directory"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        required=False,
        help="API key (OpenAI, GitHub Models, or OpenRouter)"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o",
        help="Model to use (default: gpt-4o)"
    )
    parser.add_argument(
        "--provider",
        type=str,
        default="openai",
        choices=["openai", "github", "openrouter"],
        help="API provider: openai, github, or openrouter (default: openai)"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode (logs all LLM inputs/outputs)"
    )
    parser.add_argument(
        "--debug-file",
        type=str,
        default="debug_log.txt",
        help="Debug log file path (default: debug_log.txt)"
    )

    args = parser.parse_args()

    if args.generate:
        if not args.api_key:
            print("ERROR: --api-key is required for generation")
            return

        if not args.input:
            print("ERROR: --input is required for generation")
            return

        generator = TestCaseGenerator(
            api_key=args.api_key,
            model=args.model,
            provider=args.provider,
            debug=args.debug,
            debug_file=args.debug_file
        )

        generator.generate(
            functional_desc_path=args.input,
            credentials_path=args.credentials,
            output_dir=args.output
        )
    else:
        parser.print_help()
        print("\n" + "-" * 60)
        print("\nExample usage:")
        print('  python main.py --generate --input parabank.json --api-key "sk-xxx" --provider openai --debug')


if __name__ == "__main__":
    main()
