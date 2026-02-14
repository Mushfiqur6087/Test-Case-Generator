"""
Verifier Pipeline - Enhances test cases and functional descriptions
by traversing the actual website and comparing against generated content.
"""

import os
import sys
import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from test_case_enhancer.browser.browser_context import BrowserSession
from test_case_enhancer.agent.core_utils.llm import LLMClient
from test_case_enhancer.agent.verification_agent.prompts import (
    get_test_case_verification_prompt,
    get_functional_desc_enhancement_prompt
)


@dataclass
class NavigationContext:
    """Tracks navigation state across the website"""
    current_page: str
    current_url: str
    visited_pages: List[str]
    navigation_map: Dict[str, Dict[str, Any]]  # page -> {url, links, requires_auth}
    
    def to_dict(self) -> Dict:
        return asdict(self)
    
    def update_from_result(self, nav_update: Dict):
        """Update navigation map from verification result"""
        if nav_update:
            page_name = nav_update.get('current_page', self.current_page)
            self.navigation_map[page_name] = {
                'url': nav_update.get('current_url', self.current_url),
                'available_links': nav_update.get('available_links', []),
                'requires_auth': nav_update.get('requires_auth', False)
            }


@dataclass
class VerificationResult:
    """Result from verifying a single test case"""
    original_test_case: Dict
    enhanced_test_case: Dict
    issues_found: List[Dict]
    navigation_update: Dict
    verification_status: str  # passed, fixed, needs_review


class VerifierPipeline:
    """
    Main pipeline that:
    1. Navigates to each module page
    2. Fixes test cases one by one
    3. Finally fixes functional description
    4. Builds complete navigation map
    """
    
    def __init__(
        self,
        test_cases_path: str,
        functional_desc_path: str,
        credentials_path: str,
        api_key: str,
        provider: str = 'gemini',
        headless: bool = False
    ):
        """
        Initialize the verifier pipeline.
        
        Args:
            test_cases_path: Path to generated test-cases.json
            functional_desc_path: Path to functional description JSON (e.g., parabank.json)
            credentials_path: Path to credentials.json
            api_key: API key for LLM
            provider: LLM provider ('gemini' or 'openai')
            headless: Run browser in headless mode
        """
        self.test_cases = self._load_json(test_cases_path)
        self.functional_desc = self._load_json(functional_desc_path)
        self.credentials = self._load_json(credentials_path)
        
        self.llm = LLMClient(api_key=api_key, provider=provider)
        self.browser = BrowserSession()
        self.headless = headless
        
        # Results
        self.enhanced_test_cases: List[Dict] = []
        self.enhanced_functional_desc: Dict = {}
        self.all_issues: List[Dict] = []
        self.navigation_context = NavigationContext(
            current_page="",
            current_url="",
            visited_pages=[],
            navigation_map={}
        )
        
    def _load_json(self, path: str) -> Dict:
        """Load JSON file"""
        with open(path, 'r') as f:
            return json.load(f)
    
    def _save_json(self, data: Dict, path: str):
        """Save JSON file"""
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def _get_page_state(self) -> Dict[str, Any]:
        """Get current page state from browser"""
        page = self.browser.get_current_page()
        if not page:
            return {"error": "No active page"}
        
        return {
            "url": page.url,
            "title": page.title(),
            "elements": self.browser.get_element_tree_string(refresh=True)
        }
    
    def _group_test_cases_by_module(self) -> Dict[str, List[Dict]]:
        """Group test cases by module title"""
        grouped = {}
        
        test_cases_list = self.test_cases.get('test_cases', [])
        
        for tc in test_cases_list:
            module = tc.get('module_title', 'Unknown')
            if module not in grouped:
                grouped[module] = []
            grouped[module].append(tc)
        
        return grouped
    
    def _get_module_func_desc(self, module_title: str) -> Optional[Dict]:
        """Get functional description for a specific module"""
        modules = self.functional_desc.get('modules', [])
        for module in modules:
            if module.get('title', '').lower() == module_title.lower():
                return module
        return None
    
    def _navigate_to_module(self, module_title: str) -> bool:
        """Navigate to a module's page using navigation map or known paths"""
        module_lower = module_title.lower()
        
        # Check if we have this in navigation map
        if module_lower in self.navigation_context.navigation_map:
            url = self.navigation_context.navigation_map[module_lower].get('url')
            if url:
                self.browser.navigate_to(url)
                return True
        
        # Try to find link on current page
        page_state = self._get_page_state()
        elements = page_state.get('elements', '')
        
        # Use LLM to find the right link to click
        # For now, try common patterns
        page = self.browser.get_current_page()
        if page:
            try:
                # Try clicking on link with module name
                page.click(f"text={module_title}", timeout=3000)
                page.wait_for_load_state("networkidle", timeout=5000)
                return True
            except:
                pass
        
        return False
    
    def _verify_single_test_case(
        self,
        test_case: Dict,
        page_state: Dict,
        func_desc: Dict
    ) -> VerificationResult:
        """Verify and enhance a single test case"""
        
        prompt = get_test_case_verification_prompt(
            page_state=page_state,
            test_case=test_case,
            functional_desc=func_desc,
            navigation_context=self.navigation_context.to_dict()
        )
        
        response = self.llm.ask(prompt)
        
        try:
            # Parse JSON response
            result = self._parse_llm_json(response)
            
            return VerificationResult(
                original_test_case=test_case,
                enhanced_test_case=result.get('enhanced_test_case', test_case),
                issues_found=result.get('issues_found', []),
                navigation_update=result.get('navigation_update', {}),
                verification_status=result.get('verification_status', 'needs_review')
            )
        except Exception as e:
            print(f"Error parsing verification result: {e}")
            return VerificationResult(
                original_test_case=test_case,
                enhanced_test_case=test_case,
                issues_found=[{"issue": f"Parse error: {str(e)}", "severity": "high"}],
                navigation_update={},
                verification_status='needs_review'
            )
    
    def _enhance_functional_description(
        self,
        module_func_desc: Dict,
        page_state: Dict,
        issues_collected: List[Dict]
    ) -> Dict:
        """Enhance functional description based on collected issues and page state"""
        
        prompt = get_functional_desc_enhancement_prompt(
            page_state=page_state,
            original_func_desc=module_func_desc,
            issues_found=issues_collected,
            navigation_context=self.navigation_context.to_dict()
        )
        
        response = self.llm.ask(prompt)
        
        try:
            result = self._parse_llm_json(response)
            return result.get('enhanced_functional_description', module_func_desc)
        except Exception as e:
            print(f"Error parsing functional desc enhancement: {e}")
            return module_func_desc
    
    def _parse_llm_json(self, response: str) -> Dict:
        """Parse JSON from LLM response, handling markdown code blocks"""
        response = response.strip()
        
        # Remove markdown code blocks
        if "```json" in response:
            start = response.find("```json") + 7
            end = response.find("```", start)
            if end != -1:
                response = response[start:end].strip()
        elif "```" in response:
            start = response.find("```") + 3
            end = response.find("```", start)
            if end != -1:
                response = response[start:end].strip()
        
        return json.loads(response)
    
    def run(self) -> Dict[str, Any]:
        """
        Run the complete verification pipeline.
        
        Returns:
            Dict with enhanced test cases, functional description, navigation map, and issues
        """
        print("=" * 60)
        print("STARTING VERIFICATION PIPELINE")
        print("=" * 60)
        
        # Initialize browser
        start_url = self.functional_desc.get('website_url', '')
        if not start_url:
            raise ValueError("No website_url in functional description")
        
        print(f"\n1. Navigating to: {start_url}")
        page = self.browser.get_current_page()
        self.browser.navigate_to(start_url)
        
        # Update navigation context
        self.navigation_context.current_url = start_url
        self.navigation_context.current_page = "login"
        self.navigation_context.visited_pages.append("login")
        
        # Group test cases by module
        grouped_tcs = self._group_test_cases_by_module()
        print(f"\n2. Found {len(grouped_tcs)} modules to process")
        
        enhanced_modules = []
        
        # Process each module
        for module_title, module_tcs in grouped_tcs.items():
            print(f"\n{'='*40}")
            print(f"Processing Module: {module_title}")
            print(f"Test Cases: {len(module_tcs)}")
            print(f"{'='*40}")
            
            # Get functional description for this module
            module_func_desc = self._get_module_func_desc(module_title)
            if not module_func_desc:
                print(f"  ⚠️ No functional description found for {module_title}")
                module_func_desc = {"title": module_title, "description": ""}
            
            # Navigate to module page (if not already there)
            # For login page, we're already there
            if module_title.lower() != "login":
                print(f"  → Navigating to {module_title} page...")
                self._navigate_to_module(module_title)
            
            # Get current page state
            page_state = self._get_page_state()
            print(f"  Current URL: {page_state.get('url', 'unknown')}")
            
            # Collect issues for this module
            module_issues = []
            
            # STEP 1: Fix test cases one by one
            print(f"\n  Processing test cases:")
            for i, tc in enumerate(module_tcs, 1):
                tc_id = tc.get('id', f'TC-{i}')
                print(f"    [{i}/{len(module_tcs)}] {tc_id}: {tc.get('title', 'No title')[:40]}...")
                
                result = self._verify_single_test_case(
                    test_case=tc,
                    page_state=page_state,
                    func_desc=module_func_desc
                )
                
                # Store enhanced test case
                self.enhanced_test_cases.append(result.enhanced_test_case)
                
                # Collect issues
                module_issues.extend(result.issues_found)
                self.all_issues.extend(result.issues_found)
                
                # Update navigation
                self.navigation_context.update_from_result(result.navigation_update)
                
                # Status indicator
                status_icon = {
                    'passed': '✓',
                    'fixed': '🔧',
                    'needs_review': '⚠️'
                }.get(result.verification_status, '?')
                print(f"      Status: {status_icon} {result.verification_status}")
                
                if result.issues_found:
                    for issue in result.issues_found:
                        print(f"      Issue: {issue.get('issue', '')[:50]}...")
            
            # STEP 2: Fix functional description (after all TCs)
            print(f"\n  Enhancing functional description for {module_title}...")
            enhanced_module = self._enhance_functional_description(
                module_func_desc=module_func_desc,
                page_state=page_state,
                issues_collected=module_issues
            )
            enhanced_modules.append(enhanced_module)
            print(f"  ✓ Functional description enhanced")
        
        # Build final output
        self.enhanced_functional_desc = {
            "project_name": self.functional_desc.get('project_name', ''),
            "website_url": self.functional_desc.get('website_url', ''),
            "navigation_overview": self.functional_desc.get('navigation_overview', ''),
            "modules": enhanced_modules
        }
        
        # Close browser
        self.browser.close()
        
        print("\n" + "=" * 60)
        print("VERIFICATION COMPLETE")
        print("=" * 60)
        print(f"  Enhanced Test Cases: {len(self.enhanced_test_cases)}")
        print(f"  Enhanced Modules: {len(enhanced_modules)}")
        print(f"  Total Issues Found: {len(self.all_issues)}")
        print(f"  Pages in Navigation Map: {len(self.navigation_context.navigation_map)}")
        
        return {
            'enhanced_test_cases': self.enhanced_test_cases,
            'enhanced_functional_description': self.enhanced_functional_desc,
            'navigation_map': self.navigation_context.navigation_map,
            'all_issues': self.all_issues
        }
    
    def save_results(self, output_dir: str = "output/enhanced"):
        """Save all enhanced results to files"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Save enhanced test cases
        self._save_json(
            {'test_cases': self.enhanced_test_cases},
            os.path.join(output_dir, 'enhanced-test-cases.json')
        )
        
        # Save enhanced functional description
        self._save_json(
            self.enhanced_functional_desc,
            os.path.join(output_dir, 'enhanced-functional-desc.json')
        )
        
        # Save navigation map
        self._save_json(
            self.navigation_context.navigation_map,
            os.path.join(output_dir, 'navigation-map.json')
        )
        
        # Save issues
        self._save_json(
            {'issues': self.all_issues},
            os.path.join(output_dir, 'issues-found.json')
        )
        
        print(f"\nResults saved to: {output_dir}/")


def main():
    """Main entry point for the verifier pipeline"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Verify and enhance test cases')
    parser.add_argument('--test-cases', required=True, help='Path to test-cases.json')
    parser.add_argument('--func-desc', required=True, help='Path to functional description JSON')
    parser.add_argument('--credentials', required=True, help='Path to credentials.json')
    parser.add_argument('--api-key', required=True, help='LLM API key')
    parser.add_argument('--provider', default='gemini', choices=['gemini', 'openai'], help='LLM provider')
    parser.add_argument('--headless', action='store_true', help='Run browser in headless mode')
    parser.add_argument('--output-dir', default='output/enhanced', help='Output directory')
    
    args = parser.parse_args()
    
    pipeline = VerifierPipeline(
        test_cases_path=args.test_cases,
        functional_desc_path=args.func_desc,
        credentials_path=args.credentials,
        api_key=args.api_key,
        provider=args.provider,
        headless=args.headless
    )
    
    results = pipeline.run()
    pipeline.save_results(args.output_dir)


if __name__ == "__main__":
    main()
