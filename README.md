# 📊 Customer Churn Prediction App

This is an interactive machine learning application built with **Streamlit** to predict whether a customer is likely to churn based on various features.

## 🚀 How It Works

- Loads a pre-trained Logistic Regression model.
- Accepts numeric input for features.
- Predicts churn using the provided values.
- Provides feedback on whether a customer is likely to stay or churn.

## 🧠 Model Used

- **Logistic Regression**
- Trained on the Telco Customer Churn dataset.
- Stored in `models/logistic_regression_model.pkl`.

## 📁 Project Structure

Customer_Churn_Prediction/
│
├── src/
│   └── predict.py
├── models/
│   ├── logistic_regression_model.pkl
│   └── model_features.pkl
├── data/
│   └── cleaned_customer_churn_dataset.csv
├── app.py
├── requirements.txt
└── README.md

## 🧪 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

🌐 Deployment

Deployed via Streamlit Cloud.

📌 Built with ❤️ by Zeeshan 
