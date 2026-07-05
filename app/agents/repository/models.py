from pydantic import BaseModel, Field

class Language(BaseModel):
    name: str
    file_count: int = 0

class Framework(BaseModel):
    name: str
    path: str

class PackageManager(BaseModel):
    name: str
    manifest: str

# class TestFramework(BaseModel):
#     name: str
#     path: str

# class DockerConfiguration(BaseModel):
#     file: str

# class CICDProvider(BaseModel):
#     name: str
#     path: str
    
class RepositorySummary(BaseModel):
    project_name : str
    repository_path : str
    is_git_repository : bool
    languages : list[Language] = Field(default_factory=list)
    frameworks : list[Framework] = Field(default_factory=list)
    package_manager : list[PackageManager] = Field(default_factory=list)
    test_framework : str | None = None
    root_files : list[str] = []
    directories : list[str] = []
    tree : str = "" 