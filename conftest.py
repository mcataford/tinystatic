import pytest

from tinystatic.steps.copy_static_assets_step import CopyStaticAssetsStep
from tinystatic.steps.generate_pages_step import GeneratePagesStep
from tinystatic.steps.prepare_environment_step import PrepareEnvironmentStep


@pytest.fixture
def prepare_env_step():
    return PrepareEnvironmentStep()


@pytest.fixture
def generate_pages_step():
    return GeneratePagesStep()


@pytest.fixture
def copy_static_assets_step():
    return CopyStaticAssetsStep()
