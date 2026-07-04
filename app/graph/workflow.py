from langgraph.graph import START, END, StateGraph
from app.llm.openai_client import OpenAIClient
from app.graph.state import WorkFlowState
from app.graph.nodes.planner_node import PlannerNode

llm = OpenAIClient()

builder = StateGraph(WorkFlowState)

builder.add_node(
    "planner",
    PlannerNode(llm),
)

builder.add_edge(
    START,
    "planner"
)

builder.add_edge(
    "planner",
    END
)

graph = builder.compile()