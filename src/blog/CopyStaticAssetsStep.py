import logging
from pathlib import Path
import shutil

from .logger import get_logger
from .base import PipelineStep, PipelineOutputs


PROJECT_ROOT = Path(__file__).parent.parent.parent
STATIC_ASSETS_PATH = PROJECT_ROOT.joinpath(Path("_static"))


class CopyStaticAssetsStep(PipelineStep):
    STEP_NAME = "CopyStaticAssets"
    logger = get_logger(STEP_NAME)

    def run(self, previous_outputs: PipelineOutputs):
        project_root = previous_outputs["PrepareEnvironmentStep"].project_root
        config = previous_outputs["PrepareEnvironmentStep"].config

        static_path = Path(project_root, config["paths"]["static_path"])

        for asset in static_path.iterdir():
            source = asset.relative_to(project_root)
            destination = Path("dist", asset.name)
            self.logger.info(f"{source} -> {destination}")

            shutil.copy(source, destination)
