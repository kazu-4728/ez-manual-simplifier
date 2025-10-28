# AGENTS Playbook (All Agents: Copilot / Codex / Cursor-Claude / Gemini / o3)

## ゴール
- すべての **エージェント**（Copilot, Codex, Cursor/Claude, Gemini, o3 など）が **同じルール** と **同じ手順** でMarkdownを扱い、CIの`markdownlint`を100%合格する。
- 迷ったらここに書かれた順序で実行する（Lint-First）。

## ルール（Markdown）
- 見出し階層は飛ばさない（# → ## → ###）。
- 行長は原則120。**表/URL/コードブロックは免除**。
- インラインHTMLは許可（必要最小限）。
- 箇条書きは `-` に統一。番号は `1.` で良い（自動連番）。
- 必要に応じて次行のみ免除：`<!-- markdownlint-disable-next-line ルール名 -->`

## ワークフロー（必ずこの順）
1. 自動整形：`pwsh -File ./tools/fix_md_blanklines.ps1`
2. 直らない箇所のみ **ピンポイントで** 免除コメントを付ける
3. コミット→PR。PR本文に *目的/変更点/検証手順/ロールバック* を明記
4. CIで自動的に `markdownlint-cli2-action` が実行される

## エージェント別の注意
- **Copilot**: `.github/copilot-instructions.md` と `.github/instructions/` を優先読解。提案が大幅改変になりそうなら理由をPR本文へ。
- **Codex**: 変更は最小差分（DIFF）。`AGENTS.md`の手順を守り、CIが緑になるまで再提案。
- **Cursor/Claude**: 大きなリライトは避け、章立て/表/図の**構造を維持**。長文は120桁制約を意識。
- **Gemini/o3**: 日本語文体のゆれを抑制し、機械可読性（表・リスト・コードブロック）を優先。

## 失敗時の処置
- CI `markdownlint` が赤：ログのルール名→該当行を修正。表やURLなら `.markdownlint.json` で免除済みか確認。
- 既存大ファイルで大量落ちる：段階的修正に切替。PR粒度は小さく、毎回CI緑で進める。

## 使用ツール
- **PowerShellスクリプト**: `tools/fix_md_blanklines.ps1` - 自動整形（空行、見出し、リスト、コードブロックなど）
- **CI/CD**: GitHub Actions の `markdownlint-cli2-action` - 静的検査
- **設定**: `.markdownlint.json` - ルール設定（行長120、表/URLは免除など）
