#!/usr/bin/env python3
"""
Test Case Generator - Main Entry Point (LangGraph)

Orchestrates the test case generation pipeline using LangGraph.

Graph topology:
    Input -> ParserAgent --+--> NavigationAgent ----------------+
                           +--> ChunkerAgent -> TestGenAgent ---+--> AssemblerAgent
                           +--> SummaryAgent -------------------+
    -> VerificationFlagAgent -> IdealVerificationAgent
    -> VerificationMatcherAgent (RAG) -> ExecutionPlanAgent -> Finalize -> JSON Output
"""

import json
import os
from typing import Any, Dict, List

from .agents.base import BaseAgent
from .graph import build_graph
from .models.schemas import TestSuiteOutput
from .state import PipelineState


class TestCaseGenerator:
    """
    Main orchestrator for test case generation.

    Uses a compiled LangGraph StateGraph under the hood.
    The public API (__init__ / generate) is unchanged so
    existing callers (run_generator.sh, CLI) keep working.
    """

    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4o",
        provider: str = "openai",
        debug: bool = False,
        debug_file: str = "debug_log.txt",
    ):
        self.api_key = api_key
        self.model = model
        self.provider = provider
        self.debug = debug
        self.debug_file = debug_file

        # Initialize debug session once
        if debug:
            BaseAgent.reset_debug_state()
            BaseAgent.init_debug_session(debug_file, model)

        # Compile the LangGraph pipeline once
        self.graph = build_graph()

    # ----------------------------------------------------------
    # Public API
    # ----------------------------------------------------------

    def generate(
        self,
        functional_desc_path: str,
        credentials_path: str = None,
        output_dir: str = "output",
    ) -> TestSuiteOutput:
        """
        Generate test cases from a functional description.

        Args:
            functional_desc_path: Path to functional_desc.json
            credentials_path: Optional path to credentials.json
            output_dir: Directory to save output files

        Returns:
            TestSuiteOutput with navigation graph and test cases
        """

        print("=" * 60)
        print("TEST CASE GENERATOR  (LangGraph Pipeline)")
        print("=" * 60)
        if self.debug:
            print(f"Debug mode: ON (logging to {self.debug_file})")

        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        # Load inputs
        print("\nLoading input files...")
        functional_desc = self._load_json(functional_desc_path)
        credentials = None
        if credentials_path:
            credentials = self._load_json(credentials_path)
            print(f"  - Loaded: {functional_desc_path}, {credentials_path}")
        else:
            print(f"  - Loaded: {functional_desc_path}")

        # Build the initial state for the graph
        initial_state: PipelineState = {
            # Inputs
            "functional_desc": functional_desc,
            "credentials": credentials,
            # Config
            "api_key": self.api_key,
            "model": self.model,
            "provider": self.provider,
            "debug": self.debug,
            "debug_file": self.debug_file,
            "output_dir": output_dir,
        }

        # -- Run the graph --
        final_state = self.graph.invoke(initial_state)

        # -- Extract the final output --
        output: TestSuiteOutput = final_state["output"]

        # Print summary
        self._print_summary(output)

        return output

    # ----------------------------------------------------------
    # Private helpers
    # ----------------------------------------------------------

    @staticmethod
    def _load_json(path: str) -> Dict[str, Any]:
        """Load a JSON file."""
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def _print_summary(output: TestSuiteOutput):
        """Print summary statistics."""
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)

        summary = output.summary
        print(f"Total Test Cases: {summary.get('total_tests', 0)}")

        print("\nBy Type:")
        for t, count in summary.get("by_type", {}).items():
            print(f"  - {t}: {count}")

        print("\nBy Priority:")
        for p, count in summary.get("by_priority", {}).items():
            print(f"  - {p}: {count}")

        print("\nBy Module:")
        for m, count in summary.get("by_module", {}).items():
            print(f"  - {m}: {count}")

        # Post-verification coverage
        post_verif = summary.get("post_verification", {})
        if post_verif:
            print("\nPost-Verification Coverage:")
            print(f"  - Tests needing verification: {post_verif.get('tests_needing_verification', 0)}")
            print(f"  - Full coverage: {post_verif.get('full_coverage', 0)}")
            print(f"  - Partial coverage: {post_verif.get('partial_coverage', 0)}")
            print(f"  - No coverage: {post_verif.get('no_coverage', 0)}")
            gaps = post_verif.get("coverage_gaps", [])
            if gaps:
                print(f"  - Coverage gaps ({len(gaps)}):")
                for gap in gaps[:5]:
                    gap_text = gap[:80] + "..." if len(gap) > 80 else gap
                    print(f"    ! {gap_text}")

        # Execution plans
        exec_plans = summary.get("execution_plans", {})
        if exec_plans:
            print("\nExecution Plans:")
            print(f"  - Total plans: {exec_plans.get('total_plans', 0)}")
            print(f"  - Automated steps: {exec_plans.get('total_automated_steps', 0)}")
            print(f"  - Manual steps: {exec_plans.get('total_manual_steps', 0)}")
            print(f"  - Automation rate: {exec_plans.get('automation_rate', 0)}%")

        print(f"\nNavigation Graph:")
        print(f"  - Total nodes: {len(output.navigation_graph.nodes)}")
        if output.navigation_graph.graph_image_path:
            print(f"  - Graph image: {output.navigation_graph.graph_image_path}")
        for node in output.navigation_graph.nodes.values():
            tc_count = len(node.test_case_ids)
            print(f"  - {node.title}: {tc_count} test cases, connects to {len(node.connected_to)} pages")


# ==============================================================
# CLI entry point
# ==============================================================

def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Test Case Generator (LangGraph)")
    parser.add_argument(
        "--generate", action="store_true",
        help="Generate test cases using the LLM",
    )
    parser.add_argument("--input", type=str, required=False, help="Path to functional description JSON")
    parser.add_argument("--credentials", type=str, default=None, help="Path to credentials JSON (optional)")
    parser.add_argument("--output", type=str, default="output", help="Output directory")
    parser.add_argument(
        "--api-key", type=str, required=False,
        help="API key (OpenAI, GitHub Models, or OpenRouter)",
    )
    parser.add_argument("--model", type=str, default="gpt-4o", help="Model to use (default: gpt-4o)")
    parser.add_argument(
        "--provider", type=str, default="openai",
        choices=["openai", "github", "openrouter"],
        help="API provider: openai, github, or openrouter (default: openai)",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug mode (logs all LLM inputs/outputs)")
    parser.add_argument("--debug-file", type=str, default="debug_log.txt", help="Debug log file path")

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
            debug_file=args.debug_file,
        )

        generator.generate(
            functional_desc_path=args.input,
            credentials_path=args.credentials,
            output_dir=args.output,
        )
    else:
        parser.print_help()
        print("\n" + "-" * 60)
        print("\nExample usage:")
        print(
            '  python -m test_case_generator.main --generate '
            '--input parabank.json --api-key "sk-xxx" --provider openai --debug'
        )


if __name__ == "__main__":
    main()
