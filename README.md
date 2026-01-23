# LLM-Powered Test Case Generator

An intelligent test case generation system that automatically creates comprehensive test suites from functional descriptions of web applications using a multi-agent LLM architecture with RAG-based post-verification matching.

## Features

- **Multi-Agent Architecture**: Specialized agents handle parsing, navigation analysis, chunking, test generation, and assembly
- **Comprehensive Test Coverage**: Automatically generates positive, negative, and edge case tests
- **Post-Verification with RAG**: Automatically identifies which test cases need post-verification and matches them to existing tests using semantic search
- **Visual Navigation Graph**: Creates interactive visualizations of application navigation flow
- **Markdown Export**: Human-readable test case documentation with verification info
- **LLM Agnostic**: Works with OpenAI, GitHub Models, or OpenRouter APIs
- **Debug Mode**: Full logging of LLM interactions for troubleshooting

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         GENERATION PIPELINE                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────┐                                                        │
│  │ Parser      │ Extract UI elements, workflows, business rules         │
│  └──────┬──────┘                                                        │
│         ▼                                                               │
│  ┌─────────────┐                                                        │
│  │ Navigation  │ Build navigation graph + generate visual diagram       │
│  └──────┬──────┘                                                        │
│         ▼                                                               │
│  ┌─────────────┐                                                        │
│  │ Chunker     │ Split modules into testable workflow chunks            │
│  └──────┬──────┘                                                        │
│         ▼                                                               │
│  ┌─────────────┐                                                        │
│  │ Test Gen    │ Generate test cases for each workflow                  │
│  └──────┬──────┘                                                        │
│         ▼                                                               │
│  ┌─────────────┐                                                        │
│  │ Assembler   │ Deduplicate, sort, assign IDs                          │
│  └──────┬──────┘                                                        │
│         │                                                               │
├─────────┴───────────────────────────────────────────────────────────────┤
│                    POST-VERIFICATION PIPELINE                           │
├─────────────────────────────────────────────────────────────────────────┤
│         │                                                               │
│         ▼                                                               │
│  ┌─────────────┐                                                        │
│  │ Summary     │ Generate 2-line summaries + state capabilities         │
│  └──────┬──────┘                                                        │
│         ▼                                                               │
│  ┌─────────────┐                                                        │
│  │ Flag        │ Identify POSITIVE tests needing post-verification      │
│  └──────┬──────┘                                                        │
│         ▼                                                               │
│  ┌─────────────┐                                                        │
│  │ Ideal       │ Generate ideal verification scenarios                  │
│  └──────┬──────┘                                                        │
│         ▼                                                               │
│  ┌─────────────┐                                                        │
│  │ RAG Matcher │ Match verifications to actual tests via embeddings     │
│  └──────┬──────┘                                                        │
│         ▼                                                               │
│  ┌─────────────┐                                                        │
│  │ Exec Plan   │ Compile execution sequences for verification           │
│  └──────┬──────┘                                                        │
│         ▼                                                               │
│  ┌─────────────┐                                                        │
│  │ JSON/MD     │ Export with verification coverage + execution plans    │
│  └─────────────┘                                                        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

## Installation

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

**Note:** The RAG system uses `sentence-transformers` for embeddings. On first run, it will download the `all-MiniLM-L6-v2` model (~80MB). If sentence-transformers is not installed, the system falls back to keyword-based matching.

## Usage

### Generate Test Cases

```bash
python -m test_case_generator.main \
    --generate \
    --input path/to/functional_description.json \
    --credentials path/to/credentials.json \
    --output output_dir \
    --api-key "sk-or-v1-xxx" \
    --model "google/gemini-2.0-flash-exp:free" \
    --debug
```

### Export to Markdown

```bash
python -m test_case_generator.export_to_markdown \
    --input output/test-cases.json \
    --output output/test-cases.md
```

## Input Format

### Functional Description (`functional_desc.json`)

```json
{
  "project_name": "ParaBank",
  "website_url": "https://parabank.parasoft.com",
  "navigation_overview": "Description of site navigation structure",
  "modules": [
    {
      "id": 1,
      "title": "Login",
      "description": "The login page has Username and Password fields..."
    }
  ]
}
```

### Credentials (Optional - `credentials.json`)

```json
{
  "valid_user": {
    "username": "testuser",
    "password": "testpass"
  }
}
```

## Output

### Test Cases JSON (`test-cases.json`)

Structured JSON containing:
- Navigation graph with visual diagram
- Comprehensive test cases with IDs, steps, expected results
- Summary statistics

### Navigation Graph (`navigation_graph.png`)

Visual representation showing:
- Login/entry points (green)
- Authenticated pages (blue)
- Public pages (orange)
- Navigation connections
- Test case counts per page

### Markdown Report (`test-cases.md`)

Human-readable test documentation with:
- Summary tables including verification coverage
- Test cases grouped by module and type
- **Verification information** for each test:
  - State dependencies (reads/writes)
  - Pre-verification steps
  - Post-verification steps
  - Test dependencies (verified by which tests)
- Verification chain table showing test relationships
- Navigation structure

## Command Line Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--generate` | Yes | Run test generation |
| `--input` | Yes | Path to functional description JSON |
| `--credentials` | No | Path to credentials JSON |
| `--output` | No | Output directory (default: `output`) |
| `--api-key` | Yes | OpenRouter API key |
| `--model` | No | Model identifier (default: `google/gemini-2.0-flash-exp:free`) |
| `--debug` | No | Enable debug logging |
| `--debug-file` | No | Debug log path (default: `debug_log.txt`) |

## Supported Models

Works with any model via [OpenRouter](https://openrouter.ai):

**Free Models:**
- `google/gemini-2.0-flash-exp:free`
- `meta-llama/llama-3.2-3b-instruct:free`

**Paid Models:**
- `openai/gpt-4o`
- `anthropic/claude-3.5-sonnet`
- `google/gemini-pro`

## Project Structure

```
test_case_generator/
├── agents/
│   ├── base.py                      # Base agent with LLM integration
│   ├── parser_agent.py              # Parse functional descriptions
│   ├── navigation_agent.py          # Build navigation graph
│   ├── chunker_agent.py             # Split into workflow chunks
│   ├── test_generation_agent.py     # Generate test cases
│   ├── assembler_agent.py           # Assemble and export
│   ├── summary_agent.py             # Generate module summaries
│   ├── verification_flag_agent.py   # Flag tests needing verification
│   ├── ideal_verification_agent.py  # Generate ideal verifications
│   ├── verification_matcher_agent.py# Match via RAG
│   └── rag_indexer.py               # Vector embedding & search
├── models/
│   └── schemas.py                   # Data models
├── main.py                          # Main orchestrator
└── export_to_markdown.py            # Markdown export tool
```

## Post-Verification System

The post-verification system automatically identifies test cases that modify application state and need external verification, then matches them to existing test cases that can verify the results.

### How It Works

```
┌───────────────────────────────────────────────────────────────────────┐
│ EXAMPLE: Data Submission/Transfer Test Case                           │
├───────────────────────────────────────────────────────────────────────┤
│                                                                       │
│ 1. FLAG PHASE                                                         │
│    Test: "SUBMIT-001: Submit new record/form"                         │
│    → needs_post_verification: true                                    │
│    → modifies_state: ["record_list", "submission_history"]            │
│                                                                       │
│ 2. IDEAL VERIFICATION PHASE                                           │
│    Generate what SHOULD be verified:                                  │
│    → "Verify new record appears in the list/overview"                 │
│    → "Verify record details are correct"                              │
│    → "Verify submission appears in history"                           │
│                                                                       │
│ 3. RAG MATCHING PHASE                                                 │
│    Search existing test cases using semantic similarity:              │
│    → Query: "verify record list display overview"                     │
│    → Found: OVERVIEW-002 (similarity: 0.89)                           │
│    → LLM validates: "Yes, this test can verify the new record"        │
│                                                                       │
│ 4. FINAL OUTPUT                                                       │
│    post_verifications:                                                │
│      - ideal: "Verify record appears in list"                         │
│        status: "found"                                                │
│        matched_test_id: "OVERVIEW-002"                                │
│        execution_note: "Run after submission to verify"               │
│      - ideal: "Verify in submission history"                          │
│        status: "not_found"                                            │
│        reason: "No test for history verification"                     │
│        suggested_manual_step: "Navigate to History and check..."      │
│                                                                       │
│    verification_coverage: "partial" (50%)                             │
│    coverage_gaps: ["No test for history verification"]                │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```

### Verification Status Types

| Status | Meaning |
|--------|---------|
| `found` | An existing test case can fully verify this requirement |
| `partial` | An existing test case partially covers the verification |
| `not_found` | No existing test can verify this - manual step suggested |

### What Gets Flagged for Post-Verification

| Action Type | Needs Verification | Reason |
|-------------|-------------------|--------|
| Data Transfers | ✓ Yes | Data changes in multiple places |
| Submissions/Payments | ✓ Yes | Record created + status change |
| Profile/Settings Updates | ✓ Yes | Data persistence verification |
| Applications/Requests | ✓ Yes | Record appears in list/history |
| Record Creation | ✓ Yes | New record appears in list |
| Login/Logout | ✗ No | Session state only |
| Registration | ✗ No | Self-contained success |
| Read-only Pages | ✗ No | No state modification |
| Negative Tests | ✗ No | Validation failure, no state change |

### RAG Implementation

The system uses **sentence-transformers** for generating embeddings:

```python
# Model: all-MiniLM-L6-v2 (lightweight, fast)
# Embedding dimension: 384
# Search: Cosine similarity

# Each test case is embedded as:
text = f"{title} {module} {workflow} {expected_result} {steps}"
embedding = model.encode(text)

# Query for verification matching:
query = f"{ideal_description} {verification_action} {target_module}"
candidates = rag.search(query, top_k=5, module_filter=target_module)
```

If sentence-transformers is not installed, the system falls back to Jaccard similarity-based keyword matching.

## Example Output

### Test Case with Post-Verification (JSON)

```json
{
  "id": "TRAFUN-001",
  "title": "Transfer funds between accounts",
  "module_title": "Transfer Funds",
  "test_type": "positive",
  "priority": "High",
  "steps": [
    "Select source account from dropdown",
    "Select destination account from dropdown",
    "Enter transfer amount",
    "Click Transfer button"
  ],
  "expected_result": "Transfer successful message displayed",
  "needs_post_verification": true,
  "modifies_state": ["account_balance", "transaction_history"],
  "post_verifications": [
    {
      "ideal": "Verify source account balance decreased by transfer amount",
      "status": "found",
      "matched_test_id": "ACCOVR-002",
      "matched_test_title": "Verify account balance display",
      "confidence": 0.89,
      "execution_note": "Execute on source account after transfer completes"
    },
    {
      "ideal": "Verify destination account balance increased",
      "status": "found",
      "matched_test_id": "ACCOVR-002",
      "matched_test_title": "Verify account balance display",
      "confidence": 0.87,
      "execution_note": "Execute on destination account after transfer"
    },
    {
      "ideal": "Verify transfer transaction in activity history",
      "status": "not_found",
      "reason": "No test case exists for viewing transaction details",
      "suggested_manual_step": "Navigate to Account Activity, verify transfer transaction listed"
    }
  ],
  "verification_coverage": "partial",
  "coverage_gaps": [
    "No test case exists for viewing transaction details"
  ]
}
```

### Summary Output

```
Post-Verification Coverage:
  - Tests needing verification: 15
  - Full coverage: 8
  - Partial coverage: 5
  - No coverage: 2
  - Coverage gaps (3):
    ! No test case for viewing transaction history
    ! No test case for loan status verification
    ! External payment verification not possible
```

## Key Features

### Fixed LLM Hallucinations

The prompts have been optimized to:
- Focus on primary workflows (form submissions, not navigation links)
- Generate only automation-friendly tests
- Avoid device-specific tests (touch, mobile gestures)
- Exclude browser-specific features (right-click, new tabs)
- Skip network condition tests (offline, server errors)
- Ground all tests strictly in the functional description

### Test Quality

- Covers all scenarios mentioned in descriptions
- Includes input variations (username vs email login)
- Tests key validation rules and error conditions
- Maintains reasonable test counts per module

### Verification Coverage Analysis

- Automatically identifies verification gaps
- Suggests manual steps when automation isn't possible
- Calculates coverage percentage per test case
- Aggregates coverage statistics in summary

## Example

See `parabank.json` for a complete functional description example and `CLAUDE.md` for detailed project documentation.

## License

MIT License - feel free to use and modify for your projects.

## Contributing

Contributions welcome! Please open an issue or submit a pull request.

## Author

Built with Claude Code and the Claude Agent SDK.
