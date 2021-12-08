from importlib import import_module

from tinystatic.core.runner import runner


def build(*, cwd: str, config):
    """
    Runs the pipeline defined in the provided configuration.
    """

    stash_preload = {"cwd": cwd, "config": config}

    pipeline = [import_module(step) for step in config["pipeline"]["steps"]]

    runner(pipeline, stash_preload)


COMMAND_HANDLERS = {"build": build}
