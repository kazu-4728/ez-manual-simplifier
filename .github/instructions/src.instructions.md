# Source Code Instructions / ソースコード手順

The `src/` directory was cleared during the repository reset. Recreate the package only when new
functionality is ready.

`src/` ディレクトリはリポジトリのリセット時にクリアされました。新しい機能の準備ができた時のみ、パッケージを再作成してください。

## Expected Structure / 期待される構造

- `src/`: Python package root for the manual simplification engine
- `src/__init__.py`: Exposes public entry points
- Additional modules should be introduced per feature (e.g., `simplifier.py`, `converter.py`)

- `src/`: マニュアル簡略化エンジンの Python パッケージルート
- `src/__init__.py`: パブリックエントリーポイントを公開
- 機能ごとに追加モジュールを導入する（例：`simplifier.py`、`converter.py`）

## Development Guidelines / 開発ガイドライン

- Use Python 3.11+ type hints and dataclasses where appropriate
- Keep business logic in pure functions or small classes to help Copilot reason about them
- Write docstrings in English; include Japanese comments only when necessary for stakeholders
- Validate all external inputs and raise descriptive `ValueError` exceptions for invalid states

- 適切な場合は Python 3.11+ の型ヒントとデータクラスを使用する
- Copilot が理解しやすいように、ビジネスロジックは純粋関数または小さなクラスに保つ
- docstring は英語で記述し、ステークホルダー向けに必要な場合のみ日本語コメントを含める
- すべての外部入力を検証し、無効な状態に対して説明的な `ValueError` 例外を発生させる

## Testing Hooks / テストフック

- Mirror each new module with targeted tests under `tests/`
- Provide minimal reproduction snippets in docstrings to improve Copilot completions
- Run `python -m pytest` locally before submitting pull requests

- 新しいモジュールごとに `tests/` 下にターゲットテストを作成する
- Copilot の補完を改善するため、docstring に最小限の再現スニペットを提供する
- プルリクエストを送信する前に、ローカルで `python -m pytest` を実行する
