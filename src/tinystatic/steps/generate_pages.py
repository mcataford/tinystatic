from typing import Generator
from pathlib import Path

from markdown2 import Markdown
import frontmatter
from jinja2 import Environment, FileSystemLoader

from tinystatic.logger import get_logger
from tinystatic.base import GeneratePagesStepOutput, PipelineOutputs

STEP_NAME = "GeneratePagesStep"
logger = get_logger(STEP_NAME)


def _get_content(content_path: Path) -> Generator[Path, None, None]:
    for content in Path(content_path).iterdir():
        if content.suffix != ".md":
            continue

        yield content


def run(previous_outputs: PipelineOutputs, _) -> GeneratePagesStepOutput:
    """
    Generate pages based on markdown content.
    """
    config = previous_outputs["PrepareEnvironmentStep"].config
    project_root = previous_outputs["PrepareEnvironmentStep"].project_root

    content_path = Path(project_root, config["paths"]["content_path"])
    templates_path = Path(project_root, config["paths"]["templates_path"])

    env = Environment(loader=FileSystemLoader(templates_path))
    markdown_converter = Markdown()

    count = 0

    for content_item_path in _get_content(content_path):
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
                    }
                )
            )

        count += 1

    logger.info("Generated %s files", count)

    return GeneratePagesStepOutput(generated_count=count)
