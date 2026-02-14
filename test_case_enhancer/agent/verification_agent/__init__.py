"""
Verification Agent Package
"""

from .prompts import (
    get_test_case_verification_prompt,
    get_functional_desc_enhancement_prompt
)

__all__ = [
    'get_test_case_verification_prompt',
    'get_functional_desc_enhancement_prompt'
]
