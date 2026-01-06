from dataclasses import dataclass, field
from typing import List, Dict, Optional


# ============================================================================
# Parser Agent Output
# ============================================================================

@dataclass
class ParsedModule:
    """Output from ParserAgent - represents a parsed module/page"""
    id: int
    title: str
    raw_description: str
    mentioned_items: List[str] = field(default_factory=list)
    workflows: List[str] = field(default_factory=list)
    business_rules: List[str] = field(default_factory=list)
    expected_behaviors: List[str] = field(default_factory=list)
    requires_auth: bool = True


@dataclass
class ParsedFunctionalDescription:
    """Complete parsed functional description"""
    project_name: str
    base_url: str
    navigation_overview: str
    modules: List[ParsedModule] = field(default_factory=list)


# ============================================================================
# Chunker Agent Output
# ============================================================================

@dataclass
class WorkflowChunk:
    """A chunk representing a single workflow within a module"""
    chunk_id: str
    module_id: int
    module_title: str
    workflow_name: str
    workflow_description: str
    related_items: List[str] = field(default_factory=list)
    related_rules: List[str] = field(default_factory=list)
    related_behaviors: List[str] = field(default_factory=list)


# ============================================================================
# Navigation Agent Output
# ============================================================================

@dataclass
class NavigationNode:
    """A node in the navigation graph representing a page/module"""
    module_id: int
    title: str
    requires_auth: bool
    url_path: Optional[str] = None
    connected_to: List[int] = field(default_factory=list)  # Module IDs reachable from here
    test_case_ids: List[str] = field(default_factory=list)  # Linked test cases


@dataclass
class NavigationGraph:
    """Navigation graph of the website"""
    nodes: Dict[int, NavigationNode] = field(default_factory=dict)
    login_module_id: Optional[int] = None
    graph_image_path: Optional[str] = None  # Path to generated graph image

    def to_dict(self) -> dict:
        """Convert to JSON-serializable dictionary"""
        return {
            "login_module_id": self.login_module_id,
            "graph_image_path": self.graph_image_path,
            "nodes": [
                {
                    "module_id": node.module_id,
                    "title": node.title,
                    "requires_auth": node.requires_auth,
                    "url_path": node.url_path,
                    "connected_to": node.connected_to,
                    "test_case_ids": node.test_case_ids
                }
                for node in self.nodes.values()
            ]
        }


# ============================================================================
# Test Case Output
# ============================================================================

@dataclass
class TestCase:
    """A single test case - simplified format"""
    id: str                      # LOGIN-001
    title: str                   # "Valid login with username"
    module_id: int
    module_title: str            # "Login"
    workflow: str                # "Login with credentials"
    test_type: str               # "positive" | "negative" | "edge_case"
    priority: str                # "High" | "Medium" | "Low"
    preconditions: str           # Single string or "None"
    steps: List[str] = field(default_factory=list)  # Test steps (no navigation)
    expected_result: str = ""    # Single expected outcome

    # Verification fields (populated by VerificationAgent for positive tests)
    reads_state: List[str] = field(default_factory=list)   # State this test reads/checks (e.g., ["account_balance"])
    writes_state: List[str] = field(default_factory=list)  # State this test modifies (e.g., ["account_balance"])
    verification_test_ids: List[str] = field(default_factory=list)  # Test IDs that can verify this test's result
    pre_verification_steps: List[str] = field(default_factory=list)   # Steps to verify initial state
    post_verification_steps: List[str] = field(default_factory=list)  # Steps to verify final state

    def to_dict(self) -> dict:
        """Convert to JSON-serializable dictionary"""
        result = {
            "id": self.id,
            "title": self.title,
            "module_id": self.module_id,
            "module_title": self.module_title,
            "workflow": self.workflow,
            "test_type": self.test_type,
            "priority": self.priority,
            "preconditions": self.preconditions,
            "steps": self.steps,
            "expected_result": self.expected_result
        }

        # Only include verification fields for positive tests that have them
        if self.test_type == "positive":
            if self.reads_state:
                result["reads_state"] = self.reads_state
            if self.writes_state:
                result["writes_state"] = self.writes_state
            if self.verification_test_ids:
                result["verification_test_ids"] = self.verification_test_ids
            if self.pre_verification_steps:
                result["pre_verification_steps"] = self.pre_verification_steps
            if self.post_verification_steps:
                result["post_verification_steps"] = self.post_verification_steps

        return result


# ============================================================================
# Final Output
# ============================================================================

@dataclass
class TestSuiteOutput:
    """Final output containing navigation graph and test cases"""
    project_name: str
    base_url: str
    generated_at: str
    navigation_graph: NavigationGraph
    test_cases: List[TestCase] = field(default_factory=list)
    summary: Dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to JSON-serializable dictionary"""
        return {
            "project_name": self.project_name,
            "base_url": self.base_url,
            "generated_at": self.generated_at,
            "navigation_graph": self.navigation_graph.to_dict(),
            "test_cases": [tc.to_dict() for tc in self.test_cases],
            "summary": self.summary
        }
