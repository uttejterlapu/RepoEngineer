from app.agents.planner.prompt import PlannerAgent
from app.graph.state import WorkFlowState
from app.llm.base import LLMClient

class PlannerNode:
    def __init__(self, llm : LLMClient):
        self.agent = PlannerAgent(llm)
    
    def __call__(self, state : WorkFlowState):
        plan = self.agent.run(
            state["user_request"]
        )
        return {
            "plan" : plan
        }