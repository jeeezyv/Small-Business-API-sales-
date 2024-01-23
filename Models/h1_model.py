import sqlite3
from pathlib import Path

def get_sales_customer_type():
    #Define the path to the data
    data_folder = Path ("Data")
        #This line creates a variable named data_folder and assigns it a path using the Path class from the pathlib module. 
        # path "Data" is a relative path. It indicates that there is a folder named "Data" that is running the code
    #here just created another variable to sign the path above    
    db_filename = data_folder / "Primary Database.db"

    #make a connection to the database
    conn = sqlite3.connect(db_filename)

    #make a cursor that can be used to run a query on the new connection
    cur = conn.cursor()

    #1st query to sum the sales quantity (Net_Quantity) by Customer_Type (Either first-time or returning customer)

    query = """
            Select customer_type, SUM (Net_quantity) AS total_sales
            FROM Sales
            Where customer_type IN ('First-time', 'Returning')
            Group By customer_type
            """

    # Execute the query and fetch the results
    sales_by_customer_type = cur.execute(query).fetchall()

    # # Print the results
    # for row in sales_by_customer_type:
    #     customer_type, total_sales = row
    #     print(f"Customer Type: {customer_type}, Total Sales: {total_sales}")


    #2st query I will just bring the results in %
    query1 = """
            Select 
                customer_type, 
                COUNT(*) *100/ (Select COUNT (*) FROM Sales) AS Percentage
            FROM Sales
            Group By customer_type
            """
    # Execute the query and fetch the results
    percentage_by_customer_type = cur.execute(query1).fetchall()

    #close cursor
    cur.close()

    #close connection
    conn.close()

    return (sales_by_customer_type, percentage_by_customer_type)
    
    # #Print results
    # for row in percentage_by_customer_type:
    #     customer_type, percentage = row
    #     print(f"Customer_Type: {customer_type}, Percentage: {percentage:.2f}%")

    


