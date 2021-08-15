from copy import deepcopy

from tinystatic.steps.prepare_environment_step import PrepareEnvironmentStep
from tinystatic.steps.generate_pages_step import GeneratePagesStep
from tinystatic.steps.copy_static_assets_step import CopyStaticAssetsStep

pipeline = [PrepareEnvironmentStep(), GeneratePagesStep(), CopyStaticAssetsStep()]

def run():
    outputs = {}

    for step in pipeline:
        outputs[step.STEP_NAME] = step.run(deepcopy(outputs))

    print(outputs)
