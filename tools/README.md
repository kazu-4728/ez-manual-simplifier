# Tools Directory

このディレクトリには、EZ Manual Simplifier プロジェクトの開発・保守に使用するツールが含まれています。

## 利用可能なツール

### `fix_md_blanklines.ps1`

**目的**: Markdownファイルの自動フォーマット

**機能**:

- リストの前後に適切な空行を挿入

- コードフェンスの前後に空行を挿入

- 見出しの前後に空行を挿入

- 重複する空行の削除

- 行末の不要な空白削除

- 裸のURLを自動リンク化

- 重複見出しの自動リネーム

**使用方法**:

```powershell
# VS Code タスクから実行（推奨）
Ctrl+Shift+P → "Tasks: Run Task" → "Fix Markdown spacing"

# PowerShellから直接実行
powershell -NoProfile -ExecutionPolicy Bypass -File tools/fix_md_blanklines.ps1 -Root .
```

**対象ファイル**: `**/*.md` (リポジトリ内のすべてのMarkdownファイル)

### `install_hooks.ps1`

**目的**: Git pre-commit フックの有効化

**機能**:

- `.githooks/pre-commit` をGitフックとして設定

- コミット前の自動Markdownフォーマット実行

**使用方法**:

```powershell
# ローカルリポジトリ用（推奨）
powershell -NoProfile -ExecutionPolicy Bypass -File tools/install_hooks.ps1

# グローバル設定用
powershell -NoProfile -ExecutionPolicy Bypass -File tools/install_hooks.ps1 -Global
```

## CI/CD 統合

これらのツールは GitHub Actions ワークフロー (`.github/workflows/markdownlint.yml`) と統合されており、PR時に自動実行されます。

## トラブルシューティング

### PowerShell 実行ポリシーエラー

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### ファイルが見つからないエラー

リポジトリのルートディレクトリから実行してください：

```powershell
cd c:\Users\MF-P0624\git_cusor\ez-manual-simplifier
```

## 開発者向け情報

- **言語**: PowerShell 5.1+ / PowerShell Core 6.0+

- **依存関係**: なし（Windows標準のPowerShellで動作）

- **テスト**: CI/CDパイプラインで自動テスト実行

