from collections import namedtuple
from abc import ABC, abstractmethod
from typing import Dict, Union

PrepareEnvironmentStepOutput = namedtuple(
    "PrepareEnvironmentStepOutput", ["project_root", "config"]
)
CopyAssetsStepOutput = namedtuple("CopyStaticAssetsStepOutput", "")
GeneratePagesStepOutput = namedtuple("GeneratePagesStepOutput", ["generated_count"])

PipelineOutputs = Dict[
    str,
    Union[PrepareEnvironmentStepOutput, CopyAssetsStepOutput, GeneratePagesStepOutput],
]

CliContext = namedtuple("CliContext", ["cwd"])


class PipelineException(Exception):
    pass


class PipelineStep(ABC):
    @abstractmethod
    def run(self, previous_outputs: PipelineOutputs, cli_args: CliContext):
        raise NotImplementedError()
