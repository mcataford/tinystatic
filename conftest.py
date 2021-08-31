import pytest

from tinystatic.steps import copy_static_assets, generate_pages, prepare_environment


@pytest.fixture
def prepare_env_step():
    return prepare_environment.run


@pytest.fixture
def generate_pages_step():
    return generate_pages.run


@pytest.fixture
def copy_static_assets_step():
    return copy_static_assets.run
