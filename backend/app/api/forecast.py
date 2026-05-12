from fastapi import APIRouter
from app.services.forecast_service import get_forecast

router = APIRouter()

@router.get("/forecast")
def forecast():

    result = get_forecast()

    return result