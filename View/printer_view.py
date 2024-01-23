
#function to print the results of the query h1_model
def print_sales_customertype (sales_by_customer_type, percentage_by_customer_type):
            # Print the results
    for row in sales_by_customer_type:
        customer_type, total_sales = row
        print(f"Customer Type: {customer_type}, Total Sales: {total_sales}")
            #Print results
    for row in percentage_by_customer_type:
        customer_type, percentage = row
        print(f"Customer_Type: {customer_type}, Percentage: {percentage:.2f}%")


#function to print the results of the query h2_model
def print_sales_month (sales_month):
            # Print the results
    for row in sales_month:
        print(row)

#function to print the results of the query h4_model
def print_sales_qty_product_type (sales_qty_product_type):
            # Print the results
    for row in sales_qty_product_type:
        print(row)

#function to print the results of the query h5_model
def print_unique_list_product_type(unique_products_type):
            # Print the results
    for row in unique_products_type:
        print(row)

#function to print the results of the query h6_model
def print_products(product_list):
    if product_list is None or len(product_list) == 0:
        pass
    else:
        for row in product_list:
            print(row)


# def print_products(product_list):
#             # Print the results
#     for row in product_list:
#         print(row)

#function to print the results of the query h7_model
def print_sales_per_product(sales_per_product):
   if sales_per_product is None or len(sales_per_product) == 0:
        pass
   else:
    for row in sales_per_product:
        print(row)
# function to print the results of the query h8_model
def print_sales_per_weekday(sales_per_weekday):
     if sales_per_weekday is None or len(sales_per_weekday) == 0:
        pass
     else:
      for row in sales_per_weekday:
        print(row)