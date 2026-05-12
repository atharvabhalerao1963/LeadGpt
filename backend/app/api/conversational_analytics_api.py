from fastapi import APIRouter

from app.services.conversational_analytics_service import (
    analyze_business_question
)

router = APIRouter()

# =====================================================
# CONVERSATIONAL ANALYTICS API
# =====================================================

@router.post("/analytics-chat")
def analytics_chat(data: dict):

    question = data["question"]

    answer = analyze_business_question(question)

    return {
        "answer": answer
    }