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


def escape_md(text: str) -> str:
    """Escape markdown special characters and handle newlines for table cells."""
    if not text:
        return ""
    # Replace newlines with <br> for table cells
    text = str(text).replace('\n', '<br>')
    # Escape pipe characters
    text = text.replace('|', '\\|')
    return text


def truncate(text: str, max_len: int = 60) -> str:
    """Truncate text to max length."""
    if not text:
        return ""
    text = str(text)
    if len(text) > max_len:
        return text[:max_len-3] + "..."
    return text


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
        lines.append("| Metric | Count |")
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

        # Post-verification summary
        post_verif = summary.get('post_verification', {})
        if post_verif and post_verif.get('tests_needing_verification', 0) > 0:
            lines.append("### Post-Verification Coverage")
            lines.append("")
            lines.append("| Metric | Count |")
            lines.append("|--------|-------|")
            lines.append(f"| Tests Needing Verification | {post_verif.get('tests_needing_verification', 0)} |")
            lines.append(f"| Full Coverage | {post_verif.get('full_coverage', 0)} |")
            lines.append(f"| Partial Coverage | {post_verif.get('partial_coverage', 0)} |")
            lines.append(f"| No Coverage | {post_verif.get('no_coverage', 0)} |")
            lines.append("")

        # Execution plans summary
        exec_plans = summary.get('execution_plans', {})
        if exec_plans and exec_plans.get('total_plans', 0) > 0:
            lines.append("### Execution Plans")
            lines.append("")
            lines.append("| Metric | Value |")
            lines.append("|--------|-------|")
            lines.append(f"| Total Plans | {exec_plans.get('total_plans', 0)} |")
            lines.append(f"| Automated Steps | {exec_plans.get('total_automated_steps', 0)} |")
            lines.append(f"| Manual Steps | {exec_plans.get('total_manual_steps', 0)} |")
            lines.append(f"| Automation Rate | {exec_plans.get('automation_rate', 0)}% |")
            lines.append("")

    lines.append("---")
    lines.append("")

    # Group test cases by module
    test_cases = data.get('test_cases', [])
    modules = defaultdict(list)
    for tc in test_cases:
        module_title = tc.get('module_title', 'Unknown')
        modules[module_title].append(tc)

    # Test Cases by Module - TABLE FORMAT
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
            'positive': '✅ Functional Tests',
            'negative': '❌ Negative Tests',
            'edge_case': '🔄 Edge Case Tests'
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
                title = escape_md(tc.get('title', 'N/A'))
                preconditions = escape_md(tc.get('preconditions', 'None'))
                steps = tc.get('steps', [])
                # Format steps as numbered list with <br>
                steps_str = "<br>".join([f"{i+1}. {escape_md(step)}" for i, step in enumerate(steps)])
                expected = escape_md(tc.get('expected_result', 'N/A'))
                priority = tc.get('priority', 'Medium')

                lines.append(f"| {tc_id} | {title} | {preconditions} | {steps_str} | {expected} | {priority} |")

            lines.append("")

        lines.append("---")
        lines.append("")

    # Post-Verification Details Section
    # Collect all tests that need post-verification
    tests_with_verification = [tc for tc in test_cases if tc.get('needs_post_verification')]
    
    # Create a lookup dictionary for all test cases by ID
    test_case_lookup = {tc.get('id'): tc for tc in test_cases}
    
    if tests_with_verification:
        lines.append("## Post-Verification Details")
        lines.append("")
        lines.append("This section shows verification requirements for tests that modify application state.")
        lines.append("")
        
        for tc in tests_with_verification:
            tc_id = tc.get('id', 'N/A')
            title = tc.get('title', 'N/A')
            coverage = tc.get('verification_coverage', 'unknown')
            coverage_icon = '✅' if coverage == 'full' else ('⚠️' if coverage in ['partial', 'minimal'] else '❌')
            modifies = tc.get('modifies_state', [])
            
            lines.append(f"### {tc_id}: {title}")
            lines.append("")
            lines.append(f"**Coverage:** {coverage_icon} {coverage.title()}")
            if modifies:
                lines.append(f"**Modifies State:** {', '.join(modifies)}")
            lines.append("")
            
            post_verifs = tc.get('post_verifications', [])
            matched_test_ids = set()  # Collect matched test IDs
            
            if post_verifs:
                lines.append("| # | Verification Needed | Status | Matched Test | Confidence | Remarks |")
                lines.append("|---|---------------------|--------|--------------|------------|---------|")
                
                for i, pv in enumerate(post_verifs, 1):
                    ideal = escape_md(truncate(pv.get('ideal', 'N/A'), 50))
                    status = pv.get('status', 'unknown')
                    status_icon = '✅' if status == 'found' else ('⚠️' if status == 'partial' else '❌')
                    matched_id = pv.get('matched_test_id', '-')
                    matched_title = escape_md(truncate(pv.get('matched_test_title', ''), 30))
                    confidence = pv.get('confidence', 0)
                    conf_str = f"{confidence:.0%}" if confidence else "-"
                    
                    # Track matched test IDs for later
                    if matched_id and matched_id != '-':
                        matched_test_ids.add(matched_id)
                    
                    # Build remarks
                    remarks = []
                    if pv.get('execution_note'):
                        remarks.append(escape_md(truncate(pv.get('execution_note'), 50)))
                    if status != 'found' and pv.get('reason'):
                        remarks.append(escape_md(truncate(pv.get('reason'), 50)))
                    if pv.get('suggested_manual_step'):
                        remarks.append(f"**Manual:** {escape_md(truncate(pv.get('suggested_manual_step'), 40))}")
                    remarks_str = "<br>".join(remarks) if remarks else "-"
                    
                    matched_str = f"{matched_id}<br>({matched_title})" if matched_id != '-' and matched_title else matched_id
                    
                    lines.append(f"| {i} | {ideal} | {status_icon} {status} | {matched_str} | {conf_str} | {remarks_str} |")
                
                lines.append("")
            
            # Coverage gaps
            gaps = tc.get('coverage_gaps', [])
            if gaps:
                lines.append("**⚠️ Coverage Gaps:**")
                for gap in gaps:
                    lines.append(f"- {truncate(gap, 100)}")
                lines.append("")
            
            # Print the matched test cases in detail
            if matched_test_ids:
                lines.append("#### 📋 Verification Test Cases to Execute")
                lines.append("")
                lines.append("The following test cases should be executed to verify the action:")
                lines.append("")
                lines.append("| TC ID | Test Case | Preconditions | Steps | Expected Result | Priority |")
                lines.append("|-------|-----------|---------------|-------|-----------------|----------|")
                
                for matched_id in matched_test_ids:
                    matched_tc = test_case_lookup.get(matched_id)
                    if matched_tc:
                        m_id = matched_tc.get('id', 'N/A')
                        m_title = escape_md(matched_tc.get('title', 'N/A'))
                        m_preconditions = escape_md(matched_tc.get('preconditions', 'None'))
                        m_steps = matched_tc.get('steps', [])
                        m_steps_str = "<br>".join([f"{i+1}. {escape_md(step)}" for i, step in enumerate(m_steps)])
                        m_expected = escape_md(matched_tc.get('expected_result', 'N/A'))
                        m_priority = matched_tc.get('priority', 'Medium')
                        
                        lines.append(f"| {m_id} | {m_title} | {m_preconditions} | {m_steps_str} | {m_expected} | {m_priority} |")
                
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
