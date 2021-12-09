import argparse
from pathlib import Path

from tinystatic.core.load_configuration import load_configuration
from tinystatic.commands import COMMAND_HANDLERS


def tinystatic():
    """
    Entry point for all flows. Loads the configuration file and
    routes the CLI call to the right place based on parsed arguments
    and calls the command-specific handler.
    """

    parser = argparse.ArgumentParser(
        description="Generate quick static websites from markdown.", add_help=False
    )
    parser.add_argument(
        "--cwd",
        type=Path,
        default=str(Path.cwd()),
        help="Project root (current directory if not specified)",
    )
    subparsers = parser.add_subparsers()

    # Build
    build_subparser = subparsers.add_parser("build", parents=[parser])
    build_subparser.set_defaults(command="build")

    # Init command
    init_subparser = subparsers.add_parser("init", parents=[parser])
    init_subparser.set_defaults(command="init")

    args = parser.parse_args()

    config = None
    if args.command != "init":
        config = load_configuration(project_root=args.cwd)

    COMMAND_HANDLERS[args.command](cwd=args.cwd, config=config)
