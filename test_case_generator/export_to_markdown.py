#!/usr/bin/env python3
"""
Export test cases from JSON to human-readable Markdown format.

Usage:
    python -m test_case_generator.export_to_markdown --input output/test-cases.json --output output/test-cases.md
"""

import argparse
import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict


def load_test_cases(input_path: str) -> dict:
    """Load test cases from JSON file."""
    with open(input_path, 'r') as f:
        return json.load(f)


def generate_markdown(data: dict) -> str:
    """Generate markdown content from test case data."""
    lines = []

    # Header
    lines.append(f"# {data.get('project_name', 'Test Cases')}")
    lines.append("")
    lines.append(f"**Base URL:** {data.get('base_url', 'N/A')}")
    lines.append(f"**Generated:** {data.get('generated_at', 'N/A')}")
    lines.append("")

    # Summary
    summary = data.get('summary', {})
    if summary:
        lines.append("## Summary")
        lines.append("")
        lines.append(f"| Metric | Count |")
        lines.append("|--------|-------|")
        lines.append(f"| **Total Tests** | {summary.get('total_tests', 0)} |")
        lines.append("")

        by_type = summary.get('by_type', {})
        if by_type:
            lines.append("### By Type")
            lines.append("")
            lines.append("| Type | Count |")
            lines.append("|------|-------|")
            for test_type, count in by_type.items():
                lines.append(f"| {test_type.replace('_', ' ').title()} | {count} |")
            lines.append("")

        by_priority = summary.get('by_priority', {})
        if by_priority:
            lines.append("### By Priority")
            lines.append("")
            lines.append("| Priority | Count |")
            lines.append("|----------|-------|")
            for priority, count in by_priority.items():
                lines.append(f"| {priority} | {count} |")
            lines.append("")

        # Verification coverage
        verification = summary.get('verification_coverage', {})
        if verification:
            lines.append("### Verification Coverage")
            lines.append("")
            lines.append("| Metric | Count |")
            lines.append("|--------|-------|")
            lines.append(f"| Positive Tests | {verification.get('total_positive_tests', 0)} |")
            lines.append(f"| Tests that Write State | {verification.get('tests_that_write_state', 0)} |")
            lines.append(f"| Tests that Read State | {verification.get('tests_that_read_state', 0)} |")
            lines.append(f"| Tests with Verification Links | {verification.get('tests_with_verification_links', 0)} |")
            lines.append(f"| Tests with Pre-Verification Steps | {verification.get('tests_with_pre_verification_steps', 0)} |")
            lines.append(f"| Tests with Post-Verification Steps | {verification.get('tests_with_post_verification_steps', 0)} |")
            lines.append("")

            # State categories
            unique_writes = verification.get('unique_states_written', [])
            unique_reads = verification.get('unique_states_read', [])
            unverified = verification.get('unverified_states', [])

            if unique_writes or unique_reads:
                lines.append("**State Categories:**")
                lines.append("")
                if unique_writes:
                    lines.append(f"- **Written:** {', '.join(unique_writes)}")
                if unique_reads:
                    lines.append(f"- **Read:** {', '.join(unique_reads)}")
                if unverified:
                    lines.append(f"- **Unverified:** {', '.join(unverified)}")
                lines.append("")

    # Group test cases by module
    test_cases = data.get('test_cases', [])
    modules = defaultdict(list)
    for tc in test_cases:
        module_title = tc.get('module_title', 'Unknown')
        modules[module_title].append(tc)

    # Test Cases by Module
    lines.append("---")
    lines.append("")
    lines.append("## Test Cases")
    lines.append("")

    for module_title, cases in modules.items():
        lines.append(f"### {module_title}")
        lines.append("")

        # Group by test type within module
        by_type = defaultdict(list)
        for tc in cases:
            by_type[tc.get('test_type', 'other')].append(tc)

        type_order = ['positive', 'negative', 'edge_case']
        type_labels = {
            'positive': 'Functional Tests',
            'negative': 'Negative Tests',
            'edge_case': 'Boundary/Edge Case Tests'
        }

        for test_type in type_order:
            if test_type not in by_type:
                continue

            type_cases = by_type[test_type]
            lines.append(f"#### {type_labels.get(test_type, test_type.title())}")
            lines.append("")

            for tc in type_cases:
                tc_id = tc.get('id', 'N/A')
                title = tc.get('title', 'N/A')
                preconditions = tc.get('preconditions', 'None')
                steps = tc.get('steps', [])
                expected = tc.get('expected_result', 'N/A')
                priority = tc.get('priority', 'Medium')

                # Test case header
                lines.append(f"**{tc_id}** - {title}")
                lines.append("")
                lines.append(f"- **Priority:** {priority}")
                lines.append(f"- **Preconditions:** {preconditions}")

                # State information (for positive tests with verification)
                reads_state = tc.get('reads_state', [])
                writes_state = tc.get('writes_state', [])
                verification_ids = tc.get('verification_test_ids', [])

                if reads_state or writes_state:
                    lines.append("")
                    if reads_state:
                        lines.append(f"- **Reads State:** {', '.join(reads_state)}")
                    if writes_state:
                        lines.append(f"- **Writes State:** {', '.join(writes_state)}")
                    if verification_ids:
                        lines.append(f"- **Verified By:** {', '.join(verification_ids)}")

                # Pre-verification steps
                pre_steps = tc.get('pre_verification_steps', [])
                if pre_steps:
                    lines.append("")
                    lines.append("**Pre-Verification Steps:**")
                    for i, step in enumerate(pre_steps, 1):
                        lines.append(f"{i}. {step}")

                # Main test steps
                lines.append("")
                lines.append("**Test Steps:**")
                for i, step in enumerate(steps, 1):
                    lines.append(f"{i}. {step}")

                # Post-verification steps
                post_steps = tc.get('post_verification_steps', [])
                if post_steps:
                    lines.append("")
                    lines.append("**Post-Verification Steps:**")
                    for i, step in enumerate(post_steps, 1):
                        lines.append(f"{i}. {step}")

                # Expected result
                lines.append("")
                lines.append(f"**Expected Result:** {expected}")
                lines.append("")
                lines.append("---")
                lines.append("")

        lines.append("---")
        lines.append("")

    # Verification Chain
    # Build verification relationships
    verification_chain = {}
    for tc in test_cases:
        if tc.get('test_type') == 'positive' and tc.get('verification_test_ids'):
            verification_chain[tc.get('id')] = {
                'title': tc.get('title'),
                'writes': tc.get('writes_state', []),
                'verified_by': tc.get('verification_test_ids', [])
            }

    if verification_chain:
        lines.append("## Verification Chain")
        lines.append("")
        lines.append("This section shows which test cases verify the results of other tests.")
        lines.append("")
        lines.append("| Test ID | Test Name | Writes State | Verified By |")
        lines.append("|---------|-----------|--------------|-------------|")

        for test_id, info in verification_chain.items():
            writes_str = ', '.join(info['writes']) if info['writes'] else 'N/A'
            verified_by_str = ', '.join(info['verified_by']) if info['verified_by'] else 'N/A'
            title = info['title'].replace('|', '\\|')
            writes_str = writes_str.replace('|', '\\|')
            verified_by_str = verified_by_str.replace('|', '\\|')
            lines.append(f"| {test_id} | {title} | {writes_str} | {verified_by_str} |")

        lines.append("")

    # Navigation Graph Info
    nav_graph = data.get('navigation_graph', {})
    if nav_graph:
        lines.append("## Navigation Graph")
        lines.append("")
        if nav_graph.get('graph_image_path'):
            lines.append(f"![Navigation Graph]({nav_graph['graph_image_path']})")
            lines.append("")

        nodes = nav_graph.get('nodes', [])
        if nodes:
            lines.append("### Pages")
            lines.append("")
            lines.append("| Module | URL | Auth Required | Test Cases |")
            lines.append("|--------|-----|---------------|------------|")
            for node in nodes:
                title = node.get('title', 'N/A')
                url = node.get('url_path', 'N/A')
                auth = 'Yes' if node.get('requires_auth') else 'No'
                tc_count = len(node.get('test_case_ids', []))
                lines.append(f"| {title} | {url} | {auth} | {tc_count} |")
            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description='Export test cases to Markdown')
    parser.add_argument('--input', '-i', required=True, help='Input JSON file path')
    parser.add_argument('--output', '-o', help='Output Markdown file path (default: same as input with .md extension)')

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        return 1

    output_path = args.output
    if not output_path:
        output_path = input_path.with_suffix('.md')

    print(f"Reading test cases from: {input_path}")
    data = load_test_cases(input_path)

    print("Generating Markdown...")
    markdown = generate_markdown(data)

    print(f"Writing to: {output_path}")
    with open(output_path, 'w') as f:
        f.write(markdown)

    test_count = len(data.get('test_cases', []))
    print(f"Done! Exported {test_count} test cases to Markdown.")
    return 0


if __name__ == '__main__':
    exit(main())
