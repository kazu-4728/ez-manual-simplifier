# Test Instructions

This directory contains test files for the EZ Manual Simplifier project.

## Test Structure

- Tests use manual path insertion: `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))`
- All test files follow the `test_*.py` naming convention
- Use pytest framework for running tests

## Key Test Files

- `test_simplifier.py`: Tests for core simplification functionality
- `test_converter.py`: Tests for document format conversion
- `test_simplifier_integration.py`: Integration tests

## Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python tests/test_simplifier.py
```

## Test Requirements

- Development dependencies are in `extras_require["dev"]` in setup.py
- Minimum pytest version: 7.0.0
