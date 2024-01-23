import sqlite3
from pathlib import Path

def get_sales_month():
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

# d.Year, d.Month_Num, '$' || CAST (SUM (s.total_sales) AS TEXT) AS monthly_sales
    query = """
            Select 
                d.Year, d.Month_Num, SUM(s.total_sales) AS monthly_sales
                
            FROM 
                Sales AS s
            Join 
                Date AS d ON s.Date = d.Date 
            Group By
                d.Year, d.Month_Num
            Order By
                d.Year, d.Month_Num;     
            """

    # Execute the query and fetch the results
    sales_month = cur.execute(query).fetchall()

    result = [{'Year': row[0], 'Month_Num': row[1], 'Monthly_Sales$': row[2]} for row in sales_month]
    # # Print the results
    # for row in sales_month:
    #     print(row)

    #close cursor
    cur.close()

    #close connection
    conn.close()

    return (result)
    