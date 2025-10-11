# フィーチャーブランチワークフローガイド

## 🔄 新しい開発フロー

### 基本方針

- **メインブランチへの直接プッシュ禁止**

- **すべての変更はフィーチャーブランチ経由**

- **プルリクエストによるレビュー必須**

- **マージはプロジェクトオーナーのみ実行**

## 📋 ワークフロー手順

### 1. フィーチャーブランチの作成

```bash
# 最新のmainブランチに切り替え
git checkout main
git pull origin main

# 新しいフィーチャーブランチを作成
git checkout -b feature/機能名-YYYY-MM-DD
# 例: git checkout -b feature/gemini-api-integration-2025-10-11
```

### 2. 開発作業の実行

```bash
# 変更を加える
# ファイルの編集、新規作成など

# 変更をステージング
git add .

# コミット（日本語OK）
git commit -m "✨ Add Gemini API integration

- Implement basic text simplification functionality
- Add API client with error handling
- Update requirements.txt with new dependencies

Related to #1"
```

### 3. フィーチャーブランチのプッシュ

```bash
# フィーチャーブランチをリモートにプッシュ
git push origin feature/機能名-YYYY-MM-DD
```

### 4. プルリクエストの作成

1. **GitHubのWebインターフェース**にアクセス

2. **"Compare & pull request"** ボタンをクリック

3. **プルリクエストの詳細を記入**:

   - タイトル: 機能の概要

   - 説明: 変更内容、テスト結果、関連Issue

   - レビュワー: @kazu-4728 を指定

   - ラベル: `enhancement`, `bugfix`, `documentation` など

### 5. レビューとマージ

- **プロジェクトオーナーがレビュー**

- **承認後にマージ実行**

- **フィーチャーブランチの削除**

## 🏷️ ブランチ命名規則

### フィーチャーブランチ

``` text
feature/機能名-YYYY-MM-DD
例:
- feature/gemini-api-integration-2025-10-11
- feature/web-interface-2025-10-12
- feature/error-handling-2025-10-13
```

### バグ修正ブランチ

``` text
bugfix/問題の概要-YYYY-MM-DD
例:
- bugfix/api-timeout-error-2025-10-11
- bugfix/ui-responsive-issue-2025-10-12
```

### ドキュメント更新ブランチ

``` text
docs/更新内容-YYYY-MM-DD
例:
- docs/update-readme-2025-10-11
- docs/add-api-documentation-2025-10-12
```

### リファクタリングブランチ

``` text
refactor/対象機能-YYYY-MM-DD
例:
- refactor/simplifier-module-2025-10-11
- refactor/error-handling-2025-10-12
```

## 📝 コミットメッセージ規則

### 基本形式

``` text
📝 タイプ: 簡潔な説明

詳細な説明（必要に応じて）

関連Issue: #1, #2
```

### 絵文字の意味

- **✨**: 新機能追加

- **🐛**: バグ修正

- **📝**: ドキュメント更新

- **🔧**: リファクタリング

- **⚡**: パフォーマンス改善

- **🔒**: セキュリティ修正

- **♻️**: コード整理

- **📦**: 依存関係更新

- **🎨**: UI/UX改善

- **🧪**: テスト追加・修正

### 例

```bash
git commit -m "✨ Add Gemini API integration

- Implement text simplification with 3 levels (low/medium/high)
- Add error handling for API rate limits
- Include retry mechanism for failed requests
- Update requirements.txt with google-generativeai dependency

Related to #1"
```

## 🔍 プルリクエストテンプレート

### タイトル

``` text
[フィーチャー] 機能の概要
例: [フィーチャー] Gemini API統合によるテキスト簡易化機能
```

### 説明

```markdown
## 📋 概要
このPRで何を実装したかを簡潔に説明

## 🔧 変更内容
- [ ] 変更点1
- [ ] 変更点2
- [ ] 変更点3

## 🧪 テスト
- [ ] 単体テスト追加
- [ ] 統合テスト実行
- [ ] 手動テスト完了

## 📸 スクリーンショット（UI変更の場合）
<!-- 変更前後のスクリーンショット -->

## 🔗 関連Issue
Closes #1
Related to #2

## ✅ チェックリスト
- [ ] コードレビュー完了
- [ ] テスト実行完了
- [ ] ドキュメント更新完了
- [ ] 破壊的変更なし
```

## 🚨 緊急時の例外

### ホットフィックス

```bash
# 緊急バグ修正の場合のみ、直接mainにプッシュ可能
git checkout main
git pull origin main
# 修正を加える
git add .
git commit -m "🚨 HOTFIX: Critical security vulnerability fix"
git push origin main
```

### 注意事項

- **緊急時のみ使用**

- **修正後すぐにフィーチャーブランチで詳細説明PR作成**

- **セキュリティ関連は特に注意**

## 📊 進捗管理

### 作業記録の更新

プルリクエスト作成時は `docs/WORK_LOG.md` も更新：

```markdown
#### 🔄 進行中タスク
- [ ] Gemini API統合の実装 (PR #1 作成済み)
- [ ] Webインターフェースの設計

#### ⏳ レビュー待ち
- [ ] PR #1: Gemini API統合機能
```

### マイルストーンの更新

機能完成時はマイルストーンも更新：

```markdown
### Phase 1 マイルストーン
- [x] **M1.1**: 基本機能実装完了 (完了: 10月15日)
- [ ] **M1.2**: Webインターフェース完成 (予定: 10月20日)
```

## 🎯 メリット

### 品質向上

- **コードレビューによる品質確保**

- **バグの早期発見**

- **設計の改善**

### 協力開発

- **変更履歴の明確化**

- **責任の明確化**

- **知識の共有**

### 安全性

- **メインブランチの安定性**

- **ロールバックの容易さ**

- **実験的機能の分離**

---

**作成日**: 2025年10月11日
**バージョン**: 1.0
**作成者**: kazu-4728
**適用開始**: 2025年10月11日

