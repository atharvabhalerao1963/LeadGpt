import pandas as pd
from pathlib import Path

# =====================================================
# LOAD DATASET
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_PATH = BASE_DIR / "app" / "data" / "project_sales_data.csv"

df = pd.read_csv(DATA_PATH)

# =====================================================
# ANALYTICS FUNCTIONS
# =====================================================

def top_sales_agents():

    agent_counts = (
        df["Sales_Agent"]
        .value_counts()
        .head(5)
    )

    results = []

    for agent, count in agent_counts.items():

        results.append({
            "Sales Agent": agent,
            "Lead Count": int(count)
        })

    return results


# =====================================================

def top_lead_sources():

    source_counts = (
        df["Source"]
        .value_counts()
        .head(5)
    )

    results = []

    for source, count in source_counts.items():

        results.append({
            "Lead Source": source,
            "Count": int(count)
        })

    return results


# =====================================================

def lead_status_distribution():

    status_counts = (
        df["Status"]
        .value_counts()
    )

    results = []

    for status, count in status_counts.items():

        results.append({
            "Status": status,
            "Count": int(count)
        })

    return results


# =====================================================

def top_locations():

    location_counts = (
        df["Location"]
        .fillna("Unknown")
        .value_counts()
        .head(10)
    )

    results = []

    for location, count in location_counts.items():

        results.append({
            "Location": location,
            "Lead Count": int(count)
        })

    return results


# =====================================================

def converted_leads_count():

    converted = df[
        df["Status"]
        .astype(str)
        .str.lower()
        .str.contains("converted", na=False)
    ]

    return {
        "Converted Leads": len(converted)
    }


# =====================================================

def total_leads():

    return {
        "Total Leads": len(df)
    }


# =====================================================

def get_product_ids():

    products = (
        df["Product_ID"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    products.sort()

    return products


# =====================================================

def get_sales_agents():

    agents = (
        df["Sales_Agent"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    agents.sort()

    return agents


# =====================================================

def get_locations():

    locations = (
        df["Location"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    locations.sort()

    return locations


# =====================================================

def get_product_ids():

    products = (
        df["Product_ID"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    products.sort()

    return products


# =====================================================

def get_sales_agents():

    agents = (
        df["Sales_Agent"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    agents.sort()

    return agents


# =====================================================

def get_locations():

    locations = (
        df["Location"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    locations.sort()

    return locations