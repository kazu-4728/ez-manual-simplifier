"""Integration tests for the simplifier module."""

import pytest
from pathlib import Path
import tempfile


# Import with path handling for tests
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from simplifier import simplify_text, simplify_file


class TestSimplifyText:
    """Test cases for simplify_text function."""
    
    def test_basic_simplification(self):
        """Test basic text simplification."""
        text = "This is a complex technical document."
        result = simplify_text(text)
        assert result is not None
        assert len(result) > 0
    
    def test_simplification_levels(self):
        """Test all three simplification levels."""
        text = "The implementation leverages sophisticated algorithms."
        
        for level in ["low", "medium", "high"]:
            result = simplify_text(text, level=level)
            assert result is not None
            assert level in result
    
    def test_invalid_level(self):
        """Test that invalid levels raise ValueError."""
        text = "Test text"
        
        with pytest.raises(ValueError) as exc_info:
            simplify_text(text, level="invalid")
        
        assert "Invalid simplification level" in str(exc_info.value)
        assert "invalid" in str(exc_info.value)
    
    def test_level_validation_message(self):
        """Test that error message includes valid options."""
        text = "Test text"
        
        with pytest.raises(ValueError) as exc_info:
            simplify_text(text, level="extreme")
        
        error_msg = str(exc_info.value)
        assert "low" in error_msg or "medium" in error_msg or "high" in error_msg


class TestSimplifyFile:
    """Test cases for simplify_file function."""
    
    def test_file_not_found(self):
        """Test that FileNotFoundError is raised for non-existent files."""
        with pytest.raises(FileNotFoundError):
            simplify_file("nonexistent_file.txt")
    
    def test_simplify_file_basic(self):
        """Test basic file simplification."""
        try:
            # Create a temporary text file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
                f.write("This is a test document.\nIt has multiple lines.")
                temp_path = f.name
            
            try:
                result = simplify_file(temp_path, level="medium")
                assert result is not None
                assert "test" in result or "Test" in result
            finally:
                Path(temp_path).unlink()
                
        except ImportError:
            pytest.skip("markitdown not installed")
    
    def test_simplify_file_with_output(self):
        """Test file simplification with output file."""
        try:
            # Create a temporary input file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
                f.write("Test content for output.")
                input_path = f.name
            
            # Create a temporary output path
            output_fd, output_path = tempfile.mkstemp(suffix='.md')
            os.close(output_fd)
            
            try:
                result = simplify_file(input_path, level="low", output=output_path)
                
                # Check that output file was created
                assert Path(output_path).exists()
                
                # Check that output file has content
                output_content = Path(output_path).read_text(encoding="utf-8")
                assert len(output_content) > 0
                assert "Test" in output_content or "test" in output_content
                
                # Check that function still returns the result
                assert result is not None
                
            finally:
                Path(input_path).unlink()
                if Path(output_path).exists():
                    Path(output_path).unlink()
                    
        except ImportError:
            pytest.skip("markitdown not installed")
    
    def test_simplify_file_invalid_level(self):
        """Test that invalid level raises ValueError even with valid file."""
        try:
            # Create a temporary text file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
                f.write("Test content")
                temp_path = f.name
            
            try:
                with pytest.raises(ValueError):
                    simplify_file(temp_path, level="invalid_level")
            finally:
                Path(temp_path).unlink()
                
        except ImportError:
            pytest.skip("markitdown not installed")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
