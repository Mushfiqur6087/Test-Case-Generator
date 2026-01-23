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
            
            gaps = post_verif.get('coverage_gaps', [])
            if gaps:
                lines.append("#### Coverage Gaps")
                lines.append("")
                for gap in gaps:
                    lines.append(f"- {gap}")
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
            
            coverage_dist = exec_plans.get('coverage_distribution', {})
            if coverage_dist:
                lines.append("#### Coverage Distribution")
                lines.append("")
                lines.append("| Coverage Level | Count |")
                lines.append("|----------------|-------|")
                for level, count in coverage_dist.items():
                    lines.append(f"| {level.title()} | {count} |")
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

                # Main test steps
                lines.append("")
                lines.append("**Test Steps:**")
                for i, step in enumerate(steps, 1):
                    lines.append(f"{i}. {step}")

                # Expected result
                lines.append("")
                lines.append(f"**Expected Result:** {expected}")

                # Post-verification info (for positive tests that need it)
                if tc.get('needs_post_verification') and tc.get('post_verifications'):
                    lines.append("")
                    lines.append(f"**Post-Verification Required:** ✓ ({tc.get('verification_coverage', 'unknown')} coverage)")
                    lines.append("")
                    lines.append("| Verification | Status | Matched Test | Note |")
                    lines.append("|--------------|--------|--------------|------|")
                    
                    for pv in tc.get('post_verifications', []):
                        ideal = pv.get('ideal', 'N/A')[:40]
                        status = pv.get('status', 'unknown')
                        status_icon = '✓' if status == 'found' else ('⚠' if status == 'partial' else '✗')
                        matched_id = pv.get('matched_test_id', '-')
                        note = pv.get('execution_note', pv.get('reason', '-'))[:50]
                        lines.append(f"| {ideal}... | {status_icon} {status} | {matched_id} | {note} |")
                    lines.append("")
                    
                    # Coverage gaps for this test
                    gaps = tc.get('coverage_gaps', [])
                    if gaps:
                        lines.append("**Coverage Gaps:**")
                        for gap in gaps[:3]:
                            lines.append(f"- ⚠ {gap}")
                        lines.append("")

                lines.append("")
                lines.append("---")
                lines.append("")

        lines.append("---")
        lines.append("")

    # Execution Plans Section (after test cases)
    execution_plans = data.get('execution_plans', {})
    if execution_plans:
        lines.append("## Execution Plans")
        lines.append("")
        lines.append("This section shows the recommended test execution sequence for each test case that requires post-verification.")
        lines.append("")
        
        for test_id, plan in execution_plans.items():
            source_title = plan.get('source_test_title', 'Unknown')
            coverage = plan.get('verification_coverage', 'unknown')
            coverage_icon = '✓' if coverage == 'full' else ('⚠' if coverage in ['partial', 'minimal'] else '✗')
            
            lines.append(f"### {test_id}: {source_title}")
            lines.append("")
            lines.append(f"**Coverage:** {coverage_icon} {coverage.title()}")
            lines.append("")
            
            # Execution order
            exec_order = plan.get('execution_order', [])
            if exec_order:
                lines.append("**Verification Sequence:**")
                lines.append("")
                for step in exec_order:
                    step_num = step.get('step', '?')
                    action = step.get('action', 'execute_test')
                    test_id_ref = step.get('test_id', 'N/A')
                    test_title = step.get('test_title', 'N/A')
                    purpose = step.get('purpose', '')
                    exec_note = step.get('execution_note', '')
                    confidence = step.get('confidence', 0)
                    
                    action_icon = '🔄' if action == 'execute_test_partial' else '▶️'
                    lines.append(f"{step_num}. {action_icon} **{test_id_ref}** - {test_title}")
                    if purpose:
                        lines.append(f"   - *Purpose:* {purpose[:100]}")
                    if exec_note:
                        lines.append(f"   - *Note:* {exec_note}")
                    if confidence > 0:
                        lines.append(f"   - *Confidence:* {confidence:.0%}")
                    lines.append("")
            
            # Manual steps
            manual_steps = plan.get('manual_steps', [])
            if manual_steps:
                lines.append("**Manual Verification Required:**")
                lines.append("")
                for ms in manual_steps:
                    purpose = ms.get('purpose', 'N/A')
                    suggested = ms.get('suggested_step', '')
                    reason = ms.get('reason', '')
                    
                    lines.append(f"- ⚠ {purpose}")
                    if suggested:
                        lines.append(f"  - *Suggested:* {suggested}")
                    if reason:
                        lines.append(f"  - *Reason:* {reason}")
                lines.append("")
            
            # Notes
            notes = plan.get('notes', '')
            if notes:
                lines.append(f"**Quick Reference:** {notes}")
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
