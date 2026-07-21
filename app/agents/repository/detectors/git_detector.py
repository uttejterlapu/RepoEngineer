from pathlib import Path
from app.agents.repository.detectors.detector import Detector

class GitDetector(Detector):
    def detect(self, root: Path) -> bool:
        return (root / ".git").exists()