import pandas as pd
from prophet import Prophet

# LOAD DATASET

df = pd.read_csv("/Users/atharvabhalerao/Desktop/LeadGPT/backend/app/forecasting/project_sales_data.csv")

# CONVERT DATE

df["Created"] = pd.to_datetime(df["Created"])

# DAILY LEAD COUNT

daily_leads = (
    df.groupby(df["Created"].dt.date)
    .size()
    .reset_index(name="y")
)

daily_leads.columns = ["ds", "y"]

# CREATE MODEL

model = Prophet()

model.fit(daily_leads)

# FUTURE DATES

future = model.make_future_dataframe(periods=30)

# FORECAST

forecast = model.predict(future)

# SAVE FORECAST

forecast.to_csv("forecast_output.csv", index=False)

print(forecast[["ds", "yhat"]].tail(20))