# AGENTS Playbook (All Agents: Copilot / Codex / Cursor-Claude / Gemini / o3)

## ゴール
- すべての **エージェント** が **同じルール** と **同じ手順** でMarkdownを扱い、**執筆は止めずに** 最終成果物だけ整える。
- Lintは **VS Codeのローカル設定（.vscode/settings.json）** で制御。CIのmarkdownlintは **既定で無効**。

## ルール（Markdown）
- 見出し階層は飛ばさない（# → ## → ###）。
- 行長は自由（120目安）。**表/URL/コードは免除**。
- インラインHTMLは必要最小限で許可。
- 箇条書きは `-` に統一。番号は `1.` で良い。
- 必要に応じて次行のみ免除：`<!-- markdownlint-disable-next-line ルール名 -->`。

## ワークフロー（最短手順）
1. 執筆/修正を行う（Lintで止めない）
2. 気になる箇所のみ `Ctrl+Shift+P → Markdown: Open Preview` で見た目確認
3. 必要なら `Format Document`（整形）
4. コミット→PR。PR本文に *目的/変更点/検証手順/ロールバック* を明記

## エージェント別の注意
- **Copilot / Codex / Cursor/Claude / Gemini / o3**: 大きなリライトは避け、章立て/表/図の**構造を維持**。
- Lint違反が出ても **コミットを止めない**。必要なら `.vscode/settings.json` を見直す。

## 失敗時の処置
- VS Codeで赤線が多い：拡張の競合（markdownlint/Prettier/他Lint）。**拡張を一時無効化**または本設定で緩和。
- 既存大ファイルで大量落ちる：段階的修正。PR粒度は小さく、毎回目視で整える。
