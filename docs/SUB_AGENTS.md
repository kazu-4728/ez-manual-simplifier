# サブエージェント定義

## 目的

コンテキスト消費を抑制するため、専門的なサブエージェントを定義し、各エージェントが最小限のコンテキストで作業できるようにする。

## サブエージェント一覧

### 1. Converter Sub-Agent

**コンテキスト**: `src/converter.py` のみ

**責任範囲**:
- ドキュメント変換機能の実装・修正
- markitdown統合の管理
- ファイル形式対応の拡張

**参照ドキュメント**:
- `.github/instructions/src.instructions.md`
- `docs/COST_OPTIMIZATION.md` (API使用時のみ)

**制約**:
- `DocumentConverter` クラスのインターフェースを維持
- エラーハンドリングパターンを統一

### 2. Simplifier Sub-Agent

**コンテキスト**: `src/simplifier.py` のみ

**責任範囲**:
- テキスト簡易化ロジックの実装
- Gemini API統合
- レベル別簡易化の実装

**参照ドキュメント**:
- `docs/COST_OPTIMIZATION.md` (必須)
- `docs/API_SPEC.md` (将来)

**制約**:
- コスト最適化ガイドライン遵守
- コンテキストオーバー防止（チャンク分割）

### 3. Researcher Sub-Agent

**コンテキスト**: `src/researcher.py` (新規作成)

**責任範囲**:
- ユーザーリクエストに基づくリサーチ
- マニュアル作成支援
- MCP/API連携の管理

**参照ドキュメント**:
- `docs/COST_OPTIMIZATION.md` (必須)
- `docs/AGENT_ORCHESTRATION.md`

**制約**:
- コストを最小限に抑制
- リサーチ結果は必ずキャッシュ
- 不要なAPI呼び出しを避ける

### 4. API Sub-Agent

**コンテキスト**: `src/api/` ディレクトリ

**責任範囲**:
- FastAPI/Flask実装
- エンドポイント定義
- リクエスト/レスポンス処理

**参照ドキュメント**:
- `docs/API_SPEC.md` (必須)
- `.github/instructions/src.instructions.md`

**制約**:
- RESTful API設計原則に従う
- エラーハンドリングを統一

### 5. Frontend Sub-Agent

**コンテキスト**: `web/` ディレクトリ

**責任範囲**:
- HTML/CSS/JavaScript実装
- UI/UXデザイン
- レスポンシブ対応

**参照ドキュメント**:
- `docs/API_SPEC.md` (API仕様)
- `.github/instructions/frontend.instructions.md` (将来)

**制約**:
- バックエンドAPI仕様に準拠
- モダンブラウザ対応（IE非対応）

### 6. Test Sub-Agent

**コンテキスト**: `tests/` ディレクトリ + 該当するソースファイル

**責任範囲**:
- テストケース作成
- テスト実行と検証
- カバレッジ管理

**参照ドキュメント**:
- `.github/instructions/tests.instructions.md`
- 該当するソースファイルのdocstring

**制約**:
- カバレッジ80%以上を維持
- テストは独立して実行可能に

### 7. Docs Sub-Agent

**コンテキスト**: `docs/` ディレクトリ + 関連するソースファイル

**責任範囲**:
- ドキュメント作成・更新
- Markdown整形
- ドキュメント構造管理

**参照ドキュメント**:
- `.github/instructions/docs.instructions.md`
- `.markdownlint.json`

**制約**:
- Markdownリンターに準拠
- 日本語と英語の両方で記載（必要に応じて）

## サブエージェント起動プロトコル

### 起動前チェックリスト

1. **コンテキスト確認**
   - [ ] 必要なファイルのみを読み込む
   - [ ] 不要なドキュメントを読み込まない
   - [ ] 参照ドキュメントを明確化

2. **制約確認**
   - [ ] コスト制約を理解しているか
   - [ ] コンテキスト制限を考慮しているか
   - [ ] インターフェースを維持するか

3. **作業範囲確認**
   - [ ] 担当範囲を超えていないか
   - [ ] 他のエージェントの領域に侵入していないか

### 起動メッセージフォーマット

```markdown
## サブエージェント起動

- **エージェント名**: [サブエージェント名]
- **タスクID**: [TASK-ID]
- **作業範囲**: [ファイル/ディレクトリ]
- **参照ドキュメント**: [ドキュメントリスト]
- **制約**: [制約リスト]

作業を開始します。
```

## コンテキスト消費管理

### ファイル読み込みルール

**原則**: 必要なファイルのみを読み込む

**例**:
- Converter Sub-Agent: `src/converter.py` のみ
- Simplifier Sub-Agent: `src/simplifier.py` + `docs/COST_OPTIMIZATION.md`
- Test Sub-Agent: テストファイル + 対象ソースファイル

### ドキュメント参照ルール

**最小限の参照**:
- 作業に直接必要なドキュメントのみ
- 全体を読み込まず、必要な部分のみ

**参照順序**:
1. 該当する `.github/instructions/` ファイル
2. 該当する `docs/` ファイル
3. 必要に応じて `PROJECT_REQUIREMENTS.md`

## エージェント間連携

### 連携が必要な場合

**例**: Simplifier Sub-Agent が Converter Sub-Agent の機能を使う場合

```python
# Simplifier Sub-Agent の実装
from src.converter import DocumentConverter

def simplify_file(filepath: str, level: str = "medium") -> str:
    # Converter Sub-Agent の機能を利用
    converter = DocumentConverter()
    markdown = converter.convert_to_markdown(filepath)
    # 簡易化処理
    return simplify_text(markdown, level)
```

**注意**: Converter Sub-Agent の内部実装には依存しない

### インターフェースの維持

- 公開APIのみを使用
- プライベートメソッドにはアクセスしない
- インターフェース変更時は影響範囲を確認

## チェックリスト

サブエージェントが作業を開始する前に確認:

- [ ] コンテキストが最小限か？
- [ ] 必要なドキュメントのみを参照しているか？
- [ ] 制約を理解しているか？
- [ ] 作業範囲を超えていないか？
- [ ] インターフェースを維持しているか？

---

**最終更新**: 2025-01-11
**バージョン**: 1.0