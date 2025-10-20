# Source Code Instructions

This directory contains the core Python source code for the EZ Manual Simplifier project.

## Key Files

- `simplifier.py`: Main simplification logic with `simplify_text()` function
- `converter.py`: Document format conversion using markitdown library
- `__init__.py`: Package initialization

## Development Guidelines

- All functions must have type hints
- Use English for code identifiers, docstrings, and comments
- Follow PEP 8 style guidelines
- Validate input parameters (e.g., simplification level must be in ["low", "medium", "high"])
- Error handling using ValueError for invalid inputs

## Testing

- Tests are located in `/tests/` directory
- Use manual path insertion for imports in tests
- Run tests with: `python -m pytest`
