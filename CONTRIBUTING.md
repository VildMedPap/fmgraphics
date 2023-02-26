# Contributing

## Setup

### Requirements

-   Make:
    -   MacOS: `brew install make`
    -   Linux: [https://www.gnu.org/software/make](https://www.gnu.org/software/make)
-   [Pyenv](https://github.com/pyenv/pyenv)
-   [Poetry](https://poetry.eustace.io/docs/#installation) (version ~1.3.2)

### Installation

Install project dependencies into a virtual environment:

```make
make install
```

This will:

-   Create a virtual environment (`.venv`)
-   Install direct dependencies including all group dependencies
-   Install pre-commit hooks

To activate the virtual environment either use the command `poetry shell` (`exit` to leave it again) or `source .venv/bin/activate` (`deactivate` to leave it again).

## Development Tasks

### Manual

Run test suite:

```make
make test
```

Run formatters (`black` and `ruff --fix`):

```make
make formatting
```

Run linters (`mypy` and `ruff`):

```make
make linting
```

Compute code complexity (`radon`):

```make
make cc
```

To make sure your code will pass the CI pipeline, you can run all linters and tests using:

```make
make --keep-going ci
```

Clean all temporary folder/files on the project:

```make
make clean
```

## Version control

For version control, we follow the [OneFlow](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow) branching model.
