import pandas as pd

from pathlib import Path

# =====================================================
# LOAD DATASET
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_PATH = BASE_DIR / "app" / "data" / "project_sales_data.csv"

df = pd.read_csv(DATA_PATH)

# =====================================================
# GENERATE RECOMMENDATIONS
# =====================================================

def generate_recommendations():

    recommendations = []

    # =================================================
    # TOP LEAD SOURCE
    # =================================================

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

    recommendations.append(
        f"📞 '{top_source}' is the strongest lead source with {top_source_count} leads. Consider increasing investment in this acquisition channel."
    )

    # =================================================
    # TOP SALES AGENT
    # =================================================

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

    recommendations.append(
        f"🏆 {top_agent} is the top-performing sales agent handling {top_agent_count} leads. Analyze and replicate their workflow across the sales team."
    )

    # =================================================
    # JUNK LEADS
    # =================================================

    junk_leads = len(
        df[
            df["Status"]
            .astype(str)
            .str.lower()
            .str.contains("junk", na=False)
        ]
    )

    if junk_leads > 1000:

        recommendations.append(
            f"⚠ High number of Junk Leads detected ({junk_leads}). Improve lead qualification and filtering strategies."
        )

    # =================================================
    # CONVERSION RATE
    # =================================================

    converted = len(
        df[
            df["Status"]
            .astype(str)
            .str.lower()
            .str.contains("converted", na=False)
        ]
    )

    conversion_rate = (
        converted / len(df)
    ) * 100

    if conversion_rate < 20:

        recommendations.append(
            f"📉 Conversion rate is currently low at {conversion_rate:.1f}%. Improve follow-up workflows and customer engagement strategies."
        )

    else:

        recommendations.append(
            f"✅ Conversion rate is healthy at {conversion_rate:.1f}%. Continue optimizing successful lead conversion practices."
        )

    # =================================================
    # TOP LOCATION
    # =================================================

    top_location = (
        df["Location"]
        .fillna("Unknown")
        .value_counts()
        .idxmax()
    )

    recommendations.append(
        f"🌍 {top_location} generates the highest number of leads. Consider region-specific marketing expansion strategies."
    )

    return recommendations