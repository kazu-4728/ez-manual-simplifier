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

1. `npx markdownlint-cli2 "**/*.md"` で静的検査（または `pwsh tools/fix_md_blanklines.ps1` で事前整形）
2. 自動整形：`pwsh tools/fix_md_blanklines.ps1`（リスト・フェンス・見出し周りの空行を自動修正）
3. 直らない箇所のみ **ピンポイントで** 免除コメントを付ける
4. コミット→PR。PR本文に *目的/変更点/検証手順/ロールバック* を明記

## エージェント別の注意

- **Copilot**: `.github/copilot-instructions.md` と `.github/instructions/` を優先読解。提案が大幅改変になりそうなら理由をPR本文へ。
- **Codex**: 変更は最小差分（DIFF）。`AGENTS.md`の手順を守り、`md:check`が緑になるまで再提案。
- **Cursor/Claude**: 大きなリライトは避け、章立て/表/図の**構造を維持**。長文は120桁制約を意識。
- **Gemini/o3**: 日本語文体のゆれを抑制し、機械可読性（表・リスト・コードブロック）を優先。

## 失敗時の処置

- CI `markdownlint` が赤：ログのルール名→該当行を修正。表やURLなら `.markdownlint.json` で免除済みか確認。
- 既存大ファイルで大量落ちる：段階的修正に切替。PR粒度は小さく、毎回CI緑で進める。

## コマンド例

```bash
# 静的検査（CI で実行）
npx markdownlint-cli2 "**/*.md"

# 自動整形（PowerShell スクリプト）
pwsh tools/fix_md_blanklines.ps1

# または markdownlint-cli2-fix で自動修正
npx markdownlint-cli2-fix "**/*.md"
```

**注**: このプロジェクトは Python ベースで、`package.json` は使用していません。
CI では GitHub Actions が `markdownlint-cli2-action` を使用し、ローカルでは PowerShell スクリプトで整形します。
