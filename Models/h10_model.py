import sqlite3
from flask import jsonify

def delete_product_by_id(product_id):
    # Define the path to the database
    db_filename = "Data/Primary Database.db"
    
    # Connect to the database
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    # Construct the SQL query to delete the product based on product_id
    delete_query = "DELETE FROM Product_Table WHERE product_id = ?"
    
    try:
        # Execute the query with the provided product_id
        cur.execute(delete_query, (product_id,))
        
        # Check if any rows were affected (i.e., if the product existed and was deleted)
        if cur.rowcount > 0:
            # Commit the changes to the database
            conn.commit()
            message = "Product with product_id {} has been deleted.".format(product_id)
        else:
            message = "Product with product_id {} not found.".format(product_id)
    except sqlite3.Error as e:
        # Handle any potential database errors
        message = "Error deleting product: " + str(e)
    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

    return jsonify({"message": message})