"""
Unit tests for the simplifier module.
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from simplifier import simplify_text


def test_simplify_text_basic():
    """Test basic text simplification."""
    text = "This is a test text."
    result = simplify_text(text)
    assert isinstance(result, str)
    assert len(result) > 0


def test_simplify_text_levels():
    """Test different simplification levels."""
    text = "This is a test text."
    
    # Test valid levels
    for level in ["low", "medium", "high"]:
        result = simplify_text(text, level=level)
        assert isinstance(result, str)


def test_simplify_text_invalid_level():
    """Test that invalid level raises ValueError."""
    text = "This is a test text."
    
    try:
        simplify_text(text, level="invalid")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Invalid simplification level" in str(e)


if __name__ == "__main__":
    print("Running tests...")
    test_simplify_text_basic()
    print("✓ test_simplify_text_basic passed")
    
    test_simplify_text_levels()
    print("✓ test_simplify_text_levels passed")
    
    test_simplify_text_invalid_level()
    print("✓ test_simplify_text_invalid_level passed")
    
    print("\nAll tests passed!")
