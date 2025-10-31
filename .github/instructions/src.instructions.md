# Source Code Instructions

The `src/` directory was cleared during the repository reset. Recreate the package only when new
functionality is ready.

## Expected Structure

- `src/`: Python package root for the manual simplification engine
- `src/__init__.py`: Exposes public entry points
- Additional modules should be introduced per feature (e.g., `simplifier.py`, `converter.py`)

## Development Guidelines

- Use Python 3.11+ type hints and dataclasses where appropriate
- Keep business logic in pure functions or small classes to help Copilot reason about them
- Write docstrings in English; include Japanese comments only when necessary for stakeholders
- Validate all external inputs and raise descriptive `ValueError` exceptions for invalid states

## Testing Hooks

- Mirror each new module with targeted tests under `tests/`
- Provide minimal reproduction snippets in docstrings to improve Copilot completions
- Run `python -m pytest` locally before submitting pull requests
