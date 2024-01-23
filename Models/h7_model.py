import sqlite3
from pathlib import Path
#
#def sales_per_product():
#    data_folder = Path ("Data")
#    db_filename = data_folder / "Primary Database.db"
#    
#    
#    conn = sqlite3.connect(db_filename)
#    cur = conn.cursor()
#    
#    productSales = cur.execute("""Select Product_Name, sum(total_sales) from Product_Table a join sales b on a.product_id = b.product_id where total_sales > 0 group 
#                                 by Product_name order by total_sales desc """).fetchall()
#    
#    
#    #sales = cur.execute("""Select a.product_id from product_table a join sales b on a.product_id = b.product_id """).fetchall()
#    
#    result = [{'Product': row[0], 'Total Sales': row[1]} for row in productSales]
#    # result = [{'weekday': row[0], 'total_sales': row[1]} for row in productSalesPerDay]
#
#    #sales2= cur.execute("""Select distinct product_id from product_table""").fetchall()
#    
#    #print (sales2)
#    #for row in productSales:
#    #    print(f'Product:,{row[0]},Total Sales: , {row[1]}')
#    
#    
#    
#    cur.close()
#    
#    conn.close()
#
#    return result

def sales_per_product(limit=None):
    data_folder = Path ("Data")
    db_filename = data_folder / "Primary Database.db"
    
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    
    if limit is not None:
        productSales = cur.execute(f"""Select Product_Name, sum(total_sales) from Product_Table a join sales b on a.product_id = b.product_id where total_sales > 0 group 
                                     by Product_name order by total_sales desc LIMIT {limit}""").fetchall()
    else:
        productSales = cur.execute("""Select Product_Name, sum(total_sales) from Product_Table a join sales b on a.product_id = b.product_id where total_sales > 0 group 
                                     by Product_name order by total_sales desc """).fetchall()

    result = [{'Product': row[0], 'Total Sales': row[1]} for row in productSales]

    cur.close()
    conn.close()

    return result


# Old API Endpoint

#@app.route("/SalesPerProduct", methods=['GET'])
#def get_spp():
#   
#   Sales_Per_Product = h7_model.sales_per_product()
#   # orginal # return jsonify(Sales_Per_Product), 200
#   # Create an empty list to store one product per line
#   result_lines = []
#    
#   for product in Sales_Per_Product:
#        # Round the Total Sales to two decimal places
#        total_sales_rounded = round(product['Total Sales'], 2)
#        
#        # Format the product information and append it to the list
#        result_lines.append(f"Product: {product['Product']}, Total Sales: {total_sales_rounded:.2f}<br>")
#    
#    # Join the lines with line breaks to make them separate lines in the response
#   result_text = "\n".join(result_lines)
#    
#   return result_text, 200