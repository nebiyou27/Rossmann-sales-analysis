import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_cleaning import clean_data  # Assuming clean_data is in src/data_cleaning.py
from src.logging_config import logger  # Assuming logging_config.py is in src/

def explore_data(df, dataset_name="Dataset"):
    """
    Performs exploratory data analysis on the input DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
        dataset_name (str): The name of the dataset (for logging and titles).
    """
    logger.info(f"Starting exploratory data analysis for {dataset_name}...")

    try:
        # Visualize sales distribution
        if 'Sales' in df.columns:
            plt.figure(figsize=(10, 6))
            sns.histplot(df['Sales'], bins=50, kde=True, color='blue')
            plt.title(f'Sales Distribution - {dataset_name}')
            plt.xlabel('Sales')
            plt.ylabel('Frequency')
            plt.show()
            logger.info(f"Visualized sales distribution for {dataset_name}.")

        # Explore sales trends over time
        if 'Date' in df.columns and 'Sales' in df.columns:
            plt.figure(figsize=(12, 6))
            sns.lineplot(x='Date', y='Sales', data=df, ci=None)
            plt.title(f'Sales Trend Over Time - {dataset_name}')
            plt.xlabel('Date')
            plt.ylabel('Sales')
            plt.xticks(rotation=45)
            plt.show()
            logger.info(f"Visualized sales trend over time for {dataset_name}.")

        # Additional exploratory plots
        if 'DayOfWeek' in df.columns and 'Sales' in df.columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x='DayOfWeek', y='Sales', data=df)
            plt.title(f'Sales by Day of the Week - {dataset_name}')
            plt.xlabel('Day of the Week')
            plt.ylabel('Sales')
            plt.show()
            logger.info(f"Visualized sales by day of the week for {dataset_name}.")

    except KeyError as e:
        logger.error(f"KeyError during exploration of {dataset_name}: {e}")
    except Exception as e:
        logger.error(f"Error during exploratory data analysis of {dataset_name}", exc_info=True)

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
        store_df_cleaned = clean_data(store_df)

        logger.info("Data cleaning completed for train and store datasets.")

        # Perform exploratory analysis
        explore_data(train_df_cleaned, dataset_name="Train Dataset")
        explore_data(store_df_cleaned, dataset_name="Store Dataset")

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
    except Exception as e:
        logger.error("Error in the main execution block", exc_info=True)