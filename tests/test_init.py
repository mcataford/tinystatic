from pathlib import Path

import pytest

from tinystatic.base import tinystatic


def test_init_creates_placeholder_dirs_and_config_file(tmpdir, patched_cli_args):
    with patched_cli_args(["tinystatic", "init", "--cwd", str(tmpdir)]):
        tinystatic()

    generated = {Path(file).relative_to(Path(tmpdir)) for file in tmpdir.listdir()}

    assert {
        Path("_static"),
        Path("_content"),
        Path("_templates"),
        Path("site_config.toml"),
    } == generated
