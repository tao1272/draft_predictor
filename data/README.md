# Local data

Store downloaded and processed datasets in this folder. Git ignores its contents
except this README, so match data and large generated files are not committed
accidentally.

Suggested local subfolders are `raw/` and `processed/`. Record data sources,
collection dates, game patches, and preparation steps in `docs/` when data
collection is implemented.

Small test fixtures should live in `tests/fixtures/` rather than this ignored
folder. No datasets are included in the initial scaffold.
