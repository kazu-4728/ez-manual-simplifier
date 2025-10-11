"""Tests for the command-line interface entry point."""

import sys
from pathlib import Path

import importlib

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT / "src"))


def test_main_prints_placeholder_message(capsys):
    """Ensure the main entry point emits the expected placeholder message."""
    module = importlib.import_module("simplifier")

    module.main()

    captured = capsys.readouterr()
    assert "EZ Manual Simplifier - Coming Soon!" in captured.out
