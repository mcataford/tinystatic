from contextlib import contextmanager
from pathlib import Path

import pytest

from tinystatic.steps import copy_static_assets, generate_pages


@pytest.fixture
def set_up_files(tmpdir):
    def _set_up_files(files):
        for file in files:
            file_path = Path(tmpdir, file)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(files[file])

    return _set_up_files


@pytest.fixture
def patched_cli_args(monkeypatch):
    @contextmanager
    def _patched_cli_args(argv):
        try:
            monkeypatch.setattr("sys.argv", argv)
            yield
        finally:
            monkeypatch.undo()

    return _patched_cli_args


@pytest.fixture
def generate_pages_step():
    return generate_pages.run


@pytest.fixture
def copy_static_assets_step():
    return copy_static_assets.run
