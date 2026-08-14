"""Tests for the CLI entry point."""

import pytest
from shadow313 import __version__, main
from shadow313.core.kernel import Kernel


def test_version():
    """Test that version is a string."""
    assert isinstance(__version__, str)
    assert __version__ == "2.0.0"


def test_kernel_creation():
    """Test Kernel initialization."""
    kernel = Kernel()
    assert kernel.verbose is False
    assert kernel.no_ai is False
    assert kernel.lab_mode is False


def test_kernel_creation_with_args():
    """Test Kernel with custom args."""
    kernel = Kernel(verbose=True, no_ai=True, lab_mode=True)
    assert kernel.verbose is True
    assert kernel.no_ai is True
    assert kernel.lab_mode is True


def test_kernel_dispatch_recon():
    """Test recon dispatch."""
    kernel = Kernel()
    result = kernel.dispatch("recon", target="example.com", mode="quick")
    assert result["status"] == "success"
    assert result["command"] == "recon"
    assert result["target"] == "example.com"


def test_kernel_dispatch_vuln():
    """Test vuln dispatch."""
    kernel = Kernel()
    result = kernel.dispatch("vuln", target="example.com")
    assert result["status"] == "success"
    assert result["command"] == "vuln"


def test_kernel_dispatch_network():
    """Test network dispatch."""
    kernel = Kernel()
    result = kernel.dispatch("network", interface="eth0", mode="monitor")
    assert result["status"] == "success"
    assert result["command"] == "network"
    assert result["interface"] == "eth0"


def test_kernel_dispatch_unknown():
    """Test unknown command."""
    kernel = Kernel()
    result = kernel.dispatch("unknown")
    assert result["status"] == "error"


def test_output_print_result():
    """Test output formatting."""
    output = Kernel().output
    # Just ensure it doesn't crash
    output.print_result({"key": "value"})
    output.print_result("plain string")
