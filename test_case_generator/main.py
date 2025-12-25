#!/usr/bin/env python3
"""
Test Case Generator - Main Entry Point

This script orchestrates the test case generation process using multiple agents.

Pipeline:
    Input → ParserAgent → ChunkerAgent → NavigationAgent → TestGenerationAgent → AssemblerAgent → JSON Output
"""

import json
import os
from typing import Dict, Any, List

from .agents import (
    ParserAgent,
    NavigationAgent,
    ChunkerAgent,
    TestGenerationAgent,
    AssemblerAgent
)
from .agents.base import BaseAgent
from .models.schemas import (
    WorkflowChunk,
    TestCase,
    TestSuiteOutput
)


class TestCaseGenerator:
    """Main orchestrator for test case generation"""

    def __init__(
        self,
        api_key: str,
        model: str = "openai/gpt-4o",
        debug: bool = False,
        debug_file: str = "debug_log.txt"
    ):
        self.api_key = api_key
        self.model = model
        self.debug = debug
        self.debug_file = debug_file

        # Initialize debug session once (handles file clearing and header)
        if debug:
            BaseAgent.reset_debug_state()
            BaseAgent.init_debug_session(debug_file, model)

        # Initialize agents with debug settings
        self.parser_agent = ParserAgent(
            api_key=api_key, model=model, debug=debug, debug_file=debug_file
        )
        self.navigation_agent = NavigationAgent(
            api_key=api_key, model=model, debug=debug, debug_file=debug_file
        )
        self.chunker_agent = ChunkerAgent(
            api_key=api_key, model=model, debug=debug, debug_file=debug_file
        )
        self.test_gen_agent = TestGenerationAgent(
            api_key=api_key, model=model, debug=debug, debug_file=debug_file
        )
        self.assembler_agent = AssemblerAgent(
            api_key=api_key, model=model, debug=debug, debug_file=debug_file
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
        print("\n[1/6] Loading input files...")
        functional_desc = self._load_json(functional_desc_path)
        if credentials_path:
            _ = self._load_json(credentials_path)  # For future use with test data
            print(f"  - Loaded: {functional_desc_path}, {credentials_path}")
        else:
            print(f"  - Loaded: {functional_desc_path}")

        # Step 1: Parse functional description
        print("\n[2/6] Parsing functional description...")
        parsed_desc = self.parser_agent.run(functional_desc)
        print(f"  - Project: {parsed_desc.project_name}")
        print(f"  - Modules found: {len(parsed_desc.modules)}")
        for m in parsed_desc.modules:
            print(f"    • {m.title}: {len(m.workflows)} workflows, {len(m.mentioned_items)} items")

        # Step 2: Build navigation graph
        print("\n[3/6] Building navigation graph...")
        nav_graph = self.navigation_agent.run(parsed_desc)
        print(f"  - Login module ID: {nav_graph.login_module_id}")
        print(f"  - Page nodes: {len(nav_graph.nodes)}")

        # Step 3: Split modules into workflow chunks
        print("\n[4/6] Splitting modules into workflow chunks...")
        all_chunks: List[WorkflowChunk] = []

        for module in parsed_desc.modules:
            chunks = self.chunker_agent.run(module)
            all_chunks.extend(chunks)
            print(f"  - {module.title}: {len(chunks)} chunk(s)")
            for chunk in chunks:
                print(f"    • {chunk.workflow_name}")

        # Step 4: Generate test cases for each chunk
        print("\n[5/6] Generating test cases...")
        all_tests: List[TestCase] = []

        for chunk in all_chunks:
            print(f"  - Generating tests for: {chunk.module_title} / {chunk.workflow_name}")
            tests = self.test_gen_agent.run(chunk)
            print(f"    • Generated {len(tests)} test cases")
            all_tests.extend(tests)

        # Step 5: Assemble final output
        print("\n[6/6] Assembling final output...")
        output = self.assembler_agent.run(
            test_cases=all_tests,
            nav_graph=nav_graph,
            project_name=parsed_desc.project_name,
            base_url=parsed_desc.base_url
        )

        # Generate navigation graph image
        print("  - Generating navigation graph image...")
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
        help="OpenRouter API key"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="google/gemini-2.0-flash-exp:free",
        help="Model to use (default: google/gemini-2.0-flash-exp:free)"
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
        print('  python main.py --generate --input parabank.json --api-key "sk-or-v1-xxx" --debug')


if __name__ == "__main__":
    main()
