from app.agents.planner.models import Plan
from app.agents.planner.prompt import SYSTEM_PROMPT
from app.llm.base import LLMClient

class PlannerAgent:
    def __init__(self, llm: LLMClient):
        self.llm = llm

    def run(self, user_input: str) -> Plan:
        return self.llm.generate(
            system_prompt=SYSTEM_PROMPT,
            user_prompt= f"""User Request:\n{user_input}""",
            response_model=Plan,
        )