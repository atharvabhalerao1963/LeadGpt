import pandas as pd

from pathlib import Path

# =====================================================
# LOAD DATASET
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_PATH = BASE_DIR / "app" / "data" / "project_sales_data.csv"

df = pd.read_csv(DATA_PATH)

# =====================================================
# CONVERSATIONAL ANALYTICS ENGINE
# =====================================================

def analyze_business_question(question):

    question = question.lower()

    # =================================================
    # TOP SALES AGENT
    # =================================================

    if "top sales agent" in question or \
       "best sales agent" in question:

        top_agent = (
            df["Sales_Agent"]
            .value_counts()
            .idxmax()
        )

        top_count = (
            df["Sales_Agent"]
            .value_counts()
            .max()
        )

        return f"""
        🏆 Top Sales Agent: {top_agent}

        Lead Count: {top_count}

        Insight:
        This sales agent currently handles the highest lead volume in the business pipeline.
        """

    # =================================================
    # TOP LEAD SOURCE
    # =================================================

    elif "top lead source" in question or \
         "best lead source" in question:

        top_source = (
            df["Source"]
            .value_counts()
            .idxmax()
        )

        top_count = (
            df["Source"]
            .value_counts()
            .max()
        )

        return f"""
        📞 Top Lead Source: {top_source}

        Lead Count: {top_count}

        Insight:
        This acquisition channel currently generates the highest lead volume.
        """

    # =================================================
    # CONVERTED LEADS
    # =================================================

    elif "converted leads" in question:

        converted = len(
            df[
                df["Status"]
                .astype(str)
                .str.lower()
                .str.contains("converted", na=False)
            ]
        )

        return f"""
        ✅ Total Converted Leads: {converted}

        Insight:
        These leads successfully completed the conversion process.
        """

    # =================================================
    # TOP LOCATION
    # =================================================

    elif "top location" in question or \
         "best location" in question:

        top_location = (
            df["Location"]
            .fillna("Unknown")
            .value_counts()
            .idxmax()
        )

        location_count = (
            df["Location"]
            .fillna("Unknown")
            .value_counts()
            .max()
        )

        return f"""
        🌍 Top Location: {top_location}

        Lead Count: {location_count}

        Insight:
        This region currently contributes the highest lead volume.
        """

    # =================================================
    # TOTAL LEADS
    # =================================================

    elif "total leads" in question:

        total = len(df)

        return f"""
        📊 Total Leads: {total}

        Insight:
        This represents the total business lead volume in the dataset.
        """

    # =================================================
    # DEFAULT RESPONSE
    # =================================================

    else:

        return """
        ❌ Sorry, I could not understand the business question.

        Try asking questions like:
        - Who is the top sales agent?
        - What is the top lead source?
        - How many converted leads exist?
        - Which location generates most leads?
        """