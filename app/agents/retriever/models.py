from pydantic import BaseModel, Field # type: ignore[import]

class RetrievedFile(BaseModel):
    path : str
    score : str
    reason : str

class RetrievedContext(BaseModel):
    files : list[RetrievedFile] = Field(default_factory=list)