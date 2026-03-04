"""cx-Freeze build script with automatic entry point discovery."""

import os
from pathlib import Path

from cx_Freeze import Executable, setup

# プロジェクトルートに移動（scripts/ から実行されても正しく動くようにする）
project_root = Path(__file__).resolve().parent.parent
os.chdir(project_root)

# main*.py パターンに一致するファイルを自動検出してビルド対象にする
executables = [
    Executable(script=str(path), target_name=path.stem)
    for path in sorted(Path(".").glob("main*.py"))
]

setup(
    executables=executables,
    options={
        "build_exe": {
            "include_path": ["src"],
        },
    },
)
