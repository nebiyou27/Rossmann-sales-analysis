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

    # Visualize sales distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Sales'], bins=50)
    plt.title('Sales Distribution')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.show()
    logger.info("Visualized sales distribution.")

    # Explore sales trends over time
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Sales', data=df)
    plt.title('Sales Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.show()
    logger.info("Visualized sales trend over time.")

    # ... Add more exploration functions as needed ...

if __name__ == "__main__":
    data_path = "C:\\Users\\neba\\Rossmann-sales-analysis\\data\\test.csv" 
    df = pd.read_csv(data_path) 
    df_cleaned = clean_data(df) 

    explore_data(df_cleaned)