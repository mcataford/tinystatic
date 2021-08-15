import pytest

from tinystatic.steps.generate_pages_step import GeneratePagesStep
from tinystatic.steps.prepare_environment_step import PrepareEnvironmentStep


@pytest.fixture
def prepare_env_step():
    return PrepareEnvironmentStep()


@pytest.fixture
def generate_pages_step():
    return GeneratePagesStep()
