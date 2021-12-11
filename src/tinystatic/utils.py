from pathlib import Path
from typing import Generator


def get_content_item_paths(content_path: Path) -> Generator[Path, None, None]:
    for content_item_path in content_path.iterdir():
        if content_item_path.suffix != ".md":
            continue

        yield content_item_path
