from typing import List, Callable


class PipelineException(Exception):
    pass


def runner(pipeline: List[Callable], stash_preload):
    # Store used for cross-step communications.
    # Steps are responsible to assert that any dependencies on the
    # stash is met before running.
    stash = {**stash_preload}

    for step in pipeline:
        try:
            step.run(stash)
        except Exception as exc:
            raise PipelineException("Failed at %s" % step.STEP_NAME) from exc
