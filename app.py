import streamlit as st
import pandas as pd
import joblib
from src.predict import make_prediction

# Load model and features
model = joblib.load("models/logistic_regression_model.pkl")
feature_columns = joblib.load("models/model_features.pkl")

# App Title
st.set_page_config(page_title="Customer Churn Prediction", layout="centered")
st.title("📊 Customer Churn Prediction App")

# Input Fields
st.header("Enter Customer Information")
user_input = {}

for feature in feature_columns:
    user_input[feature] = st.number_input(f"{feature}", step=1.0)

# Prediction
if st.button("Predict Churn"):
    input_df = pd.DataFrame([user_input])
    prediction = make_prediction(model, input_df)
    st.subheader("Prediction Result")
    if prediction == 1:
        st.error("❌ This customer is likely to churn.")
    else:
        st.success("✅ This customer is likely to stay.")
