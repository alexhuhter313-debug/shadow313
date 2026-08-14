"""Shadow313 v2 — Local-First AI-Powered Security Intelligence CLI."""

__version__ = "2.0.0"
__author__ = "mohamad"

from shadow313.core.kernel import Kernel
from shadow313.cli import main

__all__ = ["Kernel", "main", "__version__"]
