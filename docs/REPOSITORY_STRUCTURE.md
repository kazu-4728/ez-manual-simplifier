# リポジトリ構成ガイド

## 更新日: 2025年11月1日

このドキュメントは、リポジトリの構成と各ディレクトリ・ファイルの役割を明確にします。

---

## 📁 ディレクトリ構成

```
/workspace/
│
├─ web/                           # フロントエンド（Phase 1で作成予定）
│   ├─ index.html                 # メインページ
│   ├─ css/
│   │   └─ style.css              # デザイン
│   ├─ js/
│   │   ├─ app.js                 # メインロジック
│   │   ├─ ui.js                  # UI操作
│   │   └─ mock-data.js           # モックデータ（Week 1のみ）
│   └─ assets/
│       └─ icons/                 # アイコン
│
├─ api/                           # バックエンド（Phase 1で作成予定）
│   ├─ index.js                   # メインエンドポイント
│   ├─ scraper.js                 # URL取得
│   ├─ simplifier.js              # 簡易化ロジック
│   ├─ llm.js                     # LLM統合
│   ├─ wrangler.toml              # Cloudflare Workers設定
│   └─ package.json               # Node.js依存関係
│
├─ .github/
│   └─ workflows/                 # CI/CD（Phase 1で作成予定）
│       ├─ deploy-frontend.yml    # フロントエンドデプロイ
│       └─ deploy-api.yml         # バックエンドデプロイ
│
├─ src/                           # Python実装（保留）
│   ├─ __init__.py
│   ├─ converter.py               # ファイル変換（Phase 1後半で使用予定）
│   └─ simplifier.py              # 参考実装
│
├─ tests/                         # テスト（保留）
│   ├─ test_converter.py
│   └─ test_simplifier_integration.py
│
├─ docs/                          # ドキュメント
│   ├─ PROJECT_REQUIREMENTS.md    # 要件定義（✅ 更新済み）
│   ├─ TASKS.md                   # タスク一覧（✅ 更新済み）
│   ├─ IMPLEMENTATION_SUMMARY.md  # 実装サマリー（✅ 更新済み）
│   ├─ PROGRESS_TRACKING.md       # 進捗管理（✅ 更新済み）
│   ├─ REPOSITORY_STRUCTURE.md    # このファイル
│   ├─ AGENT_ORCHESTRATION.md     # エージェント体制
│   ├─ TASK_MANAGEMENT.md         # タスク管理システム
│   ├─ COST_OPTIMIZATION.md       # コスト最適化
│   └─ SUB_AGENTS.md              # サブエージェント定義
│
├─ .env.example                   # 環境変数サンプル（✅ 作成済み）
├─ .gitignore                     # Git除外設定
├─ requirements.txt               # Python依存関係（保留）
├─ package.json                   # Node.js依存関係（Phase 1で作成予定）
├─ README.md                      # プロジェクト説明（✅ 更新済み）
└─ LICENSE                        # MITライセンス
```

---

## 📂 ディレクトリ別の詳細

### `/web/` - フロントエンド

**状態**: Phase 1 Week 1で作成予定

**役割**: 
- ユーザーが使うWebページ
- URL入力、結果表示
- 静的HTML + CSS + JavaScript

**デプロイ先**: GitHub Pages

**担当エージェント**: Frontend Sub-Agent

---

### `/api/` - バックエンド

**状態**: Phase 1 Week 2で作成予定

**役割**:
- Webスクレイピング
- LLM API呼び出し
- キャッシュ管理

**デプロイ先**: Cloudflare Workers

**担当エージェント**: Backend Sub-Agent, Simplifier Sub-Agent

---

### `/.github/workflows/` - CI/CD

**状態**: Phase 1 Week 2で作成予定

**役割**:
- 自動デプロイ
- GitHub Secretsから環境変数取得

**使用サービス**: GitHub Actions

**担当エージェント**: Orchestrator

---

### `/src/` - Python実装（保留）

**状態**: 保留（削除しない）

**役割**:
- ファイルアップロード機能（Phase 1後半で使用予定）
- markitdown統合
- 参考実装として保持

**理由**: 
- URL変換（JavaScript）が最優先
- ファイル処理はPythonが適している
- 将来的に使用する可能性あり

---

### `/tests/` - テスト（保留）

**状態**: 保留

**役割**:
- Python実装のテスト
- 参考として保持

**理由**: 
- 現在の優先度は低い
- テストケースは参考になる

---

### `/docs/` - ドキュメント

**状態**: 主要ドキュメント更新済み ✅

**役割**:
- プロジェクト全体の設計・管理
- 作業再開時のガイド

**主要ファイル**:
1. `PROJECT_REQUIREMENTS.md` - 要件定義（✅）
2. `TASKS.md` - タスク一覧（✅）
3. `IMPLEMENTATION_SUMMARY.md` - 実装状況（✅）
4. `PROGRESS_TRACKING.md` - 進捗管理（✅）

---

## 🔄 ファイルの状態

### ✅ 更新済み（2025-11-01）

- `docs/PROJECT_REQUIREMENTS.md`
- `docs/TASKS.md`
- `docs/IMPLEMENTATION_SUMMARY.md`
- `docs/PROGRESS_TRACKING.md`
- `docs/REPOSITORY_STRUCTURE.md`（このファイル）
- `.env.example`
- `README.md`

### 🟡 保留（既存）

- `src/converter.py`
- `src/simplifier.py`
- `tests/test_converter.py`
- `tests/test_simplifier_integration.py`
- `requirements.txt`

### ⏳ 未作成（Phase 1で作成予定）

- `web/` ディレクトリ全体
- `api/` ディレクトリ全体
- `.github/workflows/` ディレクトリ全体
- `package.json`

---

## 🎯 作業再開時のガイド

### どのファイルを読むべきか

**全体把握**:
1. `README.md` - プロジェクト概要
2. `docs/PROJECT_REQUIREMENTS.md` - 詳細要件
3. `docs/IMPLEMENTATION_SUMMARY.md` - 技術仕様

**タスク確認**:
1. `docs/TASKS.md` - 次に何をするか
2. `docs/PROGRESS_TRACKING.md` - 現在の進捗

**作業開始**:
1. 該当するタスクのファイルを読む
2. エージェントに指示を出す

### 作業開始コマンド

```
# Week 1開始
「TASK-UI-001を開始してください」

# Week 2開始
「TASK-BACKEND-001を開始してください」

# 統合フェーズ開始
「TASK-INT-001を開始してください」
```

---

## 🗂️ ファイルの命名規則

### ドキュメント
- 大文字スネークケース: `PROJECT_REQUIREMENTS.md`
- 内容が明確に分かる名前

### コード
- kebab-case（HTML/CSS）: `index.html`, `style.css`
- camelCase（JavaScript）: `app.js`, `mockData.js`
- snake_case（Python）: `converter.py`, `test_converter.py`

---

## 📝 .gitignore の重要性

### 絶対にコミットしてはいけないファイル

```gitignore
# 環境変数（APIキー含む）
.env

# Node.js
node_modules/
package-lock.json

# Python
__pycache__/
*.pyc
.pytest_cache/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

**重要**: `.env` ファイルは絶対にコミットしない！

---

## 🔐 セキュリティ

### APIキーの管理

**開発時**:
- `.env` ファイル（ローカルのみ、Git除外）

**本番環境**:
- GitHub Secrets（リポジトリ設定）
- Cloudflare Workers環境変数

**絶対にやってはいけないこと**:
- ❌ コードにAPIキーを直接書く
- ❌ `.env` をコミットする
- ❌ ブラウザにAPIキーを露出する

---

## 📊 リポジトリの健全性チェック

### 作業前の確認

- [ ] `.env` が `.gitignore` に含まれている
- [ ] ドキュメントが最新
- [ ] ブランチが正しい
- [ ] 依存関係がインストール済み

### 作業後の確認

- [ ] コミットメッセージが明確
- [ ] APIキーが含まれていない
- [ ] ドキュメントを更新した
- [ ] テストが通る（該当する場合）

---

## 🎬 次のアクション

**現在地**: Phase 1a準備完了

**次のステップ**: TASK-UI-001（基本レイアウト作成）

**推奨コマンド**:
```
「TASK-UI-001を開始してください」
```

---

**最終更新**: 2025年11月1日
**作成者**: Orchestrator Agent
