import pytest

from pathlib import Path

from tinystatic.base import CliContext
from tinystatic.steps.prepare_environment_step import (
    InvalidConfigFileException,
    MissingConfigFileException,
    PrepareEnvironmentStep,
)


@pytest.fixture
def mock_config():
    return """
[paths]
static_path = 'static'
content_path = 'content'
templates_path = 'templates'
    """


@pytest.fixture
def mock_config_dict():
    return {
        "paths": {
            "static_path": "static",
            "content_path": "content",
            "templates_path": "templates",
        }
    }


def test_fails_if_config_file_not_found(tmpdir, prepare_env_step):
    with pytest.raises(MissingConfigFileException):
        prepare_env_step.run({}, CliContext(cwd=tmpdir))


def test_fails_if_config_file_exists_but_invalid_toml(tmpdir, prepare_env_step):
    config_file = Path(tmpdir, "site_config.toml")

    config_file.write_text("invalid-config-what-is-this-even-anymore")

    with pytest.raises(InvalidConfigFileException):
        prepare_env_step.run({}, CliContext(cwd=tmpdir))


def test_honors_working_directory_overrides_via_cli_context(
    tmpdir, mock_config, mock_config_dict, prepare_env_step
):
    config_file = Path(tmpdir, "subdir", "site_config.toml")
    config_file.parent.mkdir(parents=True)
    config_file.write_text(mock_config)

    output = prepare_env_step.run({}, CliContext(cwd=Path(tmpdir, "subdir")))

    assert output.project_root == Path(tmpdir, "subdir")
    assert output.config == mock_config_dict


def test_outputs_project_root_and_config_file(
    tmpdir, prepare_env_step, mock_config, mock_config_dict
):
    config_file = Path(tmpdir, "site_config.toml")

    config_file.write_text(mock_config)

    output = prepare_env_step.run({}, CliContext(cwd=tmpdir))

    assert output.project_root == tmpdir
    assert output.config == mock_config_dict
