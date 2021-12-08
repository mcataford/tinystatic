import argparse
from pathlib import Path

from tinystatic.core.load_configuration import load_configuration
from tinystatic.commands import build


def tinystatic():
    commands = {"build": build}

    parser = argparse.ArgumentParser(
        description="Generate quick static websites from markdown."
    )
    parser.add_argument("command", type=str, choices=list(commands.keys()))
    parser.add_argument("--cwd", type=str, default=str(Path.cwd()))

    args = parser.parse_args()

    config = load_configuration(project_root=args.cwd)

    commands[args.command](cwd=args.cwd, config=config)
