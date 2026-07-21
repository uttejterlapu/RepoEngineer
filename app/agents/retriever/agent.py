from pathlib import Path

from app.agents.retriever.models import ( RetrievedContext, RetrievedFile )
from app.agents.retriever.retrievers.keyword import ( KeywordRetriever )

class RetrieverAgent:
    
    def __init__(self):
        self.retrievers = [
            KeywordRetriever(),
            # SymbolRetriever(),
            # DependencyRetriever(),
        ]
    
    def run(
        self,
        user_request : str,
        repository_path : str,
    ) -> RetrievedContext:
        root = Path(repository_path)
        
        files : dict[str, RetrievedFile] = {}        
        
        for retriever in self.retrievers:
            results = retriever.retrieve(
                user_request,
                root,
            )
            
            for result in results:
                existing = files.get(result.path)
                if(
                    existing is None
                    or result.score > existing.score
                ):
                    files[result.path] = result
        
        return RetrievedContext(
            files=sorted(
                files.values(),
                key=lambda file: file.score,
                reverse=True
            )
        )