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

            # Table header
            lines.append("| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |")
            lines.append("|-------|-----------|---------------|-------|-----------------|----------|")

            for tc in type_cases:
                tc_id = tc.get('id', 'N/A')
                title = tc.get('title', 'N/A')
                preconditions = tc.get('preconditions', 'None')
                steps = tc.get('steps', [])
                expected = tc.get('expected_result', 'N/A')
                priority = tc.get('priority', 'Medium')

                # Format steps as numbered list (inline)
                steps_str = " ".join([f"{i+1}. {step}" for i, step in enumerate(steps)])

                # Escape pipe characters in content
                title = title.replace('|', '\\|')
                preconditions = preconditions.replace('|', '\\|')
                steps_str = steps_str.replace('|', '\\|')
                expected = expected.replace('|', '\\|')

                lines.append(f"| {tc_id} | {title} | {preconditions} | {steps_str} | {expected} | {priority} |")

            lines.append("")

        lines.append("---")
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
