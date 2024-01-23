import sqlite3
from pathlib import Path

#Define the path to the data
data_folder = Path ("C:\\Project\\ISYS5713\\GroupProject - Fall23\\Group-Project-ISYS-5713-Hannala-Jacob")

#set the database filename
db_filename = data_folder / "Sales_Table.db"
        #Another way how to do it
            #db_filename = path ("C:\\Project\\ISYS5713\\GroupProject - Fall23\\Group-Project-ISYS-5713-Hannala-Jacob\\Sales_Table.db")

#Set the data filename
data_filename = data_folder / "Sales_Table.csv"

#Create the database
#   connect to the database
conn = sqlite3.connect(db_filename)

#   create the cursor object
cur = conn.cursor()

#   drop the table if it exists
cur.execute("DROP TABLE IF EXISTS Sales")

#   create the table
cur.execute("CREATE TABLE Sales (" + 
            "product_title TEXT, variant_title TEXT, variant_sku TEXT, order_name TEXT, day DATE, " +
            "net_quantity REAL, net_sales REAL, customer_type TEXT, api_client_title TEXT, variant_id TEXT)")


# cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cur.fetchall()
# print(tables)

#load data from data file 
#   Load data from csv file
for row in open(data_filename):
    #   skip the header row
    if row.startswith('product_title'): #my values start on the second line so need to fix that 
            continue
    #split the rows in values 
    values = row.split(',')
    #Check if there are 10 values before attempting to insert
    if len(values) == 10:
    #   insert the data into the table
        cur.execute("INSERT INTO Sales VALUES (?,?,?,?,?,?,?,?,?,?)", values)
        
#   commit the changes (when we put data into the database) (we write all the changes and then commit to put all changes into the database)
    conn.commit()

#Select all rows from the table
cur.execute("SELECT *FROM Sales")

#print the results
print(cur.fetchall())

#close cursor
cur.close()

#close connection
conn.close()

