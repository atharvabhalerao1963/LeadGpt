# import pandas as pd
# from prophet import Prophet

# # LOAD DATASET

# df = pd.read_csv("/Users/atharvabhalerao/Desktop/LeadGPT/backend/app/forecasting/project_sales_data.csv")

# # CONVERT DATE

# df["Created"] = pd.to_datetime(df["Created"])

# # DAILY LEAD COUNT

# daily_leads = (
#     df.groupby(df["Created"].dt.date)
#     .size()
#     .reset_index(name="y")
# )

# daily_leads.columns = ["ds", "y"]

# # CREATE MODEL

# model = Prophet()

# model.fit(daily_leads)

# # FUTURE DATES

# future = model.make_future_dataframe(periods=30)

# # FORECAST

# forecast = model.predict(future)

# # SAVE FORECAST

# forecast.to_csv("forecast_output.csv", index=False)

# print(forecast[["ds", "yhat"]].tail(20))


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
# CONVERT DATE
# =====================================================

df["Created"] = pd.to_datetime(
    df["Created"],
    dayfirst=True,
    errors="coerce"
)

# REMOVE INVALID DATES

df = df.dropna(subset=["Created"])

# =====================================================
# DAILY LEAD COUNT
# =====================================================

daily_leads = (
    df.groupby(df["Created"].dt.date)
    .size()
    .reset_index(name="y")
)

daily_leads.columns = ["ds", "y"]

# =====================================================
# CREATE MODEL
# =====================================================

model = Prophet()

model.fit(daily_leads)

# =====================================================
# FUTURE DATES
# =====================================================

future = model.make_future_dataframe(periods=30)

# =====================================================
# FORECAST
# =====================================================

forecast = model.predict(future)

# =====================================================
# SAVE FORECAST
# =====================================================

OUTPUT_PATH = BASE_DIR / "forecast_output.csv"

forecast.to_csv(OUTPUT_PATH, index=False)

# =====================================================
# PRINT RESULTS
# =====================================================

print(forecast[["ds", "yhat"]].tail(20))