# GitHub Copilot Instructions for EZ Manual Simplifier

## Project Overview

This is a Python-based manual simplification tool in early development (v0.1.0) designed to transform complex technical documentation into accessible formats using AI. The project follows a three-phase roadmap: Phase 1 (current) focuses on core simplification via Gemini API, Phase 2 adds agent coordination, and Phase 3 targets full automation.

## Architecture

- **Core Module**: `src/simplifier.py` contains the main `simplify_text()` function with validation for levels ["low", "medium", "high"]

- **Planned Structure**: Future expansion includes `api/`, `web/`, and `utils/` subdirectories under `src/`

- **Test Strategy**: Tests use manual path insertion for imports: `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))`

- **Packaging**: Console script entry point defined as `ez-manual-simplifier=simplifier:main` in `setup.py`

## Development Workflows

### Testing

- Run tests with: `python -m pytest` or directly `python tests/test_simplifier.py`

- Tests require manual path setup due to current project structure

- Development dependencies installed via `extras_require["dev"]` in setup.py

### Code Quality

- **Markdown**: Auto-formatting via PowerShell script `tools/fix_md_blanklines.ps1`

- **CI/CD**: GitHub Actions runs markdownlint on all .md files

- **Config**: `.markdownlint.json` disables line length (MD013) and heading levels (MD001)

- **Available Task**: Use `run_task` with "Fix Markdown spacing" for local formatting

### Version Control

- **Branch Strategy**: Feature branches follow `feature/功能名` pattern (Japanese)

- **PR Template**: Includes Japanese sections for 概要, 変更点, テスト, チェックリスト

- **Required Checks**: markdownlint must pass; formatting script detects issues

## Project Conventions

### Language Support

- **Bilingual**: All major documentation exists in both English and Japanese (e.g., `README.md` + `README.ja.md`)

- **Documentation**: Development guides and architectural docs are primarily in Japanese

- **Code**: Python code uses English identifiers, docstrings, and comments

### Documentation Structure

- `docs/PROJECT_REQUIREMENTS.md`: Contains 3-phase roadmap and technical specs

- `docs/DEVELOPMENT_GUIDE.md`: Comprehensive Japanese development workflow guide

- `agents/README.md`: Future AI agent coordination specifications

- `ARCHITECTURE.md`: System design with modular component breakdown

### Error Handling Pattern

```python
def simplify_text(text: str, level: str = "medium") -> str:
    if level not in ["low", "medium", "high"]:
        raise ValueError(f"Invalid simplification level: {level}")
    # Implementation follows...
```

## Integration Points

- **Future AI Integration**: Gemini API planned for text processing

- **Web Interface**: Flask/FastAPI backend with vanilla JavaScript frontend planned

- **Deployment**: GitHub Pages + Cloudflare Pages for hosting

- **Agent System**: GitHub Actions integration for automation workflows

## Key Files for Context

- `src/simplifier.py`: Main entry point and core logic

- `setup.py`: Package configuration with bilingual metadata

- `docs/PROJECT_REQUIREMENTS.md`: Complete roadmap and technical requirements

- `tools/fix_md_blanklines.ps1`: Critical formatting automation script

- `.github/workflows/markdownlint.yml`: CI pipeline with PowerShell formatting check

When contributing, always check existing Japanese documentation first, maintain bilingual approach for user-facing content, and use the available markdown formatting task for consistency.

