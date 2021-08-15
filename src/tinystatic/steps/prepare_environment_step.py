from pathlib import Path

import toml

from tinystatic.logger import get_logger
from tinystatic.base import (
    CliContext,
    PipelineStep,
    PrepareEnvironmentStepOutput,
    PipelineOutputs,
)


class PrepareEnvironmentStep(PipelineStep):
    STEP_NAME = "PrepareEnvironmentStep"
    logger = get_logger(STEP_NAME)

    def run(
        self, previous_outputs: PipelineOutputs, cli_args: CliContext
    ) -> PrepareEnvironmentStepOutput:
        project_root = Path(cli_args.cwd)
        config_path = project_root.joinpath("site_config.toml")

        with open(config_path, "r") as config_file:
            config = toml.loads(config_file.read())

        self.logger.info("Loaded config from %s", config_path.relative_to(project_root))

        return PrepareEnvironmentStepOutput(project_root=project_root, config=config)
