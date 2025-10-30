# タスク索引（要件 ⇔ 実装 ⇔ 進捗）

## 2025-10-30 監査トレース
| トピック | 要件出典 | 実装出典 | 作業ログ出典 | 整合性メモ |
| --- | --- | --- | --- | --- |
| テキスト簡易化（3レベル対応/Gemini API） | [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md#phase-1-%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A2%E3%83%AB%E7%B0%A1%E6%98%93%E5%8C%96%E3%82%B5%E3%82%A4%E3%83%88%E6%A9%9F%E8%83%BD) | [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md#1-%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88%E5%A4%89%E6%8F%9B%E6%A9%9F%E8%83%BD-srcconverterpy) / [src/simplifier.py](../src/simplifier.py) | [WORK_LOG.md](WORK_LOG.md#-%E9%80%B2%E8%A1%8C%E4%B8%AD%E3%82%BF%E3%82%B9%E3%82%AF%E8%A9%B3%E7%B4%B0%E3%83%AD%E3%82%B0) | 簡易化レベル検証は実装済みだが、Gemini API連携は未完了。実際の変換処理はプレースホルダー。 |
| Webインターフェース/リアルタイムプレビュー | [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md#web%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%95%E3%82%A7%E3%83%BC%E3%82%B9) | 未実装（該当コード・ドキュメントなし） | 未着手（ログ記載なし） | Phase 1要件だがリポジトリに痕跡無し。優先タスクに再掲必要。 |
| 出力形式（HTML/Markdown/テキスト） | [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md#%E5%87%BA%E5%8A%9B%E5%BD%A2%E5%BC%8F) | CLIでMarkdown/テキストまでは下準備 ([src/simplifier.py](../src/simplifier.py)) | 明示的な実績記録無し | HTML出力は未対応。Markdown保存は `simplify_file` で対応可能。 |
| CLI/パイプライン整備 | [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md#phase-1-%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A2%E3%83%AB%E7%B0%A1%E6%98%93%E5%8C%96%E3%82%B5%E3%82%A4%E3%83%88) | [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md#2-%E7%B0%A1%E7%95%A5%E5%8C%96%E3%83%91%E3%82%A4%E3%83%97%E3%83%A9%E3%82%A4%E3%83%B3-srcsimplifierpy) | [WORK_LOG.md](WORK_LOG.md#-%E5%AE%8C%E4%BA%86%E3%82%BF%E3%82%B9%E3%82%AF) | CLI操作とファイルパイプラインは実装・記録済み。 |
| Phase進捗表示 | [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md#phase-1-%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A2%E3%83%AB%E7%B0%A1%E6%98%93%E5%8C%96%E3%82%B5%E3%82%A4%E3%83%88) | [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md#phase-1-%E9%80%B2%E6%8D%97%E7%8A%B6%E6%B3%81)（80%と明記） | [WORK_LOG.md](WORK_LOG.md#-%E5%85%A8%E4%BD%93%E9%80%B2%E6%8D%97)（80%と一致） | `docs/README.md` はPhase 1進捗15%と記述しており矛盾。更新必要。 |
| Phase 2/3 準備タスク | [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md#phase-2-%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E9%80%A3%E6%90%BA%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0) | [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md#phase-2%E6%BA%96%E5%82%99) | [WORK_LOG.md](WORK_LOG.md#phase-2-%E3%82%BF%E3%82%B9%E3%82%AF%E3%83%AA%E3%82%B9%E3%83%88%E4%BA%88%E5%AE%9A) | 要件・設計・ログすべてで「未着手/予定」と一致。 |

## インデックスメモ
- 進捗指標は `IMPLEMENTATION_SUMMARY.md` と `WORK_LOG.md` が一致しており、`PROJECT_REQUIREMENTS.md` のPhase構造とも整合。`docs/README.md` の数値のみ古い。
- Web UIやHTML出力など未実装要件は作業ログに現れていないため、次回更新で優先度付けが必要。
- `WORK_LOG.md` にGemini統合作業が残課題として明記されており、実装・要件の差分を吸収する計画が提示されている。

---

## 2025-10-31 再評価トレース
| トピック | 要件出典 | 実装出典 | 作業ログ出典 | 現状診断 |
| --- | --- | --- | --- | --- |
| Gemini API を用いたテキスト簡易化 | [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md#%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E7%B0%A1%E6%98%93%E5%8C%96%E6%A9%9F%E8%83%BD) | [src/simplifier.py](../src/simplifier.py#L21-L43) | [WORK_LOG.md](WORK_LOG.md#-%E9%80%B2%E8%A1%8C%E4%B8%AD%E3%82%BF%E3%82%B9%E3%82%AF) | `simplify_text` が入力を返すだけで Gemini API 連携はゼロ。ログ上も着手記録なし。 |
| Web インターフェースおよびリアルタイムプレビュー | [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md#web%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%95%E3%82%A7%E3%83%BC%E3%82%B9) | 実装なし | 未着手 | UI 関連ファイルやログが存在せず、Phase 1 要件が未対応。 |
| 多形式出力（HTML/Markdown/テキスト） | [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md#%E5%87%BA%E5%8A%9B%E5%BD%A2%E5%BC%8F) | [src/simplifier.py](../src/simplifier.py#L45-L87) | 記録なし | Markdown への保存は可能だが HTML/プレーンテキスト切替は実装されていない。 |
| マニュアル変換（markitdown 依存） | [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md#phase-1-%E6%8A%80%E8%A1%93%E4%BB%95%E6%A7%98) | [src/converter.py](../src/converter.py) | [tests/test_converter.py](../tests/test_converter.py) | ライブラリ未導入環境では ImportError となり、pytest も skip 条件が多い。運用環境での検証が必要。 |
| Phase 進捗評価 | [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md#phase-1-%E9%80%B2%E6%8D%97%E7%8A%B6%E6%B3%81) | [WORK_LOG.md](WORK_LOG.md#-%E5%85%A8%E4%BD%93%E9%80%B2%E6%8D%97) | [docs/REPOSITORY_AUDIT_REPORT.md](REPOSITORY_AUDIT_REPORT.md#61-phase-1-%E5%AE%9F%E8%A3%85%E5%86%8D%E8%A9%95%E4%BE%A1) | 現状のコードから判断すると Phase 1 達成度は 15〜20% 程度。各文書の数値更新が必要。 |

### 追記メモ
- 元々の目的は HTML/PDF/Excel/Word など多形態への出力を見据えており、Markdown/テキスト限定という記述は GPT 作業メモに基づく暫定情報である。
- markdownlint は VS Code 側で無効化しており、レポジトリ設定での強制は作業効率を阻害するため慎重に扱うこと。必要な整形は手動で維持する。 
- 次フェーズでは Gemini 連携と Web UI の最小実装を優先し、作業ログに着手記録を残すことが求められる。
