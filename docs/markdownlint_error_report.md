# Markdownlint Error Report (2025-10-11)

## 概要

- 発生日時: 2025年10月11日

- 発生場所: VS Code 上での Markdown 構文修正作業中

- 影響範囲: 既存 Markdown ファイル 17 件（主にドキュメント群）

- 参照ログ: `docs/WORK_LOG.md` の「2025年10月11日（Markdownlint 対策）」セクション

## 検出されたルール違反

| ルールID | 内容 | 主な原因例 |
| --- | --- | --- |
| MD012 | 連続した空行 | 自動整形により空行が2行以上続いた箇所 |
| MD022 | 見出しと本文の間の空行不足 | 見出し直下に本文が続き、空行がないケース |
| MD031 | コードブロック周辺の空行不足 | コードフェンス前後に空行がない箇所 |
| MD032 | リストとその他要素の間の空行不足 | 箇条書きと段落／コードブロックが連結していた箇所 |
| MD040 | コードフェンスの閉じ忘れ・言語指定不足 | 3バッククォートの閉じ忘れや言語未指定のコードブロック |

## 実施済みの対応

- 既存 Markdown 17 ファイルの整形とルール違反の一括修正

- 自動修正スクリプトの追加と実行

  - `tools/fix_md_blanklines.ps1`

  - `tools/fix_md_blanklines.py`

- 自動修正スクリプトの不具合修正（2025-10-11）

  - **問題**: スクリプトが `.github/` 内のファイルを処理せず、修正後も MD012 エラーが残存

  - **原因1**: `Get-ChildItem` に `-Force` フラグが欠けていたため、隠しディレクトリを処理できなかった

  - **原因2**: `$text -split "\r?\n", -1` の `, -1` パラメータにより、テキストが行分割されなかった

  - **原因3**: `Set-Content` で `-NoNewline` フラグがなく、保存時に余分な改行が追加されていた

  - **修正内容**: 上記3点を修正し、LF改行への対応も追加

- lint 設定の明示化

  - `.markdownlint.json`

  - `.vscode/settings.json`

- VS Code 用スニペット／タスクの整備

  - `.vscode/snippets/markdown.json`

  - `.vscode/tasks.json`

- Git フックとインストールスクリプトの導入

  - `.githooks/pre-commit`

  - `tools/install_hooks.ps1`

- CI への Markdownlint チェック追加

  - `.github/workflows/markdownlint.yml`

## 今後の対応予定

- ~~コードフェンスへの言語指定の精緻化（例：`bash`, `markdown` など）~~ 完了

- ~~追加の lint 違反が検出された場合の個別対処~~ 完了（全エラー解消）

- Markdownlint ルール調整案の検討と合意形成（必要に応じて）

## リスクと留意事項

- 自動整形スクリプト適用時には、ドキュメントの意味的な改変が行われていないかをレビューすること

- VS Code 以外のエディタを使用する場合、`.markdownlint.json` を参照するよう設定すること

- 新規ドキュメント追加時は、見出しやリスト前後の空行を意識し再発防止を図ること

## 参考

- 詳細ログ: [`docs/WORK_LOG.md`](./WORK_LOG.md)

- Markdownlint ルール一覧: <https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md>
