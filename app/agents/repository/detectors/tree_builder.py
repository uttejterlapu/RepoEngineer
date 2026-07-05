from pathlib import Path
from app.agents.repository.detectors import Detector

class TreeBuilder(Detector):
    IGNORE = {
        ".git",
        ".github",          # optional
        "venv",
        ".venv",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        "node_modules",
        ".idea",
        ".vscode",
        ".DS_Store",
    }

    @classmethod
    def detect(self, root: Path) -> str:
        lines = [root.name]
        self._walk(root, "", lines)
        return "\n".join(lines)
    
    @classmethod
    def _walk(self, directory : Path, prefix : str, lines : list[str]):
        children = sorted(
            [
                child
                for child in directory.iterdir()
                if child.name not in self.IGNORE
            ],
            key = lambda p: (p.is_file(), p.name.lower()),
        )

        for index, child in enumerate(children):
            connector = "└── " if index == len(children) -1 else "├── "
            lines.append(prefix + connector + child.name)

            if child.is_dir():
                extension = "    " if index == len(children) - 1 else "│   "
                self._walk(
                    child,
                    prefix + extension,
                    lines
                )