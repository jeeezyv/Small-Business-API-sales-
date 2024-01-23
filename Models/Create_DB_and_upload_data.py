import sqlite3
from pathlib import Path

#Define the path to the data
data_folder = Path ("Data")

#set the database filename
db_filename = data_folder / "Primary Database.db"
        #Another way how to do it
            #db_filename = path ("C:\\Project\\ISYS5713\\GroupProject - Fall23\\Group-Project-ISYS-5713-Hannala-Jacob\\Sales_Table.db")

#Set the data filename
# I created a different variable for each CSV that will be uploaded. Each CSV includes only the data for the intended table

Sales_data_filename = data_folder / "Sales_Table_Primary.csv"
Date_data_filename = data_folder /  "Date_Table_Primary.csv"
Product_data_filename = data_folder / "Product_table_Primary.csv"
#Create the database
#   connect to the database
conn = sqlite3.connect(db_filename)

#   create the cursor object
cur = conn.cursor()

# Just dropping each of the three tables we are creating

cur.execute("DROP TABLE IF EXISTS Product_Table")
cur.execute("DROP TABLE IF EXISTS Sales")
cur.execute("DROP TABLE IF EXISTS Date")

# Here I state a name for each column in the table being created, the variable type(and maximum length), and if it can be null(blank) or not
# you will notice that I assign the Primary Key to one of my colmns I have created for the table
cur.executescript("CREATE TABLE Product_Table ("+
           "product_id INT NOT NULL," +
           "Product_Type VARCHAR(100),"+
  "Product_name VARCHAR(100),"+
  "Product_Cat_1 VARCHAR(100),"+
  "Product_Cat_2 VARCHAR(100),"+
  "PRIMARY KEY (product_id));"+

  # The same is being done here

"CREATE TABLE Date("+
  "Date DATE NOT NULL,"+
  "Month_Num INT NOT NULL,"+
  "Year INT NOT NULL,"+
  "Quarter_Num INT NOT NULL,"+
  "Week_Num INT NOT NULL,"+
  "Business_Day CHAR(1) NOT NULL,"+
 "Week_Day VARCHAR(50) NOT NULL,"+
  "PRIMARY KEY (Date));"+
# The same is being done here. You will notice that two of the columns in the sales table are Foreign Keys from the Product and Date Table

"CREATE TABLE Sales("+
    "Unique_id VARCHAR(50) NOT NULL, " +
  "Order_ID VARCHAR(50) NOT NULL,"+
  "order_name VARCHAR(10) NOT NULL,"+
  "Net_Quantity INT NOT NULL,"+
  "total_sales VARCHAR(50) NOT NULL,"+
  "Channel_ID VARCHAR(50) NOT NULL,"+
  "Product_ID INT NOT NULL,"+
  "Date DATE NOT NULL,"+
  "customer_type NOT NULL,"+
  "PRIMARY KEY (Unique_id),"+
  "FOREIGN KEY (Product_ID) REFERENCES Product_Table(product_id),"+
  "FOREIGN KEY (Date) REFERENCES Date(Date));"
  )

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print(tables)


#load Sales data from Sales file 
#   Load data from csv file
for row in open(Sales_data_filename):
    #   skip the header row
    if row.startswith('Order_ID'): 
            continue
    #split the rows in values 
    values = row.strip().split(',')
    #Check if there are 8 values before attempting to insert. This number  has to match the number of colmns in the CSV
    if len(values) == 9:
    #   insert the data into the table. The number of "?" need to match the number of columns
        cur.execute("INSERT INTO Sales VALUES (?,?,?,?,?,?,?,?,?)", values)
        
#   commit the changes (when we put data into the database) (we write all the changes and then commit to put all changes into the database)
    conn.commit()


 #load Date data from Date file  
for row in open(Date_data_filename):
  #   skip the header row
    if row.startswith('Date'): 
            continue
    #split the rows in values 
    values = row.strip().split(',')
    #Check if there are 7 values before attempting to insert. This number  has to match the number of colmns in the CSV
    if len(values) == 7:
    #   insert the data into the table. The number of "?" need to match the number of columns
        cur.execute("INSERT INTO Date VALUES (?,?,?,?,?,?,?)", values)


 #load Product data from Produce file  
for row in open(Product_data_filename):
  #   skip the header row
    if row.startswith('product_id'): 
            continue
    #split the rows in values 
    values = row.split(',')
    #Check if there are 5 values before attempting to insert. This number  has to match the number of colmns in the CSV
    if len(values) == 5:
    #   insert the data into the table. The number of "?" need to match the number of columns
        cur.execute("INSERT INTO Product_Table VALUES (?,?,?,?,?)", values)

#Select all rows from the table
TestTable = cur.execute("SELECT product_type FROM product_table").fetchall()

#print the results
print(TestTable)

# Commit
conn.commit()

#close cursor
cur.close()

#close connection
conn.close()


