"""Project initialization script for template customization."""

import re
import sys
from pathlib import Path

# プロジェクトルート
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# テンプレートのデフォルトパッケージ名
TEMPLATE_NAME = "pylibrarytemplate"


def initialize_project(project_name: str) -> None:
    """テンプレートのパッケージ名を指定した名前に置き換える。"""
    if not re.fullmatch(r"[a-z][a-z0-9_]*", project_name):
        raise ValueError(
            f"Invalid project name: '{project_name}'. "
            "Use lowercase letters, digits, and underscores only. "
            "Must start with a letter."
        )

    src_dir = PROJECT_ROOT / "src"
    old_package = src_dir / TEMPLATE_NAME
    new_package = src_dir / project_name

    if not old_package.exists():
        raise FileNotFoundError(f"Template package not found: {old_package}")

    if new_package.exists():
        raise FileExistsError(f"Package already exists: {new_package}")

    # 1. ディレクトリリネーム
    old_package.rename(new_package)

    # 2. pyproject.toml の置換
    pyproject = PROJECT_ROOT / "pyproject.toml"
    pyproject.write_text(
        pyproject.read_text(encoding="utf-8").replace(TEMPLATE_NAME, project_name),
        encoding="utf-8",
    )

    # 3. README.md をプロジェクト名のタイトルのみにリセット
    readme = PROJECT_ROOT / "README.md"
    readme.write_text(f"# {project_name}\n", encoding="utf-8")

    print(f"Project initialized: {TEMPLATE_NAME} -> {project_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(__file__).name} <project_name>")
        sys.exit(1)

    initialize_project(sys.argv[1])
