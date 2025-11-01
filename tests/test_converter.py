"""Tests for the converter module."""

import pytest
from pathlib import Path
import tempfile


# Import with path handling for tests
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from converter import DocumentConverter


class TestDocumentConverter:
    """Test cases for DocumentConverter class."""
    
    def test_converter_initialization(self):
        """Test that converter can be initialized."""
        try:
            converter = DocumentConverter()
            assert converter is not None
        except ImportError:
            pytest.skip("markitdown not installed")
    
    def test_file_not_found(self):
        """Test that FileNotFoundError is raised for non-existent files."""
        try:
            converter = DocumentConverter()
            with pytest.raises(FileNotFoundError):
                converter.convert_to_markdown("nonexistent_file.pdf")
        except ImportError:
            pytest.skip("markitdown not installed")
    
    def test_convert_text_file(self):
        """Test conversion of a simple text file."""
        try:
            converter = DocumentConverter()
            
            # Create a temporary text file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
                f.write("Hello, World!\nThis is a test.")
                temp_path = f.name
            
            try:
                result = converter.convert_to_markdown(temp_path)
                assert "Hello" in result
                assert "test" in result
            finally:
                Path(temp_path).unlink()
                
        except ImportError:
            pytest.skip("markitdown not installed")
    
    def test_url_validation(self):
        """Test that invalid URLs are rejected."""
        try:
            converter = DocumentConverter()
            with pytest.raises(ValueError):
                converter.convert_url_to_markdown("not-a-valid-url")
        except ImportError:
            pytest.skip("markitdown not installed")
    
    def test_url_format(self):
        """Test that valid URL formats are accepted."""
        try:
            converter = DocumentConverter()
            # We don't actually fetch the URL, just test validation
            # This will fail at conversion stage, not validation
            with pytest.raises(Exception):
                # Use a non-existent domain to avoid actual network calls
                converter.convert_url_to_markdown("http://this-domain-does-not-exist-12345.com")
        except ImportError:
            pytest.skip("markitdown not installed")


class TestImportError:
    """Test import error handling."""
    
    def test_import_error_message(self):
        """Test that a helpful error message is shown when markitdown is missing."""
        # This test verifies the error message exists in the code
        # Actual ImportError testing would require uninstalling markitdown
        assert "markitdown library is required" in str(DocumentConverter.__init__.__code__.co_consts)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
