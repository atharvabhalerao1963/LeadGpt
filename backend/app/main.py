from fastapi import FastAPI

from app.api.predict import router as predict_router
from app.api.insight import router as insight_router
from app.api.forecast import router as forecast_router
from app.api.rag_api import router as rag_router
from app.api.analytics_api import router as analytics_router
from app.api.report_api import router as report_router

from app.api.recommendation_api import (
    router as recommendation_router
)
from app.api.conversational_analytics_api import (
    router as conversational_router
)

app = FastAPI()

app.include_router(conversational_router)

app.include_router(predict_router)

app.include_router(insight_router)

app.include_router(forecast_router)

app.include_router(rag_router)

app.include_router(analytics_router)

app.include_router(recommendation_router)

app.include_router(report_router)

@app.get("/")
def home():

    return {
        "message": "LeadGPT API Running"
    }