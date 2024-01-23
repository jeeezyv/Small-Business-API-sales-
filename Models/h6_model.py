import sqlite3
from pathlib import Path
#
#def get_list_of_products(limit=None): 
#    data_folder = Path ("Data")
#    db_filename = data_folder / "Primary Database.db"
#
#
#    conn = sqlite3.connect(db_filename)
#    cur = conn.cursor()
#
#    # If a limit was provided, add a LIMIT clause to the SQL query
#    if limit is not None:
#        uniqueProducts = cur.execute(f"""Select Product_Name, Product_id from Product_Table order by Product_Name asc LIMIT {limit}""").fetchall()
#    else:
#        uniqueProducts = cur.execute("""Select Product_Name, Product_id from Product_Table order by Product_Name asc """).fetchall()
#
#
#    print('A List of Products:')
#
#    result = [{'Product': row[0], 'Product_id': row[1]} for row in uniqueProducts]
#    #for row in uniqueProducts:
#    #    print(row[0])
#
#    # cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
#    # tables = cur.fetchall()
#    # print(tables)
#
#    cur.close()
#
#    conn.close()
#
#    return result




def get_list_of_products(limit=None, product_type=None):
    data_folder = Path("Data")
    db_filename = data_folder / "Primary Database.db"

    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    if limit is not None and product_type is not None:
        uniqueProducts = cur.execute(
            f"""
            SELECT Product_Name, Product_id
            FROM Product_Table
            WHERE Product_Type = ?
            ORDER BY Product_Name ASC
            LIMIT {limit}
            """, (product_type,)
        ).fetchall()
    elif limit is not None:
        uniqueProducts = cur.execute(
            f"""
            SELECT Product_Name, Product_id
            FROM Product_Table
            ORDER BY Product_Name ASC
            LIMIT {limit}
            """
        ).fetchall()
    elif product_type is not None:
        uniqueProducts = cur.execute(
            """
            SELECT Product_Name, Product_id
            FROM Product_Table
            WHERE Product_Type = ?
            ORDER BY Product_Name ASC
            """, (product_type,)
        ).fetchall()
    else:
        uniqueProducts = cur.execute(
            """
            SELECT Product_Name, Product_id
            FROM Product_Table
            ORDER BY Product_Name ASC
            """
        ).fetchall()

    result = [{'Product': row[0], 'Product_id': row[1]} for row in uniqueProducts]

    cur.close()
    conn.close()

    return result

#def get_list_of_products(limit=None, product_type=None):
#    data_folder = Path("Data")
#    db_filename = data_folder / "Primary Database.db"
#
#    conn = sqlite3.connect(db_filename)
#    cur = conn.cursor()
#
#    # If a limit and product_type were provided, add a LIMIT clause and a WHERE clause to the SQL query
#    if limit is not None and product_type is not None:
#        uniqueProducts = cur.execute(
#            f"""
#            SELECT Product_Name, Product_id
#            FROM Product_Table
#            WHERE Product_Type = ?
#            ORDER BY Product_Name ASC
#            LIMIT {limit}
#            """, (product_type,)
#        ).fetchall()
#    else:
#        # If only a limit is provided, use the LIMIT clause without filtering by product_type
#        uniqueProducts = cur.execute(
#            """
#            SELECT Product_Name, Product_id
#            FROM Product_Table
#            ORDER BY Product_Name ASC
#            """
#        ).fetchall()
#
#    result = [{'Product': row[0], 'Product_id': row[1]} for row in uniqueProducts]
#
#    cur.close()
#    conn.close()
#
#    return result


# OG API ENDPOINT
#@app.route("/products", methods=['GET'])
#def get_products():
#    # Get the 'limit' query parameter
#    limit = request.args.get('limit')
#
#    # Convert the limit to an integer, if it was provided
#    if limit is not None:
#        try:
#            limit = int(limit)
#        except ValueError:
#            return jsonify({'error': 'Invalid limit format'}), 400
#
#    # Get the list of products
#    products = h6_model.get_list_of_products(limit)
#
#    return jsonify(products), 200

# OG API ENDPOINT 2 

#@app.route("/products", methods=['GET'])
#
#def get_products():
#    products = h6_model.get_list_of_products()
#    return jsonify(products), 200