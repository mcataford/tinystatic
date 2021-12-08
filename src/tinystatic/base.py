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
        description="Generate quick static websites from markdown."
    )
    parser.add_argument("command", type=str, choices=list(COMMAND_HANDLERS.keys()))
    parser.add_argument("--cwd", type=str, default=str(Path.cwd()))

    args = parser.parse_args()

    config = load_configuration(project_root=args.cwd)

    COMMAND_HANDLERS[args.command](cwd=args.cwd, config=config)
