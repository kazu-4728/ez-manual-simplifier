# タスク管理システム

## 目的

プロジェクトのタスクを体系的に管理し、エージェント間で作業を効率的に分担するためのシステム。

## タスク分類

### タスクタイプ

1. **feature**: 新機能実装
2. **bugfix**: バグ修正
3. **refactor**: リファクタリング
4. **test**: テスト追加・改善
5. **docs**: ドキュメント更新
6. **infra**: インフラ・CI/CD改善
7. **research**: リサーチ・調査

### 優先度

- **critical**: ブロッカー、緊急対応が必要
- **high**: 重要な機能、早急に対応
- **medium**: 通常の優先度
- **low**: 時間があるときに対応

### ステータス

- **pending**: 未着手
- **in_progress**: 作業中
- **review**: レビュー待ち
- **testing**: テスト中
- **blocked**: ブロック中
- **completed**: 完了
- **cancelled**: キャンセル

## タスク構造

```yaml
task_id: TASK-001
title: Gemini API統合実装
type: feature
priority: high
status: pending
assigned_to: simplifier_sub_agent
created_at: 2025-01-11
updated_at: 2025-01-11

description: |
  simplifier.py の simplify_text() 関数に
  Gemini API を統合し、実際の簡易化処理を実装する

requirements:
  - Gemini API キー設定
  - プロンプトテンプレート作成
  - レベル別簡易化ロジック実装
  - エラーハンドリング追加
  - コスト最適化（チャンク分割）

constraints:
  - cost_optimization: true
  - context_limit: 8000
  - api_quota: 1000/day

related_files:
  - src/simplifier.py
  - tests/test_simplifier_integration.py
  - docs/COST_OPTIMIZATION.md

dependencies: []
blockers: []

subtasks:
  - TASK-001-1: APIキー設定と環境変数管理
  - TASK-001-2: プロンプトテンプレート作成
  - TASK-001-3: API呼び出し実装
  - TASK-001-4: エラーハンドリング
  - TASK-001-5: テスト作成

progress: 0
estimated_hours: 8
actual_hours: 0
```

## タスク登録フォーマット

### GitHub Issue連携

Issue作成時に自動的にタスクとして登録される形式:

```markdown
## タスク情報

- **タイプ**: [feature/bugfix/refactor/test/docs/infra/research]
- **優先度**: [critical/high/medium/low]
- **担当エージェント**: [エージェント名]
- **関連ファイル**: [ファイルパス]
- **依存タスク**: [TASK-ID]

## 説明

[タスクの詳細説明]

## 制約

- コスト: [制約内容]
- コンテキスト: [制約内容]
- その他: [制約内容]

## 受け入れ基準

- [ ] [基準1]
- [ ] [基準2]
- [ ] [基準3]
```

## タスク分解ルール

### 分解の目安

- **8時間以上**: 必ずサブタスクに分解
- **複数ファイルにまたがる**: ファイル単位で分解
- **複数エージェントが必要**: エージェント単位で分解

### 分解例

```
TASK-001: Gemini API統合実装 (8時間)
  ├─ TASK-001-1: APIキー設定 (1時間)
  ├─ TASK-001-2: プロンプトテンプレート (2時間)
  ├─ TASK-001-3: API呼び出し実装 (3時間)
  ├─ TASK-001-4: エラーハンドリング (1時間)
  └─ TASK-001-5: テスト作成 (1時間)
```

## タスク割り振り

### 割り振り基準

1. **専門性**: エージェントの専門領域に合致するか
2. **現在の負荷**: 他のタスクとの兼ね合い
3. **依存関係**: 前のタスクが完了しているか
4. **優先度**: 優先度の高いタスクから割り振る

### 割り振りプロセス

```
1. Orchestrator がタスクを分析
   ↓
2. 必要なスキルを特定
   ↓
3. 適切なエージェントを選定
   ↓
4. 負荷状況を確認
   ↓
5. タスクを割り振り
   ↓
6. タスク管理システムに記録
```

## 進捗追跡

### 進捗更新ルール

- **作業開始時**: status → `in_progress`
- **ブロッカー発生時**: status → `blocked`, blockers更新
- **レビュー依頼時**: status → `review`
- **テスト実行時**: status → `testing`
- **完了時**: status → `completed`, progress → 100

### 進捗報告フォーマット

```markdown
## 進捗報告

- **タスクID**: TASK-001
- **ステータス**: in_progress
- **進捗率**: 50%
- **完了サブタスク**: 2/5
- **ブロッカー**: なし
- **次ステップ**: API呼び出し実装開始

## 変更内容

- [完了] APIキー設定完了
- [完了] プロンプトテンプレート作成完了
- [作業中] API呼び出し実装中
```

## ブロッカー管理

### ブロッカー登録

```yaml
blockers:
  - id: BLOCK-001
    description: Gemini API キーが未設定
    type: dependency
    resolution: APIキーを環境変数に設定
    assigned_to: project_owner
    created_at: 2025-01-11
```

### ブロッカー解決フロー

```
1. ブロッカー発生を報告
   ↓
2. Orchestrator が分析
   ↓
3. 解決方法を決定
   ↓
4. 必要に応じてエスカレーション
   ↓
5. 解決後、タスクを再開
```

## タスク完了チェックリスト

- [ ] 実装が完了している
- [ ] テストが作成されている
- [ ] テストがパスしている
- [ ] ドキュメントが更新されている
- [ ] コードレビューが完了している
- [ ] 受け入れ基準を満たしている
- [ ] コスト制約を遵守している
- [ ] コンテキスト制限を遵守している

## タスク一覧管理

### 現在のタスク一覧

タスク一覧は `docs/TASKS.md` で管理（別ファイル）

### タスク検索

- **ステータスで検索**: `status:in_progress`
- **担当で検索**: `assigned_to:simplifier_sub_agent`
- **優先度で検索**: `priority:high`
- **タイプで検索**: `type:feature`

---

**最終更新**: 2025-01-11
**バージョン**: 1.0