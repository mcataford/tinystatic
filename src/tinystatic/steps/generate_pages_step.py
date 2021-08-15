from typing import Generator
from pathlib import Path

from markdown2 import Markdown
import frontmatter
from jinja2 import Environment, FileSystemLoader

from tinystatic.logger import get_logger
from tinystatic.base import PipelineStep, GeneratePagesStepOutput, PipelineOutputs


class GeneratePagesStep(PipelineStep):
    STEP_NAME = "GeneratePagesStep"
    logger = get_logger(STEP_NAME)

    @staticmethod
    def _get_content(
        content_path: Path, project_root: Path
    ) -> Generator[Path, None, None]:
        for content in Path(content_path).iterdir():
            if content.suffix != ".md":
                continue

            yield content.relative_to(project_root)

    def run(self, previous_outputs: PipelineOutputs) -> GeneratePagesStepOutput:
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

        for content_path in self._get_content(content_path, project_root):
            target_path = Path("dist", *content_path.parts[1:]).with_suffix(".html")
            target_path.parent.mkdir(parents=True, exist_ok=True)

            self.logger.info("%s  -> %s", content_path, target_path)

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

        self.logger.info("Generated %s files", count)

        return GeneratePagesStepOutput(generated_count=count)
