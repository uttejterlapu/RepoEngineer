from github import Github
from app.config.settings import settings
# import base64

class GitHub:
    def __init__(self, repoName:str):
        gitClient = Github(settings.GITHUB_ACCESS_TOKEN)
        self.repo = gitClient.get_repo(repoName)
    
    def fileReader(self, fileName: str):
        file = self.repo.get_contents(fileName)
        return file.decoded_content.decode()
    
    def getGitTree(self):
        branch = self.repo.get_branch(self.repo.default_branch)
        tree = self.repo.get_git_tree(
            branch.commit.sha,
            recursive=True
        )
        treeArray =[]
        for item in tree.tree:
            treeArray.append(item.path)
        return treeArray