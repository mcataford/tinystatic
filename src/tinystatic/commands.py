from pathlib import Path
import logging
from importlib import import_module
import sys

import toml

from tinystatic.core.runner import runner


def init(**kwargs):
    """
    Sets up scaffolding for a new static site project.
    If the active directory is not empty, stops early.
    If the active directory is empty, creates the base
    folders required for operations and a stub config file.
    """

    logger = logging.getLogger("Initialize")

    if any(Path(kwargs["cwd"]).iterdir()):
        logger.warning("%s is not empty, stopping.", kwargs["cwd"])
        sys.exit(1)

    logger.info("Using %s as project root", kwargs["cwd"])

    base_config = {
        "paths": {
            "static_path": "_static",
            "content_path": "_content",
            "templates_path": "_templates",
        },
        "pipeline": {"steps": []},
    }

    for dirname in base_config["paths"].values():
        dirpath = Path(kwargs["cwd"], dirname)
        dirpath.mkdir(parents=True)
        logger.info("Created %s", dirpath)

    config_path = Path(kwargs["cwd"], "site_config.toml")
    config_path.write_text(toml.dumps(base_config))
    logger.info("Created %s", config_path)


def build(**kwargs):
    """
    Runs the pipeline defined in the provided configuration.
    """

    stash_preload = {"cwd": kwargs["cwd"], "config": kwargs["config"]}

    pipeline = [import_module(step) for step in kwargs["config"]["pipeline"]["steps"]]

    runner(pipeline, stash_preload)


COMMAND_HANDLERS = {"build": build, "init": init}
