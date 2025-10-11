# EZ Manual Simplifier 開発ガイド

## 🚀 クイックスタート

### 環境構築

```bash
# リポジトリクローン
git clone https://github.com/kazu-4728/ez-manual-simplifier.git
cd ez-manual-simplifier

# 仮想環境作成
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存関係インストール
pip install -r requirements.txt
```

### 開発サーバー起動

```bash
# テスト実行
python -m pytest

# 開発サーバー起動
python src/simplifier.py
```

## 🏗️ プロジェクト構造

``` text
ez-manual-simplifier/
├── docs/                           # ドキュメント
│   ├── PROJECT_REQUIREMENTS.md     # プロジェクト要件定義書
│   ├── WORK_LOG.md                 # 作業記録
│   ├── DEVELOPMENT_GUIDE.md        # 開発ガイド（このファイル）
│   └── README.md                   # ドキュメント概要
├── src/                            # ソースコード
│   ├── simplifier.py               # メインモジュール
│   ├── api/                        # API関連（予定）
│   │   ├── __init__.py
│   │   ├── gemini_client.py        # Gemini API クライアント
│   │   └── web_api.py              # Web API エンドポイント
│   ├── web/                        # Webインターフェース（予定）
│   │   ├── __init__.py
│   │   ├── static/                 # 静的ファイル
│   │   │   ├── css/
│   │   │   ├── js/
│   │   │   └── images/
│   │   └── templates/              # HTML テンプレート
│   └── utils/                      # ユーティリティ（予定）
│       ├── __init__.py
│       ├── text_processor.py       # テキスト処理
│       └── formatters.py           # 出力フォーマッター
├── tests/                          # テスト
│   ├── __init__.py
│   ├── test_simplifier.py          # 既存のテスト
│   ├── test_api/                   # APIテスト（予定）
│   └── test_web/                   # Webテスト（予定）
├── .github/                        # GitHub Actions（予定）
│   └── workflows/
│       ├── ci.yml                  # 継続的インテグレーション
│       └── deploy.yml              # デプロイメント
├── requirements.txt                # 依存関係
├── setup.py                        # パッケージ設定
└── README.md                       # プロジェクト概要
```

## 🔧 開発フロー

### 1. 機能開発

1. **Issue作成**: 機能要件を明確化

2. **ブランチ作成**: `feature/機能名` 形式

3. **実装・テスト**: コード作成とテスト記述

4. **PR作成**: レビュー依頼

5. **レビュー・マージ**: コードレビュー後のマージ

### 2. デプロイ

1. **自動テスト実行**: CI/CD パイプライン

2. **本番環境デプロイ**: GitHub Pages/Cloudflare Pages

3. **動作確認**: デプロイ後の動作テスト

4. **ロールバック準備**: 問題発生時の対応

### 3. バグ修正

1. **バグ報告**: Issue作成

2. **再現確認**: バグの再現手順確認

3. **修正実装**: バグ修正コード作成

4. **テスト**: 修正の動作確認

5. **デプロイ**: 修正版のリリース

## 📝 コーディング規約

### Python

```python
# 型ヒントの使用
def simplify_text(text: str, level: str = "medium") -> str:
    """
    テキストを簡易化する関数

    Args:
        text: 簡易化するテキスト
        level: 簡易化レベル ("low", "medium", "high")

    Returns:
        簡易化されたテキスト

    Raises:
        ValueError: 無効なレベルが指定された場合
    """
    if level not in ["low", "medium", "high"]:
        raise ValueError(f"Invalid simplification level: {level}")

    # 実装コード
    return processed_text
```

- **PEP 8準拠**: Python標準のコーディング規約

- **型ヒント使用**: 関数の引数と戻り値に型を明記

- **ドキュメント文字列必須**: 関数の説明を記述

- **エラーハンドリング**: 適切な例外処理

### JavaScript

```javascript
/**
 * テキスト簡易化機能のフロントエンド処理
 * @param {string} text - 入力テキスト
 * @param {string} level - 簡易化レベル
 * @returns {Promise<string>} 簡易化されたテキスト
 */
async function simplifyText(text, level = 'medium') {
    try {
        const response = await fetch('/api/simplify', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text, level })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        return result.simplified_text;
    } catch (error) {
        console.error('Error simplifying text:', error);
        throw error;
    }
}
```

- **ES6+使用**: モダンなJavaScript機能を活用

- **セミコロン必須**: コードの明確性のため

- **コメント充実**: 関数の目的と動作を説明

- **エラーハンドリング**: try-catch文での例外処理

### テスト

```python
import pytest
from src.simplifier import simplify_text

class TestSimplifier:
    """テキスト簡易化機能のテストクラス"""

    def test_simplify_text_basic(self):
        """基本的なテキスト簡易化テスト"""
        text = "This is a complex technical manual."
        result = simplify_text(text)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_simplify_text_levels(self):
        """簡易化レベルのテスト"""
        text = "This is a test text."

        for level in ["low", "medium", "high"]:
            result = simplify_text(text, level=level)
            assert isinstance(result, str)
            assert len(result) > 0

    def test_simplify_text_invalid_level(self):
        """無効なレベルのテスト"""
        text = "This is a test text."

        with pytest.raises(ValueError, match="Invalid simplification level"):
            simplify_text(text, level="invalid")
```

- **単体テスト必須**: 各関数の動作確認

- **カバレッジ80%以上**: テストカバレッジの確保

- **統合テスト推奨**: システム全体の動作確認

- **テストクラス使用**: 関連するテストのグループ化

## 🚨 トラブルシューティング

### よくある問題

#### 1. API制限エラー

``` text
Error: API quota exceeded
```

**解決策**:

- レート制限の実装

- キャッシュ機能の追加

- エラーハンドリングの強化

#### 2. デプロイ失敗

``` text
Error: Build failed on GitHub Pages
```

**解決策**:

- ビルドログの確認

- 依存関係の確認

- 設定ファイルの見直し

#### 3. テスト失敗

``` text
FAILED tests/test_simplifier.py::TestSimplifier::test_simplify_text_basic
```

**解決策**:

- ローカル環境での再現

- テストデータの確認

- 実装コードの見直し

### デバッグ手順

1. **ログ確認**: エラーログの詳細確認

2. **環境確認**: 依存関係とバージョン確認

3. **最小再現**: 問題の最小限の再現コード作成

4. **段階的テスト**: 問題箇所の特定

5. **修正実装**: 問題の修正

## 📚 参考資料

### 技術ドキュメント

- [Gemini API Documentation](https://ai.google.dev/docs)

- [GitHub Actions Documentation](https://docs.github.com/actions)

- [Flask Documentation](https://flask.palletsprojects.com/)

- [FastAPI Documentation](https://fastapi.tiangolo.com/)

### 設計資料

- [プロジェクト要件定義書](PROJECT_REQUIREMENTS.md)

- [アーキテクチャ設計書](../ARCHITECTURE.md)

- [作業記録](WORK_LOG.md)

### 外部リソース

- [Python PEP 8 Style Guide](https://pep8.org/)

- [JavaScript MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

- [HTML5 Specification](https://html.spec.whatwg.org/)

- [CSS3 Specification](https://www.w3.org/TR/css3-roadmap/)

## 🔄 継続的改善

### コードレビュー

- **機能性**: 要件を満たしているか
- **品質**: コードの可読性と保守性
- **パフォーマンス**: 実行効率の確認
- **セキュリティ**: 脆弱性の確認

### リファクタリング

- **定期的な見直し**: 月次でのコード品質確認
- **技術的負債の解消**: 古いコードの更新
- **パフォーマンス改善**: ボトルネックの特定と改善

### 学習と成長

- **技術トレンド**: 新しい技術の調査
- **ベストプラクティス**: 業界標準の学習
- **ツール改善**: 開発効率向上のためのツール導入

---

**作成日**: 2024年12月19日
**バージョン**: 1.0
**作成者**: kazu-4728
**最終更新**: 2024年12月19日

