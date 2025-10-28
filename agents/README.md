# Agents / エージェント

[English](#english) | [日本語](#japanese)

---

## English

### Overview

This directory contains agent configurations and instructions for AI-powered automation in the EZ Manual
Simplifier project. Agents can help with various tasks such as code review, documentation generation, and testing.

### Agent Types

#### Documentation Agent

- **Purpose**: Generates and maintains project documentation

- **Capabilities**:

  - Creates README files

  - Updates API documentation

  - Generates usage examples

  - Translates documentation to multiple languages

#### Code Review Agent

- **Purpose**: Reviews code changes and provides feedback

- **Capabilities**:

  - Checks code style and standards

  - Identifies potential bugs

  - Suggests improvements

  - Validates test coverage

#### Testing Agent

- **Purpose**: Assists with test creation and maintenance

- **Capabilities**:

  - Generates unit tests

  - Creates integration tests

  - Identifies missing test cases

  - Updates tests when code changes

### Usage

Agents can be invoked through various mechanisms depending on your setup:

- GitHub Actions workflows

- Command-line interface

- IDE integrations

- API calls

### Configuration

Agent configurations are stored in YAML files in this directory. Each agent has its own configuration file that defines:

- Agent name and description

- Capabilities and limitations

- Trigger conditions

- Output formats

### Best Practices

1. **Clear Instructions**: Provide clear and specific instructions to agents

2. **Review Agent Output**: Always review agent-generated content before merging

3. **Iterative Improvement**: Refine agent prompts based on output quality

4. **Version Control**: Track agent configuration changes in version control

### Future Enhancements

- Specialized agents for different programming languages

- Custom agents for project-specific tasks

- Agent orchestration for complex workflows

- Learning from feedback to improve agent performance

---

## Japanese

### 概要

このディレクトリには、EZ Manual Simplifier プロジェクトにおける AI を活用した自動化のためのエージェント設定と指示が含まれています。エージェントは、コードレビュー、ドキュメント生成、テストなど、さまざまなタスクを支援できます。

### エージェントの種類

#### ドキュメントエージェント

- **目的**: プロジェクトドキュメントの生成と保守

- **機能**:

  - README ファイルの作成

  - API ドキュメントの更新

  - 使用例の生成

  - ドキュメントの多言語翻訳

#### コードレビューエージェント

- **目的**: コード変更のレビューとフィードバックの提供

- **機能**:

  - コードスタイルと標準のチェック

  - 潜在的なバグの特定

  - 改善の提案

  - テストカバレッジの検証

#### テストエージェント

- **目的**: テストの作成と保守の支援

- **機能**:

  - ユニットテストの生成

  - 統合テストの作成

  - 不足しているテストケースの特定

  - コード変更時のテストの更新

### 使用方法

エージェントは、セットアップに応じてさまざまなメカニズムを通じて呼び出すことができます：

- GitHub Actions ワークフロー

- コマンドラインインターフェース

- IDE 統合

- API 呼び出し

### 設定

エージェント設定は、このディレクトリの YAML ファイルに保存されます。各エージェントには、以下を定義する独自の設定ファイルがあります：

- エージェント名と説明

- 機能と制限事項

- トリガー条件

- 出力形式

### ベストプラクティス

1. **明確な指示**: エージェントに明確で具体的な指示を提供する

2. **エージェント出力のレビュー**: マージする前に、エージェントが生成したコンテンツを必ずレビューする

3. **反復的改善**: 出力品質に基づいてエージェントプロンプトを改良する

4. **バージョン管理**: エージェント設定の変更をバージョン管理で追跡する

### 今後の機能強化

- さまざまなプログラミング言語用の専門エージェント

- プロジェクト固有のタスク用のカスタムエージェント

- 複雑なワークフローのためのエージェントオーケストレーション

- フィードバックから学習してエージェントのパフォーマンスを向上させる
