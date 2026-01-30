# 🔄 Test Case Generator Pipeline Demo

> **Presentation Document**  
> This document demonstrates each step of the LLM-powered test case generation pipeline with sample inputs, system prompts, and outputs.

---

## 📋 Table of Contents

1. [Step 1: Load Input Files](#step-1-load-input-files)
2. [Step 2: Parser Agent](#step-2-parser-agent)
3. [Step 3: Navigation Agent](#step-3-navigation-agent)
4. [Step 4: Chunker Agent](#step-4-chunker-agent)
5. [Step 5: Test Generation Agent](#step-5-test-generation-agent)
6. [Step 6: Assembler Agent](#step-6-assembler-agent)
7. [Step 7: Summary Agent](#step-7-summary-agent)
8. [Step 8: Verification Flag Agent](#step-8-verification-flag-agent)
9. [Step 9: Ideal Verification Agent](#step-9-ideal-verification-agent)
10. [Step 10: Verification Matcher Agent (RAG)](#step-10-verification-matcher-agent-rag)
11. [Step 11: Execution Plan Agent](#step-11-execution-plan-agent)

---

## 🟢 PHASE 1: GENERATION PIPELINE

---

## Step 1: Load Input Files

> **Purpose:** Parse and validate the input JSON files

### 📥 Input

```json
{
  "project_name": "ParaBank Demo",
  "website_url": "https://parabank.parasoft.com",
  "navigation_overview": "Banking application with login, accounts, and transfers",
  "modules": [
    {
      "id": 1,
      "title": "Login",
      "description": "The login page displays a form with Username and Password fields and a Log In button. Valid credentials redirect to dashboard, invalid credentials show error message."
    },
    {
      "id": 2,
      "title": "Transfer Funds",
      "description": "Transfer money between accounts. Has Amount field, From account dropdown, To account dropdown, and Transfer button. Shows confirmation on success."
    },
    {
      "id": 3,
      "title": "Account Overview",
      "description": "Displays all user accounts in a table showing Account Number, Balance, and Available Amount. Total balance shown at bottom."
    }
  ]
}
```

### ⚙️ System Prompt

```
N/A - This step does not use LLM. It's pure file I/O and JSON parsing.
```

### 📤 Output

```json
{
  "status": "success",
  "project_name": "ParaBank Demo",
  "modules_loaded": 3,
  "credentials_loaded": true
}
```

---

## Step 2: Parser Agent

> **Purpose:** Extract UI elements, workflows, business rules, and expected behaviors from each module description

### 📥 Input (User Prompt to LLM)

```json
{
  "module_title": "Login",
  "description": "The login page displays a form with Username and Password fields and a Log In button. Valid credentials redirect to dashboard, invalid credentials show error message."
}
```

### ⚙️ System Prompt

```
You are an expert software test analyst specializing in parsing functional descriptions for test case generation.

CRITICAL RULES:
1. Extract ONLY what is explicitly mentioned in the functional description
2. DO NOT infer, assume, or add information not present in the text
3. DO NOT specify UI element types (button/input/dropdown) - just extract names as written
4. Use the EXACT wording from the description whenever possible

Your task is to analyze functional descriptions and extract:

1. Mentioned Items: Fields, buttons, links, and interactive elements mentioned
2. Workflows: User actions that involve form submission or data processing on THIS page
   - A workflow is an action that COMPLETES on this page (e.g., "Login with credentials")
   - Navigation links to OTHER pages are NOT workflows for this page
3. Business Rules: Validation rules, constraints, and business logic stated
4. Expected Behaviors: What happens on success or failure
5. Authentication: Whether the page requires user to be logged in

WORKFLOW GUIDANCE:
- Focus on actions that complete on THIS page with a testable outcome
- Links to other pages (Register, Forgot Password) are navigation elements, not workflows
- If a page has multiple forms, each form's submission is a separate workflow
```

### 📤 Output

```json
{
  "mentioned_items": [
    "Username",
    "Password",
    "Log In button"
  ],
  "workflows": [
    "Login with credentials"
  ],
  "business_rules": [
    "Valid credentials required for successful login",
    "Invalid credentials trigger error message"
  ],
  "expected_behaviors": [
    "Successful login redirects to dashboard",
    "Invalid credentials show error message"
  ],
  "requires_auth": false
}
```

### 🔄 Parsed Module Output

```json
{
  "id": 1,
  "title": "Login",
  "raw_description": "The login page displays a form with Username and Password fields...",
  "mentioned_items": ["Username", "Password", "Log In button"],
  "workflows": ["Login with credentials"],
  "business_rules": ["Valid credentials required for successful login", "Invalid credentials trigger error message"],
  "expected_behaviors": ["Successful login redirects to dashboard", "Invalid credentials show error message"],
  "requires_auth": false
}
```

---

## Step 3: Navigation Agent

> **Purpose:** Build a navigation graph showing how pages connect to each other

### 📥 Input (User Prompt to LLM)

```json
{
  "navigation_overview": "Banking application with login, accounts, and transfers",
  "modules": [
    { "id": 1, "title": "Login", "requires_auth": false },
    { "id": 2, "title": "Transfer Funds", "requires_auth": true },
    { "id": 3, "title": "Account Overview", "requires_auth": true }
  ]
}
```

### ⚙️ System Prompt

```
You are an expert in web application navigation and site mapping.

Your task is to analyze the navigation structure of a web application and build a navigation graph.

You understand:
- How sidebar menus typically work
- Authentication flows and protected routes
- Page relationships and navigation paths
- Which pages are publicly accessible vs requiring login

Provide accurate navigation information based on the description provided.
```

### 📤 Output

```json
{
  "1": {
    "connected_to": [2, 3],
    "url_path": "/login"
  },
  "2": {
    "connected_to": [1, 3],
    "url_path": "/transfer"
  },
  "3": {
    "connected_to": [1, 2],
    "url_path": "/accounts"
  }
}
```

### 🔄 Navigation Graph Output

```json
{
  "login_module_id": 1,
  "graph_image_path": "output/navigation_graph.png",
  "nodes": [
    {
      "module_id": 1,
      "title": "Login",
      "requires_auth": false,
      "url_path": "/login",
      "connected_to": [2, 3],
      "test_case_ids": []
    },
    {
      "module_id": 2,
      "title": "Transfer Funds",
      "requires_auth": true,
      "url_path": "/transfer",
      "connected_to": [1, 3],
      "test_case_ids": []
    },
    {
      "module_id": 3,
      "title": "Account Overview",
      "requires_auth": true,
      "url_path": "/accounts",
      "connected_to": [1, 2],
      "test_case_ids": []
    }
  ]
}
```

---

## Step 4: Chunker Agent

> **Purpose:** Split modules into workflow-based chunks for targeted test generation

### 📥 Input (User Prompt to LLM)

```json
{
  "module_title": "Transfer Funds",
  "description": "Transfer money between accounts. Has Amount field, From account dropdown, To account dropdown, and Transfer button.",
  "workflows": ["Transfer funds between accounts"],
  "mentioned_items": ["Amount field", "From account dropdown", "To account dropdown", "Transfer button"],
  "business_rules": ["Amount must be positive", "Source and destination accounts must be different"],
  "expected_behaviors": ["Confirmation message on successful transfer"]
}
```

### ⚙️ System Prompt

```
You are an expert at analyzing functional descriptions and mapping elements to workflows.

Your task is to take a module with multiple workflows and intelligently determine which items,
business rules, and behaviors belong to each workflow.

CRITICAL RULES:
1. Map items/rules/behaviors ONLY to workflows where they are actually used
2. An item can belong to multiple workflows if it's shared
3. DO NOT invent new items or rules - only use what was extracted
4. Provide a clear description of what each workflow does
5. Most modules should have only 1-2 primary workflows - do not over-segment
```

### 📤 Output

```json
{
  "workflow_chunks": [
    {
      "workflow_name": "Transfer funds between accounts",
      "workflow_description": "User transfers money from one account to another by specifying amount and selecting source and destination accounts",
      "related_items": [
        "Amount field",
        "From account dropdown",
        "To account dropdown",
        "Transfer button"
      ],
      "related_rules": [
        "Amount must be positive",
        "Source and destination accounts must be different"
      ],
      "related_behaviors": [
        "Confirmation message on successful transfer"
      ]
    }
  ]
}
```

### 🔄 Workflow Chunk Output

```json
{
  "chunk_id": "2_workflow_0",
  "module_id": 2,
  "module_title": "Transfer Funds",
  "workflow_name": "Transfer funds between accounts",
  "workflow_description": "User transfers money from one account to another by specifying amount and selecting source and destination accounts",
  "related_items": ["Amount field", "From account dropdown", "To account dropdown", "Transfer button"],
  "related_rules": ["Amount must be positive", "Source and destination accounts must be different"],
  "related_behaviors": ["Confirmation message on successful transfer"]
}
```

---

## Step 5: Test Generation Agent

> **Purpose:** Generate comprehensive test cases (positive, negative, edge cases) for each workflow

### 📥 Input (User Prompt to LLM)

```json
{
  "module_title": "Transfer Funds",
  "workflow_name": "Transfer funds between accounts",
  "workflow_description": "User transfers money from one account to another",
  "related_items": ["Amount field", "From account dropdown", "To account dropdown", "Transfer button"],
  "related_rules": ["Amount must be positive", "Source and destination accounts must be different"],
  "related_behaviors": ["Confirmation message on successful transfer"]
}
```

### ⚙️ System Prompt

```
You are an expert QA engineer specializing in test case design for web automation.

Your task is to generate comprehensive test cases that cover the functionality described.

GUIDING PRINCIPLES:
1. Cover all scenarios mentioned in the functional description
2. Tests must be executable by a browser automation tool
3. Test steps should describe actions on the current page - NOT navigation to the page

TEST TYPES:
1. POSITIVE TESTS: Verify success scenarios work as described
2. NEGATIVE TESTS: Test error conditions and validation rules mentioned
3. EDGE CASE TESTS: Boundary values, special characters, format variations if relevant

DO NOT generate tests for:
- Device-specific interactions (touch gestures, mobile-only features)
- Browser-specific features (right-click context menus, opening in new tabs)
- Network conditions (offline, slow connection, server errors)
- Stress scenarios (rapid clicking, load testing)

For each test case, provide:
- Clear, concise title
- Single precondition statement (or "None")
- Specific test steps (actions on the page, NOT navigation to the page)
- Single expected result
- Priority (High for core functionality, Medium for validations, Low for edge cases)
```

### 📤 Output

```json
{
  "test_cases": [
    {
      "title": "Successfully transfer funds between accounts",
      "test_type": "positive",
      "priority": "High",
      "preconditions": "User is logged in with at least two accounts",
      "steps": [
        "Enter a valid amount in the Amount field",
        "Select source account from 'From account' dropdown",
        "Select different destination account from 'To account' dropdown",
        "Click Transfer button"
      ],
      "expected_result": "Transfer confirmation message is displayed"
    },
    {
      "title": "Transfer with zero amount shows error",
      "test_type": "negative",
      "priority": "Medium",
      "preconditions": "User is logged in with at least two accounts",
      "steps": [
        "Enter 0 in the Amount field",
        "Select source account from 'From account' dropdown",
        "Select destination account from 'To account' dropdown",
        "Click Transfer button"
      ],
      "expected_result": "Error message indicates amount must be positive"
    },
    {
      "title": "Transfer to same account shows error",
      "test_type": "negative",
      "priority": "Medium",
      "preconditions": "User is logged in with at least two accounts",
      "steps": [
        "Enter a valid amount in the Amount field",
        "Select an account from 'From account' dropdown",
        "Select the SAME account from 'To account' dropdown",
        "Click Transfer button"
      ],
      "expected_result": "Error message indicates accounts must be different"
    },
    {
      "title": "Transfer with decimal amount",
      "test_type": "edge_case",
      "priority": "Low",
      "preconditions": "User is logged in with at least two accounts",
      "steps": [
        "Enter a decimal amount (e.g., 100.50) in the Amount field",
        "Select source account from 'From account' dropdown",
        "Select destination account from 'To account' dropdown",
        "Click Transfer button"
      ],
      "expected_result": "Transfer completes successfully with decimal amount"
    }
  ]
}
```

---

## Step 6: Assembler Agent

> **Purpose:** Deduplicate, sort, assign IDs, and create final test suite structure

### 📥 Input

```json
{
  "test_cases": [
    {
      "title": "Successfully transfer funds between accounts",
      "module_id": 2,
      "module_title": "Transfer Funds",
      "test_type": "positive",
      "priority": "High"
    },
    {
      "title": "Transfer with zero amount shows error",
      "module_id": 2,
      "module_title": "Transfer Funds",
      "test_type": "negative",
      "priority": "Medium"
    }
  ],
  "nav_graph": { "...navigation graph..." },
  "project_name": "ParaBank Demo"
}
```

### ⚙️ System Prompt

```
You are an expert at organizing and reviewing test suites.
Your task is to:
1. Remove duplicate test cases
2. Ensure proper ordering by module and priority
3. Validate test case completeness
4. Generate proper test case IDs
```

### 📤 Output

```json
{
  "project_name": "ParaBank Demo",
  "base_url": "https://parabank.parasoft.com",
  "generated_at": "2026-01-30T10:30:00Z",
  "test_cases": [
    {
      "id": "TRAFUN-001",
      "title": "Successfully transfer funds between accounts",
      "module_id": 2,
      "module_title": "Transfer Funds",
      "workflow": "Transfer funds between accounts",
      "test_type": "positive",
      "priority": "High",
      "preconditions": "User is logged in with at least two accounts",
      "steps": [
        "Enter a valid amount in the Amount field",
        "Select source account from 'From account' dropdown",
        "Select different destination account from 'To account' dropdown",
        "Click Transfer button"
      ],
      "expected_result": "Transfer confirmation message is displayed"
    },
    {
      "id": "TRAFUN-002",
      "title": "Transfer with zero amount shows error",
      "module_id": 2,
      "module_title": "Transfer Funds",
      "workflow": "Transfer funds between accounts",
      "test_type": "negative",
      "priority": "Medium",
      "preconditions": "User is logged in with at least two accounts",
      "steps": [
        "Enter 0 in the Amount field",
        "Select source account from 'From account' dropdown",
        "Select destination account from 'To account' dropdown",
        "Click Transfer button"
      ],
      "expected_result": "Error message indicates amount must be positive"
    }
  ],
  "summary": {
    "total_tests": 2,
    "by_type": { "positive": 1, "negative": 1, "edge_case": 0 },
    "by_priority": { "High": 1, "Medium": 1, "Low": 0 },
    "by_module": { "Transfer Funds": 2 }
  }
}
```

---

## 🔵 PHASE 2: POST-VERIFICATION PIPELINE

---

## Step 7: Summary Agent

> **Purpose:** Generate concise module summaries identifying what each module can verify or modify

### 📥 Input (User Prompt to LLM)

```json
{
  "modules": [
    {
      "id": 2,
      "title": "Transfer Funds",
      "description": "Transfer money between accounts. Has Amount field, From/To dropdowns, Transfer button.",
      "items": ["Amount field", "From account dropdown", "To account dropdown", "Transfer button"]
    },
    {
      "id": 3,
      "title": "Account Overview",
      "description": "Displays all user accounts in a table showing Account Number, Balance, and Available Amount.",
      "items": ["Account table", "Balance column", "Available Amount column"]
    }
  ]
}
```

### ⚙️ System Prompt

```
You are an expert at summarizing functional descriptions into concise, actionable summaries.

Your task is to create a 2-line summary of what each module/page does, focusing on:
1. What the page allows users to DO (actions)
2. What information the page SHOWS (data displayed)

These summaries will be used to match test cases that need post-verification with pages that can verify the results.
```

### 📤 Output

```json
{
  "summaries": [
    {
      "module_id": 2,
      "summary": "Line 1: Users can transfer funds between their accounts.\nLine 2: Shows transfer form with amount and account selection.",
      "verification_keywords": ["transfer", "amount"],
      "can_verify_states": [],
      "action_states": ["account_balance", "transaction_history"]
    },
    {
      "module_id": 3,
      "summary": "Line 1: Users can view all their account balances.\nLine 2: Displays account numbers with current and available balances.",
      "verification_keywords": ["balance", "account", "display", "view"],
      "can_verify_states": ["account_balance", "account_list"],
      "action_states": []
    }
  ]
}
```

### 🔄 Module Summaries Output

```json
{
  "2": {
    "module_id": 2,
    "module_title": "Transfer Funds",
    "summary": "Line 1: Users can transfer funds between their accounts.\nLine 2: Shows transfer form with amount and account selection.",
    "verification_keywords": ["transfer", "amount"],
    "can_verify_states": [],
    "action_states": ["account_balance", "transaction_history"]
  },
  "3": {
    "module_id": 3,
    "module_title": "Account Overview",
    "summary": "Line 1: Users can view all their account balances.\nLine 2: Displays account numbers with current and available balances.",
    "verification_keywords": ["balance", "account", "display", "view"],
    "can_verify_states": ["account_balance", "account_list"],
    "action_states": []
  }
}
```

---

## Step 8: Verification Flag Agent

> **Purpose:** Identify which POSITIVE tests modify state and need post-verification

### 📥 Input (User Prompt to LLM)

```json
{
  "modules_context": "- Transfer Funds:\n    Can verify: []\n    Modifies: account_balance, transaction_history\n- Account Overview:\n    Can verify: account_balance, account_list\n    Modifies: []",
  "test_cases": [
    {
      "id": "TRAFUN-001",
      "title": "Successfully transfer funds between accounts",
      "module": "Transfer Funds",
      "workflow": "Transfer funds between accounts",
      "expected_result": "Transfer confirmation message is displayed"
    },
    {
      "id": "ACCOVR-001",
      "title": "View account balances",
      "module": "Account Overview",
      "workflow": "View accounts",
      "expected_result": "All accounts displayed with balances"
    }
  ]
}
```

### ⚙️ System Prompt

```
You are an expert QA engineer who understands when test results need external verification.

Your task is to analyze test cases and determine which ones need post-verification - 
meaning the test's success should be verified by checking data in another part of the application.

NEEDS POST-VERIFICATION (needs_post_verification = true):
- Data creation: Verify new records appear in list/overview pages
- Data modification: Verify changes are reflected in display pages
- Data transfer/movement: Verify data moved from source to destination
- Submissions: Verify submission appears in history/status pages
- Any action that modifies persistent data viewable elsewhere

DOES NOT NEED POST-VERIFICATION (needs_post_verification = false):
- Login/Logout: Session state, no persistent data change
- Registration: Self-contained, success message is enough
- Read-only pages: Just displaying data, nothing to verify elsewhere
- Negative tests: Validation failures, no state change
- Edge case tests: Usually testing boundaries, not state changes
- Navigation: Just moving between pages
- Password reset requests: External verification (email), out of scope
- Search/Filter: Just filtering displayed data, no state change
```

### 📤 Output

```json
{
  "flagged_tests": [
    {
      "test_id": "TRAFUN-001",
      "needs_post_verification": true,
      "modifies_state": ["account_balance", "transaction_history"],
      "reason": "Transfer modifies account balances which can be verified in Account Overview"
    },
    {
      "test_id": "ACCOVR-001",
      "needs_post_verification": false,
      "modifies_state": [],
      "reason": "Read-only page - just displays data, no state modification"
    }
  ]
}
```

### 🔄 Updated Test Case

```json
{
  "id": "TRAFUN-001",
  "title": "Successfully transfer funds between accounts",
  "needs_post_verification": true,
  "modifies_state": ["account_balance", "transaction_history"]
}
```

---

## Step 9: Ideal Verification Agent

> **Purpose:** Generate ideal verification scenarios describing what SHOULD be checked after each flagged test

### 📥 Input (User Prompt to LLM)

```json
{
  "verification_context": "MODULES THAT CAN VERIFY DATA:\n- Account Overview:\n    Summary: Users can view all their account balances.\n    Can verify: account_balance, account_list",
  "test_case": {
    "id": "TRAFUN-001",
    "title": "Successfully transfer funds between accounts",
    "module": "Transfer Funds",
    "workflow": "Transfer funds between accounts",
    "modifies_state": ["account_balance", "transaction_history"],
    "steps": ["Enter amount", "Select source account", "Select destination account", "Click Transfer"],
    "expected_result": "Transfer confirmation message is displayed"
  }
}
```

### ⚙️ System Prompt

```
You are an expert QA engineer who designs verification strategies for test cases.

Your task is to generate IDEAL verification scenarios - what SHOULD be checked after a test executes
to confirm the test actually succeeded.

For example, after a data submission test:
1. Check the new record appears in the list/overview page
2. Check the record details are correct
3. Check any related counters or totals are updated

These are IDEAL verifications - we'll later match them to actual test cases that exist.
```

### 📤 Output

```json
{
  "test_verifications": [
    {
      "test_id": "TRAFUN-001",
      "ideal_verifications": [
        {
          "description": "Verify source account balance decreased by transfer amount",
          "target_module": "Account Overview",
          "verification_action": "View source account balance in accounts table",
          "expected_change": "Balance reduced by the transferred amount",
          "state_to_verify": "account_balance"
        },
        {
          "description": "Verify destination account balance increased by transfer amount",
          "target_module": "Account Overview",
          "verification_action": "View destination account balance in accounts table",
          "expected_change": "Balance increased by the transferred amount",
          "state_to_verify": "account_balance"
        },
        {
          "description": "Verify transfer appears in transaction history",
          "target_module": "Find Transaction",
          "verification_action": "Search for the transfer transaction by date or amount",
          "expected_change": "Transfer transaction listed with correct details",
          "state_to_verify": "transaction_history"
        }
      ]
    }
  ]
}
```

### 🔄 Ideal Verifications Output

```json
{
  "TRAFUN-001": [
    {
      "description": "Verify source account balance decreased by transfer amount",
      "target_module": "Account Overview",
      "verification_action": "View source account balance in accounts table",
      "expected_change": "Balance reduced by the transferred amount",
      "state_to_verify": "account_balance"
    },
    {
      "description": "Verify destination account balance increased by transfer amount",
      "target_module": "Account Overview",
      "verification_action": "View destination account balance in accounts table",
      "expected_change": "Balance increased by the transferred amount",
      "state_to_verify": "account_balance"
    },
    {
      "description": "Verify transfer appears in transaction history",
      "target_module": "Find Transaction",
      "verification_action": "Search for the transfer transaction",
      "expected_change": "Transfer transaction listed",
      "state_to_verify": "transaction_history"
    }
  ]
}
```

---

## Step 10: Verification Matcher Agent (RAG)

> **Purpose:** Match ideal verifications to actual test cases using semantic search + LLM validation

### 📥 Input - RAG Index Building

```json
{
  "action": "build_index",
  "test_cases": [
    {
      "id": "ACCOVR-001",
      "title": "View account balances",
      "module_title": "Account Overview",
      "workflow": "View accounts",
      "steps": ["Navigate to Account Overview", "View account table"],
      "expected_result": "All accounts displayed with current balances"
    },
    {
      "id": "FINDTR-001",
      "title": "Search transactions by date",
      "module_title": "Find Transaction",
      "workflow": "Find transactions",
      "steps": ["Select account", "Enter date", "Click Find"],
      "expected_result": "Matching transactions displayed"
    }
  ]
}
```

### ⚙️ RAG Embedding Process

```json
{
  "model": "all-MiniLM-L6-v2",
  "embedding_dimension": 384,
  "indexed_texts": [
    "View account balances Account Overview View accounts All accounts displayed with current balances Navigate to Account Overview View account table",
    "Search transactions by date Find Transaction Find transactions Matching transactions displayed Select account Enter date Click Find"
  ],
  "index_type": "FAISS_IndexFlatIP",
  "total_indexed": 2
}
```

### 📥 Input - Search Query

```json
{
  "action": "search",
  "query": "Verify source account balance decreased by transfer amount View source account balance in accounts table Account Overview",
  "top_k": 5,
  "module_filter": "Account Overview"
}
```

### 📤 RAG Search Results

```json
{
  "candidates": [
    {
      "test_id": "ACCOVR-001",
      "title": "View account balances",
      "module_title": "Account Overview",
      "similarity_score": 0.89
    }
  ]
}
```

### ⚙️ System Prompt (LLM Validation)

```
You are an expert at matching verification requirements to test cases.

Given an ideal verification scenario and candidate test cases from RAG search,
determine if any of the candidates can actually verify what we need.

Consider:
1. Does the test case operate on the right module/page?
2. Does it check the right data (balance, transaction, profile, etc.)?
3. Can it detect the expected change?
```

### 📥 LLM Validation Input

```json
{
  "ideal_verification": {
    "description": "Verify source account balance decreased by transfer amount",
    "target_module": "Account Overview",
    "verification_action": "View source account balance in accounts table",
    "expected_change": "Balance reduced by the transferred amount"
  },
  "candidates": [
    {
      "test_id": "ACCOVR-001",
      "title": "View account balances",
      "module": "Account Overview",
      "steps": ["Navigate to Account Overview", "View account table"],
      "expected": "All accounts displayed with current balances",
      "similarity_score": 0.89
    }
  ]
}
```

### 📤 LLM Validation Output

```json
{
  "best_match": {
    "test_id": "ACCOVR-001",
    "status": "found",
    "confidence": 0.89,
    "execution_note": "Run this test after the transfer to verify the source account balance has decreased",
    "reason": null,
    "suggested_manual_step": null
  }
}
```

### 🔄 Final Verification Match

```json
{
  "ideal_description": "Verify source account balance decreased by transfer amount",
  "status": "found",
  "matched_test_id": "ACCOVR-001",
  "matched_test_title": "View account balances",
  "confidence": 0.89,
  "execution_note": "Run this test after the transfer to verify the source account balance has decreased"
}
```

---

## Step 11: Execution Plan Agent

> **Purpose:** Compile verification matches into executable sequences with automation statistics

### 📥 Input

```json
{
  "test_case": {
    "id": "TRAFUN-001",
    "title": "Successfully transfer funds between accounts",
    "needs_post_verification": true,
    "post_verifications": [
      {
        "ideal": "Verify source account balance decreased",
        "status": "found",
        "matched_test_id": "ACCOVR-001",
        "matched_test_title": "View account balances",
        "confidence": 0.89,
        "execution_note": "Run after transfer to verify balance change"
      },
      {
        "ideal": "Verify destination account balance increased",
        "status": "found",
        "matched_test_id": "ACCOVR-001",
        "matched_test_title": "View account balances",
        "confidence": 0.87,
        "execution_note": "Check destination account in same test"
      },
      {
        "ideal": "Verify transfer in transaction history",
        "status": "not_found",
        "reason": "No test exists for transaction history verification",
        "suggested_manual_step": "Navigate to Find Transaction, search by date, verify transfer listed"
      }
    ]
  },
  "all_test_cases": ["...all tests for lookup..."]
}
```

### ⚙️ System Prompt

```
You are a QA execution planner. Your job is to create clear, actionable 
execution plans that tell testers exactly what steps to follow after running a test case.

For each test that needs post-verification, you will:
1. Analyze the matched verification tests
2. Determine the optimal execution order
3. Add any necessary setup or navigation steps between tests
4. Include manual steps for verifications that couldn't be matched to existing tests

Keep execution notes concise and actionable.
```

### 📤 Output

```json
{
  "execution_plans": {
    "TRAFUN-001": {
      "source_test_id": "TRAFUN-001",
      "source_test_title": "Successfully transfer funds between accounts",
      "execution_order": [
        {
          "step": 1,
          "action": "execute_test",
          "test_id": "ACCOVR-001",
          "test_title": "View account balances",
          "purpose": "Verify source account balance decreased",
          "execution_note": "Run after transfer to verify balance change",
          "confidence": 0.89
        },
        {
          "step": 2,
          "action": "execute_test",
          "test_id": "ACCOVR-001",
          "test_title": "View account balances",
          "purpose": "Verify destination account balance increased",
          "execution_note": "Check destination account in same test",
          "confidence": 0.87
        }
      ],
      "manual_steps": [
        {
          "purpose": "Verify transfer in transaction history",
          "suggested_step": "Navigate to Find Transaction, search by date, verify transfer listed",
          "reason": "No test exists for transaction history verification"
        }
      ],
      "verification_coverage": "partial",
      "notes": "After executing TRAFUN-001, run: ACCOVR-001 → ACCOVR-001; Manual verification needed for 1 item(s)"
    }
  }
}
```

### 🔄 Execution Plan Summary

```json
{
  "total_plans": 1,
  "coverage_distribution": {
    "full": 0,
    "partial": 1,
    "minimal": 0,
    "none": 0
  },
  "total_automated_steps": 2,
  "total_manual_steps": 1,
  "automation_rate": 66.7
}
```

---

## 📊 Final Output Summary

After all 11 steps complete, the system produces:

### 📁 Generated Files

| File | Description |
|------|-------------|
| `test-cases.json` | Complete test suite with verification info |
| `test-cases.md` | Human-readable markdown report |
| `navigation_graph.png` | Visual navigation diagram |
| `debug_log.txt` | All LLM interactions (if debug enabled) |

### 📈 Console Summary

```
============================================================
TEST CASE GENERATOR - COMPLETE
============================================================

Pipeline Statistics:
  • Steps completed: 11/11
  • Modules processed: 3
  • Test cases generated: 15
  • Unique test cases: 14 (after deduplication)

Post-Verification:
  • Tests flagged: 5
  • Ideal verifications: 12
  • Matches found: 8
  • Coverage: 66.7%

Execution Plans:
  • Plans generated: 5
  • Automated steps: 8
  • Manual steps: 4
  • Automation rate: 66.7%

Output saved to: output/
============================================================
```

---

## 🎯 Key Takeaways

1. **Multi-Agent Architecture**: Each agent has a specialized role, making the system modular and maintainable

2. **Two-Phase Pipeline**: Generation creates tests; Post-Verification adds verification coverage

3. **RAG-Based Matching**: Semantic search finds relevant tests for verification

4. **Coverage Analysis**: Automatically identifies gaps where manual verification is needed

5. **LLM Agnostic**: Works with OpenAI, GitHub Models, or OpenRouter

---

*Generated for presentation purposes - January 2026*
