from typing import Optional
from typing_extensions import TypedDict
from app.models.planner_models import Plan

class WorkFlowState(TypedDict):
    user_request : str
    plan : Optional[Plan]
