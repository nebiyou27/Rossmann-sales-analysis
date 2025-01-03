import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from src.data_cleaning import clean_data
from src.logging_config import logger
import joblib

def train_model(df):
    """
    Trains a machine learning model.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        tuple: Trained model, X_train, X_test, y_train, y_test
    """
    logger.info("Starting model training...")

    # Feature engineering and data preparation
    X = df[['DayOfWeek', 'Month', 'CompetitionDistance']]  # Example features
    y = df['Sales']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestRegressor(random_state=42))
    ])
    
    try:
        pipeline.fit(X_train, y_train)
        logger.info("Model training completed.")
    except Exception as e:
        logger.error("Error during model training", exc_info=True)
        raise e

    # Model evaluation
    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    logger.info(f"Model Evaluation - MSE: {mse}, R2: {r2}")

    # Save the model
    joblib.dump(pipeline, 'models/sales_model.pkl')
    logger.info("Trained model saved to models/sales_model.pkl")

    return pipeline, X_train, X_test, y_train, y_test

if __name__ == "__main__":
    data_path = "data/train.csv"
    df = pd.read_csv(data_path)
    df_cleaned = clean_data(df)
    model, X_train, X_test, y_train, y_test = train_model(df_cleaned)
