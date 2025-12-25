# LLM-Powered Test Case Generator

An intelligent test case generation system that automatically creates comprehensive test suites from functional descriptions of web applications using a multi-agent LLM architecture.

## Features

- **Multi-Agent Architecture**: Specialized agents handle parsing, navigation analysis, chunking, test generation, and assembly
- **Comprehensive Test Coverage**: Automatically generates positive, negative, and edge case tests
- **Visual Navigation Graph**: Creates interactive visualizations of application navigation flow
- **Markdown Export**: Human-readable test case documentation
- **LLM Agnostic**: Works with any LLM via OpenRouter API
- **Debug Mode**: Full logging of LLM interactions for troubleshooting

## Architecture

```
┌─────────────┐
│ Parser      │ Extract UI elements, workflows, business rules
└──────┬──────┘
       ▼
┌─────────────┐
│ Navigation  │ Build navigation graph + generate visual diagram
└──────┬──────┘
       ▼
┌─────────────┐
│ Chunker     │ Split modules into testable workflow chunks
└──────┬──────┘
       ▼
┌─────────────┐
│ Test Gen    │ Generate test cases for each workflow
└──────┬──────┘
       ▼
┌─────────────┐
│ Assembler   │ Deduplicate, sort, assign IDs, export JSON
└─────────────┘
```

## Installation

```bash
# Clone the repository
git clone https://github.com/Mushfiqur6087/Test-Case-Generator.git
cd Test-Case-Generator

# Install dependencies
pip install -r test_case_generator/requirements.txt
```

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
- Summary tables
- Test cases grouped by module and type
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
│   ├── base.py                  # Base agent with LLM integration
│   ├── parser_agent.py          # Parse functional descriptions
│   ├── navigation_agent.py      # Build navigation graph
│   ├── chunker_agent.py         # Split into workflow chunks
│   ├── test_generation_agent.py # Generate test cases
│   └── assembler_agent.py       # Assemble and export
├── models/
│   └── schemas.py               # Data models
├── main.py                      # Main orchestrator
└── export_to_markdown.py        # Markdown export tool
```

## Key Improvements

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

## Example

See `parabank.json` for a complete functional description example and `CLAUDE.md` for detailed project documentation.

## License

MIT License - feel free to use and modify for your projects.

## Contributing

Contributions welcome! Please open an issue or submit a pull request.

## Author

Built with Claude Code and the Claude Agent SDK.
