import pandas as pd


def normalize_lap_times(laps: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize lap times relative to fastest lap in session.
    """
    laps = laps.copy()

    fastest = laps["LapTimeSeconds"].min()

    laps["LapTimeDelta"] = laps["LapTimeSeconds"] - fastest
    laps["LapTimePct"] = laps["LapTimeSeconds"] / fastest

    return laps
