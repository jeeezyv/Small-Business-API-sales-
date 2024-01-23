import sqlite3
from pathlib import Path


def get_unique_list_product_type():
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

    #query to get the unique list of product type
    query = """
            Select Distinct Product_Type
            FROM Product_Table
            Order By Product_Type
            """

    # Execute the query and fetch the results
    unique_products_type = cur.execute(query).fetchall()

    print('A List of Products Type:')
    
    result = [{'Product Type': row[0]} for row in unique_products_type]
    # for row in unique_products_type:
    #     print(row[0])

    cur.close()

    conn.close()

    return result