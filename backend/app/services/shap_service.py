# import joblib
# import pandas as pd
# import shap

# model = joblib.load("ml_models/ficzon_lead_model.pkl")

# explainer = shap.Explainer(model.named_steps["model"])

# def generate_shap_values(data):

#     df = pd.DataFrame([data])

#     shap_values = explainer(df)

#     feature_importance = {}

#     for feature, value in zip(df.columns, shap_values.values[0]):
#         feature_importance[feature] = float(value)

#     return feature_importance