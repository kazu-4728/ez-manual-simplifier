"""
Main simplifier module for EZ Manual Simplifier.

This module contains the core functionality for simplifying manual text
using AI (Gemini API) and document conversion capabilities.
"""

from pathlib import Path
from typing import Union, Optional

try:
    from converter import DocumentConverter
    CONVERTER_AVAILABLE = True
except ImportError:
    try:
        from .converter import DocumentConverter
        CONVERTER_AVAILABLE = True
    except ImportError:
        CONVERTER_AVAILABLE = False

# Gemini API will be integrated here
# import google.generativeai as genai


def simplify_text(text: str, level: str = "medium") -> str:
    """
    Simplify the given text.
    
    Args:
        text: The text to simplify
        level: Simplification level ("low", "medium", "high")
    
    Returns:
        Simplified text
    
    Raises:
        ValueError: If level is not valid
    """
    if level not in ["low", "medium", "high"]:
        raise ValueError(f"Invalid simplification level: {level}")
    
    # Placeholder implementation
    # Actual simplification logic will be implemented here
    return text


def simplify_file(
    file_path: Union[str, Path],
    level: str = "medium",
    output_path: Optional[Union[str, Path]] = None
) -> str:
    """
    Simplify a document file (PDF, DOCX, etc.).
    
    This function provides a complete pipeline:
    1. Convert the file to Markdown using MarkItDown
    2. Simplify the Markdown using Gemini API
    3. Optionally save to a file
    
    Args:
        file_path: Path to the document file
        level: Simplification level ("low", "medium", "high")
        output_path: Optional path to save the simplified content
    
    Returns:
        Simplified Markdown text
    
    Raises:
        ValueError: If level is not valid
        FileNotFoundError: If the file does not exist
        ImportError: If markitdown is not installed
    
    Example:
        >>> simplified = simplify_file("manual.pdf", level="high")
        >>> simplified = simplify_file("guide.docx", level="low", output_path="simple_guide.md")
    """
    if not CONVERTER_AVAILABLE:
        raise ImportError(
            "Document conversion requires markitdown. "
            "Please install it with: pip install markitdown[all]"
        )
    
    # Step 1: Convert to Markdown
    converter = DocumentConverter()
    markdown_text = converter.convert_to_markdown(file_path)
    
    # Step 2: Simplify the text
    simplified_text = simplify_text(markdown_text, level=level)
    
    # Step 3: Save if output path is provided
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(simplified_text, encoding='utf-8')
    
    return simplified_text


def main():
    """
    Main entry point for the application.
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description="EZ Manual Simplifier - Simplify technical documentation"
    )
    parser.add_argument(
        "input",
        help="Input file path (PDF, DOCX, PPTX, etc.) or text"
    )
    parser.add_argument(
        "-l", "--level",
        choices=["low", "medium", "high"],
        default="medium",
        help="Simplification level (default: medium)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (optional)"
    )
    parser.add_argument(
        "--text",
        action="store_true",
        help="Treat input as raw text instead of file path"
    )
    
    args = parser.parse_args()
    
    try:
        if args.text:
            # Simplify raw text
            result = simplify_text(args.input, level=args.level)
        else:
            # Simplify file
            result = simplify_file(
                args.input,
                level=args.level,
                output_path=args.output
            )
        
        if not args.output:
            print(result)
        else:
            print(f"Simplified content saved to: {args.output}")
    
    except Exception as e:
        print(f"Error: {e}", file=__import__('sys').stderr)
        __import__('sys').exit(1)


if __name__ == "__main__":
    main()
