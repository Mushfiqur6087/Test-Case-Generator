# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **LLM-powered Test Case Generator** that automatically generates comprehensive test cases from functional descriptions of web applications. The system uses a multi-agent architecture where each agent specializes in a specific aspect of the test generation pipeline.

**Key Features:**
- Multi-agent pipeline with specialized responsibilities
- Generates positive, negative, and edge case tests
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
│  AssemblerAgent                                             │
│  - Removes duplicate test cases                             │
│  - Sorts by module, priority, and type                      │
│  - Assigns proper IDs (MODULE-001 format)                   │
│  - Links test cases to navigation nodes                     │
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

# Test Output
TestCase(id, title, module_id, module_title, workflow, test_type,
         priority, preconditions, steps, expected_result)
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
      "id": "LOGIN-001",
      "title": "Valid login with correct credentials",
      "module_id": 1,
      "module_title": "Login",
      "workflow": "Login with credentials",
      "test_type": "positive",
      "priority": "High",
      "preconditions": "Registered user exists",
      "steps": [
        "Enter valid username",
        "Enter valid password",
        "Click Log In"
      ],
      "expected_result": "User is redirected to Accounts Overview"
    }
  ],
  "summary": {
    "total_tests": 45,
    "by_type": {"positive": 20, "negative": 18, "edge_case": 7},
    "by_priority": {"High": 25, "Medium": 15, "Low": 5},
    "by_module": {"Login": 8, "Transfer Funds": 12, "User Profile": 10}
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
