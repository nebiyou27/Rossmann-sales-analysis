
# Retail-Sales-Prediction-ML-regression-


In this project, I have attempted to analyze the retail sales dataset of Rossmann stores and build a predictive model to forecast the sales of any Rossmann store for any date. No personal information of customer is provided in this dataset.



# PROBLEM STATEMENT 
Rossmann operates over 3,000 drug stores in 7 European countries. Currently, Rossmann store managers are tasked with predicting their daily sales for up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. With thousands of individual managers predicting sales based on their unique circumstances, the accuracy of results can be quite varied. Two datasets are given: one with store data and the other with historical sales data of 1115 stores from January 2013 to July 2015. The main objective is to understand existing data and after identifying the key factors that will predict future sales, a predictive model will be built for making forecasts about future sales.

# APPROACH 
1. Understanding the business task.
2. Import relevant libraries and define useful functions.
3. Reading data from files given.
4. Data pre-processing, which involves inspection of both datasets and data cleaning.
5. Exploratory data analysis, to find which factors affect sales and how they affect it.
6. Feature engineering, to prepare data for modelling.
7. Modelling data and comparing the models to find out most suitable one for forecasting.
8. Conclusion and recommendations to boost sales.

# Exploratory Data Analysis
The following insights were gained from EDA:
* Mondays have most sales since most of the Sundays are closed.
* Promotions seem to have a significant effect on sales but not for the number of customers. It is advisable to spend more on promos to get higher returns.
* Store type b has higher sales and customers per store than other store types. More Store type b must be opened.
* Assortment b is available only at store type b and it has more sales and customers than any other assortment. More assortment b must be stocked to meet the demands of customers.
* Weekly sales and customers peak at the mid-December. It may be guessed that people buy drugs in advance just before the shops close for the holiday season.

  
# Methodology
The project follows the following steps:
* Data exploration: Analysing the dataset and getting insights about the data.
* Data preprocessing: Handling missing values and feature engineering.
* Feature engineering: Creating new features that could impact the target variable.
* Model selection: Testing different machine learning regression models.
* Model training and evaluation: Training the selected model and evaluating its performance using cross-validation.
* Hyperparameter tuning: Optimizing the model's hyperparameters.
* Final model: Training the final model on the entire dataset.
* Prediction: Using the final model to make sales predictions for the test set.

# Conclusion

The developed machine learning regression model can predict daily sales for up to six weeks in advance for Rossmann stores with a high level of accuracy. The model can help Rossmann store managers make informed decisions regarding inventory management, staffing, and promotional strategies, ultimately leading to increased sales and profitability for the business.

