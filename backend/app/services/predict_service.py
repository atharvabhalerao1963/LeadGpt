import joblib
import pandas as pd

model = joblib.load("ml_models/ficzon_lead_model.pkl")

def predict_lead(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": str(prediction),
        "probability": float(probability)
    }