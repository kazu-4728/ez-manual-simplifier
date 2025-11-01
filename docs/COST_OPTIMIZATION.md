# コスト最適化ガイドライン

## 目的

MCPやAPIを利用する際のコストを最小限に抑制し、無駄なAPI呼び出しを避ける。

## 基本原則

1. **必要な時だけAPIを呼び出す**
2. **結果をキャッシュする**
3. **バッチ処理を活用する**
4. **コンテキストを最小限に保つ**
5. **効率的なプロンプト設計**

## API使用制限

### Gemini API

**制限**:
- 1日あたり: 1000リクエスト
- 1リクエストあたり: 30,000トークン
- コスト: 無料枠内で運用

**最適化戦略**:
- プロンプトを簡潔に
- 不要なコンテキストを削除
- バッチ処理で複数テキストを一度に処理

### MCP (Model Context Protocol)

**制限**:
- コンテキスト消費を最小限に
- 必要な情報のみを取得

**最適化戦略**:
- サブエージェントで分担
- 参照ドキュメントを明確化
- 不要なファイル読み込みを避ける

## コンテキストオーバー防止

### チャンク分割

**原則**: 大きなテキストは適切に分割

**実装例**:
```python
def split_text(text: str, max_chunk_size: int = 8000) -> list[str]:
    """テキストをチャンクに分割"""
    # 段落単位で分割
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = []
    current_size = 0
    
    for para in paragraphs:
        para_size = len(para)
        if current_size + para_size > max_chunk_size:
            if current_chunk:
                chunks.append('\n\n'.join(current_chunk))
            current_chunk = [para]
            current_size = para_size
        else:
            current_chunk.append(para)
            current_size += para_size
    
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks
```

### プロンプト最適化

**良い例**:
```
以下のテキストを簡易化してください（レベル: medium）:
[テキスト]
```

**悪い例**:
```
こんにちは。このプロジェクトはマニュアル簡易化ツールです。
以下のテキストを、専門用語を避け、わかりやすい言葉に置き換え、
小学生でも理解できるレベルに簡易化してください。
ただし、重要な情報は削除せず、構造は維持してください。
レベルはmediumで、以下のガイドラインに従ってください...
[長い説明]
[テキスト]
```

### 不要なコンテキストの削除

**チェックリスト**:
- [ ] 不要な履歴を削除したか？
- [ ] 必要な情報のみをプロンプトに含めたか？
- [ ] ファイル全体を読み込まず、必要な部分だけ読み込んだか？
- [ ] 重複する情報を削除したか？

## キャッシュ戦略

### リサーチ結果のキャッシュ

```python
from functools import lru_cache
from typing import Optional
import hashlib

class ResearchCache:
    def __init__(self):
        self.cache = {}
    
    def get_cache_key(self, query: str) -> str:
        """クエリからキャッシュキーを生成"""
        return hashlib.md5(query.encode()).hexdigest()
    
    def get(self, query: str) -> Optional[str]:
        """キャッシュから取得"""
        key = self.get_cache_key(query)
        return self.cache.get(key)
    
    def set(self, query: str, result: str):
        """キャッシュに保存"""
        key = self.get_cache_key(query)
        self.cache[key] = result
```

### 変換結果のキャッシュ

- 同じファイルの変換結果はキャッシュ
- URL変換結果もキャッシュ
- キャッシュ有効期限: 24時間

## バッチ処理

### 複数テキストの一括処理

```python
def simplify_batch(texts: list[str], level: str = "medium") -> list[str]:
    """複数のテキストを一度に簡易化"""
    # プロンプトに複数テキストを含める
    prompt = f"以下の{len(texts)}個のテキストを簡易化してください（レベル: {level}）:\n\n"
    for i, text in enumerate(texts, 1):
        prompt += f"--- テキスト{i} ---\n{text}\n\n"
    
    # 1回のAPI呼び出しで処理
    result = call_gemini_api(prompt)
    
    # 結果を分割して返す
    return split_results(result, len(texts))
```

## プロンプトテンプレート

### 簡易化プロンプト（最適化版）

```python
SIMPLIFY_PROMPT_TEMPLATE = {
    "low": "以下のテキストを小学生でも理解できるレベルに簡易化してください:\n\n{text}",
    "medium": "以下のテキストを一般的な読みやすさに簡易化してください:\n\n{text}",
    "high": "以下のテキストを専門用語は残しつつ説明を追加して簡易化してください:\n\n{text}"
}
```

### リサーチプロンプト（最適化版）

```python
RESEARCH_PROMPT_TEMPLATE = "ユーザーのリクエストに基づいてマニュアルを作成してください:\n\nリクエスト: {query}\n\nマニュアル内容:"
```

## モニタリング

### コスト追跡

```python
class CostTracker:
    def __init__(self):
        self.api_calls = 0
        self.tokens_used = 0
        self.cache_hits = 0
        self.cache_misses = 0
    
    def record_api_call(self, tokens: int):
        """API呼び出しを記録"""
        self.api_calls += 1
        self.tokens_used += tokens
    
    def record_cache_hit(self):
        """キャッシュヒットを記録"""
        self.cache_hits += 1
    
    def record_cache_miss(self):
        """キャッシュミスを記録"""
        self.cache_misses += 1
    
    def get_stats(self) -> dict:
        """統計情報を取得"""
        total_requests = self.cache_hits + self.cache_misses
        cache_rate = self.cache_hits / total_requests if total_requests > 0 else 0
        
        return {
            "api_calls": self.api_calls,
            "tokens_used": self.tokens_used,
            "cache_hit_rate": cache_rate,
            "cost_saved": self.cache_hits * 0.001  # 仮の計算
        }
```

## チェックリスト

実装前に確認:

- [ ] プロンプトは簡潔か？
- [ ] 不要なコンテキストを削除したか？
- [ ] キャッシュを活用できるか？
- [ ] バッチ処理を活用できるか？
- [ ] チャンク分割が必要か？
- [ ] API呼び出し回数を最小限に抑えているか？

---

**最終更新**: 2025-01-11
**バージョン**: 1.0