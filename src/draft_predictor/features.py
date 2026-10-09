"""Placeholders for converting League of Legends drafts into model inputs."""

import pandas as pd


def build_features(matches: pd.DataFrame) -> pd.DataFrame:
    """Create draft features with one row per match, preserving the index.

    TODO: Extract both teams' champion picks and any other inputs available at
    prediction time. Exclude the outcome and post-match statistics. Keep learned
    encoders and scalers in the model pipeline so they are fitted on training
    data only. Reuse this function when predicting a new draft.
    """
    raise NotImplementedError("Implement build_features() to create draft inputs.")


def extract_target(matches: pd.DataFrame) -> pd.Series:
    """Return the outcome for each match, preserving the feature row index.

    TODO: Read or derive a binary label: 1 for a blue-team win and 0 for a
    red-team win. Validate that labels are present and contain only 0 or 1.
    """
    raise NotImplementedError("Implement extract_target() to obtain match outcomes.")
