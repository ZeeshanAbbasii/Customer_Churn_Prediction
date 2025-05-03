
# 📊 Customer Churn Prediction

A full machine learning pipeline built to **predict customer churn** using the Telco Customer dataset. The project includes preprocessing, model training, evaluation, visualization, and a Streamlit web app for real-time predictions.

---

## 🔍 Features

- Data Cleaning and Preprocessing
- Feature Engineering
- Multiple ML Models (Logistic Regression, Random Forest, XGBoost, LightGBM, SVM, KNN, MLP, CatBoost, Gradient Boosting)
- Model Evaluation & Comparison
- Interactive Streamlit App for Predictions
- Visual Insights with Seaborn and Matplotlib
- GitHub-ready project structure

---

## 🧠 Models Used

- Logistic Regression
- Random Forest
- XGBoost
- LightGBM
- Support Vector Machine
- K-Nearest Neighbors
- Multi-Layer Perceptron
- CatBoost
- Gradient Boosting

---

## 💾 Dataset

- Source: Cleaned version of Telco Customer Churn Dataset
- Files: 
  - `data/Telco-Customer-Churn-dataset-cleaned.csv`
  - `data/cleaned_customer_churn_dataset.csv`

---

## 📂 Folder Structure

```
Customer_Churn_Prediction/
├── app.py                        # Streamlit app
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── data/                        # Raw and cleaned datasets
├── src/                         # Source code for training, predicting, evaluation
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── evaluate.py
├── models/                      # Saved model and features
│   ├── logistic_regression_model.pkl
│   └── model_features.pkl
├── visuals/                     # All saved plots
├── notebooks/                   # Jupyter notebook with full analysis
│   └── customer_churn_analysis.ipynb
```

---

## 🚀 How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/ZeeshanAbbasii/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## 🌐 Streamlit Cloud Deployment

> Use `app.py` as the entry point.

---

## 🖼️ Visual Insights

Stored in `visuals/`:
- `churn_insights.png`
- `contract_vs_churn.png`
- `payment_method_vs_churn.png`
- `satisfaction_score_violinplot.png`
- `techsupport_vs_churn.png`
- `totalcharges_violinplot.png`

---

## 👨‍💻 Author

**Zeeshan Abbasi**  
Software Engineering Student  
GitHub: [ZeeshanAbbasii](https://github.com/ZeeshanAbbasii)

---

## 📌 Disclaimer

This project is for educational purposes only. Predictions should not be used in real business decisions without further validation.
