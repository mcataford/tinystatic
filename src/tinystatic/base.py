from collections import namedtuple
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
