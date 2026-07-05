from typing import Optional
from typing_extensions import TypedDict
from app.agents.planner.models import Plan
from app.agents.repository.models import RepositorySummary

class WorkFlowState(TypedDict):
    user_request : str
    repository_path : str
    plan : Optional[Plan]
    repository : Optional[RepositorySummary]
