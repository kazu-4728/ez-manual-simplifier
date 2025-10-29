# マニュアル簡易化サイト（リポジトリ案内）

> 分からない人が見ても分かる——それがマニュアル。ここは**サイトを作るためのリポジトリ**です。Copilotのイントロは保持しつつ、ユーザー案内は本ページで行います。

## 構成（壊さない方針／公開=Pages、裏方=Workers）
- `/site` …… GitHub Pages（フロント）
- `/workers` …… Cloudflare Workers（スクレイピング等の中継）
- `/data` …… 生成物（JSON/画像など）
- `/docs` …… ドキュメント（開発・運用・AIガイド）
- `/ops` …… 作業エリア（ドラフトや内部向け）
- `/.github` …… GitHub設定（Copilot Introduction など）

> Copilot の設定・指示は **`.github/copilot-instructions.md`** にあります。**削除・上書きしません**。

## まずやること（段階0：非破壊の索引追加）
1. **INDEX作成**：`/docs/_INDEX.md` とサブINDEXを追加（既存ファイルは移動しない）
2. **READMEから導線**：本READMEに目次を置き、Copilot Intro ではなく**リポジトリ全体案内**を提示
3. **Pages/Workersの入口だけ**：`/site/README.md` と `/workers/README.md` を最小で用意

## 目次（入口）
- 開発系：[`docs/dev/_INDEX.md`](docs/dev/_INDEX.md)
- AI/エージェント：[`docs/ai/_INDEX.md`](docs/ai/_INDEX.md)
- 運用・作業：[`docs/ops/_INDEX.md`](docs/ops/_INDEX.md)
- Copilot（参考）：[`.github/copilot-instructions.md`](.github/copilot-instructions.md)

## 編集方針（簡潔）
- **要約禁止／構造維持**：原文は残し、隣に“やさしい版”を並置
- **Lintはローカル吸収**：CIの強制は慎重に（運用が止まらないことを最優先）
- **非破壊**：移動は段階的に。まずはINDEXで束ね、参照切れゼロで進める

---
このREADMEは**ユーザー案内**です。Copilotイントロは保持し、ここから全体像に誘導します。