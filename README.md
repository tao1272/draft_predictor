# draft_predictor

Predicting win rate from champion drafts in League of Legends.

[![CI](https://github.com/tao1272/draft_predictor/actions/workflows/ci.yml/badge.svg)](https://github.com/tao1272/draft_predictor/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Status

This repository currently provides the Python project scaffold, machine-learning
dependencies, development tooling, and placeholder training functions. Data
collection, model training, and prediction are not implemented yet. There is no
trained model or prediction command to run.

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

On macOS, install LightGBM's OpenMP runtime with `brew install libomp` before
installing the Python dependencies. See the
[LightGBM installation instructions](https://github.com/lightgbm-org/LightGBM/blob/main/python-package/README.rst).

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
| `requirements.txt` | Alternative pip entry point for runtime dependencies |

## Training skeleton

The training workflow is outlined in
[`src/draft_predictor/train.py`](src/draft_predictor/train.py), with draft feature
functions in [`src/draft_predictor/features.py`](src/draft_predictor/features.py).

| Function | Intended responsibility |
| --- | --- |
| `load_data()` | Load and validate historical match records |
| `split_data()` | Create chronological training, validation, and test splits |
| `build_features()` | Convert champion drafts into model inputs |
| `extract_target()` | Produce binary blue-team win labels |
| `train_model()` | Fit preprocessing and a classifier on training data |
| `evaluate_model()` | Evaluate predictions and win probabilities on held-out data |
| `save_model()` | Save the fitted pipeline and its metadata |
| `main()` | Connect the stages and parse training arguments |

Each data or modeling function has a signature, a TODO docstring, and an explicit
`NotImplementedError`. The command-line interface supports help:

```bash
python -m draft_predictor.train --help
```

The future training invocation is:

```bash
python -m draft_predictor.train --data data/processed/matches.parquet --output models/draft_predictor.joblib
```

It currently exits with a message naming the first unimplemented stage. It does
not train or save a model. Implement the functions before using real match data;
use validation data to select or tune the model before final test evaluation.

## Machine-learning dependencies

The default installation includes the tools for a tabular draft-prediction
workflow. Their intended roles are:

| Packages | Purpose |
| --- | --- |
| `numpy`, `pandas`, `scipy` | Process match data and construct draft features |
| `scikit-learn` | Preprocessing, baseline classifiers, data splits, probability calibration, and evaluation |
| `xgboost`, `lightgbm` | Gradient-boosted tree classifiers |
| `optuna` | Tune model hyperparameters |
| `joblib` | Save and load trained models and preprocessing pipelines |
| `pyarrow` | Read and write Parquet datasets |
| `matplotlib`, `seaborn` | Plot model performance and inspect data |
| `requests`, `tenacity`, `tqdm` | Access the Riot API, implement retries, and display collection progress |
| `python-dotenv` | Load local API credentials from a `.env` file |

On Linux x86-64, pip installs the smaller `xgboost-cpu` distribution, which is
imported as `xgboost`. Other platforms use the standard `xgboost` distribution.
See the [XGBoost installation guide](https://xgboost.readthedocs.io/en/stable/install.html).

Optional dependency groups are available for additional workflows:

| Extra | Packages | Install command |
| --- | --- | --- |
| `notebooks` | JupyterLab and IPython kernel | `python -m pip install -e ".[dev,notebooks]"` |
| `explain` | SHAP model explanations | `python -m pip install -e ".[dev,explain]"` |
| `deep-learning` | PyTorch neural networks | `python -m pip install -e ".[dev,deep-learning]"` |

Combine extras as needed, for example:

```bash
python -m pip install -e ".[dev,notebooks,explain]"
```

The default setup supports CPU training. For a specific PyTorch CUDA build, use
the [official PyTorch installation selector](https://pytorch.org/get-started/locally/)
for your operating system and hardware.

`pyproject.toml` is the single source of dependency declarations. If you prefer
the conventional requirements-file command, run this from the repository root:

```bash
python -m pip install -r requirements.txt
```

This installs the project and its runtime dependencies; the editable command
with `[dev]` also installs the development tools. The listed minimum versions are
dependency constraints, not an exact environment lock.

## Development checks

```bash
python -m ruff check .
python -m ruff format --check .
python -m build
python -m twine check dist/*
```

To format Python files, run `python -m ruff format .`. Once tests have been added,
run `python -m pytest`. CI checks Python 3.11 through 3.14, runs tests when test
files exist, imports the core machine-learning libraries, and checks the built
package in a separate environment.

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
