import argparse
from pathlib import Path

from tinystatic.commands.generate import generate

def tinystatic():
    parser = argparse.ArgumentParser(description="Generate quick static websites from markdown.")
    parser.add_argument('command', type=str)
    parser.add_argument('--cwd', type=str, default=str(Path.cwd()))

    args = parser.parse_args()

    if args.command == 'generate':
        generate()

    
