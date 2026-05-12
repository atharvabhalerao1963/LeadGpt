from fastapi import APIRouter

from fastapi.responses import FileResponse

from app.services.report_service import (
    generate_business_report
)

router = APIRouter()

# =====================================================
# PDF REPORT API
# =====================================================

@router.get("/generate-report")
def generate_report():

    report_path = generate_business_report()

    return FileResponse(
        report_path,
        media_type="application/pdf",
        filename="LeadGPT_Business_Report.pdf"
    )