from app.llm.openai_client import OpenAIClient
from app.tools.github import GitHub
from app.agents.planner import PlannerAgent
from app.graph.workflow import graph

def main():
    # agent = LLM()
    # while True:
        # task = input('Enter Question : ')
        # if task.lower() in ["bye", "exit"]:
        #     break
        
        # resp = agent.askGitAI(task)
        # print(f"response : {resp}")

    result = graph.invoke(
        {
            "user_request" : "Add JWT authentication",
            "repository_path": "/Users/uttejterlapu/projects/ai-agents/file-agent",
        }
    )
    # print(result["plan"])
    # print(result["repository"].tree)
    # planner = PlannerAgent(OpenAIClient())
    # resp = planner.run("Add JWT authentication")
    # print(type(resp))
    # print(resp)

    # repoName = "uttejterlapu/vybe"

    # githubTool = GitHub(repoName)

    # fileName = "README.md"
    # git = githubTool.fileReader(fileName)
    # githubTool.getGitTree()
    # print(git)
        # return

if __name__ == "__main__":
    main()