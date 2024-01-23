import sqlite3

from flask import request, jsonify

def post_new_product(product_data):
    # Get data from the request
    product_id = product_data.get("product_id")
    product_type = product_data.get("product_type")
    product_name = product_data.get("product_name")
    product_cat_1 = product_data.get("product_cat_1")
    product_cat_2 = product_data.get("product_cat_2")

    # Define the path to the database
    db_filename = "Data/Primary Database.db"
    
    # Connect to the database
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    # Construct the SQL query to insert the new product
    insert_query = """INSERT INTO Product_Table (product_id, Product_Type, Product_name, Product_Cat_1, Product_Cat_2) 
    VALUES (?, ?, ?, ?, ?)"""

    # Execute the query with data from the request
    cur.execute(insert_query, (product_id, product_type, product_name, product_cat_1, product_cat_2))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()

    return "New product added to Product_Table."