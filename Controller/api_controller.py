from flask import Flask, jsonify, request
from Models import h1_model
from Models import h2_model
from Models import h4_model
from Models import h5_model
from Models import h6_model
from Models import h7_model
from Models import h8_model
from Models import h9_model
from Models import h10_model
from Models import h11_model
from Models import h12_model
from Models import h13_model
from View import printer_view
from View import api_view
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def fotoncandle_hello():
    return "<p>Hello, Welcome to Foton Candle API!</p>"

#h1_model sales by customer type

@app.route("/sales/customertype/", methods=['GET'])
def print_sales_customer_type():
    sales_by_customer_type, percentage_by_customer_type = h1_model.get_sales_customer_type()
    sales_data, percentage_data = api_view.print_sales_customertype(sales_by_customer_type, percentage_by_customer_type)

    return jsonify (sales_data, percentage_data)


#h2_model sales per month

@app.route("/sales/month/", methods=['GET'])
def print_sales_month():
    sales_month = h2_model.get_sales_month()
    return jsonify(sales_month)

# h4_model sales by product type

@app.route("/sales/producttype", methods=['GET'])
def sales_qty_product_type():
    sales_producttype = h4_model.get_sales_qty_product_type()
    return jsonify(sales_producttype)


# h5_model unique list or product_type

@app.route("/product/type", methods=['GET'])
def get_unique_list_product_type():
    unique_producttype = h5_model.get_unique_list_product_type()
    return jsonify(unique_producttype), 200


# h6_model All Products

@app.route("/product/allproductname", methods=['GET'])
def get_products():
    # Get the 'limit' query parameter
    limit = request.args.get('limit')

    # Get the 'product_type' query parameter
    product_type = request.args.get('product_type')

    # Convert the limit to an integer, if it was provided
    if limit is not None:
        try:
            limit = int(limit)
        except ValueError:
            return jsonify({'error': 'Invalid limit format'}), 400

    # Get the list of products filtered by product_type
    products = h6_model.get_list_of_products(limit, product_type)

    return jsonify(products), 200

# h7_model Sales Per Product 

@app.route("/sales/perproductname", methods=['GET'])
def get_spp():
    limit = request.args.get('limit')

    if limit is not None:
        try:
            limit = int(limit)
        except ValueError:
            return jsonify({'error': 'Invalid limit format'}), 400

    Sales_Per_Product = h7_model.sales_per_product(limit)

    return jsonify(Sales_Per_Product), 200
    
    


#h8_model Sales Per Day of Week

@app.route("/sales/perday", methods=['GET'])
def get_spd():
   

   # rank teams from most to least ppg
   Sales_Per_Day = h8_model.sales_per_weekday()
   return jsonify(Sales_Per_Day), 200

#h9_model Post New Product

@app.route("/product/postnewproduct", methods=['POST'])
def post_new_product():
    product_data = request.get_json()
    new_product = h9_model.post_new_product(product_data)
    return jsonify(new_product), 200

#h10_model Delete Product by ID

@app.route('/product/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    delete_product_result = h10_model.delete_product_by_id(product_id)
    return delete_product_result, 200

#h11_model Getting the product name by product ID
# http://127.0.0.1:5000/product/id?product_id=41339626488005

@app.route('/product/id', methods=['GET'])
def get_product_name_by_id():
    product_id = request.args.get('product_id')
    if not product_id:
        return jsonify({'error': 'Missing product_id parameter'}), 400
    try:
        product_id = int(product_id)
    except ValueError:
        return jsonify({'error': 'Invalid product_id format'}), 400

    product_name = h11_model.get_single_product_name_by_id(product_id)
    if product_name:
        return jsonify({'Product_Name': product_name})
    else:
        return jsonify({'error': 'Product not found'}), 404

#h12_model updating net quantity on a specific order and product id
#http://127.0.0.1:5000/sales/update
#Headers - Key: Content-Type Value: application/json
#Body - {  "order_name": 105221,  "Product_Id": 42347175903429,  "new_quantity": 1000}

@app.route('/sales/update', methods=['POST'])
def update_sales():
    data = request.get_json()
    order_name = data.get('order_name')
    Product_Id = data.get('Product_Id')
    new_quantity = data.get('new_quantity')

    if not all([order_name, Product_Id, new_quantity]):
        return jsonify({'error': 'Missing or invalid parameters'}), 400
    try:
        order_name = int(order_name)
        Product_Id = int(Product_Id)
        new_quantity = int(new_quantity)
    except ValueError:
        return jsonify({'error': 'Invalid parameter format'}), 400
    
    h12_model.update_sales_quantity(order_name, Product_Id, new_quantity)

    return jsonify({'message': 'Sales updated successfully'})


    h12_model.update_sales_quantity(order_name, product_id, new_quantity)

    return jsonify({'message': 'Sales updated successfully'})

#h13_model get the order details about a specific order_id
# http://127.0.0.1:5000/sales/ordername?order_name=109721    ?ordername=89921

@app.route('/sales/ordername', methods=['GET'])
def get_sales_by_order_id():
    order_name = request.args.get('order_name')
    if not order_name:
        return jsonify({'error': 'Missing order_id parameter'}), 400

    order_detail = h13_model.get_sales_by_order_id(order_name)

    if order_detail:
        column_names = ["order_id", "Net_Quantity", "total_sales", "Product_ID", "customer_type", "Date", "Product_Name"]
        sales_data_dict = [dict(zip(column_names, row)) for row in order_detail]
        for entry in sales_data_dict:
            entry["total_sales"] = f"${entry['total_sales']}"
        return jsonify({'Order_Details': sales_data_dict})
    else:
        return jsonify({'error': 'Order not found'}), 404
    

#we create this function here so we can run this app on other file instead of running here on the API controller we will run this app on the main entry point, on our app.py
def run():
    #start the API server
    app.run(debug=True, port=5000) 
        #optional paramether 'debug'it's will watch your code and if you make changes to it start the Api server
        #hand if we keep the code running and making change you don't need to start and stop every time
        #sits there and wait for changes