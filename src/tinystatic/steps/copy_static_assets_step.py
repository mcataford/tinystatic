from pathlib import Path
import shutil

from tinystatic.logger import get_logger
from tinystatic.base import PipelineStep, PipelineOutputs


class CopyStaticAssetsStep(PipelineStep):
    STEP_NAME = "CopyStaticAssets"
    logger = get_logger(STEP_NAME)

    def run(self, previous_outputs: PipelineOutputs, _):
        project_root = previous_outputs["PrepareEnvironmentStep"].project_root
        config = previous_outputs["PrepareEnvironmentStep"].config

        static_path = Path(project_root, config["paths"]["static_path"])

        for asset in static_path.iterdir():
            destination = Path(project_root, "dist", asset.name)
            self.logger.info("%s -> %s", asset, destination)

            shutil.copy(asset, destination)
