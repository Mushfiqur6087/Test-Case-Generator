# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **LLM-powered Test Case Generator** that automatically generates comprehensive test cases from functional descriptions of web applications. The system uses a multi-agent architecture where each agent specializes in a specific aspect of the test generation pipeline.

**Key Features:**
- Multi-agent pipeline with specialized responsibilities
- Generates positive, negative, and edge case tests
- **State verification for positive tests** - adds pre/post verification steps to validate expected results
- Creates visual navigation graph of the application
- Supports any LLM via OpenRouter API
- Debug logging for troubleshooting LLM interactions
- JSON output with structured test cases

## Directory Structure

```
test_case_generator/
├── __init__.py
├── main.py                      # Main orchestrator (TestCaseGenerator class)
├── requirements.txt             # Python dependencies
├── agents/
│   ├── __init__.py
│   ├── base.py                  # BaseAgent abstract class with LLM integration
│   ├── parser_agent.py          # Parses functional descriptions
│   ├── navigation_agent.py      # Builds navigation graph + generates image
│   ├── chunker_agent.py         # Splits modules into workflow chunks
│   ├── test_generation_agent.py # Generates test cases per workflow
│   ├── verification_agent.py    # Adds state verification to positive tests
│   └── assembler_agent.py       # Deduplicates, orders, exports output
└── models/
    ├── __init__.py
    └── schemas.py               # All dataclasses (ParsedModule, TestCase, etc.)
```

## Commands

```bash
# Install dependencies
pip install -r test_case_generator/requirements.txt

# Generate test cases
python -m test_case_generator.main --generate \
    --input path/to/functional_desc.json \
    --credentials path/to/credentials.json \
    --output output_dir \
    --api-key "sk-or-v1-xxx" \
    --model "google/gemini-2.0-flash-exp:free" \
    --debug

# Show help
python -m test_case_generator.main --help
```

### Command Line Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--generate` | Yes | Flag to run generation |
| `--input` | Yes | Path to functional description JSON |
| `--credentials` | No | Path to credentials JSON (for test data) |
| `--output` | No | Output directory (default: `output`) |
| `--api-key` | Yes | OpenRouter API key |
| `--model` | No | Model identifier (default: `google/gemini-2.0-flash-exp:free`) |
| `--debug` | No | Enable debug logging |
| `--debug-file` | No | Debug log path (default: `debug_log.txt`) |

## Architecture

### Pipeline Flow

```
Input (functional_desc.json, credentials.json)
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  ParserAgent                                                │
│  - Extracts UI elements, workflows, business rules          │
│  - Identifies authentication requirements per module        │
│  - Output: ParsedFunctionalDescription                      │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  NavigationAgent                                            │
│  - Builds site navigation graph                             │
│  - Identifies login module and page connections             │
│  - Generates visual graph image (PNG)                       │
│  - Output: NavigationGraph + navigation_graph.png           │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  ChunkerAgent                                               │
│  - Splits modules into workflow-based chunks                │
│  - Maps items/rules/behaviors to specific workflows         │
│  - Output: List[WorkflowChunk]                              │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  TestGenerationAgent                                        │
│  - Generates test cases for each workflow chunk             │
│  - Creates positive, negative, and edge case tests          │
│  - Output: List[TestCase]                                   │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  VerificationAgent                                          │
│  - Tags positive tests with reads_state/writes_state        │
│  - Links tests that can verify each other's results         │
│  - Generates pre/post verification steps                    │
│  - Creates missing state check tests if needed              │
│  - Output: List[TestCase] with verification data            │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  AssemblerAgent                                             │
│  - Removes duplicate test cases                             │
│  - Sorts by module, priority, and type                      │
│  - Assigns proper IDs (MODULE-001 format)                   │
│  - Updates verification_test_ids with actual IDs            │
│  - Links test cases to navigation nodes                     │
│  - Generates verification coverage summary                  │
│  - Exports to JSON                                          │
│  - Output: TestSuiteOutput                                  │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
Output (test-cases.json, navigation_graph.png)
```

### Agent Details

#### BaseAgent (`agents/base.py`)
Abstract base class providing:
- **OpenRouter API integration** via `call_llm()` and `call_llm_json()` methods
- **Debug logging** with session management (single header, no redundant prompts)
- **HTTP client** with 120-second timeout
- Class methods: `reset_debug_state()`, `init_debug_session()`

#### ParserAgent (`agents/parser_agent.py`)
Parses functional description JSON and extracts:
- `mentioned_items`: UI elements (fields, buttons, links)
- `workflows`: User actions/purposes on each page
- `business_rules`: Validation rules and constraints
- `expected_behaviors`: Success/failure outcomes
- `requires_auth`: Whether page needs authentication

#### NavigationAgent (`agents/navigation_agent.py`)
Builds navigation structure:
- Identifies login module from keywords
- Analyzes page connections via LLM
- Creates `NavigationGraph` with `NavigationNode` objects
- **Generates visual graph image** using networkx/matplotlib:
  - Green nodes: Login module
  - Blue nodes: Authenticated pages
  - Orange nodes: Public pages
  - Node size scales with test case count

#### ChunkerAgent (`agents/chunker_agent.py`)
Splits modules into workflow chunks:
- Single workflow → single chunk with all items
- Multiple workflows → LLM maps items/rules to each workflow
- Fallback: creates one chunk per workflow with all items

#### TestGenerationAgent (`agents/test_generation_agent.py`)
Generates test cases per workflow:
- **Positive tests** (2-3): Happy paths, valid inputs
- **Negative tests** (2-3): Invalid inputs, empty fields, errors
- **Edge case tests** (1-2): Boundaries, special characters
- Also supports `generate_for_type()` for specific test types

#### VerificationAgent (`agents/verification_agent.py`)
Adds state verification to positive test cases:
- **State tagging**: Uses LLM to identify what state each test reads/writes
- **Test linking**: Links state-writing tests to state-reading tests for verification
- **Verification steps**: Generates pre/post verification steps for state-changing tests
- **Missing state checks**: Creates new tests for states that have no verification test

**State Categories:**
- `account_balance`: Bank account balances
- `user_profile`: User personal information
- `transaction_history`: Records of transactions
- `loan_status`: Loan applications/status
- `payee_list`: Saved payees/recipients
- `account_list`: List of user accounts
- `session_status`: Login/logout state

**Key Methods:**
- `run(test_cases)`: Main entry point, processes all tests
- `_tag_state_for_tests()`: Tags tests with reads_state/writes_state
- `_link_verification_tests()`: Links writers to readers
- `_generate_verification_steps()`: Creates pre/post steps
- `_generate_missing_state_checks()`: Creates new verification tests
- `update_verification_ids()`: Updates titles to actual test IDs
- `get_verification_summary()`: Returns coverage statistics

**Why Only Positive Tests?**
- Positive tests: Action succeeds, state changes → Needs verification
- Negative tests: Validation fails, no state change → No verification needed
- Edge cases: Boundary testing → Typically no meaningful state change

#### AssemblerAgent (`agents/assembler_agent.py`)
Final assembly and export:
- Deduplicates based on title + first 3 steps
- Sorts by module ID, priority, test type
- Assigns IDs dynamically from module titles:
  - Single word: First 6 chars → `Login` → `LOGIN-001`
  - Two words: First 3 chars each → `Transfer Funds` → `TRAFUN-001`
  - 3+ words: First letter each → `Open New Account` → `ONA-001`
- Links test IDs to navigation nodes
- Generates summary statistics
- Validates completeness

### Data Models (`models/schemas.py`)

```python
# Parser Output
ParsedModule(id, title, raw_description, mentioned_items, workflows,
             business_rules, expected_behaviors, requires_auth)
ParsedFunctionalDescription(project_name, base_url, navigation_overview, modules)

# Chunker Output
WorkflowChunk(chunk_id, module_id, module_title, workflow_name,
              workflow_description, related_items, related_rules, related_behaviors)

# Navigation Output
NavigationNode(module_id, title, requires_auth, url_path, connected_to, test_case_ids)
NavigationGraph(nodes, login_module_id, graph_image_path)

# Test Output (with verification fields for positive tests)
TestCase(
    id, title, module_id, module_title, workflow, test_type,
    priority, preconditions, steps, expected_result,
    # Verification fields (only populated for positive tests)
    reads_state,              # List[str] - state this test reads/checks
    writes_state,             # List[str] - state this test modifies
    verification_test_ids,    # List[str] - test IDs that verify this test's result
    pre_verification_steps,   # List[str] - steps to verify initial state
    post_verification_steps   # List[str] - steps to verify final state
)
TestSuiteOutput(project_name, base_url, generated_at, navigation_graph,
                test_cases, summary)
```

## Input/Output Format

### Input - `functional_desc.json`

```json
{
  "project_name": "ParaBank",
  "website_url": "https://parabank.parasoft.com",
  "navigation_overview": "The application has a sidebar menu with: Accounts Overview, Transfer Funds, Bill Pay, Find Transactions, Update Profile, Request Loan, Log Out. Login form is on homepage.",
  "modules": [
    {
      "id": 1,
      "title": "Login",
      "description": "The login page has Username and Password fields with a Log In button. There's also a Register link and Forgot Login Info link. On successful login, user is redirected to Accounts Overview. Invalid credentials show an error message."
    },
    {
      "id": 2,
      "title": "Transfer Funds",
      "description": "Users can transfer funds between their accounts. Select source account, destination account, and enter amount. Click Transfer button. Shows confirmation on success or error if insufficient funds."
    }
  ]
}
```

### Input - `credentials.json` (Optional)

```json
{
  "valid_user": {
    "username": "john",
    "password": "demo"
  },
  "admin_user": {
    "username": "admin",
    "password": "admin123"
  }
}
```

### Output - `test-cases.json`

```json
{
  "project_name": "ParaBank",
  "base_url": "https://parabank.parasoft.com",
  "generated_at": "2024-01-15T10:30:00.000000",
  "navigation_graph": {
    "login_module_id": 1,
    "graph_image_path": "output/navigation_graph.png",
    "nodes": [
      {
        "module_id": 1,
        "title": "Login",
        "requires_auth": false,
        "url_path": "/login",
        "connected_to": [2, 3, 4],
        "test_case_ids": ["LOGIN-001", "LOGIN-002"]
      }
    ]
  },
  "test_cases": [
    {
      "id": "TRAFUN-001",
      "title": "Transfer funds between accounts",
      "module_id": 2,
      "module_title": "Transfer Funds",
      "workflow": "Transfer money",
      "test_type": "positive",
      "priority": "High",
      "preconditions": "User is logged in with multiple accounts",
      "steps": [
        "Select source account",
        "Select destination account",
        "Enter amount: $100",
        "Click Transfer"
      ],
      "expected_result": "Transfer confirmation is displayed",
      "reads_state": [],
      "writes_state": ["account_balance", "transaction_history"],
      "verification_test_ids": ["ACCOVR-001"],
      "pre_verification_steps": [
        "Navigate to Accounts Overview",
        "Note source account balance",
        "Note destination account balance"
      ],
      "post_verification_steps": [
        "Navigate to Accounts Overview",
        "Verify source balance decreased by $100",
        "Verify destination balance increased by $100"
      ]
    }
  ],
  "summary": {
    "total_tests": 45,
    "by_type": {"positive": 20, "negative": 18, "edge_case": 7},
    "by_priority": {"High": 25, "Medium": 15, "Low": 5},
    "by_module": {"Login": 8, "Transfer Funds": 12, "User Profile": 10},
    "verification_coverage": {
      "total_positive_tests": 20,
      "tests_that_write_state": 15,
      "tests_that_read_state": 12,
      "tests_with_verification_links": 14,
      "tests_with_pre_verification_steps": 15,
      "tests_with_post_verification_steps": 15,
      "unique_states_written": ["account_balance", "user_profile", "session_status"],
      "unique_states_read": ["account_balance", "user_profile"],
      "unverified_states": ["session_status"]
    }
  }
}
```

### Output - `navigation_graph.png`

Visual representation of the site navigation:
- **Green nodes**: Login/entry module
- **Blue nodes**: Authenticated pages (requires login)
- **Orange nodes**: Public pages (no auth required)
- **Arrows**: Navigation connections between pages
- **Node size**: Scales with number of test cases
- **Legend**: Color coding explanation
- **Stats**: Total nodes, connections, auth/public page counts

## Debug Logging

When `--debug` is enabled, all LLM interactions are logged to `debug_log.txt`:

```
================================================================================
DEBUG SESSION STARTED: 2024-01-15T10:30:00.000000
Model: google/gemini-2.0-flash-exp:free
================================================================================

------------------------------------------------------------
[10:30:01] Parser Agent - SYSTEM PROMPT
------------------------------------------------------------
You are an expert software test analyst...

------------------------------------------------------------
[10:30:01] Parser Agent - USER PROMPT
------------------------------------------------------------
Analyze this functional description...

------------------------------------------------------------
[10:30:05] Parser Agent - LLM RESPONSE
------------------------------------------------------------
{"mentioned_items": ["Username", "Password"], ...}
```

**Debug optimizations:**
- Session header written only once (not per agent)
- System prompts logged only once per agent (not per LLM call)
- Timestamps for tracking execution flow

## Configuration

### Supported Models (via OpenRouter)

```bash
# Free models
--model "google/gemini-2.0-flash-exp:free"
--model "meta-llama/llama-3.2-3b-instruct:free"

# Paid models
--model "openai/gpt-4o"
--model "anthropic/claude-3.5-sonnet"
--model "google/gemini-pro"
```

### Environment Variables

You can also set the API key via environment variable:
```bash
export OPENROUTER_API_KEY="sk-or-v1-xxx"
```

## Dependencies

```
httpx>=0.25.0      # HTTP client for API calls
networkx>=3.0      # Graph data structure
matplotlib>=3.7.0  # Graph visualization
```

## Error Handling

- **LLM failures**: Agents have fallback behaviors (e.g., default navigation)
- **JSON parse errors**: Logged with context, graceful degradation
- **Missing fields**: Default values applied, warnings printed
- **Validation**: AssemblerAgent validates test completeness, reports issues

## Extension Points

To add a new agent:
1. Create `agents/new_agent.py` inheriting from `BaseAgent`
2. Implement `name`, `system_prompt`, and `run()` methods
3. Add to `agents/__init__.py` exports
4. Integrate into `main.py` pipeline
