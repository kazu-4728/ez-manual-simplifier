# タスク一覧（改訂版）

## 現在のフェーズ

**Phase 1a: UIファースト開発**
- 状態: 準備完了
- 期間: Week 1（3-4日）
- 目的: デザイン・UX確認、モックデータでの動作検証

---

## Phase 1a: UIファースト（Week 1）

### TASK-UI-001: 基本レイアウト作成
- **ステータス**: pending
- **優先度**: critical
- **担当**: Frontend Sub-Agent
- **推定工数**: 1日
- **依存**: なし
- **成果物**: `web/index.html`, `web/css/style.css`

**サブタスク**:
- [ ] TASK-UI-001-1: プロジェクト構造作成（web/, css/, js/ディレクトリ）
- [ ] TASK-UI-001-2: ヘッダー・フッター実装
- [ ] TASK-UI-001-3: URL入力フォーム実装
- [ ] TASK-UI-001-4: レベル選択UI実装（low/medium/high）
- [ ] TASK-UI-001-5: 変換ボタン実装

**受け入れ基準**:
- [ ] レスポンシブデザイン対応
- [ ] 美しいデザイン（Linear/Notion参考）
- [ ] アクセシビリティ対応（ラベル、ARIA属性）

---

### TASK-UI-002: 結果表示UI作成
- **ステータス**: pending
- **優先度**: critical
- **担当**: Frontend Sub-Agent
- **推定工数**: 1日
- **依存**: TASK-UI-001

**サブタスク**:
- [ ] TASK-UI-002-1: ビフォー・アフター並列レイアウト
- [ ] TASK-UI-002-2: スクロール対応
- [ ] TASK-UI-002-3: 専門用語ハイライト機能
- [ ] TASK-UI-002-4: コピー/ダウンロードボタン
- [ ] TASK-UI-002-5: モバイル対応（縦並び表示）

**受け入れ基準**:
- [ ] 元の文書と簡易版が並んで見える
- [ ] 専門用語がハイライト表示される
- [ ] HTML/Markdown/テキストでダウンロード可能

---

### TASK-UI-003: モックデータ統合
- **ステータス**: pending
- **優先度**: high
- **担当**: Frontend Sub-Agent
- **推定工数**: 1日
- **依存**: TASK-UI-002

**サブタスク**:
- [ ] TASK-UI-003-1: `web/js/mock-data.js` 作成
  - GitHub docs Pull Requests サンプル
  - 簡易化済みバージョン（手動作成）
- [ ] TASK-UI-003-2: `web/js/app.js` 作成
  - ボタンクリックイベント
  - モックデータ表示ロジック
- [ ] TASK-UI-003-3: ローディング表示実装
- [ ] TASK-UI-003-4: エラーメッセージ表示実装

**受け入れ基準**:
- [ ] ボタンクリックで結果が表示される
- [ ] ローディング中は適切なUIが表示される
- [ ] エラー時は分かりやすいメッセージが表示される

---

### TASK-UI-004: UI/UX改善
- **ステータス**: pending
- **優先度**: medium
- **担当**: Frontend Sub-Agent
- **推定工数**: 1日
- **依存**: TASK-UI-003

**サブタスク**:
- [ ] TASK-UI-004-1: アニメーション追加（フェードイン/アウト）
- [ ] TASK-UI-004-2: ホバーエフェクト
- [ ] TASK-UI-004-3: スムーズスクロール
- [ ] TASK-UI-004-4: ツールチップ（専門用語説明）
- [ ] TASK-UI-004-5: デザイン最終調整

**受け入れ基準**:
- [ ] インタラクションが自然で心地よい
- [ ] ユーザーフレンドリー
- [ ] プロダクトオーナー（kazu-4728）が満足

---

## Phase 1b: バックエンド構築（Week 2）

### TASK-BACKEND-001: Cloudflare Workersセットアップ
- **ステータス**: pending
- **優先度**: critical
- **担当**: Backend Sub-Agent
- **推定工数**: 1日
- **依存**: なし

**サブタスク**:
- [ ] TASK-BACKEND-001-1: Cloudflare無料アカウント作成
- [ ] TASK-BACKEND-001-2: `api/` ディレクトリ作成
- [ ] TASK-BACKEND-001-3: `wrangler.toml` 設定
- [ ] TASK-BACKEND-001-4: ローカル開発環境構築
- [ ] TASK-BACKEND-001-5: Hello World デプロイテスト

**受け入れ基準**:
- [ ] ローカルで動作確認できる
- [ ] Cloudflareにデプロイできる
- [ ] エンドポイントにアクセスできる

---

### TASK-BACKEND-002: URL取得機能実装
- **ステータス**: pending
- **優先度**: critical
- **担当**: Backend Sub-Agent
- **推定工数**: 2日
- **依存**: TASK-BACKEND-001

**サブタスク**:
- [ ] TASK-BACKEND-002-1: `api/scraper.js` 作成
- [ ] TASK-BACKEND-002-2: Webスクレイピング実装
  - Cheerio使用
  - GitHub docs対応
- [ ] TASK-BACKEND-002-3: CORS対応
- [ ] TASK-BACKEND-002-4: エラーハンドリング
  - 404エラー
  - タイムアウト
  - 不正なURL
- [ ] TASK-BACKEND-002-5: テスト作成

**受け入れ基準**:
- [ ] GitHub docsのURLからコンテンツ取得できる
- [ ] エラーが適切に処理される
- [ ] robots.txt を遵守している

---

### TASK-BACKEND-003: LLM統合（Gemini API）
- **ステータス**: pending
- **優先度**: critical
- **担当**: Simplifier Sub-Agent
- **推定工数**: 2日
- **依存**: TASK-BACKEND-001

**サブタスク**:
- [ ] TASK-BACKEND-003-1: `api/llm.js` 作成
- [ ] TASK-BACKEND-003-2: Gemini API呼び出し実装
- [ ] TASK-BACKEND-003-3: プロンプトテンプレート作成
  - low: 小学生向け
  - medium: 一般向け
  - high: 専門用語残し
- [ ] TASK-BACKEND-003-4: レスポンス処理
- [ ] TASK-BACKEND-003-5: エラーハンドリング
  - API制限エラー
  - タイムアウト
- [ ] TASK-BACKEND-003-6: OpenAI APIへの切り替え機能（フォールバック）

**受け入れ基準**:
- [ ] テキストが適切に簡易化される
- [ ] 3レベルの違いが明確
- [ ] エラー時はOpenAI APIに自動切り替え（オプション）

---

### TASK-BACKEND-004: GitHub Secrets設定
- **ステータス**: pending
- **優先度**: critical
- **担当**: Orchestrator
- **推定工数**: 0.5日
- **依存**: なし
- **プロダクトオーナー作業**: APIキー登録

**サブタスク**:
- [ ] TASK-BACKEND-004-1: Gemini APIキー取得（オーナー作業）
- [ ] TASK-BACKEND-004-2: Cloudflare API Token取得（オーナー作業）
- [ ] TASK-BACKEND-004-3: GitHub Secretsに登録（オーナー作業）
  - `GEMINI_API_KEY`
  - `CLOUDFLARE_API_TOKEN`
  - `OPENAI_API_KEY`（オプション）
- [ ] TASK-BACKEND-004-4: `.env.example` 作成（参考用）

**受け入れ基準**:
- [ ] GitHub Secretsに全てのキーが登録されている
- [ ] `.env.example` でサンプルが確認できる

---

### TASK-BACKEND-005: GitHub Actionsセットアップ
- **ステータス**: pending
- **優先度**: high
- **担当**: Orchestrator
- **推定工数**: 1日
- **依存**: TASK-BACKEND-004

**サブタスク**:
- [ ] TASK-BACKEND-005-1: `.github/workflows/` ディレクトリ作成
- [ ] TASK-BACKEND-005-2: `deploy-frontend.yml` 作成
  - GitHub Pagesデプロイ
- [ ] TASK-BACKEND-005-3: `deploy-api.yml` 作成
  - Cloudflare Workersデプロイ
  - GitHub Secretsから環境変数取得
- [ ] TASK-BACKEND-005-4: デプロイテスト

**受け入れ基準**:
- [ ] mainブランチへのpushで自動デプロイされる
- [ ] 環境変数が正しく設定される
- [ ] デプロイが成功する

---

### TASK-BACKEND-006: キャッシュ機能実装
- **ステータス**: pending
- **優先度**: medium
- **担当**: Backend Sub-Agent
- **推定工数**: 1日
- **依存**: TASK-BACKEND-002, TASK-BACKEND-003

**サブタスク**:
- [ ] TASK-BACKEND-006-1: Cloudflare R2設定
- [ ] TASK-BACKEND-006-2: キャッシュキー生成（URLハッシュ）
- [ ] TASK-BACKEND-006-3: キャッシュ読み書き実装
- [ ] TASK-BACKEND-006-4: キャッシュ有効期限設定（24時間）

**受け入れ基準**:
- [ ] 同じURLは2回目以降キャッシュから取得
- [ ] API呼び出しが削減される
- [ ] コストが最小化される

---

## Phase 1c: 統合＆テスト（Week 3）

### TASK-INT-001: フロントエンド・バックエンド統合
- **ステータス**: pending
- **優先度**: critical
- **担当**: Frontend Sub-Agent + Backend Sub-Agent
- **推定工数**: 1日
- **依存**: Phase 1a完了, Phase 1b完了

**サブタスク**:
- [ ] TASK-INT-001-1: `web/js/app.js` からAPI呼び出し実装
- [ ] TASK-INT-001-2: モックデータ削除
- [ ] TASK-INT-001-3: エラーハンドリング統合
- [ ] TASK-INT-001-4: ローディング表示連携

**受け入れ基準**:
- [ ] URL入力→変換→結果表示が動作する
- [ ] エラー時は適切なメッセージが表示される

---

### TASK-INT-002: テスト実施
- **ステータス**: pending
- **優先度**: high
- **担当**: Test Sub-Agent + プロダクトオーナー
- **推定工数**: 2日
- **依存**: TASK-INT-001

**サブタスク**:
- [ ] TASK-INT-002-1: URL変換テスト
  - GitHub docs (Pull Requests)
  - GitHub docs (Issues)
  - GitHub docs (Actions)
- [ ] TASK-INT-002-2: レベル別テスト（low/medium/high）
- [ ] TASK-INT-002-3: エラーケーステスト
  - 無効なURL
  - 404ページ
  - タイムアウト
- [ ] TASK-INT-002-4: レスポンシブテスト（PC/スマホ）
- [ ] TASK-INT-002-5: プロダクトオーナーによるUAT

**受け入れ基準**:
- [ ] 全てのテストケースがパスする
- [ ] プロダクトオーナーが満足する

---

### TASK-INT-003: デプロイ＆公開準備
- **ステータス**: pending
- **優先度**: high
- **担当**: Orchestrator
- **推定工数**: 1日
- **依存**: TASK-INT-002

**サブタスク**:
- [ ] TASK-INT-003-1: GitHub Pages公開設定
- [ ] TASK-INT-003-2: カスタムドメイン設定（オプション）
- [ ] TASK-INT-003-3: README.md更新（使い方説明）
- [ ] TASK-INT-003-4: 動作確認

**受け入れ基準**:
- [ ] URLでアクセスできる
- [ ] 全機能が動作する
- [ ] ドキュメントが整っている

---

## 保留タスク（Phase 1完了後に検討）

### TASK-FUTURE-001: ファイルアップロード対応
- **ステータス**: pending
- **優先度**: low
- **依存**: Phase 1完了、価値検証済み

**概要**:
- PDF, DOCX等のアップロード
- 既存の `src/converter.py` 活用
- バックエンドでの処理

---

### TASK-FUTURE-002: 画像自動挿入
- **ステータス**: pending
- **優先度**: low
- **依存**: Phase 1完了

**概要**:
- Unsplash API統合
- 関連画像の自動検索
- マニュアルに画像埋め込み

---

### TASK-FUTURE-003: チャット形式対応
- **ステータス**: pending
- **優先度**: low
- **依存**: Phase 1完了

**概要**:
- 対話型インターフェース
- 追加質問対応
- コンテキスト保持

---

## 完了したタスク

### TASK-000: プロジェクト初期構造確立
- **ステータス**: completed
- **完了日**: 2025-01-11
- **成果物**:
  - `docs/` ディレクトリ（要件定義、タスク管理等）
  - `src/converter.py`（保留）
  - `src/simplifier.py`（保留）
  - テストフレームワーク

---

## タスク統計

- **Phase 1a**: 4タスク（pending）
- **Phase 1b**: 6タスク（pending）
- **Phase 1c**: 3タスク（pending）
- **保留**: 3タスク
- **完了**: 1タスク

**合計**: 17タスク

---

## ブロッカー

現在ブロッカーなし

---

## 作業再開ガイド

### いつでも作業を再開できるように

**Phase 1aから開始する場合**:
```
「TASK-UI-001を開始してください」
→ Frontend Sub-Agentが起動して基本レイアウトを作成
```

**Phase 1bから開始する場合**:
```
「TASK-BACKEND-001を開始してください」
→ Backend Sub-Agentが起動してCloudflare Workersをセットアップ
```

**統合フェーズから開始する場合**:
```
「TASK-INT-001を開始してください」
→ Frontend/Backend Sub-Agentが統合作業を実施
```

### 現在の推奨アクション

**次にやるべきこと**: TASK-UI-001（基本レイアウト作成）

```
指示: 「TASK-UI-001を開始してください」
```

---

**最終更新**: 2025年11月1日
**バージョン**: 2.0（全面改訂）
**次回更新予定**: タスク開始時
