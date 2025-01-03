import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from src.logging_config import logger  # Import the logger

def clean_data(df):
    """
    Cleans the input DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    logger.info("Starting data cleaning...")

    try:
        # Handle missing values
        imputer = SimpleImputer(strategy='mean')
        if 'CompetitionDistance' in df.columns:
            df['CompetitionDistance'] = imputer.fit_transform(df[['CompetitionDistance']])
            logger.info("Handled missing values for CompetitionDistance.")

        # Convert Date column to datetime
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
            logger.info("Converted Date column to datetime.")

        # Feature engineering
        if 'Date' in df.columns:
            df['DayOfWeek'] = df['Date'].dt.dayofweek
            df['Month'] = df['Date'].dt.month
            logger.info("Created DayOfWeek and Month features.")

        # Fill other missing values or drop unnecessary columns
        df.fillna(0, inplace=True)  # Example: Replace all remaining NaN with 0
        logger.info("Filled remaining missing values with 0.")

    except KeyError as e:
        logger.error(f"KeyError during data cleaning: {e}")
    except Exception as e:
        logger.error("Error during data cleaning", exc_info=True)

    logger.info("Data cleaning completed.")
    return df
