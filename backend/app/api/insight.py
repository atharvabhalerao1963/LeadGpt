from fastapi import APIRouter

from app.services.smart_insight_service import (
    generate_smart_insight
)

router = APIRouter()

# =====================================================
# SMART AI INSIGHTS API
# =====================================================

@router.post("/insight")
def get_insight(data: dict):

    prompt = data["prompt"]

    insight = generate_smart_insight(prompt)

    return {
        "insight": insight
    }