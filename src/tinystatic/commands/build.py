from copy import deepcopy

from tinystatic.base import CliContext, PipelineException
from tinystatic.steps import prepare_environment, generate_pages, copy_static_assets

pipeline = [prepare_environment, generate_pages, copy_static_assets]


def build(args):
    context = CliContext(cwd=args.cwd)

    outputs = {}

    for step in pipeline:
        try:
            outputs[step.STEP_NAME] = step.run(deepcopy(outputs), context)
        except Exception as exc:
            raise PipelineException(f"Pipeline failed at {step.STEP_NAME}") from exc
