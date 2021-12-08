# Using the configuration file

Tinystatic can be configured using a `site_config.toml` file at the root of your project. The file should have the
following layout:

```toml
[paths]
content = where/markdown/content/lives
templates = where/templates/live
static = where/static/assets/live

[pipeline]
steps = [
    step1,
    step2,
    ...
]
```

The `paths` section tells Tinystatic where to find the resources necessary to build your site, and the
`pipeline.steps` array is an ordered collection of step modules that defines the pipeline.
