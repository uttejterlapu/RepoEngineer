from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

class Detector(ABC):
    @abstractmethod
    def detect(self, root:Path) -> Any:
        raise NotImplementedError