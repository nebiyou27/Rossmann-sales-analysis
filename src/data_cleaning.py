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

  # Handle missing values
  imputer = SimpleImputer(strategy='mean')
  df['CompetitionDistance'] = imputer.fit_transform(df[['CompetitionDistance']])

  # Feature engineering (example)
  df['DayOfWeek'] = pd.to_datetime(df['Date']).dt.dayofweek
  df['Month'] = pd.to_datetime(df['Date']).dt.month

  logger.info("Data cleaning completed.")
  return df