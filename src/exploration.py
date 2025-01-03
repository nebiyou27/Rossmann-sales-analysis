import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_cleaning import clean_data  # Assuming clean_data is in src/data_cleaning.py
from src.logging_config import logger  # Assuming logging_config.py is in src/

def explore_data(df):
    """
    Performs exploratory data analysis on the input DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.
    """
    logger.info("Starting exploratory data analysis...")

    try:
        # Visualize sales distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(df['Sales'], bins=50, kde=True, color='blue')
        plt.title('Sales Distribution')
        plt.xlabel('Sales')
        plt.ylabel('Frequency')
        plt.show()
        logger.info("Visualized sales distribution.")

        # Explore sales trends over time
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='Date', y='Sales', data=df, ci=None)
        plt.title('Sales Trend Over Time')
        plt.xlabel('Date')
        plt.ylabel('Sales')
        plt.xticks(rotation=45)
        plt.show()
        logger.info("Visualized sales trend over time.")

        # Additional exploratory plots
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='DayOfWeek', y='Sales', data=df)
        plt.title('Sales by Day of the Week')
        plt.xlabel('Day of the Week')
        plt.ylabel('Sales')
        plt.show()
        logger.info("Visualized sales by day of the week.")

    except KeyError as e:
        logger.error(f"KeyError during exploration: {e}")
    except Exception as e:
        logger.error("Error during exploratory data analysis", exc_info=True)

if __name__ == "__main__":
    try:
        data_path = "C:\\Users\\neba\\Rossmann-sales-analysis\\data\\merged_data.csv" 
        df = pd.read_csv(data_path) 
        logger.info("Loaded data successfully.")

        # Clean the data
        df_cleaned = clean_data(df)
        logger.info("Data cleaning completed.")

        # Perform exploratory analysis
        explore_data(df_cleaned)

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
    except Exception as e:
        logger.error("Error in the main execution block", exc_info=True)
