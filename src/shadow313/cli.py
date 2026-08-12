"""CLI entry point for Shadow313."""

import argparse
import sys

from shadow313 import __version__
from shadow313.core.kernel import Kernel


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="shadow313",
        description="Shadow313 v2 — Local-First AI-Powered Security Intelligence CLI",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"shadow313 {__version__}",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output",
    )
    parser.add_argument(
        "--no-ai",
        action="store_true",
        help="Disable AI features",
    )
    parser.add_argument(
        "--lab-mode",
        action="store_true",
        help="Enable lab-mode for exploitation features (requires scope.yaml)",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Recon command
    recon_parser = subparsers.add_parser("recon", help="Reconnaissance module")
    recon_parser.add_argument("--target", "-t", required=True, help="Target host/domain")
    recon_parser.add_argument(
        "--mode",
        choices=["quick", "full", "passive"],
        default="quick",
        help="Recon mode",
    )

    # Vuln command
    vuln_parser = subparsers.add_parser("vuln", help="Vulnerability analysis module")
    vuln_parser.add_argument("--target", "-t", required=True, help="Target host/domain")

    # Network command
    net_parser = subparsers.add_parser("network", help="Network intelligence module")
    net_parser.add_argument("--interface", "-i", help="Network interface")
    net_parser.add_argument(
        "--mode",
        choices=["monitor", "analyze", "forensics"],
        default="monitor",
        help="Network mode",
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    # Initialize kernel
    kernel = Kernel(verbose=args.verbose, no_ai=args.no_ai, lab_mode=args.lab_mode)

    # Dispatch command
    try:
        if args.command == "recon":
            result = kernel.dispatch("recon", target=args.target, mode=args.mode)
        elif args.command == "vuln":
            result = kernel.dispatch("vuln", target=args.target)
        elif args.command == "network":
            result = kernel.dispatch("network", interface=args.interface, mode=args.mode)
        else:
            parser.print_help()
            sys.exit(1)

        # Output result
        kernel.output.print_result(result)

    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(130)
    except Exception as e:
        if args.verbose:
            raise
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
