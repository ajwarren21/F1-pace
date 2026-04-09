from fastapi import APIRouter
from scripts.run_pipeline import run

router = APIRouter()

@router.get("/rankings")
def get_rankings():
    data = run(2023, "Monza")
    return data
