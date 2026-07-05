from pathlib import Path

from app.agents.repository.detectors.git_detector import GitDetector
from app.agents.repository.detectors.tree_builder import TreeBuilder
from app.agents.repository.detectors.language_detector import LanguageDetector
from app.agents.repository.detectors.package_manager_detector import PackageManagerDetector

from app.agents.repository.models import RepositorySummary

class RepositoryAnalyzerAgent:
    
    def __init__(self):
        self.tree_builder = TreeBuilder()
        self.language_detector = LanguageDetector()
        self.package_manager_detector = PackageManagerDetector()
        self.git_detector = GitDetector()
        
    def run(self, repo_path : str) -> RepositorySummary:
        root = Path(repo_path)
        root_files = []
        directories = []

        for item in sorted(root.iterdir()):
            if item.name.startswith("."):
                continue

            if item.is_file():
                root_files.append(item.name)
            else:
                directories.append(item.name)

        return RepositorySummary(
            project_name=root.name,
            repository_path=str(root.resolve()),
            root_files=root_files,
            directories=directories,
            is_git_repository=self.git_detector.detect(root),
            tree=self.tree_builder.detect(root),
            languages=self.language_detector.detect(root),
            package_manager=self.package_manager_detector.detect(root),
        )