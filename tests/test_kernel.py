"""Tests for the core kernel."""

import pytest

from shadow313.core.kernel import Kernel


class TestKernel:
    """Test suite for Kernel class."""

    def test_kernel_init(self):
        """Test kernel initialization."""
        kernel = Kernel()
        assert kernel.verbose is False
        assert kernel.no_ai is False
        assert kernel.lab_mode is False

    def test_kernel_init_verbose(self):
        """Test kernel initialization with verbose mode."""
        kernel = Kernel(verbose=True)
        assert kernel.verbose is True

    def test_kernel_init_no_ai(self):
        """Test kernel initialization with AI disabled."""
        kernel = Kernel(no_ai=True)
        assert kernel.no_ai is True

    def test_kernel_init_lab_mode(self):
        """Test kernel initialization with lab mode."""
        kernel = Kernel(lab_mode=True)
        assert kernel.lab_mode is True

    def test_register_handler(self):
        """Test registering a command handler."""
        kernel = Kernel()

        def dummy_handler(**kwargs):
            return "test"

        kernel.register("test", dummy_handler)
        assert "test" in kernel._handlers

    def test_dispatch_command(self):
        """Test dispatching a command."""
        kernel = Kernel()

        def dummy_handler(**kwargs):
            return {"result": "success", "target": kwargs.get("target")}

        kernel.register("test", dummy_handler)
        result = kernel.dispatch("test", target="example.com")

        assert result["result"] == "success"
        assert result["target"] == "example.com"

    def test_dispatch_unknown_command(self):
        """Test dispatching an unknown command raises ValueError."""
        kernel = Kernel()

        with pytest.raises(ValueError, match="Unknown command: unknown"):
            kernel.dispatch("unknown")
