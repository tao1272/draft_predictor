# draft_predictor

Predicting win rate from champion drafts in League of Legends.

[![CI](https://github.com/tao1272/draft_predictor/actions/workflows/ci.yml/badge.svg)](https://github.com/tao1272/draft_predictor/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Status

This repository currently provides the Python project scaffold and development
tooling. Data collection, model training, and prediction are not implemented yet;
there is no trained model or prediction command to run.

## Getting started

Requirements: Python 3.11 or newer and Git. Python 3.12 is the default development
version recorded in `.python-version`.

```bash
git clone https://github.com/tao1272/draft_predictor.git
cd draft_predictor
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On Windows PowerShell, activate the environment with
`.venv\Scripts\Activate.ps1` instead.

Check that the package is installed:

```bash
python -c "import draft_predictor; print(draft_predictor.__file__)"
```

## Repository layout

| Path | Purpose |
| --- | --- |
| `src/draft_predictor/` | Installable Python package |
| `tests/` | Automated tests as functionality is added |
| `docs/` | Project and usage documentation |
| `notebooks/` | Exploratory analysis |
| `data/` | Local datasets; dataset contents are ignored by Git |
| `models/` | Local model artifacts; model contents are ignored by Git |
| `.github/` | CI, dependency updates, and contribution templates |
| `pyproject.toml` | Package metadata and development tool configuration |

## Development checks

```bash
python -m ruff check .
python -m ruff format --check .
python -m build
python -m twine check dist/*
```

To format Python files, run `python -m ruff format .`. Once tests have been added,
run `python -m pytest`. CI checks Python 3.11 through 3.14, runs tests when test
files exist, and checks the built package in a separate environment.

Add runtime dependencies to `[project].dependencies` in `pyproject.toml`, and
development dependencies to `[project.optional-dependencies].dev`.

## Data and credentials

Keep datasets in `data/` and trained models in `models/`; the README in each folder
explains the convention. Keep any future API tokens in a local `.env` file or
environment variables. The repository does not yet read these settings.

## Contributing and support

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution workflow and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community expectations. Report bugs
or suggest features using the [issue templates](https://github.com/tao1272/draft_predictor/issues/new/choose).
For security concerns, follow [SECURITY.md](SECURITY.md).

Project changes are recorded in [CHANGELOG.md](CHANGELOG.md).

## License

The source code is licensed under the [MIT License](LICENSE).
