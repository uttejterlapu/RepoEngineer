from typing import Optional
from typing_extensions import TypedDict # type: ignore[import]
from app.agents.planner.models import Plan
from app.agents.repository.models import RepositorySummary
from app.agents.retriever.models import RetrievedContext
class WorkFlowState(TypedDict):
    user_request : str
    repository_path : str
    plan : Optional[Plan]
    repository : Optional[RepositorySummary]
    retrieved_context : RetrievedContext
