from abc import ABC, abstractmethod
import logging


class PipelineStep(ABC):
    @abstractmethod
    def run():
        raise NotImplementedError()
