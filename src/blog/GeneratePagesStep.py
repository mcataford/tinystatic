from typing import Generator
from pathlib import Path
from collections import namedtuple

from markdown2 import Markdown
import frontmatter
from jinja2 import Environment, FileSystemLoader

from .logger import get_logger
from .base import PipelineStep

PROJECT_ROOT = Path(__file__).parent.parent.parent

TEMPLATE_PATH = PROJECT_ROOT.joinpath(Path("_templates"))
CONTENT_PATH = PROJECT_ROOT.joinpath(Path("_content"))

logger = get_logger("GeneratePages")

StepOutput = namedtuple("GeneratePagesStepOutput", ["generated_count"])


class GeneratePagesStep(PipelineStep):
    def _get_content(self) -> Generator[Path, None, None]:
        for content in CONTENT_PATH.iterdir():
            if content.suffix != ".md":
                continue

            yield content.relative_to(PROJECT_ROOT)

    def run(self) -> StepOutput:
        """
        Generate pages based on markdown content.
        """
        env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))
        markdown_converter = Markdown()

        count = 0

        for content_path in self._get_content():
            target_path = Path("dist", *content_path.parts[1:]).with_suffix(".html")
            target_path.parent.mkdir(parents=True, exist_ok=True)

            logger.info(f"{content_path} -> {target_path}")

            with open(content_path, "r") as infile:
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

        logger.info(f"Generated {count} files")

        return StepOutput(generated_count=count)
