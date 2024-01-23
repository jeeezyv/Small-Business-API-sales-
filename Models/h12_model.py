import sqlite3
from pathlib import Path


def update_sales_quantity(order_name, product_id, new_quantity):

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

    cur.execute("UPDATE Sales SET Net_Quantity = ? WHERE order_name = ? AND Product_Id = ?", (new_quantity, order_name, product_id))
    conn.commit()  # Commit the changes to the database

    cur.close()
    conn.close()

    