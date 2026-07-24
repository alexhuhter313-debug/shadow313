"""Core kernel — command bus and module orchestration."""

from typing import Any, Callable, Dict


class Kernel:
    """Central orchestration layer for Shadow313.

    The Kernel is a singleton per process that manages:
    - Command bus routing
    - Module registration and auto-loading
    - Session state
    - AI engine interface
    - Output formatting
    """

    def __init__(
        self,
        verbose: bool = False,
        no_ai: bool = False,
        lab_mode: bool = False,
    ):
        """Initialize the kernel.

        Args:
            verbose: Enable verbose output with full tracebacks
            no_ai: Disable AI features entirely
            lab_mode: Enable lab-mode for exploitation features
        """
        self.verbose = verbose
        self.no_ai = no_ai
        self.lab_mode = lab_mode

        self._handlers: Dict[str, Callable] = {}
        self._modules: Dict[str, Any] = {}

        # TODO: Initialize config, session, AI engine, output
        # self.config = Config()
        # self.session = Session()
        # self.ai_engine = AIEngine(disabled=no_ai)
        # self.output = Output(verbose=verbose)

        # Auto-load modules
        self._autoload_modules()

    def register(self, namespace: str, handler: Callable) -> None:
        """Register a command handler for a namespace.

        Args:
            namespace: Command namespace (e.g., 'recon', 'vuln')
            handler: Callable that handles the command
        """
        self._handlers[namespace] = handler

    def dispatch(self, namespace: str, **kwargs) -> Any:
        """Dispatch a command to the registered handler.

        Args:
            namespace: Command namespace
            **kwargs: Arguments to pass to the handler

        Returns:
            Result from the handler

        Raises:
            ValueError: If no handler is registered for the namespace
        """
        if namespace not in self._handlers:
            raise ValueError(f"Unknown command: {namespace}")

        handler = self._handlers[namespace]
        return handler(**kwargs)

    def _autoload_modules(self) -> None:
        """Auto-load all built-in v1 and v2 modules.

        Modules are imported and registered automatically, requiring no
        manual registration in user code.
        """
        # TODO: Import and register all 28 modules
        # from shadow313.modules.recon import ReconModule
        # from shadow313.modules.vuln import VulnModule
        # from shadow313.modules.network import NetworkModule
        # ...

        # Example:
        # self.register("recon", ReconModule(self).run)
        # self.register("vuln", VulnModule(self).run)
        # self.register("network", NetworkModule(self).run)

        pass
