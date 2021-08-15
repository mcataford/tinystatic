from copy import deepcopy

from tinystatic.base import CliContext, PipelineException
from tinystatic.steps.prepare_environment_step import PrepareEnvironmentStep
from tinystatic.steps.generate_pages_step import GeneratePagesStep
from tinystatic.steps.copy_static_assets_step import CopyStaticAssetsStep

pipeline = [PrepareEnvironmentStep(), GeneratePagesStep(), CopyStaticAssetsStep()]


def build(args):
    context = CliContext(cwd=args.cwd)

    outputs = {}

    for step in pipeline:
        try:
            outputs[step.STEP_NAME] = step.run(deepcopy(outputs), context)
        except Exception as exc:
            raise PipelineException(f"Pipeline failed at {step.STEP_NAME}") from exc
