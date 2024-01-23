import sqlite3
from pathlib import Path


def get_single_product_name_by_id(product_id):

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

   cur.execute("SELECT Product_Name FROM Product_Table WHERE Product_id = ?", (product_id,))
   product_name = cur.fetchone()

   cur.close()
   conn.close()

   return product_name[0] if product_name else None

  