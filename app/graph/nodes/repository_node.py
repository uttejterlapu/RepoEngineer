from app.agents.repository.agent import RepositoryAnalyzerAgent

class RepositoryNode:
    def __init__(self):
        self.agent = RepositoryAnalyzerAgent()
        
    def __call__(self, state):
        summary = self.agent.run(
            state["repository_path"]
        )
        return {
            "repository":summary
        }