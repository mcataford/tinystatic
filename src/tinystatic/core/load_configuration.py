from typing import Optional, Union
from pathlib import Path

import toml


class MissingConfigFileException(Exception):
    pass


class InvalidConfigFileException(Exception):
    pass


CONFIGURATION_FILENAME = "site_config.toml"


def load_configuration(*, project_root: Optional[Union[Path, str]] = Path.cwd()):
    """
    Loads the configuration from the site_config TOML file if it exists.
    """

    if not isinstance(project_root, Path):
        project_root = Path(project_root)

    config_path = project_root.joinpath(CONFIGURATION_FILENAME)

    if not config_path.exists():
        raise MissingConfigFileException(f"No config file found at {config_path}")

    with open(config_path, "r") as config_file:
        try:
            config = toml.loads(config_file.read())
        except Exception as exc:
            raise InvalidConfigFileException() from exc

    return config
