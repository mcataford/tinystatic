import pytest
from unittest.mock import patch
import sys

from pathlib import Path

from tinystatic.base import tinystatic


@pytest.fixture(autouse=True)
def include_cwd_in_syspath(tmpdir):
    sys.path.insert(0, str(tmpdir))


@pytest.fixture(autouse=True)
def with_sample_content(set_up_files):
    files = {
        "mock_step.py": """
def run(stash):
    pass
            """,
        "site_config.toml": """
[paths]
static_path = 'static'
content_path = 'content'
templates_path = 'templates'
[pipeline]
steps = [
    "tinystatic.steps.map_content",
    "mock_step"
]
[steps.map_content]
include = [
    "key1",
    "key2"
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
key1: a
key2: b
key3: c
---

Test post
    """,
    }

    set_up_files(files)


def test_map_content_ignores_keys_not_included_in_inclusion_list(
    tmpdir, patched_cli_args
):
    with patched_cli_args(["tinystatic", "build", "--cwd", str(tmpdir)]), patch(
        "mock_step.run"
    ) as mocked_step:
        tinystatic()

    mock_step_args = mocked_step.call_args.args[0]

    assert "key3" not in mock_step_args["content_map"]["post.md"]


def test_map_content_includes_configured_keys(tmpdir, patched_cli_args):
    with patched_cli_args(["tinystatic", "build", "--cwd", str(tmpdir)]), patch(
        "mock_step.run"
    ) as mocked_step:
        tinystatic()

    mock_step_args = mocked_step.call_args.args[0]
    
    print(mock_step_args)
    assert mock_step_args["content_map"] == {"post.md": {"key1": "a", "key2": "b"}}
