from pathlib import Path

import pytest

from tinystatic.base import CliContext
from tinystatic.steps import prepare_environment


@pytest.fixture
def with_sample_assets(tmpdir):
    config = """
[paths]
static_path = 'static'
content_path = 'content'
templates_path = 'templates'
    """

    config_file = Path(tmpdir, "site_config.toml")
    config_file.write_text(config)

    static_path = Path(tmpdir, "static")
    static_path.mkdir(parents=True)

    templates_path = Path(tmpdir, "templates")
    templates_path.mkdir(parents=True)

    content_path = Path(tmpdir, "content")
    content_path.mkdir(parents=True)

    Path(static_path, "styles.css").write_text("static-static-static")
    Path(tmpdir, "dist").mkdir(parents=True)


def test_copies_files_from_the_static_asset_dir(
    tmpdir, with_sample_assets, prepare_env_step, copy_static_assets_step
):
    cli_args = CliContext(cwd=tmpdir)
    prepare_env_outputs = prepare_env_step({}, cli_args)

    previous_outputs = {prepare_environment.STEP_NAME: prepare_env_outputs}

    outputs = copy_static_assets_step(previous_outputs, cli_args)

    assert outputs == None
    assert [path.name for path in Path(tmpdir, "static").iterdir()] == ["styles.css"]
