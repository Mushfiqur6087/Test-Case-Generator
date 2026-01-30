# LLM-Powered Test Case Generator

An intelligent test case generation system that automatically creates comprehensive test suites from functional descriptions of web applications. Built with a **multi-agent LLM architecture** and **RAG-based post-verification matching**, this tool transforms natural language functional descriptions into structured, automatable test cases.

## Table of Contents

- [Features](#features)
- [Architecture Overview](#architecture-overview)
- [Complete Pipeline](#complete-pipeline)
- [Installation](#installation)
- [Usage](#usage)
- [Input Format](#input-format)
- [Output Format](#output-format)
- [Agent Details](#agent-details)
- [Configuration](#configuration)
- [Examples](#examples)

## Features

- **Multi-Agent Architecture**: 10 specialized agents work together in a pipeline, each handling a specific aspect of test generation
- **Comprehensive Test Coverage**: Automatically generates positive, negative, and edge case tests
- **Post-Verification Pipeline**: Identifies which tests need verification and matches them to existing tests using semantic search
- **RAG-Based Matching**: Uses sentence-transformers for embedding generation and FAISS for similarity search
- **Visual Navigation Graph**: Creates PNG visualizations of application navigation flow using NetworkX
- **Dual Export**: Outputs both JSON (for automation) and Markdown (for human review)
- **LLM Provider Agnostic**: Works with OpenAI, GitHub Models, or OpenRouter APIs
- **Debug Mode**: Full logging of all LLM prompts and responses for troubleshooting

## Architecture Overview

The system uses a **two-phase pipeline architecture**:

1. **Generation Pipeline** (Steps 1-6): Transforms functional descriptions into test cases
2. **Post-Verification Pipeline** (Steps 7-11): Adds verification coverage for state-changing tests

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                              INPUT                                           │
│  functional_description.json + credentials.json (optional)                   │
└────────────────────────────────┬─────────────────────────────────────────────┘
                                 │
┌────────────────────────────────▼─────────────────────────────────────────────┐
│                       GENERATION PIPELINE                                    │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  [Step 1] Load Input Files                                                   │
│      │    Parse JSON, validate structure                                     │
│      ▼                                                                       │
│  [Step 2] Parser Agent                                                       │
│      │    Extract UI elements, workflows, business rules, behaviors          │
│      │    Output: ParsedFunctionalDescription with ParsedModule list         │
│      ▼                                                                       │
│  [Step 3] Navigation Agent                                                   │
│      │    Build navigation graph, identify login module, page connections    │
│      │    Output: NavigationGraph with NavigationNode objects                │
│      ▼                                                                       │
│  [Step 4] Chunker Agent                                                      │
│      │    Split modules into workflow-based chunks                           │
│      │    Map items/rules/behaviors to specific workflows                    │
│      │    Output: List[WorkflowChunk]                                        │
│      ▼                                                                       │
│  [Step 5] Test Generation Agent                                              │
│      │    Generate positive, negative, edge case tests per workflow          │
│      │    Output: List[TestCase] (unassigned IDs)                            │
│      ▼                                                                       │
│  [Step 6] Assembler Agent                                                    │
│      │    Deduplicate, sort by priority, assign IDs (MODULE-001 format)      │
│      │    Link test cases to navigation nodes                                │
│      │    Output: TestSuiteOutput                                            │
│      │                                                                       │
├──────┴───────────────────────────────────────────────────────────────────────┤
│                     POST-VERIFICATION PIPELINE                               │
├──────────────────────────────────────────────────────────────────────────────┤
│      │                                                                       │
│      ▼                                                                       │
│  [Step 7] Summary Agent                                                      │
│      │    Generate 2-line summaries for each module                          │
│      │    Identify what states each module can VERIFY vs MODIFY              │
│      │    Output: Dict[int, ModuleSummary]                                   │
│      ▼                                                                       │
│  [Step 8] Verification Flag Agent                                            │
│      │    Analyze POSITIVE tests only                                        │
│      │    Flag tests that modify state needing verification                  │
│      │    Output: TestCase.needs_post_verification = True/False              │
│      ▼                                                                       │
│  [Step 9] Ideal Verification Agent                                           │
│      │    Generate ideal verification scenarios for flagged tests            │
│      │    Define what SHOULD be checked after each test                      │
│      │    Output: Dict[test_id, List[IdealVerification]]                     │
│      ▼                                                                       │
│  [Step 10] Verification Matcher Agent (RAG)                                  │
│      │    Build vector index of all test cases using embeddings              │
│      │    Match ideal verifications to actual tests via semantic search      │
│      │    Use LLM to validate matches                                        │
│      │    Output: TestCase.post_verifications populated                      │
│      ▼                                                                       │
│  [Step 11] Execution Plan Agent                                              │
│      │    Compile verification matches into execution sequences              │
│      │    Generate automation rate and coverage statistics                   │
│      │    Output: Dict[test_id, ExecutionSequence]                           │
│      │                                                                       │
├──────┴───────────────────────────────────────────────────────────────────────┤
│                              OUTPUT                                          │
├──────────────────────────────────────────────────────────────────────────────┤
│      │                                                                       │
│      ▼                                                                       │
│  [Export] Generate Outputs                                                   │
│      • test-cases.json      - Structured test suite with verification info   │
│      • test-cases.md        - Human-readable markdown documentation          │
│      • navigation_graph.png - Visual graph of application structure          │
│      • debug_log.txt        - LLM interaction logs (if debug mode enabled)   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Complete Pipeline

### Phase 1: Generation Pipeline

| Step | Agent | Input | Output | Description |
|------|-------|-------|--------|-------------|
| 1 | - | JSON files | Raw data | Load and validate input files |
| 2 | **Parser Agent** | Functional description | `ParsedFunctionalDescription` | Extract UI elements, workflows, business rules, expected behaviors from each module |
| 3 | **Navigation Agent** | Parsed modules | `NavigationGraph` | Build site navigation graph, identify login module, determine page connections |
| 4 | **Chunker Agent** | Parsed modules | `List[WorkflowChunk]` | Split modules into workflow-based chunks, map related items/rules to each workflow |
| 5 | **Test Generation Agent** | Workflow chunks | `List[TestCase]` | Generate positive, negative, and edge case tests for each workflow |
| 6 | **Assembler Agent** | All test cases + nav graph | `TestSuiteOutput` | Deduplicate tests, sort by priority, assign IDs in MODULE-XXX format |

### Phase 2: Post-Verification Pipeline

| Step | Agent | Input | Output | Description |
|------|-------|-------|--------|-------------|
| 7 | **Summary Agent** | Parsed modules | `Dict[int, ModuleSummary]` | Generate 2-line summaries, identify verification and action states per module |
| 8 | **Verification Flag Agent** | Test cases + summaries | Flagged test cases | Flag POSITIVE tests that modify state requiring external verification |
| 9 | **Ideal Verification Agent** | Flagged tests + summaries | `Dict[test_id, List[IdealVerification]]` | Generate ideal verification scenarios describing what SHOULD be checked |
| 10 | **Verification Matcher Agent** | Ideal verifications + all tests | Matched verifications | Use RAG + embeddings to find actual tests that can verify each scenario |
| 11 | **Execution Plan Agent** | Matched verifications | `Dict[test_id, ExecutionSequence]` | Compile execution plans with automated steps and manual fallbacks |

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Quick Start

```bash
# Clone the repository
git clone https://github.com/Mushfiqur6087/Test-Case-Generator.git
cd Test-Case-Generator

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r test_case_generator/requirements.txt
```

### Dependencies

| Package | Purpose |
|---------|---------|
| `httpx` | HTTP client for API calls |
| `networkx` | Navigation graph building |
| `matplotlib` | Graph visualization |
| `sentence-transformers` | Embedding generation for RAG |
| `numpy` | Numerical operations |
| `faiss-cpu` (optional) | Fast similarity search |

**Note:** On first run, the RAG system downloads the `all-MiniLM-L6-v2` model (~80MB). If `sentence-transformers` is not installed, the system falls back to keyword-based matching.

## Usage

### Basic Usage

```bash
python -m test_case_generator.main \
    --generate \
    --input path/to/functional_description.json \
    --credentials path/to/credentials.json \
    --output output_dir \
    --api-key "your-api-key" \
    --provider openai \
    --model "gpt-4o" \
    --debug
```

### Using the Bash Script

```bash
# Set environment variable
export OPENROUTER_API_KEY="sk-or-v1-xxx"

# Run with script
./run_generator.sh -i parabank.json -o output3 --debug
```

### Export to Markdown

```bash
python -m test_case_generator.export_to_markdown \
    --input output/test-cases.json \
    --output output/test-cases.md
```

### Command Line Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--generate` | Yes | Run test generation |
| `--input` | Yes | Path to functional description JSON |
| `--credentials` | No | Path to credentials JSON |
| `--output` | No | Output directory (default: `output`) |
| `--api-key` | Yes | API key for LLM provider |
| `--provider` | No | API provider: `openai`, `github`, or `openrouter` (default: `openai`) |
| `--model` | No | Model identifier (default: `gpt-4o`) |
| `--debug` | No | Enable debug logging |
| `--debug-file` | No | Debug log path (default: `debug_log.txt`) |

### Supported Providers & Models

| Provider | Base URL | Example Models |
|----------|----------|----------------|
| **OpenAI** | `api.openai.com/v1` | `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo` |
| **GitHub Models** | `models.inference.ai.azure.com` | `gpt-4o`, `gpt-4o-mini` |
| **OpenRouter** | `openrouter.ai/api/v1` | `google/gemini-2.0-flash-exp:free`, `anthropic/claude-3.5-sonnet` |

## Input Format

### Functional Description (`functional_description.json`)

The main input file describing your web application:

```json
{
  "project_name": "ParaBank Functional Overview",
  "website_url": "https://parabank.parasoft.com/parabank/index.htm",
  "navigation_overview": "Description of how users navigate the application...",
  "modules": [
    {
      "id": 1,
      "title": "Login",
      "description": "The login page displays a form with Username and Password fields. When the user clicks Log In, credentials are validated. If valid, user is redirected to dashboard. If invalid, an error message is shown."
    },
    {
      "id": 2,
      "title": "Transfer Funds",
      "description": "The Transfer Funds page allows users to transfer money between their accounts. It has Amount field and two dropdowns for source and destination accounts..."
    }
  ]
}
```

### Credentials (Optional - `credentials.json`)

Test data for each module (for future use with test execution):

```json
{
  "project_name": "ParaBank Functional Overview",
  "modules": [
    {
      "id": 1,
      "title": "Login",
      "credentials": {
        "username": "john_doe",
        "password": "secret123"
      }
    }
  ]
}
```

## Output Format

### Generated Files

| File | Description |
|------|-------------|
| `test-cases.json` | Complete structured test suite with all metadata |
| `test-cases.md` | Human-readable markdown documentation |
| `navigation_graph.png` | Visual navigation diagram |
| `debug_log.txt` | LLM interaction logs (when debug mode enabled) |

### Test Case Structure (JSON)

```json
{
  "id": "TRAFUN-001",
  "title": "Transfer funds between accounts",
  "module_id": 6,
  "module_title": "Transfer Funds",
  "workflow": "Transfer funds",
  "test_type": "positive",
  "priority": "High",
  "preconditions": "User is logged in with multiple accounts",
  "steps": [
    "Select source account from 'From account number' dropdown",
    "Select destination account from 'To account number' dropdown",
    "Enter valid amount in the Amount field",
    "Click Transfer button"
  ],
  "expected_result": "Transfer confirmation message is displayed",
  "needs_post_verification": true,
  "modifies_state": ["account_balance", "transaction_history"],
  "post_verifications": [
    {
      "ideal": "Verify source account balance decreased by transfer amount",
      "status": "found",
      "matched_test_id": "ACCOVR-002",
      "matched_test_title": "View account balance in Accounts Overview",
      "confidence": 0.89,
      "execution_note": "Run after transfer to verify balance change"
    }
  ],
  "verification_coverage": "partial",
  "coverage_gaps": ["Transaction history verification not available"]
}
```

### Execution Plans (JSON)

```json
{
  "execution_plans": {
    "TRAFUN-001": {
      "source_test_id": "TRAFUN-001",
      "source_test_title": "Transfer funds between accounts",
      "execution_order": [
        {
          "step": 1,
          "action": "execute_test",
          "test_id": "ACCOVR-002",
          "test_title": "View account balance in Accounts Overview",
          "purpose": "Verify balance change",
          "confidence": 0.89
        }
      ],
      "manual_steps": [
        {
          "purpose": "Verify transaction in history",
          "suggested_step": "Navigate to Find Transactions and search for the transfer",
          "reason": "No matching automated test found"
        }
      ],
      "verification_coverage": "partial",
      "notes": "After executing TRAFUN-001, run: ACCOVR-002; Manual verification needed for 1 item(s)"
    }
  }
}
```

## Agent Details

### 1. Parser Agent

**Purpose:** Extract structured information from natural language module descriptions.

**Extracts:**
- `mentioned_items`: UI elements (fields, buttons, links)
- `workflows`: Primary actions that complete on this page
- `business_rules`: Validation rules and constraints
- `expected_behaviors`: Success/failure outcomes
- `requires_auth`: Whether page needs authentication

### 2. Navigation Agent

**Purpose:** Build a graph representation of application navigation.

**Outputs:**
- Navigation nodes for each module
- Connection edges between pages
- Login module identification
- URL paths (if inferable)
- PNG visualization of the graph

### 3. Chunker Agent

**Purpose:** Split modules with multiple workflows into testable chunks.

**Process:**
- Single workflow → single chunk with all items/rules
- Multiple workflows → LLM maps items/rules to appropriate workflows
- Fallback: assigns all items to each workflow

### 4. Test Generation Agent

**Purpose:** Generate test cases for each workflow chunk.

**Generates:**
- **Positive tests**: Happy path scenarios
- **Negative tests**: Error conditions and validations
- **Edge case tests**: Boundary values, special characters

**Avoids:**
- Device-specific tests (mobile gestures)
- Browser-specific tests (right-click menus)
- Network condition tests (offline scenarios)
- Stress tests (rapid clicking)

### 5. Assembler Agent

**Purpose:** Finalize and organize the test suite.

**Tasks:**
- Remove duplicate tests (by title + steps signature)
- Sort by module, priority, type
- Assign IDs in `MODULE-XXX` format
- Link tests to navigation nodes
- Generate summary statistics

### 6. Summary Agent

**Purpose:** Create concise module summaries for verification matching.

**Outputs:**
- 2-line summary per module (actions + data displayed)
- `can_verify_states`: States this module can READ/DISPLAY
- `action_states`: States this module MODIFIES
- Verification keywords for matching

### 7. Verification Flag Agent

**Purpose:** Identify which tests need post-verification.

**Flags POSITIVE tests that:**
- Create new records
- Modify existing data
- Transfer data between entities
- Submit forms with persistent effects

**Does NOT flag:**
- Negative tests (no state change)
- Edge case tests
- Login/logout (session only)
- Read-only operations

### 8. Ideal Verification Agent

**Purpose:** Generate verification scenarios for flagged tests.

**For each flagged test, generates:**
- Description of what to verify
- Target module that can verify it
- Verification action to perform
- Expected change to observe

### 9. Verification Matcher Agent (RAG)

**Purpose:** Match ideal verifications to actual test cases.

**Process:**
1. Build vector index of all tests using embeddings
2. For each ideal verification, search for similar tests
3. Use LLM to validate if candidate can actually verify
4. Classify as `found`, `partial`, or `not_found`

### 10. Execution Plan Agent

**Purpose:** Compile final execution sequences.

**Outputs:**
- Ordered list of verification tests to run after each test
- Manual steps for verifications without automated tests
- Coverage statistics (automation rate)

## Project Structure

```
Test-Case-Generator/
├── README.md                        # This file
├── CLAUDE.md                        # Development guidance
├── run_generator.sh                 # Bash runner script
├── parabank.json                    # Example input
├── credentials.json                 # Example credentials
│
├── test_case_generator/
│   ├── __init__.py
│   ├── main.py                      # Main orchestrator (TestCaseGenerator class)
│   ├── export_to_markdown.py        # Markdown export utility
│   ├── requirements.txt             # Python dependencies
│   │
│   ├── agents/
│   │   ├── __init__.py              # Agent exports
│   │   ├── base.py                  # BaseAgent with LLM integration
│   │   ├── parser_agent.py          # [Step 2] Parse descriptions
│   │   ├── navigation_agent.py      # [Step 3] Build nav graph
│   │   ├── chunker_agent.py         # [Step 4] Split into chunks
│   │   ├── test_generation_agent.py # [Step 5] Generate tests
│   │   ├── assembler_agent.py       # [Step 6] Assemble output
│   │   ├── summary_agent.py         # [Step 7] Module summaries
│   │   ├── verification_flag_agent.py    # [Step 8] Flag for verification
│   │   ├── ideal_verification_agent.py   # [Step 9] Ideal scenarios
│   │   ├── verification_matcher_agent.py # [Step 10] RAG matching
│   │   ├── execution_plan_agent.py  # [Step 11] Execution plans
│   │   └── rag_indexer.py           # Vector search implementation
│   │
│   └── models/
│       ├── __init__.py
│       └── schemas.py               # All dataclasses
│
└── output/                          # Generated outputs
    ├── test-cases.json
    ├── test-cases.md
    └── navigation_graph.png
```

## Data Models

### Core Schemas

| Schema | Description |
|--------|-------------|
| `ParsedModule` | Extracted module information |
| `ParsedFunctionalDescription` | Complete parsed input |
| `WorkflowChunk` | Single workflow with related items/rules |
| `TestCase` | Individual test case with verification info |
| `NavigationGraph` | Site navigation structure |
| `NavigationNode` | Single page in navigation |
| `ModuleSummary` | Module summary for matching |
| `IdealVerification` | What should be verified |
| `VerificationMatch` | Result of matching verification to test |
| `ExecutionSequence` | Ordered verification steps |
| `TestSuiteOutput` | Final complete output |

## Examples

### Console Output

```
============================================================
TEST CASE GENERATOR
============================================================
Debug mode: ON (logging to debug_log.txt)

[1/11] Loading input files...
  - Loaded: parabank.json, credentials.json

[2/11] Parsing functional description...
  - Project: ParaBank Functional Overview
  - Modules found: 11
    • Login: 1 workflows, 6 items
    • Transfer Funds: 1 workflows, 4 items
    ...

[3/11] Building navigation graph...
  - Login module ID: 1
  - Page nodes: 11

[4/11] Splitting modules into workflow chunks...
  - Login: 1 chunk(s)
    • Login with credentials
  ...

[5/11] Generating test cases...
  - Generating tests for: Login / Login with credentials
    • Generated 8 test cases
  ...

[6/11] Assembling test cases...
  - Assembled 67 unique test cases

[7/11] Generating module summaries...
  - Generated summaries for 11 modules

[8/11] Flagging positive tests for post-verification...
  - Flagged 12 positive tests as needing post-verification

[9/11] Generating ideal verification scenarios...
  - Generated 24 ideal verification scenarios for 12 tests

[10/11] Matching verifications with RAG...
  - RAG: Using sentence-transformers for embeddings
  - RAG: Indexed 67 test cases

[11/11] Generating execution plans...
  - Generated 12 execution plans
  - Automated steps: 18, Manual steps: 6
  - Automation rate: 75.0%

============================================================
SUMMARY
============================================================
Total Test Cases: 67

By Type:
  - positive: 28
  - negative: 24
  - edge_case: 15

By Priority:
  - High: 22
  - Medium: 30
  - Low: 15

Post-Verification Coverage:
  - Tests needing verification: 12
  - Full coverage: 5
  - Partial coverage: 5
  - No coverage: 2
```

## License

MIT License - feel free to use and modify for your projects.

## Contributing

Contributions welcome! Please open an issue or submit a pull request.

## Author

Built by [Mushfiqur Rahman](https://github.com/Mushfiqur6087)
