from pathlib import Path

import pytest

from tinystatic.base import tinystatic
from tinystatic.core.runner import runner


@pytest.fixture
def with_sample_assets(set_up_files):
    files = {
        "site_config.toml": """
[paths]
static_path = 'static'
content_path = 'content'
templates_path = 'templates'
[pipeline]
steps = [
    "tinystatic.steps.copy_static_assets"
]
    """,
        "static/styles.css": "static-static-static",
        "templates/template.j2": "",
        "content/content.md": "",
    }

    set_up_files(files)


def test_copies_files_from_the_static_asset_dir(
    tmpdir, with_sample_assets, patched_cli_args
):
    with patched_cli_args(["tinystatic", "build", "--cwd", str(tmpdir)]):
        tinystatic()

    originals = [
        file.relative_to(Path(tmpdir, "static"))
        for file in Path(tmpdir, "static").iterdir()
    ]
    copied = [
        file.relative_to(Path(tmpdir, "dist"))
        for file in Path(tmpdir, "dist").iterdir()
    ]

    # Paths are the same.
    assert originals == copied

    # Contents are the same.
    for file in originals:
        assert (
            Path(tmpdir, "static", file).read_text()
            == Path(tmpdir, "dist", file).read_text()
        )
