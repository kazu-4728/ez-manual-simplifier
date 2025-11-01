# EZ Manual Simplifier - 実装サマリー（改訂版）

## 更新日: 2025年11月1日

---

## 📊 プロジェクト状態

### 現在のフェーズ
**Phase 1a: UIファースト開発（準備完了）**

### 進捗状況
- **Phase 1**: 0%（要件定義完了、実装未開始）
- **全体**: 0%

---

## 🎯 プロジェクト方針の大幅変更

### 変更の背景

**以前の方針**:
- Python Backend（FastAPI/Flask）
- markitdown使用
- Gemini API統合から開始

**問題点**:
- コア価値（URL変換）が不明確
- バックエンド構築に時間がかかる
- APIキー露出のリスク

### 新しい方針

**UIファースト開発**:
```
Week 1: UI作成（モックデータ）
  ↓ デザイン確認
Week 2: バックエンド構築
  ↓ 統合
Week 3: テスト＆改善
```

**技術スタック変更**:
```
変更前: Python Backend + markitdown
変更後: JavaScript (Cloudflare Workers) + GitHub Secrets
```

**優先順位変更**:
```
変更前: テキスト入力 → ファイルアップロード → URL対応
変更後: URL対応（最優先） → テキスト入力 → ファイルアップロード
```

---

## 🏗️ 新しいアーキテクチャ

### システム構成

```
┌─────────────────────────────────────┐
│ フロントエンド（GitHub Pages）       │
│ - 静的HTML + CSS + JavaScript       │
│ - URL入力、結果表示                  │
└─────────┬───────────────────────────┘
          │ HTTPS
          ▼
┌─────────────────────────────────────┐
│ バックエンド（Cloudflare Workers）   │
│ - Webスクレイピング                  │
│ - LLM API呼び出し                    │
│ - キャッシュ管理                     │
└─────────┬───────────────────────────┘
          │
          ▼
┌─────────────────────────────────────┐
│ LLM API                             │
│ - Gemini Pro（無料枠）               │
│ - OpenAI API（予備）                 │
└─────────────────────────────────────┘
```

### セキュリティフロー

```
GitHub Secrets（APIキー保管）
  ↓
GitHub Actions（デプロイ時に環境変数設定）
  ↓
Cloudflare Workers（サーバー側で使用）
  ↓
ブラウザには結果のみ返却（APIキー露出なし）
```

---

## 📁 新しいリポジトリ構成

### ディレクトリ構造

```
/workspace/
├─ web/                        # フロントエンド（新規）
│   ├─ index.html             # メインページ
│   ├─ css/
│   │   └─ style.css          # デザイン
│   ├─ js/
│   │   ├─ app.js             # メインロジック
│   │   ├─ ui.js              # UI操作
│   │   └─ mock-data.js       # モックデータ（Week 1のみ）
│   └─ assets/
│       └─ icons/             # アイコン
│
├─ api/                        # バックエンド（新規）
│   ├─ index.js               # メインエンドポイント
│   ├─ scraper.js             # URL取得
│   ├─ simplifier.js          # 簡易化ロジック
│   ├─ llm.js                 # LLM統合
│   └─ wrangler.toml          # Cloudflare設定
│
├─ .github/
│   └─ workflows/             # CI/CD（新規）
│       ├─ deploy-frontend.yml
│       └─ deploy-api.yml
│
├─ src/                       # Python実装（保留）
│   ├─ converter.py           # ファイルアップロード対応時に使用
│   └─ simplifier.py          # 参考実装
│
├─ tests/                     # テスト（保留）
│   ├─ test_converter.py
│   └─ test_simplifier_integration.py
│
├─ docs/                      # ドキュメント
│   ├─ PROJECT_REQUIREMENTS.md  # 要件定義（更新済み）
│   ├─ TASKS.md                 # タスク一覧（更新済み）
│   ├─ IMPLEMENTATION_SUMMARY.md # このファイル
│   ├─ PROGRESS_TRACKING.md     # 進捗管理（次に更新）
│   ├─ AGENT_ORCHESTRATION.md
│   ├─ TASK_MANAGEMENT.md
│   ├─ COST_OPTIMIZATION.md
│   └─ SUB_AGENTS.md
│
├─ .env.example               # 環境変数サンプル（新規）
├─ requirements.txt           # Python依存関係（保留）
├─ package.json               # Node.js依存関係（新規）
├─ README.md
└─ LICENSE
```

### 既存ファイルの扱い

**保留（削除しない）**:
- `src/converter.py` - ファイルアップロード機能で将来使用
- `src/simplifier.py` - Python実装の参考
- `tests/` - 将来のテストに活用

**理由**:
- URL変換（JavaScript実装）が最優先
- Python実装は Phase 1後半で必要になる可能性
- 既存のテストケースは参考になる

---

## 🔧 技術仕様

### フロントエンド

**技術スタック**:
- HTML5
- CSS3（Flexbox, Grid）
- Vanilla JavaScript（フレームワーク不使用）

**デザイン方針**:
- 参考: Linear, Notion, Vercel
- カラー: インディゴ/パープル系
- レスポンシブ対応必須

**主要機能**:
1. URL入力フォーム
2. レベル選択（low/medium/high）
3. 結果表示（ビフォー・アフター並列）
4. ダウンロード機能（HTML/Markdown/テキスト）

### バックエンド

**技術スタック**:
- JavaScript/Node.js
- Cloudflare Workers
- Wrangler CLI

**主要機能**:
1. Webスクレイピング（Cheerio）
2. LLM API呼び出し（Gemini/OpenAI）
3. キャッシュ管理（Cloudflare R2）
4. エラーハンドリング

### LLM統合

**プライマリ**: Gemini 1.5 Pro
- 無料枠: 1日15リクエスト
- 用途: テスト段階

**セカンダリ**: OpenAI GPT-4o
- 課金済み: $5
- 用途: Gemini無料枠使い切った場合

**プロンプト戦略**:
```javascript
const prompts = {
  low: `
あなたは技術ドキュメントを小学生でも理解できるように変換する専門家です。

【ルール】
1. 専門用語を平易な言葉に置き換える
2. 具体的な比喩を追加
3. ステップバイステップの手順に変換

【入力】
{text}

【出力】
`,
  medium: `一般的な読みやすさに簡易化...`,
  high: `専門用語は残しつつ説明を追加...`
};
```

---

## 📅 開発スケジュール

### Week 1: UIファースト（3-4日）

| タスク | 内容 | 状態 |
|--------|------|------|
| TASK-UI-001 | 基本レイアウト | pending |
| TASK-UI-002 | 結果表示UI | pending |
| TASK-UI-003 | モックデータ統合 | pending |
| TASK-UI-004 | UI/UX改善 | pending |

**成果物**: 
- 美しいUI（モックデータ動作）
- プロダクトオーナーによるデザイン確認

### Week 2: バックエンド構築（5-7日）

| タスク | 内容 | 状態 |
|--------|------|------|
| TASK-BACKEND-001 | Cloudflare Workersセットアップ | pending |
| TASK-BACKEND-002 | URL取得機能 | pending |
| TASK-BACKEND-003 | LLM統合 | pending |
| TASK-BACKEND-004 | GitHub Secrets設定 | pending |
| TASK-BACKEND-005 | GitHub Actionsセットアップ | pending |
| TASK-BACKEND-006 | キャッシュ機能 | pending |

**成果物**:
- 動作するバックエンドAPI
- 自動デプロイ環境

### Week 3: 統合＆テスト（3-5日）

| タスク | 内容 | 状態 |
|--------|------|------|
| TASK-INT-001 | フロントエンド・バックエンド統合 | pending |
| TASK-INT-002 | テスト実施 | pending |
| TASK-INT-003 | デプロイ＆公開準備 | pending |

**成果物**:
- 完全に動作するWebサイト
- テスト完了
- ドキュメント整備

---

## 💰 コスト試算

### 無料枠（Phase 1）

| サービス | 無料枠 | 推定使用量 | コスト |
|---------|--------|-----------|-------|
| GitHub Pages | 無制限 | 1GB/月 | **$0** |
| Cloudflare Workers | 100k req/日 | 100 req/日 | **$0** |
| Gemini API | 15 req/日 | 10 req/日 | **$0** |
| GitHub Actions | 2000分/月 | 100分/月 | **$0** |
| Cloudflare R2 | 10GB | 1GB | **$0** |
| **合計** | - | - | **$0/月** |

**注意**:
- テスト段階はプロダクトオーナー1人のみ使用
- Gemini無料枠で十分
- 公開後はキャッシュで対応

---

## 🎯 Phase 1完了条件

### 技術的完了条件

- [ ] GitHub docsのURL変換が成功する
- [ ] 3段階のレベルで簡易化できる
- [ ] UIが美しく使いやすい
- [ ] APIキーが完全に保護されている
- [ ] レスポンシブ対応（PC/スマホ）
- [ ] エラーハンドリングが適切
- [ ] 自動デプロイが動作する

### ビジネス完了条件

- [ ] プロダクトオーナーが満足して使える
- [ ] 新人社員に試してもらって理解できる
- [ ] 「これは便利だ」と感じられる

### 判断基準

**成功**: Phase 2へ進む
**失敗**: 方針転換 or 撤退

---

## 🔄 エージェントオーケストラ活用

### 開発体制

```
Orchestrator（マスターエージェント）
  ├─ Frontend Sub-Agent（UI担当）
  ├─ Backend Sub-Agent（API担当）
  ├─ Simplifier Sub-Agent（LLM統合担当）
  └─ Test Sub-Agent（テスト担当）
```

### 作業割り振り

- **Week 1**: Frontend Sub-Agent主導
- **Week 2**: Backend Sub-Agent + Simplifier Sub-Agent
- **Week 3**: 全エージェント協調

### コンテキスト管理

- 各サブエージェントは必要最小限のファイルのみ読み込み
- ドキュメント参照を明確化
- 無駄なコンテキスト消費を避ける

---

## 📝 作業再開ガイド

### いつでも作業を再開できるように

**現在地**: Phase 1a準備完了

**次のアクション**:
```
指示: 「TASK-UI-001を開始してください」
```

**その他の開始方法**:
- バックエンドから: 「TASK-BACKEND-001を開始してください」
- 統合フェーズから: 「TASK-INT-001を開始してください」

---

## 📚 関連ドキュメント

- [要件定義](./PROJECT_REQUIREMENTS.md) - 更新済み ✅
- [タスク一覧](./TASKS.md) - 更新済み ✅
- [進捗管理](./PROGRESS_TRACKING.md) - 次に更新予定
- [エージェントオーケストラ体制](./AGENT_ORCHESTRATION.md)
- [コスト最適化ガイドライン](./COST_OPTIMIZATION.md)

---

## 🎉 まとめ

### 変更点
1. ✅ UIファースト開発に方針変更
2. ✅ URL変換を最優先に
3. ✅ GitHub Secrets + Cloudflare Workers構成
4. ✅ 完全無料構成
5. ✅ 段階的開発（3週間）

### 次のステップ
1. TASK-UI-001開始（基本レイアウト作成）
2. Week 1完了後、デザイン確認
3. Week 2へ進む

---

**最終更新**: 2025年11月1日
**バージョン**: 2.0（全面改訂）
**作成者**: Orchestrator Agent
