"""
Document converter module using MarkItDown.

This module provides functionality to convert various document formats
(PDF, DOCX, PPTX, XLSX, images, etc.) to Markdown format.
"""

from pathlib import Path
from typing import Union

try:
    from markitdown import MarkItDown
    MARKITDOWN_AVAILABLE = True
except ImportError:
    MARKITDOWN_AVAILABLE = False


class DocumentConverter:
    """
    Convert various document formats to Markdown using MarkItDown.
    
    Supported formats:
    - PDF (.pdf)
    - Microsoft Word (.docx, .doc)
    - Microsoft PowerPoint (.pptx, .ppt)
    - Microsoft Excel (.xlsx, .xls)
    - Images (.jpg, .jpeg, .png)
    - HTML (.html, .htm)
    - Text (.txt, .md)
    - Audio files (with transcription)
    """
    
    def __init__(self):
        """Initialize the converter."""
        if not MARKITDOWN_AVAILABLE:
            raise ImportError(
                "markitdown is not installed. "
                "Please install it with: pip install markitdown[all]"
            )
        self.converter = MarkItDown()
    
    def convert_to_markdown(self, file_path: Union[str, Path]) -> str:
        """
        Convert a file to Markdown format.
        
        Args:
            file_path: Path to the file to convert
        
        Returns:
            Markdown-formatted text content
        
        Raises:
            FileNotFoundError: If the file does not exist
            ValueError: If the file format is not supported
            Exception: If conversion fails
        
        Example:
            >>> converter = DocumentConverter()
            >>> markdown = converter.convert_to_markdown("manual.pdf")
            >>> print(markdown)
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        try:
            result = self.converter.convert(str(file_path))
            return result.text_content
        except Exception as e:
            raise Exception(f"Failed to convert {file_path}: {str(e)}")
    
    def convert_url_to_markdown(self, url: str) -> str:
        """
        Convert a URL to Markdown format.
        
        Args:
            url: URL to convert (supports YouTube, web pages, etc.)
        
        Returns:
            Markdown-formatted text content
        
        Raises:
            ValueError: If the URL is invalid
            Exception: If conversion fails
        
        Example:
            >>> converter = DocumentConverter()
            >>> markdown = converter.convert_url_to_markdown("https://example.com")
        """
        if not url.startswith(('http://', 'https://')):
            raise ValueError(f"Invalid URL: {url}")
        
        try:
            result = self.converter.convert(url)
            return result.text_content
        except Exception as e:
            raise Exception(f"Failed to convert URL {url}: {str(e)}")


def convert_to_markdown(file_path: Union[str, Path]) -> str:
    """
    Convenience function to convert a file to Markdown.
    
    Args:
        file_path: Path to the file to convert
    
    Returns:
        Markdown-formatted text content
    
    Example:
        >>> from converter import convert_to_markdown
        >>> markdown = convert_to_markdown("manual.pdf")
    """
    converter = DocumentConverter()
    return converter.convert_to_markdown(file_path)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python converter.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        converter = DocumentConverter()
        markdown = converter.convert_to_markdown(file_path)
        print(markdown)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
