from pathlib import Path
import shutil

from tinystatic.core.logger import get_logger

STEP_NAME = "CopyStaticAssets"
logger = get_logger(STEP_NAME)


def run(stash):
    project_root = stash["cwd"]
    config = stash["config"]

    static_path = Path(project_root, config["paths"]["static_path"])

    Path(project_root, "dist").mkdir(parents=True, exist_ok=True)

    for asset in static_path.iterdir():
        destination = Path(project_root, "dist", asset.name)
        logger.info("%s -> %s", asset, destination)

        shutil.copy(asset, destination)
