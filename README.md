# PyLibraryTemplate

Python ライブラリ開発用のテンプレートリポジトリです。
src layout、uv による依存管理、hatchling によるパッケージビルドを標準構成としています。

## プロジェクト構成

```
ProjectName/
├── pyproject.toml            # プロジェクト設定
├── scripts/
│   └── init.py               # テンプレート初期化スクリプト
├── src/
│   └── <package_name>/
│       └── __init__.py       # パッケージコード
├── tests/                    # テスト
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

### パッケージの追加

```bash
# 本番依存の追加
uv add <package_name>

# 開発依存の追加
uv add --group dev <package_name>
```

## ビルド

```bash
uv build
```

ビルド成果物（sdist / wheel）は `dist/` に出力されます。

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

## 設計思想

### 依存は最小限に

テンプレートの `dependencies` は空です。ライブラリの依存は利用者のプロジェクトに波及するため、必要なものだけを都度追加してください。

### 開発者が設定に触れないことを重視

- `pyproject.toml` はテンプレート初期化時に自動設定されるため、開発者が編集する必要はありません
- ビルド・リリースは CI/CD で自動実行されるため、開発者はドメインロジックとコードに集中できます
