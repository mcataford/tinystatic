from .GeneratePagesStep import GeneratePagesStep
from .CopyStaticAssetsStep import CopyStaticAssetsStep

pipeline = [GeneratePagesStep(), CopyStaticAssetsStep()]


def run():
    for step in pipeline:
        step.run()
