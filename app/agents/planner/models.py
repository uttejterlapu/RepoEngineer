from pydantic import BaseModel
from typing import List, Literal

class Task(BaseModel):
    id : int
    title : str
    description : str

class Plan(BaseModel):
    goal : str

    category : Literal[
        "feature",
        "bug_fix",
        "refactor",
        "testing",
        "documentation",
        "dependency",
        "devops",
        "performance",
        "other",
    ]

    complexity : Literal[
        "low",
        "medium",
        "high",
        "very_high"
    ]

    clarification_required : bool

    clarification_question : List[str] = []

    tasks : List[Task]