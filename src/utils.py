import pandas as pd
from datetime import datetime, timedelta

def create_date_features(df):
    """
    Extracts date features from the 'Date' column.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with added date features.
    """
    df['Date'] = pd.to_datetime(df['Date'])
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df['DayOfYear'] = df['Date'].dt.dayofyear
    # ... add more date features as needed ...
    return df

# ... other utility functions (create_promo_features, handle_missing_values, etc.) ...

def calculate_metrics(y_true, y_pred):
    """
    Calculates and returns a dictionary of evaluation metrics.

    Args:
        y_true (array-like): True values.
        y_pred (array-like): Predicted values.

    Returns:
        dict: Dictionary of evaluation metrics (RMSE, MAE, R-squared).
    """
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return {'RMSE': rmse, 'MAE': mae, 'R-squared': r2}