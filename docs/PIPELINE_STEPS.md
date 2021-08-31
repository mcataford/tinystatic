# Pipeline steps

Pipeline steps are defined as Python modules that follow the convention:

```
STEP_NAME = ... # Name used to refer to the step in logging and any step maps

def run(previous_output: PipelineStepOutput, context: CliContext) -> PipelineStepOutput:
    # Code that runs when the step is executed.
    # Each step can consume outputs from previous steps and the CLI context.
    # Each step can also produce output..
    ...
```
