# PyApplicationTemplate

Python アプリケーション開発用のテンプレートリポジトリです。
cx-Freeze によるexeビルド、src layout、uv による依存管理を標準構成としています。

## プロジェクト構成

```
ProjectName/
├── main.py                  # エントリポイント（main*.py パターンで自動検出）
├── pyproject.toml            # プロジェクト設定
├── scripts/
│   ├── build.py              # cx-Freeze 自動ビルドスクリプト
│   └── init.py               # テンプレート初期化スクリプト
├── src/
│   └── <package_name>/
│       └── __init__.py       # パッケージコード
├── tests/                    # テスト
├── docs/                     # ドキュメント
├── .python-version
├── .gitignore
└── uv.lock
```

## 前提条件

- [uv](https://docs.astral.sh/uv/) がインストールされていること

## プロジェクトの初期化

```bash
# 1. テンプレート初期化
python scripts/init.py <project_name>

# 2. 仮想環境の作成
uv venv

# 3. 依存関係をインストール
uv sync --group dev
```

### デフォルトの依存パッケージ

型安全なデータモデリングのため、[pydantic](https://docs.pydantic.dev/) がデフォルトで含まれています。

### パッケージの追加

```bash
# 本番依存の追加
uv add <package_name>

# 開発依存の追加
uv add --group dev <package_name>
```

## ビルド

```bash
uv run python scripts/build.py build
```

ビルド成果物は `build/exe.<platform>.<python_version>/` に出力されます。

### 複数エントリポイント

ルートに `main*.py` パターンのファイルを配置すると、自動で検出されそれぞれのexeが生成されます。

```
main.py      → main.exe
main_gui.py  → main_gui.exe
main_cli.py  → main_cli.exe
```

## テスト

```bash
uv run pytest tests/ -v
```

## 開発ツール

| ツール | 用途 |
|--------|------|
| uv | パッケージ管理・依存解決 |
| ruff | リンター・フォーマッター |
| pytest | テストフレームワーク |
| radon | コード複雑度計測 |
| cx-Freeze | exe ビルド |

## 設計思想

### エントリポイントをルートに配置する理由

Python の標準的な src layout では `__main__.py` をパッケージ内に配置しますが、本テンプレートでは `main*.py` をプロジェクトルートに配置しています。
これは以下の理由による意図的な選択です：

- **視認性**: プロジェクトを開いた瞬間にエントリポイントが一目でわかる
- **複数エントリポイント**: `main.py`, `main_gui.py` などを追加するだけで自動検出される
- **オンボーディング**: 新規メンバーが Python パッケージングの知識なしでもエントリポイントを認識できる

### 開発者が設定に触れないことを重視

- `pyproject.toml` はテンプレート初期化時に自動設定されるため、開発者が編集する必要はありません
- ビルド・リリースは CI/CD で自動実行されるため、開発者はドメインロジックとコードに集中できます
- エントリポイントの追加は `main*.py` ファイルを作成するだけで完了し、設定変更は不要です

### cx-Freeze を採用する理由

- PySide6（LGPL）をGUIフレームワークとして使用するため、ライセンス互換性のある cx-Freeze を採用しています
- PyInstaller の `-F`（ワンファイル）モードは LGPL のライセンス要件を満たすことが困難です
