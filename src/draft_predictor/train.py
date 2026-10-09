"""Training skeleton; the data and modeling functions still need implementation."""

import argparse
from pathlib import Path

import pandas as pd
from sklearn.pipeline import Pipeline

from draft_predictor.features import build_features, extract_target


def load_data(path: Path) -> pd.DataFrame:
    """Load historical match records from a CSV or Parquet file.

    TODO: Read the file, validate champion picks, outcomes, match identifiers,
    and timestamps, and decide how to handle missing or duplicate records.
    """
    raise NotImplementedError("Implement load_data() to read and validate match data.")


def split_data(
    matches: pd.DataFrame,
    train_fraction: float = 0.7,
    validation_fraction: float = 0.15,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Return training, validation, and test match records in that order.

    TODO: Validate the fractions and split chronologically, keeping the newest
    matches for testing. Keep all rows from the same match in the same split.
    Do this before fitting preprocessing or calculating data-derived features.
    """
    raise NotImplementedError("Implement split_data() to create chronological splits.")


def train_model(
    features: pd.DataFrame,
    target: pd.Series,
    random_state: int = 42,
) -> Pipeline:
    """Fit and return a preprocessing and classification pipeline.

    TODO: Choose a classifier, construct the preprocessing pipeline, and fit
    both on training data only. The classifier must support predict_proba().
    Use a fixed random seed where supported.
    """
    raise NotImplementedError("Implement train_model() to fit the model pipeline.")


def evaluate_model(
    model: Pipeline,
    features: pd.DataFrame,
    target: pd.Series,
) -> dict[str, float]:
    """Evaluate a fitted model on held-out data without refitting it.

    TODO: Compute accuracy, ROC AUC, log loss, and Brier score from predictions
    and blue-team win probabilities. Handle undefined metrics explicitly.
    Use validation data for model selection and the test set for final reporting.
    """
    raise NotImplementedError(
        "Implement evaluate_model() to calculate held-out metrics."
    )


def save_model(model: Pipeline, output_path: Path) -> None:
    """Save the fitted pipeline so preprocessing and prediction stay consistent.

    TODO: Create the output directory and serialize the pipeline with joblib.
    Record its feature schema, training configuration, and game patch alongside
    the model so the prediction code can load the correct artifact.
    """
    raise NotImplementedError("Implement save_model() to write the trained pipeline.")


def main() -> None:
    """Parse training arguments and connect the placeholder training stages."""
    parser = argparse.ArgumentParser(
        description="LoL draft predictor training skeleton."
    )
    parser.add_argument(
        "--data", type=Path, default=Path("data/processed/matches.parquet")
    )
    parser.add_argument(
        "--output", type=Path, default=Path("models/draft_predictor.joblib")
    )
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    try:
        matches = load_data(args.data)
        training, validation, testing = split_data(matches)

        train_features = build_features(training)
        train_target = extract_target(training)
        validation_features = build_features(validation)
        validation_target = extract_target(validation)
        test_features = build_features(testing)
        test_target = extract_target(testing)

        model = train_model(train_features, train_target, random_state=args.seed)
        validation_metrics = evaluate_model(
            model, validation_features, validation_target
        )
        test_metrics = evaluate_model(model, test_features, test_target)
        save_model(model, args.output)

        print(f"Validation metrics: {validation_metrics}")
        print(f"Test metrics: {test_metrics}")
        print(f"Saved model to {args.output}")
    except NotImplementedError as error:
        parser.exit(status=1, message=f"Training skeleton: {error}\n")


if __name__ == "__main__":
    main()
