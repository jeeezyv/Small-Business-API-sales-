import sqlite3
from pathlib import Path

def get_sales_qty_product_type():
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

        #1st query sum of sales $ by month 

    query = """
                Select 
                    p.Product_Type, SUM (s.Net_Quantity) AS sales_qty
                FROM 
                    Sales AS s
                Join 
                    Product_Table AS p on s.Product_ID = p.Product_ID 
                Group By
                    p.Product_Type
            """


        # Execute the query and fetch the results
    sales_qty_product_type = cur.execute(query).fetchall()

        # Print the results
    # for row in sales_qty_product_type:
    #     Product_Type, sales_qty = row
    #     print(f"Product_Type: {Product_Type}, sales_qty: {sales_qty}")

    result = [{'Product type': row[0], 'Sales Qty': row[1]} for row in sales_qty_product_type]
        #close cursor
    cur.close()

        #close connection
    conn.close()

    return (result)
    