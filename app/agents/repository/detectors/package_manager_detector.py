from pathlib import Path
from app.agents.repository.detectors.detector import Detector
from app.agents.repository.models import PackageManager

class PackageManagerDetector(Detector):
    PACKAGE_MANAGERS = {
        "requirements.txt": "pip",
        "pyproject.toml": "poetry",
        "poetry.lock": "poetry",
        "Pipfile": "pipenv",

        "package-lock.json": "npm",
        "package.json": "npm",
        "yarn.lock": "yarn",
        "pnpm-lock.yaml": "pnpm",

        "pom.xml": "maven",
        "build.gradle": "gradle",
        "build.gradle.kts": "gradle",

        "Cargo.toml": "cargo",
        "go.mod": "go",
    }
    
    @classmethod
    def detect(self, root: Path) -> list[PackageManager]:
        package_managers = []

        for file in root.rglob("*"):

            if not file.is_file():
                continue

            manager = self.PACKAGE_MANAGERS.get(file.name)

            if manager:

                package_managers.append(
                    PackageManager(
                        name=manager,
                        manifest=str(file.relative_to(root)),
                    )
                )

        return package_managers