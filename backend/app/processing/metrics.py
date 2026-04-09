import pandas as pd


def compute_driver_metrics(laps: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate lap data into driver-level metrics.
    """
    grouped = laps.groupby("Driver")

    metrics = grouped.agg({
        "LapTimeSeconds": "mean",
        "LapTimeDelta": "mean",
        "LapTimePct": "mean"
    }).rename(columns={
        "LapTimeSeconds": "avg_lap_time",
        "LapTimeDelta": "avg_delta",
        "LapTimePct": "avg_pct"
    })

    # Consistency
    metrics["consistency"] = grouped["LapTimeSeconds"].std()

    return metrics.reset_index()
