import logging
from pathlib import Path
import shutil

from .logger import get_logger
from .base import PipelineStep


PROJECT_ROOT = Path(__file__).parent.parent.parent
STATIC_ASSETS_PATH = PROJECT_ROOT.joinpath(Path("_static"))


class CopyStaticAssetsStep(PipelineStep):
    logger = get_logger("CopyStaticAssets")

    def run(self):
        for asset in STATIC_ASSETS_PATH.iterdir():
            source = asset.relative_to(PROJECT_ROOT)
            destination = Path("dist", asset.name)
            self.logger.info(f"{source} -> {destination}")

            shutil.copy(source, destination)
