# Test Instructions / テスト手順

The `tests/` directory will be reintroduced alongside new source modules. Use this guide when rebuilding
the test suite.

`tests/` ディレクトリは新しいソースモジュールと共に再導入されます。テストスイートを再構築する際は、このガイドを使用してください。

## Test Layout / テストレイアウト

- Place unit tests under `tests/` mirroring the package structure in `src/`
- Name files using `test_*.py` so pytest can discover them automatically
- Keep fixtures small and reuseable; prefer factory functions over global state

- `src/` のパッケージ構造を反映して、`tests/` の下にユニットテストを配置する
- pytest が自動的に検出できるように、ファイル名は `test_*.py` を使用する
- フィクスチャは小さく再利用可能に保ち、グローバルステートよりもファクトリ関数を優先する

## Running Tests / テストの実行

```bash
# Run the entire suite / テストスイート全体を実行
python -m pytest

# Run a specific file / 特定のファイルを実行
python -m pytest tests/test_simplifier.py
```

## Quality Expectations / 品質要件

- Aim for high-coverage tests on the text simplification logic
- Include regression tests for previously fixed issues when restoring functionality
- Document tricky behaviours in test docstrings to assist Copilot's suggestions

- テキスト簡略化ロジックの高いカバレッジを目指す
- 機能復元時に以前修正された問題のリグレッションテストを含める
- Copilot の提案を支援するため、トリッキーな動作をテストの docstring に記載する
