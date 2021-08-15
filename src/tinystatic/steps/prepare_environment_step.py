from pathlib import Path

import toml

from tinystatic.logger import get_logger
from tinystatic.base import PipelineStep, PrepareEnvironmentStepOutput, PipelineOutputs


class PrepareEnvironmentStep(PipelineStep):
    STEP_NAME = "PrepareEnvironmentStep"
    logger = get_logger(STEP_NAME)

    @property
    def project_root(self) -> Path:
        return Path.cwd()

    @property
    def config_path(self) -> Path:
        return self.project_root.joinpath("site_config.toml")

    def run(self, previous_outputs: PipelineOutputs) -> PrepareEnvironmentStepOutput:
        with open(self.config_path, "r") as config_file:
            config = toml.loads(config_file.read())

        self.logger.info(
            "Loaded config from %s", self.config_path.relative_to(self.project_root)
        )

        return PrepareEnvironmentStepOutput(
            project_root=self.project_root, config=config
        )
