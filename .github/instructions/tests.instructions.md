# Test Instructions

The `tests/` directory will be reintroduced alongside new source modules. Use this guide when rebuilding
the test suite.

## Test Layout

- Place unit tests under `tests/` mirroring the package structure in `src/`
- Name files using `test_*.py` so pytest can discover them automatically
- Keep fixtures small and reuseable; prefer factory functions over global state

## Running Tests

```bash
# Run the entire suite
python -m pytest

# Run a specific file
python -m pytest tests/test_simplifier.py
```

## Quality Expectations

- Aim for high-coverage tests on the text simplification logic
- Include regression tests for previously fixed issues when restoring functionality
- Document tricky behaviours in test docstrings to assist Copilot's suggestions
