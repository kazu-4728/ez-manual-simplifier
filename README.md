# ez-manual-simplifier

目的:
- 複雑なマニュアルや技術文書を、小学生でも理解できる簡単な言葉に自動変換・出力するウェブサービスを構築するプロジェクトです。
- 複数のエージェント（解析・簡易化・校正・表示など）が協調して動作します。

主要機能（予定）:
- 入力: PDF / Markdown / HTML / テキスト
- 解析エージェント: 文構造と用語を解析
- 簡易化エージェント: 難しい語彙を易しい語彙に置換、文を短く整理
- QAエージェント: 意味保持の検証と安全性チェック
- Web UI: 結果のプレビュー、難易度選択、フィードバック機能
- API: バッチ処理・外部連携用

クイックスタート（テンプレ）:
1. リポジトリをクローン:
   git clone https://github.com/kazu-4728/ez-manual-simplifier.git
   cd ez-manual-simplifier

2. 言語/スタックに応じて依存をインストール（例）
- Python:
   python -m venv .venv
   . .venv/bin/activate
   pip install -r requirements.txt
- Node:
   npm install

3. ローカル起動（例）
- Python サービス: python -m app
- Next.js: npm run dev

開発ガイド:
- ブランチ: feature/xxx、fix/xxx を使用
- PR の際は変更点の説明と手順（再現方法）を必ず記載
- エージェントを追加する際は agents/ 下に各エージェントの実装を置き、agents/README.md に仕様を追記

貢献:
- CONTRIBUTING.md を参照してください

ライセンス:
- LICENSE ファイルを参照してください

連絡:
- リポジトリオーナー: @kazu-4728
