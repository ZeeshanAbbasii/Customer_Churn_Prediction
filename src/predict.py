import pandas as pd

def make_prediction(model, input_df):
    """
    Make a prediction using a trained model and user input.

    Parameters:
        model: Trained machine learning model
        input_df (pd.DataFrame): Input features for prediction

    Returns:
        int or None: 0 (No Churn), 1 (Churn), or None on error
    """
    try:
        return model.predict(input_df)[0]
    except Exception as e:
        print(f"[Prediction Error] {e}")
        return None
