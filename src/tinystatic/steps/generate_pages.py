"""
The generate pages step will crawl and read all the content files, and
render the templates specified by the template parameter of the file
frontmatter.

The step exposes the stash.content_map metadata extracted by the map_content
step.

Depends on:
    stash.cwd
    stash.config.path.content_path
    stash.config.steps.map_content.include
    stash.content_map

The results of this step are written to disk.
"""

from pathlib import Path

from markdown2 import Markdown
import frontmatter
from jinja2 import Environment, FileSystemLoader

from tinystatic.utils import get_content_item_paths
from tinystatic.core.logger import get_logger

STEP_NAME = "GeneratePagesStep"
logger = get_logger(STEP_NAME)


def run(stash):
    """
    Generate pages based on markdown content.
    """

    # Extract data from stash.
    config = stash["config"]
    project_root = stash["cwd"]

    content_path = Path(project_root, config["paths"]["content_path"])
    templates_path = Path(project_root, config["paths"]["templates_path"])

    env = Environment(loader=FileSystemLoader(templates_path))
    markdown_converter = Markdown()

    count = 0

    for content_item_path in get_content_item_paths(content_path):
        relative_path = content_item_path.relative_to(content_path)
        target_path = Path(project_root, "dist", relative_path.with_suffix(".html"))
        target_path.parent.mkdir(parents=True, exist_ok=True)

        logger.info("%s  -> %s", content_item_path, target_path)

        with open(content_item_path, "r") as infile:
            content_text = infile.read()

        header, content = frontmatter.parse(content_text)

        with open(target_path, "w") as outfile:
            outfile.write(
                env.get_template(header["template"] + ".j2").render(
                    {
                        "title": header["title"],
                        "data": markdown_converter.convert(content),
                        "site_metadata": stash.get("content_map", {}),
                    }
                )
            )

        count += 1

    logger.info("Generated %s files", count)
