# import pandas as pd
# from prophet import Prophet

# # LOAD DATASET

# df = pd.read_csv("/Users/atharvabhalerao/Desktop/LeadGPT/backend/app/forecasting/project_sales_data.csv")

# # DATE CONVERSION

# df["Created"] = pd.to_datetime(
#     df["Created"],
#     dayfirst=True
# )

# # DAILY LEADS

# daily_leads = (
#     df.groupby(df["Created"].dt.date)
#     .size()
#     .reset_index(name="y")
# )

# daily_leads.columns = ["ds", "y"]

# # TRAIN MODEL

# model = Prophet()

# model.fit(daily_leads)

# def get_forecast():

#     future = model.make_future_dataframe(periods=30)

#     forecast = model.predict(future)

#     result = forecast[["ds", "yhat"]].tail(30)

#     result["ds"] = result["ds"].astype(str)

#     return result.to_dict(orient="records")


import pandas as pd
from prophet import Prophet
from pathlib import Path

# =====================================================
# BASE DIRECTORY
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# =====================================================
# DATASET PATH
# =====================================================

DATA_PATH = BASE_DIR / "app" / "data" / "project_sales_data.csv"

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv(DATA_PATH)

# =====================================================
# DATE CONVERSION
# =====================================================

df["Created"] = pd.to_datetime(
    df["Created"],
    dayfirst=True,
    errors="coerce"
)

# REMOVE INVALID DATES

df = df.dropna(subset=["Created"])

# =====================================================
# DAILY LEADS
# =====================================================

daily_leads = (
    df.groupby(df["Created"].dt.date)
    .size()
    .reset_index(name="y")
)

daily_leads.columns = ["ds", "y"]

# =====================================================
# TRAIN MODEL
# =====================================================

model = Prophet()

model.fit(daily_leads)

# =====================================================
# FORECAST FUNCTION
# =====================================================

def get_forecast():

    future = model.make_future_dataframe(periods=30)

    forecast = model.predict(future)

    result = forecast[["ds", "yhat"]].tail(30)

    result["ds"] = result["ds"].astype(str)

    return result.to_dict(orient="records")