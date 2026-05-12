from fastapi import APIRouter
from app.services.predict_service import predict_lead

router = APIRouter()

@router.post("/predict")
def predict(data: dict):

    result = predict_lead(data)

    return result