from collections import Counter
from pathlib import Path
from app.agents.repository.detectors.detector import Detector
from app.agents.repository.models import Language

class LanguageDetector(Detector):
    LANGUAGE_MAP = {
        ".py" : "Python",
        ".js": "JavaScript",
        ".jsx": "JavaScript",
        ".ts": "TypeScript",
        ".tsx": "TypeScript",
        ".java": "Java",
        ".kt": "Kotlin",
        ".go": "Go",
        ".rs": "Rust",
        ".cpp": "C++",
        ".cc": "C++",
        ".cxx": "C++",
        ".c": "C",
        ".cs": "C#",
        ".php": "PHP",
        ".rb": "Ruby",
        ".swift": "Swift",
        ".scala": "Scala",
        ".dart": "Dart",
        ".m": "Objective-C",
        ".mm": "Objective-C++",
        ".sh": "Shell",
    }
    
    IGNORE = {
        ".git",
        "venv",
        ".venv",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        "node_modules",
        ".idea",
        ".vscode",
    }
    
    def detect(self, root: Path) -> list[Language]:
        counter = Counter()
        for file in root.rglob("*"):
            if any(part in self.IGNORE for part in file.parts):
                continue
            
            if not file.is_file():
                continue
                
            detected_language = self.LANGUAGE_MAP.get(file.suffix)
            
            if detected_language:
                counter[detected_language] += 1

        return [
            Language(
                name=name,
                file_count=count,
            )
            for name, count in sorted(counter.items())
        ]