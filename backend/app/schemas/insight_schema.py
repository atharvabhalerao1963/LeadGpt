from pydantic import BaseModel

class InsightRequest(BaseModel):
    prompt: str  # "Request body must contain a prompt string. this ensure that output and input remains in the required format" 