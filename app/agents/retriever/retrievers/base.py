from abc import ABC, abstractmethod
from pathlib import Path

from app.agents.retriever.models import RetrievedFile

class Retriever(ABC):
    
    @abstractmethod
    def retrieve(
        self,
        user_request : str,
        repository_root : Path
    ) -> list[RetrievedFile]:
        raise NotImplementedError