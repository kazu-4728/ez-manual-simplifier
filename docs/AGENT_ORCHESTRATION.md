# エージェントオーケストラ体制（完全版）

## 更新日: 2025年11月1日

---

## 🎯 目的

複数のAIエージェントが協調して開発を進めるための統一されたガバナンス体制。

**重要原則**:
1. **統一入り口**: すべてのエージェントは`docs/PROJECT_REQUIREMENTS.md`を参照
2. **役割明確化**: 各エージェントの責任範囲を明確に
3. **情報の一元化**: 進捗、タスク、要件を分散させない
4. **方針転換対応**: ドキュメント更新→全エージェント通知の流れ

---

## 📌 唯一の真実の情報源（Single Source of Truth）

### `docs/PROJECT_REQUIREMENTS.md`

**すべてのエージェントはこのファイルを参照**:
- Orchestrator
- Copilot Agent
- GPT Agent  
- Gemini CLI
- Codex
- すべてのSub-Agents

**参照タイミング**:
- 作業開始時
- 判断に迷った時
- 方針転換時
- Phase移行時

---

## 🤖 エージェント階層構造

```
┌──────────────────────────────────────────────┐
│  Orchestrator（マスターエージェント）         │
│  - 全体統括                                   │
│  - タスク分解・割り振り                       │
│  - 進捗管理                                   │
│  - 方針転換判断                               │
└─────────────┬────────────────────────────────┘
              │
      ┌───────┴────────┐
      │                │
┌─────▼─────┐    ┌────▼──────┐
│ 開発系     │    │ 支援系     │
│ エージェント│    │ エージェント│
└─────┬─────┘    └────┬──────┘
      │                │
      │                │
┌─────▼──────────┐  ┌─▼─────────────┐
│ Sub-Agents     │  │ Support Agents │
│ - Frontend     │  │ - Copilot      │
│ - Backend      │  │ - GPT Agent    │
│ - Simplifier   │  │ - Gemini CLI   │
│ - Test         │  │ - Codex        │
└────────────────┘  └────────────────┘
```

---

## 👥 エージェント定義

### Orchestrator（マスターエージェント）

**役割**:
- 全体統括・意思決定
- タスク分解と割り振り
- 進捗管理とリスク評価
- 方針転換の判断と実行
- ドキュメント更新管理

**参照ドキュメント**（優先順）:
1. `docs/PROJECT_REQUIREMENTS.md`（必須・最優先）
2. `docs/PROGRESS_TRACKING.md`
3. `docs/TASKS.md`
4. その他すべてのdocs

**制約**:
- 必ず最新の`PROJECT_REQUIREMENTS.md`を確認
- Phase定義を遵守
- 独断で方針変更しない（プロダクトオーナーの承認必須）
- サブエージェントへの明確な指示

**使用場面**:
- プロジェクト全体の判断
- Phase移行時
- 複雑なタスクの分解
- ブロッカー解決

---

### Copilot Agent

**役割**:
- リアルタイムコード補完
- コーディング中の支援
- シンタックスチェック
- ベストプラクティス提案

**参照ドキュメント**:
1. 実装中のファイル
2. `docs/PROJECT_REQUIREMENTS.md`（技術構成セクション）
3. 関連するコードベース

**制約**:
- コンテキストは実装ファイルのみ
- 大きな設計判断はOrchestratorへエスカレーション

**使用場面**:
- コーディング中
- リファクタリング
- バグ修正

---

### GPT Agent

**役割**:
- 長文処理・要約
- 複雑なコンテキスト理解
- ドキュメント生成
- 自然言語での説明

**参照ドキュメント**:
1. `docs/`ディレクトリ全体
2. `docs/PROJECT_REQUIREMENTS.md`

**制約**:
- 実装は行わない（提案のみ）
- ドキュメント作成・更新に特化

**使用場面**:
- ドキュメント作成
- 要件整理
- ユーザー説明文作成

---

### Gemini CLI

**役割**:
- 外部情報リサーチ
- 技術調査
- 競合分析
- トレンド調査

**参照ドキュメント**:
1. `docs/PROJECT_REQUIREMENTS.md`（目的・背景セクション）
2. リサーチ対象の明確化

**制約**:
- リサーチに特化
- 実装は行わない
- 調査結果をOrchestratorに報告

**使用場面**:
- 技術選定時
- 競合調査
- ベストプラクティス調査

---

### Codex

**役割**:
- 具体的な実装
- アルゴリズム実装
- バグ修正
- テスト作成

**参照ドキュメント**:
1. `docs/TASKS.md`（具体的なタスク）
2. `docs/PROJECT_REQUIREMENTS.md`（技術仕様）
3. 実装対象ファイル

**制約**:
- タスク定義に従う
- 大きな設計変更はOrchestratorへ相談

**使用場面**:
- 実装フェーズ
- バグ修正
- テスト作成

---

### Frontend Sub-Agent

**役割**:
- UI/UX実装
- レスポンシブデザイン
- フロントエンドロジック

**参照ドキュメント**:
1. `docs/PROJECT_REQUIREMENTS.md`（Phase定義・技術構成）
2. `docs/TASKS.md`（フロントエンド関連タスク）
3. デザイン仕様（将来）

**作業範囲**:
- `web/`ディレクトリ
- HTML/CSS/JavaScript

**制約**:
- バックエンドAPIは実装しない
- デザインガイドライン遵守

**使用場面**:
- UI実装
- デザイン調整

---

### Backend Sub-Agent

**役割**:
- API実装
- サーバーサイドロジック
- データベース操作（Phase 3以降）

**参照ドキュメント**:
1. `docs/PROJECT_REQUIREMENTS.md`（Phase定義・技術構成）
2. `docs/TASKS.md`（バックエンド関連タスク）
3. API仕様（将来）

**作業範囲**:
- `api/`ディレクトリ
- Cloudflare Workers実装

**制約**:
- フロントエンドは触らない
- セキュリティ要件遵守

**使用場面**:
- API実装
- サーバーロジック

---

### Simplifier Sub-Agent

**役割**:
- LLM統合
- プロンプト設計
- 簡易化ロジック実装

**参照ドキュメント**:
1. `docs/PROJECT_REQUIREMENTS.md`（Phase定義・LLM戦略）
2. `docs/COST_OPTIMIZATION.md`
3. プロンプトテンプレート

**作業範囲**:
- `api/llm.js`
- `api/simplifier.js`
- プロンプトテンプレート

**制約**:
- コスト最適化必須
- API呼び出し最小化

**使用場面**:
- LLM統合
- プロンプト改善

---

### Test Sub-Agent

**役割**:
- テスト設計・実装
- テスト実行
- カバレッジ管理

**参照ドキュメント**:
1. `docs/TASKS.md`（テスト関連タスク）
2. 実装ファイル
3. テスト戦略

**作業範囲**:
- `tests/`ディレクトリ
- 統合テスト

**制約**:
- テストのみに特化
- カバレッジ80%以上を目標

**使用場面**:
- テスト作成
- バグ検証

---

## 🔄 エージェント連携フロー

### 基本フロー

```
1. ユーザー指示
   ↓
2. Orchestrator受信
   ↓
3. PROJECT_REQUIREMENTS.md確認
   ↓
4. 現在のPhase確認
   ↓
5. タスク分解
   ↓
6. 適切なエージェントへ割り振り
   ├─ Copilot Agent（コード支援）
   ├─ GPT Agent（ドキュメント）
   ├─ Gemini CLI（リサーチ）
   ├─ Codex（実装）
   └─ Sub-Agents（専門作業）
   ↓
7. 並行作業実行
   ↓
8. 作業完了・統合
   ↓
9. Orchestratorレビュー
   ↓
10. PROGRESS_TRACKING.md更新
   ↓
11. ユーザーへ報告
```

### Phase移行時のフロー

```
1. Phase完了判断（Orchestrator）
   ↓
2. プロダクトオーナーへ報告
   - 成果
   - 判断基準の評価
   - 次Phaseの提案
   ↓
3. プロダクトオーナー判断
   ↓ 成功
4. PROJECT_REQUIREMENTS.md更新
   - 次Phaseの詳細化
   - 技術構成の選択肢提示
   ↓
5. 全エージェントへ通知
   ↓
6. TASKS.md更新（次Phaseのタスク）
   ↓
7. 作業再開
```

### 方針転換時のフロー

```
1. トリガー
   - Phase判断で失敗
   - 重大な技術的問題
   - ユーザーフィードバック
   ↓
2. Orchestrator分析
   - 現状評価
   - 選択肢の洗い出し
   - 推奨案の提示
   ↓
3. プロダクトオーナー判断
   ↓
4. PROJECT_REQUIREMENTS.md更新
   - 新しい方針を明記
   - 影響範囲を記載
   - 代替案も残す
   ↓
5. 全エージェントへ通知
   ↓
6. TASKS.md再定義
   ↓
7. 新しい方針で作業再開
```

---

## 📋 エージェント割り振りマトリクス

| 作業タイプ | 優先エージェント | 補助エージェント | 支援エージェント |
|-----------|-----------------|-----------------|-----------------|
| 全体方針決定 | Orchestrator | GPT Agent | - |
| Phase移行判断 | Orchestrator | プロダクトオーナー | - |
| UI実装 | Frontend Sub-Agent | Copilot Agent | Codex |
| API実装 | Backend Sub-Agent | Copilot Agent | Codex |
| LLM統合 | Simplifier Sub-Agent | Gemini CLI | GPT Agent |
| テスト作成 | Test Sub-Agent | Codex | - |
| ドキュメント作成 | GPT Agent | Orchestrator | - |
| リサーチ | Gemini CLI | GPT Agent | - |
| バグ修正 | Codex | 該当Sub-Agent | Copilot Agent |
| リファクタリング | 該当Sub-Agent | Copilot Agent | Codex |

---

## 🚨 エスカレーションルール

### エスカレーション条件

1. **ブロッカー発生**: タスクが進められない
2. **方針の不明確**: Phase定義と矛盾
3. **技術的困難**: 想定以上の難易度
4. **コスト超過リスク**: 予算を超えそう
5. **スコープ外要求**: Phase定義にない機能

### エスカレーションフロー

```
サブエージェント
  ↓（即座にエスカレーション）
Orchestrator
  ↓（分析・判断）
├─ 自己解決可能 → 指示変更・サポート
├─ 方針変更必要 → プロダクトオーナーへ
└─ 技術的問題 → 他エージェントに再割り振り
```

---

## 📝 ドキュメント更新フロー

### Orchestratorが更新するドキュメント

1. **`PROJECT_REQUIREMENTS.md`**
   - Phase移行時
   - 方針転換時
   - 技術構成変更時

2. **`TASKS.md`**
   - タスク完了時
   - 新規タスク追加時
   - タスク再定義時

3. **`PROGRESS_TRACKING.md`**
   - タスク完了時
   - マイルストーン達成時
   - 週次更新

### Sub-Agentsが更新するドキュメント

1. **実装ファイル**
   - 担当範囲のコード
   - コメント・docstring

2. **README.md**（該当セクションのみ）
   - 使用方法の更新

### GPT Agentが更新するドキュメント

1. **技術ドキュメント**
   - API仕様
   - アーキテクチャ図
   - ユーザーガイド

---

## 🔐 セキュリティ・コンテキスト管理

### コンテキスト消費抑制

**原則**: 必要最小限のファイルのみ読み込む

| エージェント | 読み込み範囲 |
|------------|------------|
| Orchestrator | すべてのdocs、必要に応じて実装ファイル |
| Copilot | 実装中のファイルのみ |
| GPT Agent | docs全体、実装ファイルは参照のみ |
| Gemini CLI | PROJECT_REQUIREMENTS.mdの目的セクション |
| Codex | タスク関連ファイルのみ |
| Sub-Agents | 担当ディレクトリのみ |

### セキュリティ要件

**すべてのエージェント共通**:
- ❌ `.env`ファイルを読み込まない（`.env.example`のみOK）
- ❌ APIキーをコードに書かない
- ✅ GitHub Secretsを使用
- ✅ セキュリティ懸念はOrchestratorにエスカレーション

---

## 🎯 作業開始チェックリスト

### Orchestrator

- [ ] `PROJECT_REQUIREMENTS.md`を確認（最新版）
- [ ] 現在のPhaseを確認
- [ ] `PROGRESS_TRACKING.md`で進捗確認
- [ ] タスクの依存関係を確認
- [ ] 適切なエージェントを選定

### Sub-Agents

- [ ] Orchestratorからの指示を確認
- [ ] `PROJECT_REQUIREMENTS.md`の該当Phase確認
- [ ] `TASKS.md`の該当タスク確認
- [ ] 制約条件を確認
- [ ] 作業範囲を確認（他の領域に侵入しない）

---

## 🎬 実例: Phase 1 Week 1の連携

### シナリオ: TASK-UI-001開始

```
1. ユーザー: 「TASK-UI-001を開始してください」
   ↓
2. Orchestrator:
   - PROJECT_REQUIREMENTS.md確認
   - Phase 1であることを確認
   - TASK-UI-001の詳細を確認
   - Frontend Sub-Agentへ割り振り
   ↓
3. Frontend Sub-Agent:
   - TASK-UI-001の詳細確認
   - web/ディレクトリ作成
   - index.html作成開始
   - Copilot Agentが補完支援
   ↓
4. 並行作業:
   - Frontend Sub-Agent: HTML実装
   - Copilot Agent: コード補完
   - GPT Agent: コメント・docstring生成
   ↓
5. 完成:
   - Frontend Sub-Agentが完了報告
   - OrchestratorがPROGRESS_TRACKING.md更新
   - ユーザーへ報告
```

---

## 📚 参照ドキュメント

- [要件定義](./PROJECT_REQUIREMENTS.md) - 唯一の真実の情報源
- [タスク一覧](./TASKS.md) - 具体的なタスク
- [進捗管理](./PROGRESS_TRACKING.md) - 進捗の一元化
- [リポジトリ構成](./REPOSITORY_STRUCTURE.md) - ファイル配置

---

**最終更新**: 2025年11月1日
**バージョン**: 2.0（完全版・全エージェント定義）
**作成者**: Orchestrator Agent
