from pathlib import Path


def abs_path_from_project(relative_path: str) -> str:
    project_root = Path(__file__).resolve().parent.parent
    return str(project_root / relative_path)
