from app.agents.retriever.agent import RetrieverAgent

class RetrieverNode:
    def __init__(self):
        self.agent = RetrieverAgent()
    
    def __call__(self, state):
        retrieved_context = self.agent.run(
                user_request=state["user_request"],
                repository_path=state["repository_path"]
            )
        print(retrieved_context)
        return {
            "retrieved_context": retrieved_context
        }