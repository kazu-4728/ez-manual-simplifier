"""Text simplification module for EZ Manual Simplifier.

This module provides functionality to simplify complex text using AI.
Currently supports 3 levels of simplification: low, medium, high.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional


def simplify_text(text: str, level: str = "medium") -> str:
    """Simplify text to make it easier to understand.
    
    Args:
        text: The text to simplify
        level: Simplification level - "low", "medium", or "high"
               low: Elementary school level
               medium: General readability
               high: Keep technical terms but add explanations
    
    Returns:
        Simplified text
        
    Raises:
        ValueError: If level is not one of ["low", "medium", "high"]
    
    Example:
        >>> text = "The implementation leverages sophisticated algorithms."
        >>> simplified = simplify_text(text, level="low")
        >>> print(simplified)  # "The program uses smart methods."
    """
    if level not in ["low", "medium", "high"]:
        raise ValueError(f"Invalid simplification level: {level}. Must be one of: low, medium, high")
    
    # TODO: Integrate with Gemini API for actual simplification
    # For now, return the original text with a note
    return f"[Simplified at {level} level]\n{text}"


def simplify_file(filepath: str, level: str = "medium", output: Optional[str] = None) -> str:
    """Simplify a document file.
    
    This function implements the complete pipeline:
    1. Convert file to Markdown (using converter module)
    2. Simplify the text
    3. Optionally save to output file
    
    Args:
        filepath: Path to the file to simplify
        level: Simplification level - "low", "medium", or "high"
        output: Optional output file path. If None, returns the result as string
        
    Returns:
        Simplified text
        
    Raises:
        FileNotFoundError: If the input file doesn't exist
        ValueError: If level is invalid
    """
    from .converter import DocumentConverter
    
    # Check if file exists
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    # Convert to markdown
    converter = DocumentConverter()
    markdown_text = converter.convert_to_markdown(filepath)
    
    # Simplify the text
    simplified = simplify_text(markdown_text, level=level)
    
    # Save to file if output path provided
    if output:
        Path(output).write_text(simplified, encoding="utf-8")
    
    return simplified


def main():
    """Command-line interface for the simplifier."""
    parser = argparse.ArgumentParser(
        description="EZ Manual Simplifier - Make complex documents easy to understand"
    )
    
    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "file",
        nargs="?",
        help="Path to the file to simplify"
    )
    input_group.add_argument(
        "--text",
        help="Direct text input to simplify"
    )
    
    # Simplification options
    parser.add_argument(
        "-l", "--level",
        choices=["low", "medium", "high"],
        default="medium",
        help="Simplification level (default: medium)"
    )
    
    # Output options
    parser.add_argument(
        "-o", "--output",
        help="Output file path (optional)"
    )
    
    args = parser.parse_args()
    
    try:
        if args.text:
            # Direct text input mode
            result = simplify_text(args.text, level=args.level)
        else:
            # File input mode
            result = simplify_file(args.file, level=args.level, output=args.output)
        
        # Print to stdout if no output file specified
        if not args.output:
            print(result)
            
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
