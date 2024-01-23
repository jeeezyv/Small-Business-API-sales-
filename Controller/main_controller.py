from Models import h1_model
from Models import h2_model
from Models import h4_model
from Models import h5_model
from Models import h6_model
from Models import h7_model
from Models import h8_model
from View import printer_view
from View import api_view
from Controller import api_controller

#function to get the data from query h1_model
def print_sales_customer_type():
    sales_by_customer_type, percentage_by_customer_type = h1_model.get_sales_customer_type()
    api_view.print_sales_customertype(sales_by_customer_type, percentage_by_customer_type)
    #start API server
    api_controller.run()

# #function to get the data from query h2_model
# def get_sales_month():
#     sales_month = h2_model.get_sales_month()
#     api_view.print_sales_month(sales_month)
#     #start API server
#     api_controller.run()

# #function to get the data from query h4_model
# def print_sales_qty_product_type():
#     sales_qty_product_type = h4_model.get_sales_qty_product_type()
#     printer_view.print_sales_qty_product_type (sales_qty_product_type)

# #function to get the data from query h5_model
# def print_unique_list_product_type():
#     unique_list_product_type = h5_model.get_unique_list_product_type()
#     printer_view.print_sales_qty_product_type (unique_list_product_type)


# #function to get the data from query h6_model
# def print_products():
#     product_list = h6_model.get_list_of_products()
#     printer_view.print_products(product_list)
# #function to get the data from query h7_model
# def print_sales_per_product():
#     sales_per_product = h7_model.sales_per_product()
#     printer_view.print_sales_per_product(sales_per_product)

# # function to get the data from query h8_model
# def print_sales_per_weekday():
#     sales_per_weekday = h8_model.sales_per_weekday()
#     printer_view.print_sales_per_weekday(sales_per_weekday)
