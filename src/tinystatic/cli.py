import argparse
from pathlib import Path

from tinystatic.commands.build import build
from tinystatic.commands.init import init


def tinystatic():
    commands = {"build": build, "init": init}

    parser = argparse.ArgumentParser(
        description="Generate quick static websites from markdown."
    )
    subparsers = parser.add_subparsers()
    # Build command
    build_subparser = subparsers.add_parser("build")
    build_subparser.set_defaults(command="build")
    build_subparser.add_argument(
        "--cwd",
        type=Path,
        default=str(Path.cwd()),
        help="Project root (current directory if not specified)",
    )

    # Init command
    init_subparser = subparsers.add_parser("init")
    init_subparser.set_defaults(command="init")

    args = parser.parse_args()

    commands[args.command](args)
