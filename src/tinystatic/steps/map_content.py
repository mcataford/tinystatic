from pathlib import Path
from typing import List

import frontmatter

from tinystatic.utils import get_content_item_paths

STEP_NAME = "Map content"


def get_metadata(item_path: Path, included_keys: List[str]) -> str:
    full_text = item_path.read_text()
    parsed_frontmatter, _ = frontmatter.parse(full_text)

    return {
        included_key: parsed_frontmatter[included_key]
        for included_key in included_keys
        if included_key in included_keys
    }


def run(stash):
    """
    Discovers all available content and creates a map of content item metadata.
    The metadata includes fields defined in the configuration under steps.map_content:include.
    """

    project_root = stash["cwd"]
    content_path = stash["config"]["paths"]["content_path"]

    full_content_path = Path(project_root, content_path)
    included_metadata = (
        stash["config"].get("steps", {}).get("map_content", {}).get("include")
    )

    if not included_metadata:
        return

    content_map = {}

    for item_path in get_content_item_paths(full_content_path):
        content_map[str(item_path.relative_to(full_content_path))] = get_metadata(
            item_path, included_metadata
        )

    stash["content_map"] = content_map
