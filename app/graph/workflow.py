from langgraph.graph import START, END, StateGraph # type: ignore[import]

from app.graph.state import WorkFlowState

from app.graph.nodes.planner_node import PlannerNode
from app.graph.nodes.repository_node import RepositoryNode
from app.graph.nodes.retriever_node import RetrieverNode

from app.llm.openai_client import OpenAIClient


llm = OpenAIClient()

builder = StateGraph(WorkFlowState)

# Nodes
builder.add_node(
    "planner",
    PlannerNode(llm),
)

builder.add_node(
    "repository",
    RepositoryNode(),
)

builder.add_node(
    "retriever",
    RetrieverNode(),
)

# Edges
builder.add_edge(
    START,
    "planner",
)

builder.add_edge(
    "planner",
    "repository",
)

builder.add_edge(
    "repository",
    "retriever",
)

builder.add_edge(
    "retriever",
    END,
)

graph = builder.compile()