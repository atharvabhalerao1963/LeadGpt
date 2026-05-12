from fastapi import APIRouter

from app.services.recommendation_service import (
    generate_recommendations
)

router = APIRouter()

# =====================================================
# AI RECOMMENDATIONS API
# =====================================================

@router.get("/recommendations")
def recommendations():

    return {
        "recommendations": generate_recommendations()
    }