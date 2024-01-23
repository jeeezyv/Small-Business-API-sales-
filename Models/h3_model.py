import sqlite3
import pandas as pd #using pandas to help on the forecast model
import statsmodels.api as sm #library in Python that provides various statistical models and methods for various purposes including time series forecasting - including ARIMA, SARIMA, and other time series models.
from pathlib import Path

# Define the path to the data
data_folder = Path("Data")

# Here just created another variable to sign the path above    
db_filename = data_folder / "Primary Database.db"

# Make a connection to the database
conn = sqlite3.connect(db_filename)

# Make a cursor that can be used to run a query on the new connection
cur = conn.cursor()

#in these steps I am creating a unique list of Product Types to I can print before the imput line to
#ask which type of product the person what to query for the next 12 months.
    # Query the unique product types from the Sales table
unique_product_types_query = """
        SELECT DISTINCT Product_Type FROM Product_Table;
"""
    # Execute the query and fetch the unique product types into a list
unique_product_types = cur.execute(unique_product_types_query).fetchall()
    # Extract the product types from the query result
product_types = [row[0] for row in unique_product_types]
    # Display the unique product types to the user
print("Available product types:")
for i, product_type in enumerate(product_types, 1):
    print(f"{i}. {product_type}")

# Ask the user to select a product type
#here I will be considering the number of the product type that was listed above on the unique values 
while True:
    try:
        choice = int(input("Enter the number of the product type you want to forecast: "))
        if 1 <= choice <= len(product_types):
            selected_product_type = product_types[choice - 1]
            break
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Defining the SQL query with a parameter for the selected product type
query = """
        SELECT 
            d.year, 
            d.month_num, 
            SUM(s.Net_Quantity) AS monthly_sales 
        FROM 
            Sales AS s 
        JOIN 
            Date AS d ON s.Date = d.Date 
        JOIN
            Product_Table AS p ON s.Product_ID = p.Product_ID
        WHERE
            p.Product_Type = ?
        GROUP BY 
            d.year, d.month_num 
        ORDER BY 
            d.year, d.month_num;
"""

# Execute the query with the selected_product_type parameter and fetch the results into a pandas DataFrame
monthly_sales = cur.execute(query, (selected_product_type,)).fetchall()
monthly_sales_df = pd.DataFrame(monthly_sales, columns=["year", "month", "monthly_sales"])

# Creating a date index for the time series
monthly_sales_df["date"] = pd.to_datetime(monthly_sales_df["year"].astype(str) + "-" + monthly_sales_df["month"].astype(str), format="%Y-%m")
monthly_sales_df.set_index("date", inplace=True)

# Perform time series forecasting using statsmodels (e.g., SARIMA)
# You can replace forecasting model and parameters as necessary
model = sm.tsa.SARIMAX(monthly_sales_df["monthly_sales"], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = model.fit()

# Generate forecasts for the next 12 months
forecast_period = 12
forecast = results.get_forecast(steps=forecast_period)

# Print the forecasted values
print(forecast.predicted_mean)

# Close cursor
cur.close()

# Close connection
conn.close()
