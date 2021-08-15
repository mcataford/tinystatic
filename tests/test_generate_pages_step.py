import pytest

from pathlib import Path

from tinystatic.base import CliContext


@pytest.fixture
def with_sample_content(tmpdir):
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

    Path(templates_path, "test.j2").write_text(
        """
Template!
{{ data }}
    """
    )

    Path(content_path, "post.md").write_text(
        """
---
title: Test content
template: test
---

Test post
    """
    )


def test_generates_content(
    tmpdir, prepare_env_step, generate_pages_step, with_sample_content
):
    cli_args = CliContext(cwd=tmpdir)
    prepare_env_outputs = prepare_env_step.run({}, cli_args)

    previous_outputs = {prepare_env_step.STEP_NAME: prepare_env_outputs}

    outputs = generate_pages_step.run(previous_outputs, cli_args)

    assert outputs.generated_count == 1
    assert (
        Path(tmpdir, "dist", "post.html").read_text().strip()
        == """
Template!
<p>Test post</p>
""".strip()
    )
