from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="epistemic-canon-analyzer",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@university.edu",
    description="A framework for epistemic network analysis in bibliometric data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="[https://github.com/your-username/epistemic-canon-analyzer](https://github.com/your-username/epistemic-canon-analyzer)",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "networkx>=2.6.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scikit-learn>=0.24.0",
        "scipy>=1.7.0",
        "openpyxl>=3.0.0",
    ],
    extras_require={
        "dev": ["pytest>=6.0", "black>=21.0", "flake8>=3.9"],
        "advanced": ["powerlaw>=1.5", "python-louvain>=0.15", "plotly>=5.0.0"],
    },
)
"""
Epistemic Canon Network Analyzer
==================================
Framework for analyzing epistemic networks in bibliometric data.
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@university.edu"

# Expose the main class directly
from .core import EpistemicCanonAnalyzer

__all__ = ["EpistemicCanonAnalyzer"]
