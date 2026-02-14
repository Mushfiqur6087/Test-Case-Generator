#!/usr/bin/env python3
"""
Main entry point for the Test Case Verifier/Enhancer.
Run this script to verify and enhance generated test cases against the actual website.
"""

import os
import sys
import argparse

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from test_case_enhancer.verifier_pipeline import VerifierPipeline


def main():
    parser = argparse.ArgumentParser(
        description='Verify and enhance test cases by comparing against actual website',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
  python run_verifier.py --api-key YOUR_KEY
  python run_verifier.py --api-key YOUR_KEY --provider openai
  python run_verifier.py --api-key YOUR_KEY --headless
        """
    )
    
    parser.add_argument(
        '--test-cases', 
        default='output/test-cases.json',
        help='Path to generated test-cases.json (default: output/test-cases.json)'
    )
    parser.add_argument(
        '--func-desc', 
        default='parabank.json',
        help='Path to functional description JSON (default: parabank.json)'
    )
    parser.add_argument(
        '--credentials', 
        default='credentials.json',
        help='Path to credentials.json (default: credentials.json)'
    )
    parser.add_argument(
        '--api-key', 
        required=True,
        help='API key for LLM (Gemini or OpenAI)'
    )
    parser.add_argument(
        '--provider', 
        default='gemini',
        choices=['gemini', 'openai'],
        help='LLM provider (default: gemini)'
    )
    parser.add_argument(
        '--headless', 
        action='store_true',
        help='Run browser in headless mode'
    )
    parser.add_argument(
        '--output-dir', 
        default='output/enhanced',
        help='Output directory for enhanced files (default: output/enhanced)'
    )
    
    args = parser.parse_args()
    
    # Validate paths
    if not os.path.exists(args.test_cases):
        print(f"❌ Error: Test cases file not found: {args.test_cases}")
        sys.exit(1)
    
    if not os.path.exists(args.func_desc):
        print(f"❌ Error: Functional description file not found: {args.func_desc}")
        sys.exit(1)
    
    if not os.path.exists(args.credentials):
        print(f"❌ Error: Credentials file not found: {args.credentials}")
        sys.exit(1)
    
    print("=" * 60)
    print("TEST CASE VERIFIER & ENHANCER")
    print("=" * 60)
    print(f"Test Cases:    {args.test_cases}")
    print(f"Func Desc:     {args.func_desc}")
    print(f"Credentials:   {args.credentials}")
    print(f"LLM Provider:  {args.provider}")
    print(f"Headless:      {args.headless}")
    print(f"Output Dir:    {args.output_dir}")
    print("=" * 60)
    
    try:
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
        
        print("\n✅ Verification complete!")
        print(f"   Results saved to: {args.output_dir}/")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Verification interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
