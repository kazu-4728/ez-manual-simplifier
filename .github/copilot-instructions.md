# GitHub Copilot Instructions for EZ Manual Simplifier

## Project Overview

This is a Python-based manual simplification tool in early development (v0.1.0) designed to transform complex technical
documentation into accessible formats using AI. The project follows a three-phase roadmap: Phase 1 (current) focuses on
core simplification via Gemini API, Phase 2 adds agent coordination, and Phase 3 targets full automation.

## Architecture

- **Core Module**: `src/simplifier.py` contains the main `simplify_text()` function with validation for levels
  ["low", "medium", "high"]

- **Converter Module**: `src/converter.py` provides document conversion using markitdown library

- **Planned Structure**: Future expansion includes `api/`, `web/`, and `utils/` subdirectories under `src/`

- **Test Strategy**: Tests use manual path insertion for imports:
  `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))`

- **Agent Orchestration**: Multi-agent coordination system with clear entry points and task assignment
  See `docs/AGENT_ORCHESTRATION.md` for details

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

- **Communication with Owner**: When reviewing code, providing explanations, or responding to the repository owner (@kazu-4728), always communicate in Japanese (日本語). This includes PR comments, code review feedback, and responses to questions.

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

- **AI Integration**: Gemini API for text simplification (cost-optimized, context-aware)

- **Research Function**: MCP/API integration for research-based manual creation

- **Web Interface**: Flask/FastAPI backend with vanilla JavaScript frontend planned

- **Deployment**: GitHub Pages + Cloudflare Pages for hosting

- **Agent System**: Multi-agent orchestration with GitHub Actions integration

## Agent Orchestration System

This project uses a multi-agent orchestration system. **Before starting any work**, agents must:

1. **Check Entry Points**: Review `docs/AGENT_ORCHESTRATION.md` for entry routes
2. **Review Task Management**: Check `docs/TASK_MANAGEMENT.md` and `docs/TASKS.md`
3. **Understand Constraints**: Review `docs/COST_OPTIMIZATION.md` for cost and context limits
4. **Follow Instructions**: Check `.github/instructions/orchestrator.instructions.md` if acting as Orchestrator

**Key Rules**:
- Orchestrator must delegate implementation to sub-agents, never implement directly
- Sub-agents must work within their defined scope with minimal context
- All agents must respect cost and context constraints
- Task assignment must follow the defined workflow

## Key Files for Context

### Core Implementation
- `src/simplifier.py`: Main entry point and core logic
- `src/converter.py`: Document conversion functionality

### Documentation (Must Read Before Starting Work)
- `docs/PROJECT_REQUIREMENTS.md`: Complete roadmap and technical requirements
- `docs/AGENT_ORCHESTRATION.md`: Agent orchestration system overview
- `docs/TASK_MANAGEMENT.md`: Task management system
- `docs/PROGRESS_TRACKING.md`: Progress tracking system
- `docs/COST_OPTIMIZATION.md`: Cost and context optimization guidelines
- `docs/SUB_AGENTS.md`: Sub-agent definitions
- `docs/TASKS.md`: Current task list

### Agent Instructions
- `.github/instructions/orchestrator.instructions.md`: Orchestrator agent instructions
- `.github/instructions/src.instructions.md`: Source code development guidelines
- `.github/instructions/docs.instructions.md`: Documentation guidelines
- `.github/instructions/tests.instructions.md`: Testing guidelines

### Tooling
- `tools/fix_md_blanklines.ps1`: Critical formatting automation script
- `.github/workflows/markdownlint.yml`: CI pipeline with PowerShell formatting check

## Current Project Status

- **Phase 1 Progress**: 15% (corrected from previous 80% estimate)
- **Current Focus**: Gemini API integration, cost optimization, context management
- **Agent System**: Orchestration framework established, ready for implementation

When contributing, always check existing Japanese documentation first, maintain bilingual approach for user-facing
content, use the available markdown formatting task for consistency, and **follow the agent orchestration
system** to ensure proper task assignment and context management.
