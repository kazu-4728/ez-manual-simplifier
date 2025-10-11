"""
Tests for the document converter module.
"""

import sys
import os
import pytest
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

try:
    from converter import DocumentConverter, convert_to_markdown
    MARKITDOWN_AVAILABLE = True
except ImportError:
    MARKITDOWN_AVAILABLE = False


@pytest.mark.skipif(not MARKITDOWN_AVAILABLE, reason="markitdown not installed")
class TestDocumentConverter:
    """Test cases for DocumentConverter class."""
    
    def test_converter_initialization(self):
        """Test that converter can be initialized."""
        converter = DocumentConverter()
        assert converter is not None
        assert hasattr(converter, 'converter')
    
    def test_convert_nonexistent_file(self):
        """Test that converting a non-existent file raises FileNotFoundError."""
        converter = DocumentConverter()
        
        with pytest.raises(FileNotFoundError):
            converter.convert_to_markdown("nonexistent_file.pdf")
    
    def test_convert_text_file(self, tmp_path):
        """Test converting a simple text file."""
        converter = DocumentConverter()
        
        # Create a temporary text file
        test_file = tmp_path / "test.txt"
        test_content = "# Test Header\n\nThis is a test document."
        test_file.write_text(test_content, encoding='utf-8')
        
        # Convert to markdown
        result = converter.convert_to_markdown(test_file)
        
        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_convert_invalid_url(self):
        """Test that converting an invalid URL raises ValueError."""
        converter = DocumentConverter()
        
        with pytest.raises(ValueError):
            converter.convert_url_to_markdown("not-a-url")
    
    def test_convenience_function(self, tmp_path):
        """Test the convenience function convert_to_markdown."""
        # Create a temporary text file
        test_file = tmp_path / "test.txt"
        test_file.write_text("Test content", encoding='utf-8')
        
        # Use convenience function
        result = convert_to_markdown(test_file)
        
        assert result is not None
        assert isinstance(result, str)


def test_import_error_handling():
    """Test that appropriate error is raised when markitdown is not available."""
    if not MARKITDOWN_AVAILABLE:
        with pytest.raises(ImportError):
            DocumentConverter()
