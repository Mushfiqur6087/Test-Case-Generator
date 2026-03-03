# TestWright

AI-powered test case generation from functional specifications.

TestWright reads a functional specification (markdown or JSON), analyzes it through an 11-agent LangGraph pipeline, and produces a comprehensive test suite with navigation graphs, post-verification plans, and execution sequences.

## Features

- **Specification-driven** -- generate test cases from functional descriptions written in plain markdown
- **Multi-agent pipeline** -- 11 specialized agents (parser, navigator, chunker, summarizer, generator, assembler, verification flag/ideal/matcher, execution planner, finalizer)
- **Navigation graph** -- builds a directed graph of application pages and generates a PNG visualization
- **Post-verification** -- flags state-changing tests, generates ideal verification scenarios, matches them to existing test cases via RAG, and compiles before/after execution plans
- **Multiple providers** -- works with OpenAI, GitHub Models, and OpenRouter
- **Dual output** -- exports to both JSON and Markdown

## Quick Start

### Install

```bash
pip install -e .
```

Or with requirements file:

```bash
pip install -r requirements.txt
pip install -e .
```

### Generate test cases

```bash
# From a directory of markdown files
testwright --generate \
  --input examples/parabank/ \
  --api-key "sk-..." \
  --provider openai \
  --output output/

# From a JSON file
testwright --generate \
  --input functional_desc.json \
  --api-key "sk-..." \
  --provider openai
```

### Export to Markdown

```bash
testwright export-md --input output/test-cases.json --output output/test-cases.md
```

### Python API

```python
from testwright import TestCaseGenerator

generator = TestCaseGenerator(
    api_key="sk-...",
    model="gpt-4o",
    provider="openai",
)

output = generator.generate("examples/parabank/", output_dir="output/")
print(f"Generated {output.summary['total_tests']} test cases")
```

## Architecture

```
Input (functional spec + navigation + mock data)
  |
  v
[1] Parser -----> Structured modules & workflows
  |
  v
[2] Navigation -> Directed page graph (nodes + edges)
  |
  v
[3] Chunker ----> Workflow-based chunks per module
  |
  v
[4] Summary ----> Module summaries (verify/action states)
  |
  v
[5] Generator --> Raw test cases (positive, negative, edge)
  |
  v
[6] Assembler --> Deduplicated, ID'd, nav-linked test suite
  |
  v
[7] Flag -------> Flags state-changing tests
  |
  v
[8] Ideal ------> Ideal verification scenarios per flag
  |
  v
[9] Matcher ----> RAG-matched verification test cases
  |
  v
[10] Planner ---> PRE -> ACTION -> POST execution plans
  |
  v
[11] Finalize --> Summary, graph image, JSON export
```

### Agent Responsibilities

| Agent | File | Role |
|---|---|---|
| Parser | `agents/parser.py` | Parse functional spec into structured modules |
| Navigation | `agents/navigation.py` | Build page graph, generate PNG |
| Chunker | `agents/chunker.py` | Split modules into workflow chunks |
| Summary | `agents/summary.py` | Summarize modules (verify/action states) |
| Test Generator | `agents/test_generator.py` | Generate positive, negative, edge-case tests |
| Assembler | `agents/assembler.py` | Deduplicate, assign IDs, link to nav graph |
| Verify Flag | `agents/verify_flag.py` | Flag tests that modify persistent state |
| Verify Ideal | `agents/verify_ideal.py` | Design ideal verification scenarios |
| Verify Matcher | `agents/verify_matcher.py` | Match ideal verifications to tests via RAG |
| Execution Planner | `agents/execution_planner.py` | Compile before/after execution sequences |
| RAG Indexer | `agents/rag_indexer.py` | Embedding-based test case search |

## Project Structure

```
testwright/
├── pyproject.toml
├── requirements.txt
├── README.md
│
├── examples/
│   ├── parabank/
│   │   ├── functional_specification.md
│   │   ├── navigation.md
│   │   └── mock_data.md
│   └── moodle/
│       ├── functional_specification.md
│       ├── navigation.md
│       └── mock_data.md
│
├── src/
│   └── testwright/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       │
│       ├── core/
│       │   ├── generator.py       # TestCaseGenerator orchestrator
│       │   ├── state.py           # LangGraph PipelineState schema
│       │   ├── graph.py           # StateGraph builder
│       │   └── nodes.py           # Node functions for each agent
│       │
│       ├── agents/                # All 11 agents
│       │   ├── base.py            # BaseAgent (LLM calls, debug, retry)
│       │   ├── parser.py
│       │   ├── navigation.py
│       │   ├── chunker.py
│       │   ├── summary.py
│       │   ├── test_generator.py
│       │   ├── assembler.py
│       │   ├── verify_flag.py
│       │   ├── verify_ideal.py
│       │   ├── verify_matcher.py
│       │   ├── execution_planner.py
│       │   └── rag_indexer.py
│       │
│       ├── models/
│       │   ├── schemas.py         # Dataclasses (TestCase, NavGraph, etc.)
│       │   └── enums.py           # TestType, Priority, ExecutionStrategy
│       │
│       └── exporters/
│           ├── json_exporter.py
│           └── markdown_exporter.py
│
└── tests/
```

## Input Format

TestWright accepts a directory containing up to three markdown files:

### `functional_specification.md` (required)

Describe each module/page as an `## H2` heading. Under each heading, describe the features, fields, workflows, and validation rules.

```markdown
## Login Page
Users enter their username and password to access the system.
- Fields: username, password
- "Login" button submits credentials
- Displays error on invalid login

## Dashboard
Shows account overview after login.
- Displays account balances
- Links to Transfer, Bill Pay, etc.
```

### `navigation.md` (optional)

Describe how pages connect to each other.

```markdown
Login -> Dashboard (after successful login)
Dashboard -> Transfer Funds
Dashboard -> Bill Pay
Dashboard -> Account Statements
```

### `mock_data.md` (optional)

Provide test credentials and sample data.

```markdown
## Test Users
- Username: testuser / Password: Test@1234
- Username: admin / Password: Admin@5678

## Sample Data
- Account: 12345 (Checking, balance $1000)
- Account: 67890 (Savings, balance $5000)
```

## Output Format

### JSON (`test-cases.json`)

Complete structured output including test cases, navigation graph, verification plans, and summary statistics.

### Markdown (`test-cases.md`)

Human-readable report with:
- Summary tables (by type, priority, module)
- Test case tables grouped by module and type
- Post-verification details with execution plans
- Navigation graph image

### Navigation Graph (`navigation_graph.png`)

Visual representation of application page flow.

## Configuration

### LLM Providers

| Provider | Flag | API Key Source |
|---|---|---|
| OpenAI | `--provider openai` | OpenAI API key |
| GitHub Models | `--provider github` | GitHub PAT |
| OpenRouter | `--provider openrouter` | OpenRouter API key |

### Options

```
--model MODEL       LLM model name (default: gpt-4o)
--debug             Log all LLM inputs/outputs
--debug-file PATH   Debug log location (default: debug_log.txt)
--output DIR        Output directory (default: output/)
```

## Examples

Two example specifications are included:

- **ParaBank** (`examples/parabank/`) -- online banking app with transfers, bill pay, loans, investments
- **Moodle** (`examples/moodle/`) -- learning management system with courses, assignments, grading, forums

```bash
# Generate tests for ParaBank
testwright --generate --input examples/parabank/ --api-key "sk-..." --output output/parabank/

# Generate tests for Moodle
testwright --generate --input examples/moodle/ --api-key "sk-..." --output output/moodle/
```

## License

MIT
