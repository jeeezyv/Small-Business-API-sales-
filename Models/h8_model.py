import sqlite3
from pathlib import Path

def sales_per_weekday():
   data_folder = Path ("Data")
   db_filename = data_folder / "Primary Database.db"
   
   
   conn = sqlite3.connect(db_filename)
   cur = conn.cursor()
   #productSalesPerDay = cur.execute("""Select date from sales""").fetchall()
   #print(productSalesPerDay)
   productSalesPerDay = cur.execute("""Select distinct week_day,sum(total_sales) from date 
                                    a join sales b on a.date =b.date group by week_day """).fetchall()
   # dates = cur.execute("""Select week_day  from date a join sales b on a.date =b.date """).fetchall()
   # for row in productSalesPerDay:
   #   print(row[0], row[1])
   result = [{'weekday': row[0], 'total_sales': row[1]} for row in productSalesPerDay]
   # days= cur.execute("""Select date from sales order by date desc""").fetchall()
   # print(days)
   # cur.close()
   conn.close()

   return result

#import sqlite3
#from pathlib import Path
#
#def sales_per_weekday():
#   data_folder = Path("Data")
#   db_filename = data_folder / "Primary Database.db"
#
#   try:
#       conn = sqlite3.connect(db_filename)
#       cur = conn.cursor()
#
#       productSalesPerDay = cur.execute("""
#           SELECT week_day, SUM(total_sales)
#           FROM date a
#           JOIN sales b ON a.date = b.date
#           GROUP BY week_day
#       """).fetchall()
#
#       result = [{'weekday': row[0], 'total_sales': row[1]} for row in productSalesPerDay]
#
#       cur.close()
#       conn.close()
#
#       return result
#
#   except sqlite3.Error as e:
#       # Print the error for debugging
#       print("SQLite error:", e)
#       return {'error': 'An error occurred while retrieving data'}
#
#   except Exception as e:
#       # Handle other exceptions
#       print("Error:", e)
#       return {'error': 'An unexpected error occurred'}