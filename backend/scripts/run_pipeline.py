from app.data.fetch import load_session, get_laps
from app.processing.clean import filter_clean_laps
from app.processing.normalize import normalize_lap_times
from app.processing.metrics import compute_driver_metrics
from app.processing.scoring import compute_pace_score


def run(year: int, gp: str):
    session = load_session(year, gp)
    laps = get_laps(session)

    laps = filter_clean_laps(laps)
    laps = normalize_lap_times(laps)

    metrics = compute_driver_metrics(laps)
    rankings = compute_pace_score(metrics)

    return rankings.to_dict(orient="records")


if __name__ == "__main__":
    run(2023, "Monza")
    