from pathlib import Path
import logging
from importlib import import_module
import sys

import toml

from tinystatic.core.runner import runner


def init():
    """
    Sets up scaffolding for a new static site project.
    If the active directory is not empty, stops early.
    If the active directory is empty, creates the base
    folders required for operations and a stub config file.
    """

    logger = logging.getLogger("Initialize")

    cwd = Path.cwd()

    if any(cwd.iterdir()):
        logger.warning("%s is not empty, stopping.", cwd)
        sys.exit(1)

    logger.info("Using %s as project root", cwd)

    base_config = {
        "paths": {
            "static_path": "_static",
            "content_path": "_content",
            "templates_path": "_templates",
        },
        "pipeline": {"steps": []},
    }

    for dirname in base_config["paths"].values():
        dirpath = Path(cwd, dirname)
        dirpath.mkdir(parents=True)
        logger.info("Created %s", dirpath)

    config_path = Path(cwd, "site_config.toml")
    config_path.write_text(toml.dumps(base_config))
    logger.info("Created %s", config_path)


def build(*, cwd: str, config):
    """
    Runs the pipeline defined in the provided configuration.
    """

    stash_preload = {"cwd": cwd, "config": config}

    pipeline = [import_module(step) for step in config["pipeline"]["steps"]]

    runner(pipeline, stash_preload)


COMMAND_HANDLERS = {"build": build, "init": init}
