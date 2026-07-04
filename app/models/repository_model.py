from pydantic import BaseModel

class RepositorySummary(BaseModel):

    project_name : str
    repository_path : str
    