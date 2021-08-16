# Tinystatic

[![CICD](https://github.com/mcataford/tinystatic/actions/workflows/main.yml/badge.svg)](https://github.com/mcataford/tinystatic/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/mcataford/tinystatic/branch/main/graph/badge.svg?token=EG5UGO5R3W)](https://codecov.io/gh/mcataford/tinystatic)

## Overview

`tinystatic` is a small, pipeline-based static site generator. It uses Markdown and Jinja templates to give you a quick
and easy way to get your words out there and to customize the process to fit your needs.

## Usage

Until `tinystatic` makes it up to PyPi, you can clone this repository and build your own wheel using `poetry build`.

### Configuration

You should have a `site-config.toml` configuration file at the root of your project. In it, you will define where
`tinystatic` can find your content, page templates and static assets:

```
# site-config.toml

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
