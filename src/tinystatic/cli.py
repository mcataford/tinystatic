import argparse
from pathlib import Path

from tinystatic.commands.build import build


def tinystatic():
    commands = {"build": build}

    parser = argparse.ArgumentParser(
        description="Generate quick static websites from markdown."
    )
    parser.add_argument("command", type=str, choices=list(commands.keys()))
    parser.add_argument("--cwd", type=str, default=str(Path.cwd()))

    args = parser.parse_args()

    commands[args.command](args)
