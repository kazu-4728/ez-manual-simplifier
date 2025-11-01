"""Document converter module using markitdown library.

This module provides functionality to convert various document formats
(PDF, DOCX, PPTX, XLSX, images, HTML, audio) to Markdown format.
"""

import sys
from pathlib import Path
from typing import Optional


class DocumentConverter:
    """Convert various document formats to Markdown using markitdown.
    
    Supports: PDF, DOCX, PPTX, XLSX, images, HTML, audio files
    """
    
    def __init__(self):
        """Initialize the converter.
        
        Raises:
            ImportError: If markitdown library is not installed
        """
        try:
            from markitdown import MarkItDown
            self._converter = MarkItDown()
        except ImportError:
            raise ImportError(
                "markitdown library is required. Install it with: pip install markitdown[all]"
            )
    
    def convert_to_markdown(self, filepath: str) -> str:
        """Convert a file to Markdown format.
        
        Args:
            filepath: Path to the file to convert
            
        Returns:
            Markdown-formatted text
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the file format is not supported
            Exception: For other conversion errors
        """
        path = Path(filepath)
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        
        try:
            result = self._converter.convert(str(path))
            return result.text_content
        except Exception as e:
            raise Exception(f"Failed to convert file: {e}")
    
    def convert_url_to_markdown(self, url: str) -> str:
        """Convert a URL to Markdown format.
        
        Args:
            url: URL to convert
            
        Returns:
            Markdown-formatted text
            
        Raises:
            ValueError: If the URL is invalid
            Exception: For conversion errors
        """
        if not url.startswith(("http://", "https://")):
            raise ValueError(f"Invalid URL format: {url}")
        
        try:
            result = self._converter.convert(url)
            return result.text_content
        except Exception as e:
            raise Exception(f"Failed to convert URL: {e}")


def main():
    """Command-line interface for the converter."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Document Converter - Convert files to Markdown"
    )
    
    parser.add_argument(
        "input",
        help="File path or URL to convert"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Output file path (optional, prints to stdout if not specified)"
    )
    
    args = parser.parse_args()
    
    try:
        converter = DocumentConverter()
        
        # Determine if input is URL or file
        if args.input.startswith(("http://", "https://")):
            result = converter.convert_url_to_markdown(args.input)
        else:
            result = converter.convert_to_markdown(args.input)
        
        # Output result
        if args.output:
            Path(args.output).write_text(result, encoding="utf-8")
            print(f"Converted to: {args.output}")
        else:
            print(result)
            
    except (FileNotFoundError, ValueError, ImportError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
