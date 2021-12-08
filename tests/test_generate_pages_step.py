import pytest

from pathlib import Path

from tinystatic.base import tinystatic


@pytest.fixture(autouse=True)
def with_sample_content(set_up_files):
    files = {
        "site_config.toml": """
[paths]
static_path = 'static'
content_path = 'content'
templates_path = 'templates'
[pipeline]
steps = [
    "tinystatic.steps.generate_pages"
]
    """,
        "static/styles.css": "",
        "templates/test.j2": """
Template!
{{ data }}
    """,
        "content/post.md": """
---
title: Test content
template: test
---

Test post
    """,
    }

    set_up_files(files)


def test_skips_non_markdown_files(tmpdir, set_up_files, patched_cli_args):
    set_up_files({"content/non-markdown.txt": "wow"})

    with patched_cli_args(["tinystatic", "build", "--cwd", str(tmpdir)]):
        tinystatic()

    original_files = [
        Path(file).relative_to(tmpdir) for file in Path(tmpdir, "content").iterdir()
    ]

    generated_files = [
        Path(file).relative_to(tmpdir) for file in Path(tmpdir, "dist").iterdir()
    ]

    # Not counting the added textfile.
    assert len(generated_files) == len(original_files) - 1


def test_generates_content(tmpdir, patched_cli_args):

    with patched_cli_args(["tinystatic", "build", "--cwd", str(tmpdir)]):
        tinystatic()

    assert (
        Path(tmpdir, "dist", "post.html").read_text().strip()
        == """
Template!
<p>Test post</p>
""".strip()
    )
