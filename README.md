# Tinystatic

[![CICD](https://github.com/mcataford/tinystatic/actions/workflows/main.yml/badge.svg)](https://github.com/mcataford/tinystatic/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/mcataford/tinystatic/branch/main/graph/badge.svg?token=EG5UGO5R3W)](https://codecov.io/gh/mcataford/tinystatic)
[![releases](https://img.shields.io/github/v/release/mcataford/tinystatic?label=latest%20github%20release)](https://github.com/mcataford/tinystatic/releases)

## Overview

`tinystatic` is a small, pipeline-based static site generator. It uses Markdown and Jinja templates to give you a quick
and easy way to get your words out there and to customize the process to fit your needs.

## Usage

You can install `tinystatic` using published artifacts available in the [project
releases](https://github.com/mcataford/tinystatic/releases).

### Configuration

You should have a `site-config.toml` configuration file at the root of your project. In it, you will define where
`tinystatic` can find your content, page templates and static assets:

```
# site_config.toml

[paths]
content   = "path/to/where/I/store/markdown"
static    = "path/to/styles"
templates = "path/to/my/templates"
```

Once this is set up, your are one `tinystatic build` away from a statically generated site.

## Contributing

This project uses [Poetry](https://python-poetry.org/) and [pyenv](https://github.com/pyenv/pyenv). To set both of these
up, you can simply `. script/bootstrap`. ([Read more](https://github.blog/2015-06-30-scripts-to-rule-them-all/) about the "scripts to rule them all" pattern).

Once set up, `poetry run tinystatic` will run the CLI locally.

## Releases

The project is currently only released on Github, with manual releases until the first production-ready PyPi release is
up to snuff. To trigger a release, create a tag of the format `v0.0.x` (with `x` being sequential based on whatever is
latest) and push it. The release workflow will create a draft release for the version and attach build artifacts to the
draft. From there, fill up the release description and publish.
