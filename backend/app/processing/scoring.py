import pandas as pd


def compute_pace_score(metrics: pd.DataFrame) -> pd.DataFrame:
    """
    Create a composite score (lower is better).
    """
    df = metrics.copy()

    # Normalize components
    df["norm_delta"] = (df["avg_delta"] - df["avg_delta"].min()) / (
        df["avg_delta"].max() - df["avg_delta"].min()
    )

    df["norm_consistency"] = (df["consistency"] - df["consistency"].min()) / (
        df["consistency"].max() - df["consistency"].min()
    )

    # Weighted score
    df["pace_score"] = (
        0.7 * df["norm_delta"] +
        0.3 * df["norm_consistency"]
    )

    return df.sort_values("pace_score")
