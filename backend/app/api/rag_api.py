from fastapi import APIRouter
from app.rag.rag_service import ask_rag

router = APIRouter()

@router.post("/rag")

def rag_chat(data: dict):

    question = data["question"]

    answer = ask_rag(question)

    return {
        "answer": answer
    }