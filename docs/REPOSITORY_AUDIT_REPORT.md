# リポジトリ構成監査レポート（Phase 1）

## 1. 対象ディレクトリのツリー構造
```text
docs/
  BRANCH_WORKFLOW_GUIDE.md
  CHAT_FIX_REPORT.md
  DEVELOPMENT_GUIDE.md
  IMPLEMENTATION_SUMMARY.md
  PROJECT_REQUIREMENTS.md
  README.md
  REPOSITORY_AUDIT_REPORT.md
  TASKS_INDEX.md
  WORK_LOG.md
  _INDEX.md
  markdownlint_error_report.md
  ai/
    _INDEX.md
  dev/
    _INDEX.md
  ops/
    _INDEX.md
src/
  __init__.py
  converter.py
  simplifier.py
ops/
  README.md
  agents/
    AGENTS_DETAILS.md
  docs/
    README.md
agents/
  README.md
  README.ja.md
workers/
  README.md
.github/
  README.md
  copilot-instructions.md
  pull_request_template.md
  CODEOWNERS
  instructions/
    docs.instructions.md
    src.instructions.md
    tests.instructions.md
  ISSUE_TEMPLATE/
    bug_report.md
    feature_request.md
    question.md
  prompts/
    README.md
```

## 2. ファイル詳細（.md / .py / .json / .html）
### docs ディレクトリ
| パス | 種別 | 役割 | 最終更新 (UTC) | 依存・関連 |
| --- | --- | --- | --- | --- |
| docs/PROJECT_REQUIREMENTS.md | md | Phase1〜3の要件定義書。Gemini APIやWeb UIなどの必須機能を規定。 | 2025-10-30 | 実装確認時の基準文書。 |
| docs/IMPLEMENTATION_SUMMARY.md | md | 実装済み機能と残課題の整理。Phase1進捗80%を報告。 | 2025-10-30 | src/converter.py, src/simplifier.py の現状を反映。 |
| docs/WORK_LOG.md | md | 日次作業記録とタスクリスト。Gemini統合など未完タスクを列挙。 | 2025-10-30 | 実装サマリーと整合。 |
| docs/README.md | md | ドキュメント入口。Phase1進捗15%と記載されているが、最新の再評価（行134-138）では15〜20%が実態に近く、docs/IMPLEMENTATION_SUMMARY.mdの80%は過大評価。必要に応じて値の更新・整合を推奨。 | 2025-10-30 | 要件・実装との整合が必要。 |
| docs/DEVELOPMENT_GUIDE.md | md | 開発手順とワークフローの詳細。 | 2025-10-30 | `.github/instructions/src.instructions.md` と内容が補完関係。 |
| docs/BRANCH_WORKFLOW_GUIDE.md | md | ブランチ戦略の手順書。 | 2025-10-30 | CONTRIBUTINGドキュメントと一貫。 |
| docs/CHAT_FIX_REPORT.md | md | Copilot Chat整備の経緯レポート。 | 2025-10-30 | `.github/instructions/` や CODEOWNERS 導入背景を記録。 |
| docs/_INDEX.md | md | docs配下のリンク索引スタブ。 | 2025-10-30 | dev/ai/ops 各インデックスと連携。 |
| docs/dev/_INDEX.md | md | 開発系資料の索引スタブ。 | 2025-10-30 | 実ファイルは未整備。 |
| docs/ai/_INDEX.md | md | AI/エージェント資料の索引スタブ。 | 2025-10-30 | `.github/copilot-instructions.md` 等への誘導。 |
| docs/ops/_INDEX.md | md | 運用資料の索引スタブ。 | 2025-10-30 | `ops/` 配下との連携予定。 |
| docs/markdownlint_error_report.md | md | Markdownlint修正の結果ログ。 | 2025-10-30 | `.markdownlint.json` 設定変更の履歴。 |
| docs/TASKS_INDEX.md | md | 本監査で追加した要件⇔実装⇔進捗トレーサビリティ索引。 | 2025-10-30 | PROJECT_REQUIREMENTS.md / IMPLEMENTATION_SUMMARY.md / WORK_LOG.md を参照。 |
| docs/REPOSITORY_AUDIT_REPORT.md | md | 本レポート。 | 2025-10-30 | 全体監査結果。 |

### src ディレクトリ
| パス | 種別 | 役割 | 最終更新 (UTC) | 依存・関連 |
| --- | --- | --- | --- | --- |
| src/converter.py | py | markitdownを利用した多形式→Markdown変換クラス。 | 2025-10-30 | `markitdown[all]` が必須依存。 |
| src/simplifier.py | py | 簡略化パイプラインとCLI。Gemini連携は未実装。 | 2025-10-30 | converterモジュール・将来のGemini APIに依存予定。 |
| src/__init__.py | py | パッケージメタ情報。 | 2025-10-30 | 他モジュールへの依存なし。 |

### ops ディレクトリ
| パス | 種別 | 役割 | 最終更新 (UTC) | 依存・関連 |
| --- | --- | --- | --- | --- |
| ops/README.md | md | 作業用ディレクトリの方針。 | 2025-10-30 | docs/ops/_INDEX.md と連動。 |
| ops/docs/README.md | md | 作業系ドキュメントの集約方針。 | 2025-10-30 | 今後docs配下を移設予定。 |
| ops/agents/AGENTS_DETAILS.md | md | エージェント運用の詳細ルール。 | 2025-10-30 | ルートのAGENTS.mdを補完。 |

### agents ディレクトリ
| パス | 種別 | 役割 | 最終更新 (UTC) | 依存・関連 |
| --- | --- | --- | --- | --- |
| agents/README.md | md | エージェント活用ガイド（英語）。 | 2025-10-30 | 日本語版 README.ja.md と内容連携。 |
| agents/README.ja.md | md | エージェント活用ガイド（日本語）。 | 2025-10-30 | 英語版とほぼ同構成。 |

### workers ディレクトリ
| パス | 種別 | 役割 | 最終更新 (UTC) | 依存・関連 |
| --- | --- | --- | --- | --- |
| workers/README.md | md | バックエンド作業領域のスタブ。 | 2025-10-30 | 今後のWeb/API実装の置き場。 |

### .github ディレクトリ
| パス | 種別 | 役割 | 最終更新 (UTC) | 依存・関連 |
| --- | --- | --- | --- | --- |
| .github/README.md | md | .githubの役割案内スタブ。 | 2025-10-30 | ルートREADMEと役割分担。 |
| .github/copilot-instructions.md | md | Copilot向けガイドライン。 | 2025-10-30 | AGENTS運用と関連。 |
| .github/pull_request_template.md | md | PRテンプレート。 | 2025-10-30 | ワークフロー遵守。 |
| .github/instructions/docs.instructions.md | md | ドキュメント領域向け指示。 | 2025-10-30 | docs配下ドキュメントと連携。 |
| .github/instructions/src.instructions.md | md | ソースコード領域向け指示。 | 2025-10-30 | src配下の規約。 |
| .github/instructions/tests.instructions.md | md | テスト領域向け指示。 | 2025-10-30 | testsディレクトリに適用。 |
| .github/ISSUE_TEMPLATE/bug_report.md | md | バグ報告テンプレート。 | 2025-10-30 | GitHub Issues。 |
| .github/ISSUE_TEMPLATE/feature_request.md | md | 機能要望テンプレート。 | 2025-10-30 | GitHub Issues。 |
| .github/ISSUE_TEMPLATE/question.md | md | 質問テンプレート。 | 2025-10-30 | GitHub Issues。 |
| .github/prompts/README.md | md | プロンプト保存方針の案内。 | 2025-10-30 | 今後のテンプレート配置予定。 |

## 3. 重複・未使用ファイルの観点
- `agents/README.md` と `agents/README.ja.md` は内容が近いが、バイリンガル運用として維持されている。
- `docs/_INDEX.md` および配下の `_INDEX.md` はスタブ状態で、実際のリンクが不足。移設計画の途中段階。
- `docs/markdownlint_error_report.md` はlint作業ログの記録のみで、現状参照箇所がない。アーカイブ扱いで問題ないが、ops/docs配下への移動検討余地あり。
- `docs/README.md` のPhase 1進捗 (15%) が他ドキュメントの数値 (80%) と乖離しており、情報重複による整合性エラー。

## 4. タスク整合性サマリー
- `PROJECT_REQUIREMENTS.md` のPhase1要件（Gemini連携、Web UI、HTML出力など）は現時点で未実装要素が多く、`IMPLEMENTATION_SUMMARY.md` と `WORK_LOG.md` の記録でも未完了として扱われている。
- 新設した `docs/TASKS_INDEX.md` にて要件⇔実装⇔進捗を照合し、Gemini API統合やWeb UI未着手といった差分を明示。
- Phase進捗は `IMPLEMENTATION_SUMMARY.md` と `WORK_LOG.md` が80%で一致。`docs/README.md` の更新遅延のみが不整合として残存。

## 5. 改善提案
1. `docs/README.md` の進捗指標・マイルストーンを `IMPLEMENTATION_SUMMARY.md`/`WORK_LOG.md` に合わせて更新し、情報源の矛盾を解消する。
2. Web UI・HTML出力・Gemini連携など未着手要件を `WORK_LOG.md` の次回作業予定やIssue化で明示化し、Phase1残タスクを可視化する。
3. `docs/_INDEX.md` およびサブ索引に具体的なリンク/概要を追記するか、移設完了までのロードマップを `ops/docs/README.md` に追記してスタブ状態を管理する。

---

## 6. 追加監査所見（2025-10-31）

### 6.1 Phase 1 実装再評価
- `docs/IMPLEMENTATION_SUMMARY.md` と `docs/WORK_LOG.md` に記載された「Phase 1 進捗80%」は、コード実装の実態と乖離しています。
- `src/simplifier.py` の `simplify_text` 関数はプレースホルダーであり、Gemini API 連携も簡易化ロジックも存在しません。
- `simplify_file` は Markdown 変換を呼び出すのみで、HTML/テキスト出力やレベル別要約処理は実装されていません。
- `src/converter.py` は markitdown ライブラリのラッパーに留まり、ライブラリ未導入環境では ImportError となるため、テストも `@pytest.mark.skipif` で多くが未実行になります。
- 以上を踏まえ、Phase 1 の達成度は「基盤コードの雛形が存在する段階（推定 15〜20%）」と評価し、要件達成には Gemini 連携・Web UI・多形式出力・実稼働テストの整備が必要です。

| 要件観点 | 期待される成果 | 現状のコード/ドキュメント | 評価 |
| --- | --- | --- | --- |
| テキスト簡易化（Gemini API） | Gemini API を利用した 3 レベルの簡易化処理 | `simplify_text` が入力をそのまま返すのみ。Gemini API 設定・呼び出しなし。 | 未実装 |
| Web インターフェース | HTML/JS ベースの UI、リアルタイムプレビュー | 該当コード・ドキュメントなし。 | 未着手 |
| 多形式出力 | HTML・Markdown・テキストの選択出力 | `simplify_file` で Markdown 保存のみ。HTML/テキスト切り替えなし。 | 部分的 |
| テスト整備 | markitdown 連携を含むテスト 17 件合格 | markitdown 未導入時は主要テストが skip。実測の成功証跡なし。 | 未確認 |

### 6.2 目的・出力形式の再確認
- `docs/PROJECT_REQUIREMENTS.md` では、PDF・Word・Excel・HTML など多様な入力に対応し、出力も HTML/Markdown/テキストへ展開する Web アプリを Phase 1 のゴールに設定しています。
- 既存ドキュメントにある「出力は HTML・Markdown・テキスト」という記述は GPT 作業ログ由来のメモであり、当初の設計意図（多形態への展開、将来的な Word/Excel/PDF 生成など）を再度強調する必要があります。

### 6.3 Markdownlint 運用メモ
- `docs/markdownlint_error_report.md` にあるように、VS Code 上の markdownlint による誤検知が生産性を阻害したため、ローカル設定で lint を停止しています。
- リポジトリ（CI）側の markdownlint 設定は既に有効化・運用中です。ローカル（VS Code）での lint のみ停止しています。各エージェントは整形ルール（Heading のレベル順序、テーブルの整列など）を手動で維持しつつ、不要なローカル設定追加を避けてください。
- 今後ローカル lint を再有効化する場合は `.vscode/settings.json` と CI 設定を調整し、既存ドキュメントへの影響を最小化する手順を整備することが推奨されます。
