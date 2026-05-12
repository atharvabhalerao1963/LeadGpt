import pandas as pd

from pathlib import Path

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
# LOAD DATASET
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_PATH = BASE_DIR / "app" / "data" / "project_sales_data.csv"

df = pd.read_csv(DATA_PATH)

# =====================================================
# SMART AI INSIGHT ENGINE
# =====================================================

def generate_smart_insight(user_question):

    # =================================================
    # BUSINESS ANALYTICS
    # =================================================

    total_leads = len(df)

    top_source = (
        df["Source"]
        .value_counts()
        .idxmax()
    )

    top_source_count = (
        df["Source"]
        .value_counts()
        .max()
    )

    top_agent = (
        df["Sales_Agent"]
        .value_counts()
        .idxmax()
    )

    top_agent_count = (
        df["Sales_Agent"]
        .value_counts()
        .max()
    )

    top_status = (
        df["Status"]
        .value_counts()
        .idxmax()
    )

    top_location = (
        df["Location"]
        .fillna("Unknown")
        .value_counts()
        .idxmax()
    )

    converted_count = len(
        df[
            df["Status"]
            .astype(str)
            .str.lower()
            .str.contains("converted", na=False)
        ]
    )

    # =================================================
    # ANALYTICS SUMMARY
    # =================================================

    analytics_summary = f"""
    BUSINESS ANALYTICS SUMMARY

    Total Leads: {total_leads}

    Top Lead Source:
    {top_source} ({top_source_count} leads)

    Top Sales Agent:
    {top_agent} ({top_agent_count} leads)

    Most Common Lead Status:
    {top_status}

    Top Lead Location:
    {top_location}

    Converted Leads:
    {converted_count}
    """

    # =================================================
    # AI PROMPT
    # =================================================

    prompt = f"""
    You are LeadGPT, an AI Business Intelligence Assistant.

    Analyze the following real business analytics data
    and answer the user's question professionally.

    IMPORTANT:
    - Use ONLY the analytics data provided.
    - Give business-focused insights.
    - Mention trends and patterns.
    - Give actionable recommendations.
    - Keep response concise but intelligent.

    USER QUESTION:
    {user_question}

    ANALYTICS DATA:
    {analytics_summary}

    PROFESSIONAL BUSINESS INSIGHT:
    """

    # =================================================
    # LLM RESPONSE
    # =================================================

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )

    return response.choices[0].message.content