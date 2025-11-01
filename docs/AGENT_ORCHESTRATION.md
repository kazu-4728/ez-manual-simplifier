# エージェントオーケストラ体制

## 目的

複数のAIエージェントが協調して開発を進めるためのガバナンス体制。各エージェントが勝手な行動を取らないよう、明確な入り口ルートと作業割り振りを定義する。

## エージェント階層構造

```
┌─────────────────────────────────────────┐
│  Orchestrator (マスターエージェント)     │
│  - タスク分解・割り振り                  │
│  - 進捗管理                             │
│  - コンテキスト管理                      │
└────────────┬────────────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
┌───▼────┐      ┌────▼─────┐
│Frontend│      │Backend   │
│Agent   │      │Agent     │
└───┬────┘      └────┬─────┘
    │                │
    └────────┬───────┘
             │
    ┌────────▼────────┐
    │ Sub-Agents      │
    │ - Converter     │
    │ - Simplifier    │
    │ - Researcher    │
    │ - Test Agent    │
    └─────────────────┘
```

## 入り口ルート（Entry Points）

### 1. 新規機能追加リクエスト

**入り口**: GitHub Issue / Cursor Chat

**処理フロー**:
```
1. Orchestrator が Issue を分析
   ↓
2. タスク分解と優先度決定
   ↓
3. 適切なエージェントに割り振り
   ↓
4. サブエージェントが実装
   ↓
5. Test Agent が検証
   ↓
6. Orchestrator が統合・レビュー
```

**チェックポイント**:
- [ ] 要件定義書との整合性確認
- [ ] 既存コードとの競合チェック
- [ ] テストカバレッジ確認
- [ ] コスト影響評価

### 2. バグ修正リクエスト

**入り口**: GitHub Issue (bug_report.md)

**処理フロー**:
```
1. Test Agent が再現テスト作成
   ↓
2. Orchestrator が原因分析を割り振り
   ↓
3. 該当モジュールのサブエージェントが修正
   ↓
4. Test Agent が回帰テスト実行
   ↓
5. Orchestrator がマージ可否判定
```

### 3. ドキュメント更新リクエスト

**入り口**: GitHub Issue / 実装完了時の自動トリガー

**処理フロー**:
```
1. Docs Agent が対象ファイル特定
   ↓
2. 変更内容を反映
   ↓
3. Markdown リンターで検証
   ↓
4. Orchestrator が承認
```

## エージェント定義

### Orchestrator (マスターエージェント)

**役割**:
- タスクの分解と優先度付け
- エージェントへの作業割り振り
- 進捗管理とリスク評価
- コンテキスト消費の監視
- 最終承認とマージ判断

**制約**:
- 必ず `docs/AGENT_ORCHESTRATION.md` を参照
- 勝手に実装を開始しない（必ずサブエージェントに割り振る）
- 作業前に必ず `docs/TASK_MANAGEMENT.md` を更新

**参照ドキュメント**:
- `docs/PROJECT_REQUIREMENTS.md`
- `docs/TASK_MANAGEMENT.md`
- `docs/PROGRESS_TRACKING.md`

### Frontend Agent

**専門領域**:
- HTML/CSS/JavaScript 実装
- UI/UX デザイン
- レスポンシブ対応
- ブラウザ互換性

**作業範囲**:
- `web/` ディレクトリ内のファイル
- フロントエンド関連のテスト

**制約**:
- バックエンドAPI仕様は `docs/API_SPEC.md` を参照
- スタイルガイドは `.github/instructions/frontend.instructions.md` を参照

### Backend Agent

**専門領域**:
- Python (Flask/FastAPI) 実装
- API設計
- データベース設計
- セキュリティ実装

**作業範囲**:
- `src/api/` ディレクトリ
- `src/utils/` ディレクトリ
- バックエンド関連のテスト

**制約**:
- API仕様は `docs/API_SPEC.md` に従う
- コスト最適化ガイドラインは `docs/COST_OPTIMIZATION.md` を参照

### Converter Sub-Agent

**専門領域**:
- ドキュメント変換（markitdown統合）
- ファイル形式対応
- URL処理

**作業範囲**:
- `src/converter.py` の拡張・修正
- `tests/test_converter.py` の更新

**制約**:
- 既存の `DocumentConverter` クラスインターフェースを維持
- エラーハンドリングパターンを統一

### Simplifier Sub-Agent

**専門領域**:
- テキスト簡易化ロジック
- Gemini API統合
- レベル別簡易化

**作業範囲**:
- `src/simplifier.py` の実装
- `tests/test_simplifier_integration.py` の更新

**制約**:
- コスト最適化ガイドライン遵守
- コンテキストオーバー防止（チャンク分割など）

### Researcher Sub-Agent

**専門領域**:
- ユーザーリクエストに基づくリサーチ
- マニュアル作成支援
- MCP/API連携

**作業範囲**:
- `src/researcher.py` (新規作成)
- `tests/test_researcher.py` (新規作成)

**制約**:
- コストを最小限に抑制
- リサーチ結果はキャッシュする
- 不要なAPI呼び出しを避ける

### Test Agent

**専門領域**:
- テストケース作成
- テスト実行と検証
- カバレッジ管理

**作業範囲**:
- `tests/` ディレクトリ全体
- CI/CD パイプライン

**制約**:
- 新機能実装時は必ずテストを追加
- カバレッジ80%以上を維持

### Docs Agent

**専門領域**:
- ドキュメント作成・更新
- Markdown整形
- ドキュメント構造管理

**作業範囲**:
- `docs/` ディレクトリ
- `README.md`
- `.github/instructions/` ディレクトリ

**制約**:
- Markdownリンターに準拠
- 日本語と英語の両方で記載（必要に応じて）

## 作業割り振りルール

### 割り振りマトリクス

| 作業タイプ | 優先エージェント | 補助エージェント |
|-----------|-----------------|-----------------|
| フロントエンド実装 | Frontend Agent | Test Agent |
| バックエンド実装 | Backend Agent | Test Agent |
| API設計 | Backend Agent | Docs Agent |
| ドキュメント変換 | Converter Sub-Agent | Test Agent |
| テキスト簡易化 | Simplifier Sub-Agent | Test Agent |
| リサーチ機能 | Researcher Sub-Agent | Backend Agent |
| テスト作成 | Test Agent | 該当エージェント |
| ドキュメント更新 | Docs Agent | Orchestrator |

### 割り振り判断フロー

```
1. Orchestrator がタスクを分析
   ↓
2. 専門領域を特定
   ↓
3. 優先エージェントを決定
   ↓
4. 補助エージェントを割り当て
   ↓
5. タスク管理システムに記録
   ↓
6. エージェントに通知
```

## コンテキスト消費抑制

### サブエージェント活用

**原則**: 大きなタスクは必ずサブエージェントに分割

**例**:
- ❌ Orchestrator が全実装を担当
- ✅ Orchestrator がタスク分解 → 各サブエージェントが実装

### コンテキスト管理

1. **参照ドキュメントの明確化**
   - 各エージェントが参照すべきドキュメントを定義
   - 必要最小限のファイルのみ読み込む

2. **チャンク分割**
   - 大きなテキストは適切に分割
   - 簡易化処理は段落単位で実行

3. **キャッシュ活用**
   - リサーチ結果はキャッシュ
   - 変換結果は一時保存

4. **段階的処理**
   - 一度に全処理しない
   - 中間結果を保存して段階的に処理

## エージェント間通信

### 通信プロトコル

**タスク受け渡し**:
```json
{
  "task_id": "TASK-001",
  "type": "implementation",
  "assigned_to": "simplifier_sub_agent",
  "priority": "high",
  "description": "Gemini API統合実装",
  "constraints": ["cost_optimization", "context_limit"],
  "related_files": ["src/simplifier.py"],
  "dependencies": []
}
```

**進捗報告**:
```json
{
  "task_id": "TASK-001",
  "status": "in_progress",
  "progress": 50,
  "blockers": [],
  "estimated_completion": "2025-01-15"
}
```

### コミュニケーションルール

1. **明確な指示**: 曖昧な指示は避ける
2. **制約の明示**: コスト、コンテキスト制限を明記
3. **依存関係の宣言**: 他のタスクとの依存を明記
4. **定期的な報告**: 進捗は定期的に更新

## エスカレーション

### エスカレーション条件

- ブロッカーが発生した場合
- コスト上限に達しそうな場合
- コンテキストオーバーの可能性がある場合
- 要件定義との不整合が見つかった場合

### エスカレーションフロー

```
サブエージェント
  ↓
Backend/Frontend Agent
  ↓
Orchestrator
  ↓
プロジェクトオーナー (@kazu-4728)
```

## チェックリスト

エージェントが作業を開始する前に確認:

- [ ] 入り口ルートが明確か？
- [ ] 適切なエージェントに割り振られているか？
- [ ] 参照すべきドキュメントを確認したか？
- [ ] コスト制約を理解しているか？
- [ ] コンテキスト制限を考慮しているか？
- [ ] テスト計画はあるか？
- [ ] タスク管理システムに記録したか？

---

**最終更新**: 2025-01-11
**バージョン**: 1.0
**作成者**: Orchestrator Agent