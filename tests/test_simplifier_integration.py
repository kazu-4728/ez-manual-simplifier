"""
Integration tests for simplifier module with converter.
"""

import sys
import os
import pytest
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from simplifier import simplify_text, simplify_file

try:
    from converter import DocumentConverter
    MARKITDOWN_AVAILABLE = True
except ImportError:
    MARKITDOWN_AVAILABLE = False


class TestSimplifyText:
    """Test cases for simplify_text function."""
    
    def test_simplify_text_basic(self):
        """Test basic text simplification."""
        text = "This is a test document."
        result = simplify_text(text, level="medium")
        
        assert result is not None
        assert isinstance(result, str)
        # Currently returns the same text (placeholder implementation)
        assert result == text
    
    def test_simplify_text_levels(self):
        """Test all simplification levels."""
        text = "Test content"
        
        for level in ["low", "medium", "high"]:
            result = simplify_text(text, level=level)
            assert result is not None
    
    def test_simplify_text_invalid_level(self):
        """Test that invalid level raises ValueError."""
        with pytest.raises(ValueError):
            simplify_text("Test", level="invalid")


@pytest.mark.skipif(not MARKITDOWN_AVAILABLE, reason="markitdown not installed")
class TestSimplifyFile:
    """Test cases for simplify_file function."""
    
    def test_simplify_file_basic(self, tmp_path):
        """Test basic file simplification."""
        # Create a test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("# Test Document\n\nThis is test content.", encoding='utf-8')
        
        # Simplify the file
        result = simplify_file(test_file, level="medium")
        
        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_simplify_file_with_output(self, tmp_path):
        """Test file simplification with output file."""
        # Create a test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("Test content", encoding='utf-8')
        
        # Output file
        output_file = tmp_path / "output.md"
        
        # Simplify and save
        result = simplify_file(test_file, level="low", output_path=output_file)
        
        assert result is not None
        assert output_file.exists()
        
        # Check output file content
        saved_content = output_file.read_text(encoding='utf-8')
        assert saved_content == result
    
    def test_simplify_nonexistent_file(self):
        """Test that simplifying a non-existent file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            simplify_file("nonexistent.pdf")
    
    def test_simplify_file_invalid_level(self, tmp_path):
        """Test that invalid level raises ValueError."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("Test", encoding='utf-8')
        
        with pytest.raises(ValueError):
            simplify_file(test_file, level="invalid")


def test_simplify_file_without_markitdown():
    """Test that simplify_file raises ImportError when markitdown is not available."""
    if not MARKITDOWN_AVAILABLE:
        with pytest.raises(ImportError):
            simplify_file("test.pdf")
