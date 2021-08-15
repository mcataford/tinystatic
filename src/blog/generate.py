from copy import deepcopy

from .PrepareEnvironmentStep import PrepareEnvironmentStep
from .GeneratePagesStep import GeneratePagesStep
from .CopyStaticAssetsStep import CopyStaticAssetsStep

pipeline = [PrepareEnvironmentStep(), GeneratePagesStep(), CopyStaticAssetsStep()]


def run():
    outputs = {}

    for step in pipeline:
        outputs[step.STEP_NAME] = step.run(deepcopy(outputs))

    print(outputs)
