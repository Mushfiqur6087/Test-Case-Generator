"""
Verification Agent Prompts - For test case verification and functional description enhancement
"""

import json
from typing import Dict, Any, List


def get_test_case_verification_prompt(
    page_state: Dict[str, Any],
    test_case: Dict[str, Any],
    functional_desc: Dict[str, Any],
    navigation_context: Dict[str, Any]
) -> str:
    """
    Generate prompt for verifying and enhancing a single test case.
    
    Args:
        page_state: Current page URL, title, and elements
        test_case: The test case to verify
        functional_desc: Module's functional description
        navigation_context: Current navigation state
    
    Returns:
        Prompt string for LLM
    """
    
    return f"""You are a test case verification agent. Your job is to verify ONE test case against the actual webpage and fix any issues.

## CURRENT PAGE STATE

**URL:** {page_state.get('url', 'Unknown')}
**Title:** {page_state.get('title', 'Unknown')}

**Page Elements (DOM Tree):**
```
{page_state.get('elements', 'No elements available')}
```

## CURRENT NAVIGATION CONTEXT

```json
{json.dumps(navigation_context, indent=2)}
```

## FUNCTIONAL DESCRIPTION (for reference)

**Module:** {functional_desc.get('title', 'Unknown')}
**Description:** {functional_desc.get('description', 'No description')}

## TEST CASE TO VERIFY

```json
{json.dumps(test_case, indent=2)}
```

## YOUR TASKS

### 1. VERIFY TEST CASE STEPS
For each step in the test case, check:
- Does the element/field mentioned actually exist on the page?
- Is the action (click, input, select) possible with the elements available?
- Are the field names correct (e.g., "Username" vs "Email")?

### 2. VERIFY EXPECTED RESULT
- Is the expected result realistic based on what the page can do?
- Does it match typical behavior for this type of action?

### 3. FIX ANY ISSUES
If you find issues:
- Correct field names to match actual page elements
- Fix steps that reference non-existent elements
- Update expected results if needed
- Add any missing preconditions

### 4. UPDATE NAVIGATION INFO
Based on what you see on the page:
- What links/buttons are available for navigation?
- What pages can be reached from here?
- Does this page require authentication?

## OUTPUT FORMAT

Return ONLY valid JSON in this exact format:

```json
{{
  "enhanced_test_case": {{
    "id": "{test_case.get('id', 'TC-001')}",
    "title": "The test case title (fixed if needed)",
    "module_title": "{test_case.get('module_title', 'Unknown')}",
    "test_type": "{test_case.get('test_type', 'positive')}",
    "preconditions": "Fixed preconditions",
    "steps": [
      "Step 1 - corrected to match actual page",
      "Step 2 - corrected to match actual page"
    ],
    "expected_result": "Fixed expected result",
    "priority": "{test_case.get('priority', 'Medium')}",
    "changes_made": [
      "Description of change 1",
      "Description of change 2"
    ]
  }},
  "navigation_update": {{
    "current_page": "login",
    "current_url": "{page_state.get('url', '')}",
    "available_links": [
      {{"text": "Link text", "likely_destination": "page-name"}},
      {{"text": "Another link", "likely_destination": "other-page"}}
    ],
    "requires_auth": false
  }},
  "issues_found": [
    {{
      "issue": "Description of the issue found",
      "severity": "low|medium|high",
      "fixed": true,
      "original_value": "what it was",
      "corrected_value": "what it should be"
    }}
  ],
  "verification_status": "passed|fixed|needs_review"
}}
```

**Verification Status:**
- `passed`: Test case is correct, no changes needed
- `fixed`: Found issues and fixed them
- `needs_review`: Found issues that require human review

Return ONLY the JSON, no other text."""


def get_functional_desc_enhancement_prompt(
    page_state: Dict[str, Any],
    original_func_desc: Dict[str, Any],
    issues_found: List[Dict[str, Any]],
    navigation_context: Dict[str, Any]
) -> str:
    """
    Generate prompt for enhancing functional description based on collected issues.
    
    Args:
        page_state: Current page URL, title, and elements
        original_func_desc: Original functional description for the module
        issues_found: All issues collected from test case verification
        navigation_context: Current navigation state
    
    Returns:
        Prompt string for LLM
    """
    
    return f"""You are a functional description enhancement agent. Your job is to update the functional description to accurately reflect the actual webpage.

## CURRENT PAGE STATE

**URL:** {page_state.get('url', 'Unknown')}
**Title:** {page_state.get('title', 'Unknown')}

**Page Elements (DOM Tree):**
```
{page_state.get('elements', 'No elements available')}
```

## CURRENT NAVIGATION CONTEXT

```json
{json.dumps(navigation_context, indent=2)}
```

## ORIGINAL FUNCTIONAL DESCRIPTION

```json
{json.dumps(original_func_desc, indent=2)}
```

## ISSUES FOUND DURING TEST CASE VERIFICATION

These issues were discovered when verifying test cases against the actual page:

```json
{json.dumps(issues_found, indent=2)}
```

## YOUR TASKS

### 1. ANALYZE THE PAGE
Look at the actual page elements and identify:
- What fields/inputs are actually present
- What buttons/actions are available
- What links exist for navigation
- What the page actually does

### 2. UPDATE FUNCTIONAL DESCRIPTION
Based on the actual page and collected issues:
- Fix any incorrect field names (e.g., "Email" → "Username")
- Add any missing fields or features
- Remove any features that don't exist
- Update the description to be accurate

### 3. ADD STRUCTURAL INFO
Enhance the description with:
- List of actual form fields with their requirements
- Available actions/buttons
- Navigation links from this page
- Any validation messages visible

## OUTPUT FORMAT

Return ONLY valid JSON in this exact format:

```json
{{
  "enhanced_functional_description": {{
    "id": {original_func_desc.get('id', 1)},
    "title": "{original_func_desc.get('title', 'Unknown')}",
    "description": "Updated accurate description based on actual page",
    "actual_url": "{page_state.get('url', '')}",
    "fields": [
      {{
        "name": "Field Name",
        "type": "text|password|dropdown|button",
        "required": true,
        "label_on_page": "Actual label shown"
      }}
    ],
    "available_actions": [
      {{
        "name": "Action name",
        "element_type": "button|link",
        "text_on_page": "Actual button/link text"
      }}
    ],
    "navigation_links": [
      {{
        "text": "Link text",
        "destination": "Where it likely goes"
      }}
    ],
    "changes_made": [
      "Change 1: what was fixed",
      "Change 2: what was added"
    ]
  }}
}}
```

Return ONLY the JSON, no other text."""
