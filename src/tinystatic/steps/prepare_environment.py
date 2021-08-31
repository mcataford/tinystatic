from pathlib import Path

import toml

from tinystatic.logger import get_logger
from tinystatic.base import (
    CliContext,
    PrepareEnvironmentStepOutput,
)


class MissingConfigFileException(Exception):
    pass


class InvalidConfigFileException(Exception):
    pass


STEP_NAME = "PrepareEnvironmentStep"
logger = get_logger(STEP_NAME)


def run(_, cli_args: CliContext) -> PrepareEnvironmentStepOutput:
    project_root = Path(cli_args.cwd)
    config_path = project_root.joinpath("site_config.toml")

    if not config_path.exists():
        raise MissingConfigFileException(f"No config file found at {config_path}")

    with open(config_path, "r") as config_file:
        try:
            config = toml.loads(config_file.read())
        except Exception as exc:
            raise InvalidConfigFileException() from exc

    logger.info("Loaded config from %s", config_path.relative_to(project_root))

    return PrepareEnvironmentStepOutput(project_root=project_root, config=config)
