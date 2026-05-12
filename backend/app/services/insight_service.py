from groq import Groq
from dotenv import load_dotenv

import os

# =====================================================
# LOAD ENV VARIABLES
# =====================================================

load_dotenv()

# =====================================================
# GROQ CLIENT
# =====================================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# =====================================================
# GENERATE BUSINESS INSIGHT
# =====================================================

def generate_insight(prompt):

    system_prompt = f"""
    You are LeadGPT, an AI-powered Business Intelligence Assistant.

    Your task is to provide professional business insights
    based on the user's question.

    Keep answers:
    - concise
    - professional
    - actionable
    - business-oriented
    """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )

    return response.choices[0].message.content