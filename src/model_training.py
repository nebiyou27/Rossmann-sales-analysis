import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from src.data_cleaning import clean_data  # Assuming clean_data is in src/data_cleaning.py
from src.logging_config import logger  # Assuming logging_config.py is in src/

def train_model(train_data, target_column="Sales"):
    """
    Trains a Random Forest Regressor on the provided dataset.

    Args:
        train_data (pd.DataFrame): The training dataset.
        target_column (str): The target column name.

    Returns:
        model: Trained Random Forest model.
    """
    logger.info("Starting model training...")

    try:
        # Separate features and target
        X = train_data.drop(columns=[target_column])
        y = train_data[target_column]

        # Split into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        logger.info("Split data into training and testing sets.")

        # Train the model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        logger.info("Model training completed.")

        # Evaluate the model
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        logger.info(f"Model evaluation completed. Mean Squared Error: {mse}")

        return model

    except KeyError as e:
        logger.error(f"KeyError during model training: {e}")
    except Exception as e:
        logger.error("Error during model training", exc_info=True)

if __name__ == "__main__":
    try:
        # Update file paths
        train_path = r"C:\Users\neba\Downloads\Compressed\rossmann-store-sales\train.csv"
        store_path = r"C:\Users\neba\Downloads\Compressed\rossmann-store-sales\store.csv"

        # Load datasets
        train_df = pd.read_csv(train_path)
        store_df = pd.read_csv(store_path)

        logger.info("Loaded train and store datasets successfully.")

        # Clean the datasets
        train_df_cleaned = clean_data(train_df)

        # Merge store data if necessary (optional)
        # train_df_cleaned = train_df_cleaned.merge(store_df, on="Store", how="left")

        logger.info("Data cleaning completed for train dataset.")

        # Train the model
        trained_model = train_model(train_df_cleaned)

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
    except Exception as e:
        logger.error("Error in the main execution block", exc_info=True)
