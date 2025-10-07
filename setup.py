"""
Setup configuration for EZ Manual Simplifier.
"""

from setuptools import setup, find_packages
import os


def read_file(filename):
    """Read file contents."""
    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as f:
        return f.read()


setup(
    name="ez-manual-simplifier",
    version="0.1.0",
    author="kazu-4728",
    author_email="",
    description="A tool to simplify complex manuals and documentation",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/kazu-4728/ez-manual-simplifier",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Core dependencies will be added here
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ez-manual-simplifier=simplifier:main",
        ],
    },
)
