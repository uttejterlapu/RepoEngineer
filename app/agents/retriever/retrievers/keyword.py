from pathlib import Path

from app.agents.retriever.models import RetrievedFile
from app.agents.retriever.retrievers.base import Retriever

class KeywordRetriever(Retriever):
    STOP_WORDS = {
        "add",
        "create",
        "update",
        "modify",
        "implement",
        "the",
        "a",
        "an",
        "to",
        "for",
        "with",
        "of",
    }

    IGNORE = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        "node_modules",
    }
    
    def retrieve(
        self,
        user_request : str,
        repository_root : Path,
    ) -> list[RetrievedFile]:
        keywords = [
            word.lower()
            for word in user_request.split()
            if word.lower() not in self.STOP_WORDS
        ]
        
        results = []
        for file in repository_root.rglob("*"):
            if any(part in self.IGNORE for part in file.parts):
                continue
            
            if not file.is_file():
                continue
            
            filename = file.name.lower()
            
            for keyword in keywords:
                if keyword in filename:
                    results.append(
                        RetrievedFile(
                            path=str(file.relative_to(repository_root)),
                            score=0.8,
                            reason=f"Filename matched '{keyword}'",
                        )
                    )
                    
                    break
        return results