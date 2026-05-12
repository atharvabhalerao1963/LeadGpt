import pandas as pd
from prophet import Prophet

# LOAD DATASET

df = pd.read_csv("/Users/atharvabhalerao/Desktop/LeadGPT/backend/app/forecasting/project_sales_data.csv")

# DATE CONVERSION

df["Created"] = pd.to_datetime(
    df["Created"],
    dayfirst=True
)

# DAILY LEADS

daily_leads = (
    df.groupby(df["Created"].dt.date)
    .size()
    .reset_index(name="y")
)

daily_leads.columns = ["ds", "y"]

# TRAIN MODEL

model = Prophet()

model.fit(daily_leads)

def get_forecast():

    future = model.make_future_dataframe(periods=30)

    forecast = model.predict(future)

    result = forecast[["ds", "yhat"]].tail(30)

    result["ds"] = result["ds"].astype(str)

    return result.to_dict(orient="records")