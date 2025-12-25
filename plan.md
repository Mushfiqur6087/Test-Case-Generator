# Test Case Generation System - Focused Plan


This plan focuses **only** on:
1. Generating test cases from functional descriptions
2. Building navigation context
3. Outputting structured test cases in a format compatible with your Testing-Agent




## System Architecture (Generation Only)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         TEST CASE GENERATOR                                 │
│                    (Orchestrates the entire process)                        │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              INPUTS                                         │
│  ┌──────────────────────┐    ┌──────────────────────┐                       │
│  │ functional_desc.json │    │  credentials.json    │                       │
│  └──────────────────────┘    └──────────────────────┘                       │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            ▼                       ▼                       ▼
┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
│   PARSER AGENT      │  │  NAVIGATION AGENT   │  │   CHUNKER AGENT     │
│                     │  │                     │  │                     │
│ • Parse JSON input  │  │ • Build site map    │  │ • Handle long       │
│ • Extract modules   │  │ • Find routes       │  │   descriptions      │
│ • Identify UI       │  │ • Auth requirements │  │ • Preserve context  │
│   elements          │  │ • Module deps       │  │ • Semantic splits   │
└─────────────────────┘  └─────────────────────┘  └─────────────────────┘
            │                       │                       │
            └───────────────────────┼───────────────────────┘
                                    ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                        TEST GENERATION AGENT                               │
│                                                                            │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │ POSITIVE TESTS  │  │ NEGATIVE TESTS  │  │  EDGE CASES     │             │
│  │                 │  │                 │  │                 │             │
│  │ • Happy paths   │  │ • Empty fields  │  │ • Boundaries    │             │
│  │ • Valid flows   │  │ • Invalid input │  │ • Max lengths   │             │
│  │ • Alt scenarios │  │ • Wrong types   │  │ • Special chars │             │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘             │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ASSEMBLER AGENT                                     │
│                                                                             │
│ • Combine all tests                                                         │
│ • Add navigation steps to each test                                         │
│ • Remove duplicates                                                         │
│ • Order by module and priority                                              │
│ • Format as Markdown / JSON                                                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              OUTPUT                                         │
│                                                                             │
│  ┌──────────────────────┐    ┌──────────────────────┐                       │
│  │   test-cases.md      │    │   test-cases.json    │                       │
│  │   (Human readable)   │    │   (For Testing-Agent)│                       │
│  └──────────────────────┘    └──────────────────────┘                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Agent Details

### Agent 1: Parser Agent

**Purpose**: Parse and understand the functional description JSON

**Input**: 
```json
{
  "project_name": "Parabank",
  "website_url": "https://...",
  "navigation_overview": "...",
  "modules": [...]
}
```

**Processing**:
1. Validate JSON structure
2. Extract project metadata
3. For each module:
   - Parse title and description
   - Extract UI elements (buttons, inputs, dropdowns, tables)
   - Identify validation rules mentioned
   - Identify actions users can perform

**Output**:
```
ParsedFunctionalDescription
├── project_name: str
├── base_url: str
├── navigation_overview: str
└── modules: List[ParsedModule]
    ├── id: int
    ├── title: str
    ├── raw_description: str
    ├── ui_elements: List[UIElement]
    │   ├── name: str
    │   └── is_required: string/mentioned in description/not mentioned/ required
    ├── business_rules: List[str]
    ├── requires_auth: bool
    └── possible_actions: List[str]
```

**LLM Usage**: 
- Use LLM to extract UI elements and rules from natural language descriptions
- Prompt: "Extract all UI elements  from this description..."

---

### Agent 2: Navigation Agent

**Purpose**: Build a navigation graph of the website

**Input**: 
- `navigation_overview` string
- List of modules

**Processing**:
1. Parse the navigation overview to understand site structure
2. Identify which modules are accessible from the sidebar menu
3. Identify authentication requirements (login module = no auth, others = auth required)
4. Build relationships between modules

**Output**:
```
NavigationGraph
├── nodes: Dict[module_id → PageNode]
│   ├── module_id: int
│   ├── title: str
│   ├── requires_auth: bool
│   └── reachable_from: List[int]
│
└── get_route(from_module, to_module) → List[NavigationStep]
    ├── action: str (click, navigate)
    ├── target: str (element to click)
    └── expected_result: str
```

**Key Logic**:
```
For ParaBank example:
- Login (id=1): requires_auth=False, is_entry=True
- Register (id=3): requires_auth=False
- Forgot Password (id=2): requires_auth=False
- All others: requires_auth=True, reachable from sidebar after login

Route to "Transfer Funds":
1. Navigate to login page
2. Enter credentials
3. Click "Log In"
4. Click "Transfer Funds" in sidebar
```

---

### Agent 3: Chunker Agent

**Purpose**: Handle long functional descriptions that exceed LLM context limits

**When to Use**: Only when a module description is too long (> 2000 tokens)

**Input**: A single module with long description

**Processing**:
1. Estimate token count of description
2. If under limit → return as single chunk
3. If over limit → split by semantic sections:
   - Forms section (inputs, fields)
   - Table/Display section
   - Action section (buttons, workflows)
   - Validation section (error conditions)

**Output**:
```
List[Chunk]
├── chunk_id: str
├── module_id: int
├── module_title: str
├── content: str (the chunk text)
├── chunk_type: str (form/table/action/full)
├── context: str (summary of other parts)
└── token_count: int
```

**Context Preservation**:
Each chunk includes:
- Global context: Project name, URL, navigation summary (max 200 tokens)
- Module context: Summary of other sections in same module
- This ensures LLM understands the full picture even when processing a chunk

---
