# Contributing

Bug reports, documentation improvements, and code contributions are welcome.
Please read the [code of conduct](CODE_OF_CONDUCT.md) before participating.

## Discuss a change

Search existing [issues](https://github.com/tao1272/draft_predictor/issues) first.
For a substantial change, open a feature request describing the problem and your
proposed approach. Use the bug-report template for reproducible defects.
Follow [SECURITY.md](SECURITY.md) for vulnerabilities.

## Set up development

Fork the repository if you do not have write access, then clone your fork.
Create a branch from the latest `main`:

```bash
git switch main
git pull --ff-only
git switch -c feature/short-description
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Windows PowerShell users can activate with `.venv\Scripts\Activate.ps1`.

## Make and check changes

- Put reusable Python code in `src/draft_predictor/`.
- Add tests for new behavior in `tests/`, using `test_*.py` or `*_test.py` filenames.
- Keep notebooks reproducible and remove credentials and unnecessary outputs.
- Record substantial user-facing changes under `Unreleased` in the changelog.
- Update documentation when installation, configuration, or behavior changes.
- Keep datasets, trained models, and credentials out of commits.

Run these checks before submitting:

```bash
python -m ruff check .
python -m ruff format --check .
python -m build
python -m twine check dist/*
```

When tests exist, also run `python -m pytest`. The initial scaffold contains no
behavioral tests. CI starts running pytest automatically when test files are added.

For future prediction work, document the dataset source, game patch, target
definition, and evaluation split so results can be reproduced.

## Open a pull request

Use a clear title and complete the pull-request template. Explain the problem,
the resulting behavior, and how you verified it. Keep each pull request focused
on one change and link any related issue. A maintainer will review the change.

By submitting a contribution, you agree that it may be distributed under this
repository's [MIT License](LICENSE).
