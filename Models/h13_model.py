import sqlite3
from pathlib import Path


def get_sales_by_order_id(order_name):

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

    # Perform a JOIN operation between Sales and Product_Table based on Product_ID
   cur.execute("""
        SELECT s.order_name, s.Net_Quantity, s.total_sales, s.Product_ID, s.customer_type, s.Date, p.Product_Name
        FROM Sales s
        INNER JOIN Product_Table p ON s.Product_ID = p.Product_ID
        WHERE s.order_name = ?
    """, (order_name,))
   
   sales_data = cur.fetchall()
   
   cur.close()
   conn.close()

   return sales_data

   
  