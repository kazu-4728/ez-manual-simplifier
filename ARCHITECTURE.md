# Architecture / アーキテクチャ

[English](#english) | [日本語](#japanese)

---

## English

### System Architecture

EZ Manual Simplifier is designed with a modular architecture that separates concerns and allows for easy extension and maintenance.

#### Core Components

``` text
┌─────────────────────────────────────────┐
│            User Interface               │
│   (CLI / Web Interface / API)           │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│      Simplification Engine              │
│  - Text Analysis                        │
│  - Language Processing                  │
│  - Simplification Rules                 │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│       Document Processors               │
│  - Format Parsers                       │
│  - Content Extractors                   │
│  - Output Formatters                    │
└─────────────────────────────────────────┘
```

#### Key Design Principles

1. **Modularity**: Each component is independent and can be replaced or upgraded

2. **Extensibility**: New document formats and simplification strategies can be easily added

3. **Testability**: Components are designed to be easily testable in isolation

4. **Performance**: Efficient algorithms for processing large documents

5. **Maintainability**: Clear code structure and comprehensive documentation

#### Data Flow

1. **Input**: User provides a document in supported format

2. **Parsing**: Document is parsed and content is extracted

3. **Analysis**: Content is analyzed for complexity

4. **Simplification**: Text is simplified according to specified level

5. **Formatting**: Simplified content is formatted for output

6. **Output**: Simplified document is returned to user

#### Technology Stack

- **Language**: Python 3.8+

- **Testing**: pytest

- **Code Quality**: black, flake8, mypy

- **Documentation**: Markdown

#### Future Architecture Considerations

- Microservices architecture for scalability

- Message queue for asynchronous processing

- Caching layer for frequently processed documents

- Plugin system for custom simplification rules

---

## Japanese

### システムアーキテクチャ

EZ Manual Simplifier は、関心事を分離し、拡張と保守を容易にするモジュラーアーキテクチャで設計されています。

#### コアコンポーネント

``` text
┌─────────────────────────────────────────┐
│          ユーザーインターフェース        │
│   (CLI / ウェブインターフェース / API)   │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│        簡素化エンジン                   │
│  - テキスト分析                         │
│  - 言語処理                             │
│  - 簡素化ルール                         │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│      ドキュメントプロセッサ              │
│  - フォーマットパーサー                 │
│  - コンテンツ抽出器                     │
│  - 出力フォーマッター                   │
└─────────────────────────────────────────┘
```

#### 主要な設計原則

1. **モジュラー性**: 各コンポーネントは独立しており、交換またはアップグレードできます

2. **拡張性**: 新しいドキュメント形式と簡素化戦略を簡単に追加できます

3. **テスト容易性**: コンポーネントは分離してテストしやすいように設計されています

4. **パフォーマンス**: 大きなドキュメントを処理するための効率的なアルゴリズム

5. **保守性**: 明確なコード構造と包括的なドキュメント

#### データフロー

1. **入力**: ユーザーがサポートされている形式でドキュメントを提供します

2. **パース**: ドキュメントが解析され、コンテンツが抽出されます

3. **分析**: コンテンツの複雑さが分析されます

4. **簡素化**: 指定されたレベルに従ってテキストが簡素化されます

5. **フォーマット**: 簡素化されたコンテンツが出力用にフォーマットされます

6. **出力**: 簡素化されたドキュメントがユーザーに返されます

#### 技術スタック

- **言語**: Python 3.8+

- **テスト**: pytest

- **コード品質**: black, flake8, mypy

- **ドキュメント**: Markdown

#### 将来のアーキテクチャ検討事項

- スケーラビリティのためのマイクロサービスアーキテクチャ

- 非同期処理のためのメッセージキュー

- 頻繁に処理されるドキュメントのキャッシュレイヤー

- カスタム簡素化ルールのプラグインシステム
