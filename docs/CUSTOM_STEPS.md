# Custom pipeline steps

Tinystatic pipeline steps are Python modules with predefined exports.

A step should always expose the following:

```python

# How the step is called in logs.
STEP_NAME = "..."

# Step's business logic
def run(stash):
    ...
```

Each step has access to a shared datastore (`stash`) that steps can write to or read from. It is the responsibility of
each step to verify that any assumptions made on the stash are true -- it does not enforce anything by itself.

Once your step is implemented, you can include it in your pipeline via the `pipeline.steps` parameter:

```toml
[pipeline]
steps = [
    "my_cool_step"
]
```

The module in which your step lives should be importable; `tinystatic` will dynamically import it when the pipeline
is run.
