import os

from pathlib import Path

import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

# =====================================================
# LOAD DATASET
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_PATH = BASE_DIR / "app" / "data" / "project_sales_data.csv"

REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

# =====================================================
# GENERATE PDF REPORT
# =====================================================

def generate_business_report():

    report_path = REPORTS_DIR / "LeadGPT_Business_Report.pdf"

    # =================================================
    # ANALYTICS
    # =================================================

    total_leads = len(df)

    converted = len(
        df[
            df["Status"]
            .astype(str)
            .str.lower()
            .str.contains("converted", na=False)
        ]
    )

    top_agent = (
        df["Sales_Agent"]
        .value_counts()
        .idxmax()
    )

    top_source = (
        df["Source"]
        .value_counts()
        .idxmax()
    )

    # =================================================
    # PDF SETUP
    # =================================================

    doc = SimpleDocTemplate(
        str(report_path)
    )

    styles = getSampleStyleSheet()

    elements = []

    # =================================================
    # TITLE
    # =================================================

    elements.append(
        Paragraph(
            "LeadGPT AI Business Intelligence Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    # =================================================
    # BUSINESS SUMMARY
    # =================================================

    summary = f"""
    <b>Total Leads:</b> {total_leads}<br/><br/>

    <b>Converted Leads:</b> {converted}<br/><br/>

    <b>Top Sales Agent:</b> {top_agent}<br/><br/>

    <b>Top Lead Source:</b> {top_source}<br/><br/>
    """

    elements.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    # =================================================
    # AI RECOMMENDATIONS
    # =================================================

    recommendations = f"""
    <b>AI Recommendations:</b><br/><br/>

    • Focus more on high-performing lead sources.<br/><br/>

    • Replicate the workflow of top-performing sales agents.<br/><br/>

    • Improve lead qualification to reduce junk leads.<br/><br/>

    • Optimize follow-up strategies for better conversion.<br/><br/>
    """

    elements.append(
        Paragraph(
            recommendations,
            styles["BodyText"]
        )
    )

    # =================================================
    # BUILD PDF
    # =================================================

    doc.build(elements)

    return str(report_path)