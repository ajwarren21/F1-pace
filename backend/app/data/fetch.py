import fastf1
import pandas as pd
from pathlib import Path

# Enable caching (IMPORTANT)
CACHE_DIR = Path("cache/raw")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

fastf1.Cache.enable_cache(str(CACHE_DIR))


def load_session(year: int, gp: str, session_type: str = "R"):
    """
    Load a race session.
    Example: load_session(2023, "Monza", "R")
    """
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    return session


def get_laps(session) -> pd.DataFrame:
    """
    Return laps as a pandas DataFrame.
    """
    laps = session.laps
    return laps
