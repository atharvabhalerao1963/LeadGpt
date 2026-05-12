from fastapi import APIRouter

from app.services.analytics_service import (
    top_sales_agents,
    top_lead_sources,
    lead_status_distribution,
    top_locations,
    converted_leads_count,
    total_leads,
    get_product_ids,
    get_sales_agents,
    get_locations
)

router = APIRouter()

# =====================================================
# TOP SALES AGENTS
# =====================================================

@router.get("/top-agents")
def get_top_agents():

    return top_sales_agents()


# =====================================================
# TOP LEAD SOURCES
# =====================================================

@router.get("/top-sources")
def get_top_sources():

    return top_lead_sources()


# =====================================================
# LEAD STATUS DISTRIBUTION
# =====================================================

@router.get("/lead-status")
def get_lead_status():

    return lead_status_distribution()


# =====================================================
# TOP LOCATIONS
# =====================================================

@router.get("/top-locations")
def get_top_locations_api():

    return top_locations()


# =====================================================
# CONVERTED LEADS
# =====================================================

@router.get("/converted-leads")
def get_converted_leads():

    return converted_leads_count()


# =====================================================
# TOTAL LEADS
# =====================================================

@router.get("/total-leads")
def get_total_leads():

    return total_leads()



# =====================================================
# PRODUCT IDS
# =====================================================

@router.get("/product-ids")
def product_ids():

    return get_product_ids()


# =====================================================
# SALES AGENTS
# =====================================================

@router.get("/sales-agents")
def sales_agents():

    return get_sales_agents()


# =====================================================
# LOCATIONS
# =====================================================

@router.get("/locations")
def locations():

    return get_locations()


# =====================================================
# PRODUCT IDS
# =====================================================

@router.get("/product-ids")
def product_ids():

    return get_product_ids()


# =====================================================
# SALES AGENTS
# =====================================================

@router.get("/sales-agents")
def sales_agents():

    return get_sales_agents()


# =====================================================
# LOCATIONS
# =====================================================

@router.get("/locations")
def locations():

    return get_locations()