import pandas as pd


def filter_clean_laps(laps: pd.DataFrame) -> pd.DataFrame:
    """
    Remove invalid laps:
    - Pit in/out laps
    - Slow laps (outliers)
    """
    laps = laps.copy()

    # Remove pit laps
    laps = laps[~laps["PitInTime"].notna()]
    laps = laps[~laps["PitOutTime"].notna()]

    # Remove very slow laps (basic outlier filter)
    laps = laps[laps["LapTime"].notna()]
    laps["LapTimeSeconds"] = laps["LapTime"].dt.total_seconds()

    # Keep laps within reasonable range
    mean = laps["LapTimeSeconds"].mean()
    std = laps["LapTimeSeconds"].std()

    laps = laps[
        (laps["LapTimeSeconds"] > mean - 2 * std) &
        (laps["LapTimeSeconds"] < mean + 2 * std)
    ]

    return laps
