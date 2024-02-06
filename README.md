# Small Business Operational Anlytics Database, API & Dashboard


# API Documentation
This API provides operational performance analytics to a small business that it uses to assist them in making data-driven decisions.The API also provides a mechanism for the users to be viewed, added, updated, and deleted.

**Tables and Endpoints:**
1. Static tables:
    - <ins>Date table:</ins>
        <!-- The Date Table, with date, month_num, year, quarter_num, week_Num, Business_Day, and Week_Day, is another static table. It permits the GET operation. This table will be used combined with sales and produce table to retrieve sales data in terms of time. -->

2. Tables for Updating and Deleting:
   
    - <ins>Sales table:</ins>
        <!-- The primary data source, the Sales Table, featuring unique_id, order_id, order_name, net_quantity, total_sales$, channel_id, Product_id, Date, and customer_type. It permits the GET operation. This table is accessible through /api/sales for CRUD operations. -->
    - <ins>Product table:</ins>
      <!-- The Product Table contians the following fields: Product_Id, product_type, product_name, Product_Cat1, Product_Cat2. This table premits the GET POST, PUT & DELETE operations. These actions should be subject to  strict security controls. This table is exposed through the endpoint /api/products for querying product-related information. -->
        <!-- -   '/api/products'
            - GET: retrieve sales data
            - POST: Create new product in product table.
            - PUT: Update product details in product table.
            - DELETE: Delete a product from product table. -->
         
Table Relationships:

![image](https://github.com/HannalaMattar/Group-Project-ISYS-5713-Hannala-Jacob/assets/143145674/94acb10b-e3cd-4cfb-af7c-bddc63e27578)





    

**Table of Contents**

1. [Getting Started](#Getting-Started)
    - Downloading Respository & Dependencies 
2. [Using the HTML Page](#HTML)

3. [Product Endpoints](#product-endpoints)
    - [Get Unique list of Products Type](#get-unique-list-product-type) 
    <!-- (#h5_model) -->
    
    - [Get Unique List of Products Name](#get-unique-list-of-products) 
    <!-- (#h6_model)  -->
       
    - [Add a New Product to the Product_Table](#add-product)   
    <!-- (#h9_model) -->
      
    - [Delete a Product on the Product List](#delete-product)   
    <!-- (#h10_model) -->

    - [Get single product name by Product_ID](#get-single-product-name-by-product_id)   
    <!-- (#h11_model) -->

    
4. [Sales Endpoints](#sales-endpoints)

    - [Get Total Sales Qty by Customer Type](#get-sales-by-customer-type) 
    <!-- (#h1_model) -->
    
    - [Get Total Sales Qty by month](#get-sales-by-month) 
    <!-- (#h2_model) -->
   
    - [Get Total Sales Qty by product type](#get-sales-qty-product-type) 
    <!-- (#h4_model) -->
   
    - [Get Sales by Product Name](#sales-by-product) 
    <!-- (#h7_model) -->
               
    - [Get Total Sales per Day of the Week](#sales-per-day) 
    <!-- (#h8_model) -->

    - [Update Order_ID](#update-orderid) 
    <!-- (#h12_model) -->

    - [Get Detail about one specific order id](#get-orderdetails-by-order-id) 
    <!-- (#h13_model) -->

<a id="Getting-Started"></a>
## Getting Started

First things first:

Begin by downloading this repository and saving it to your local computer. 

Please install the dependencies by navigating to the repository where this project located in GIT CMD. It should look someting like this:
![image](https://github.com/HannalaMattar/Group-Project-ISYS-5713-Hannala-Jacob/assets/143145674/b4bf2b5c-fa35-4c44-a629-897761ed5511)


Run the following in  GIT CMD:
       
![image](https://github.com/HannalaMattar/Group-Project-ISYS-5713-Hannala-Jacob/assets/143145674/4f2a8345-0fbb-4fc4-8650-fe5e57d6fe2b)

Use Visual Studio code to open the app.py file. In the top left corder of the screen, select on Explorer:

![image](https://github.com/HannalaMattar/Group-Project-ISYS-5713-Hannala-Jacob/assets/143145674/525c812d-19d4-473c-a974-9a523499eb40)

Then select Open Folder: 

![image](https://github.com/HannalaMattar/Group-Project-ISYS-5713-Hannala-Jacob/assets/143145674/30699056-230a-4736-895e-0591fcc3c8fc)

Then select Select Folder:

![image](https://github.com/HannalaMattar/Group-Project-ISYS-5713-Hannala-Jacob/assets/143145674/aa7eec56-2d1f-4da1-a4f4-194db7571c85)

Once this is done and the other files are visable on the left part of your Visual Stuido page, you can run the Python file. Once you do, the bottom results in the terminal should look like: 

![image](https://github.com/HannalaMattar/Group-Project-ISYS-5713-Hannala-Jacob/assets/143145674/f965c36f-f1da-4498-99d1-099d6002390f)

You can then open the U4_API_Front_End file in Chrome and use accordingly. 

<a id="HTML"></a>   

## Using the HTML


Get Functions that require no input:
 - GETsales-per-day Sales Per Day. 
 - GET Sales Per Month
 - GET Sales Per Product Type
 - GET Sales Per Customer Type
 - GET Sale Per Product Name
 - GET List All Products
 - GET List All Product Types

GET Functions that require input:
 - GET Products List With Specified Limit: Enter a numeric value for the number of values to return. It will return them in alphabetical order
 - GET Products Per Product Type: Enter one of the values that is returned on the "GET List All Products Type" to find all the products with that specific Type
 - GET Product Name by ID: Enter any Product_ID that is returned on the "GET List All Products" selection to return the Product Name
 - GET Order By Order ID: You must enter an order ID to pull up the information relating to the order. The Order IDs are located in the data. Some example Order IDs are (109001, 91651, 103601, 109391)

POST Functions that require input:
- POST New Product: 
  - This will ask you to enter a:
    - Product ID(Numerical)
    - Product Type(Enter a new name or an existing one)
    - Category 1(Enter a description of the product)
    - Category 2(Add a secondary description of the product)
- POST Update Sales Quantity
  - This will ask you to enter:
  - An order ID(Must be an existing order)
  - Enter Product ID: ( This would be a product ID that was on the order already)
  - Add the new quantity number for that item in the order(Numeric)
DELETE Function that requires an input:
- DELETE Product by ID:
  - Enter the ProductID you want to delete(Best to use an example product that you create to delete)



   

<a id="product-endpoints"></a>
## Product Endpoints


<a id="get-unique-list-product-type"></a>
### `/products/type`

|METHOD|`GET`|
|-------|-----|
|**Description**|Gets all Product Types|


#### Example Request
[/product/type]

#### Example Response:
```json
[
    {
        "Product Type": "18oz candle"
    },
    {
        "Product Type": "2gal bucket"
    },
    {
        "Product Type": "55lb bulk bag"
    },
    {
        "Product Type": "Product_Type"
    },
    {
        "Product Type": "Sample"
    },
    {
        "Product Type": "Test2"
    },
    {
        "Product Type": "Wicks"
    }
]
```

<a id="get-unique-list-of-products"></a>
### `/products`

|METHOD|`GET`|
|-------|-----|
|**Description**|Gets all Products|
|**Parameters**|*limit* (optional) - limits the number of results returned EX. /products/allproductname?limit=10|
|**Parameters**|*filter* (optional) - filters the results by a Product Type EX. /products/allproductname?product_type=18oz candle|

#### Example Request
[/product/allproductname]

#### Example Response:
```json
[
    {
        "Product": "18oz Box Dreamy Dunes",
        "Product_id": 41200104603845
    },
    {
        "Product": "18oz Box Dreamy Dunes + Vase",
        "Product_id": 40863057445061
    },
    {
        "Product": "18oz Box Festive Fir",
        "Product_id": 42345978003653
    },
    {
        "Product": "18oz Box Lazy Lulu",
        "Product_id": 41200107192517
    },
    {
        "Product": "18oz Box Lazy Lulu + Vase",
        "Product_id": 40863057477829
    }
    ...
]
```


<a id="add-product"></a>
### `/PostNewProduct`

|METHOD|`POST`|
|-------|-----|
|**Description**|POST New Product|


#### Example Request
[/product/postnewproduct]

#### Example Input:
```json
{
    "product_id": 999999,
    "product_type": "Test2",
    "product_name": "ProducTest2",
    "product_cat_1": "Test2",
    "product_cat_2": "Test2"
}

```

<a id="delete-product"></a>
### `/delete_product/<int:product_id>`

|METHOD|`DELETE`|
|-------|-----|
|**Description**|DELETE a Product|


#### Example Request
[/product/delete_product/<int:product_id"]

#### Example Input: /delete_product/"Insert Product ID Here"


<a id="get-single-product-name-by-product_id"></a>
### `/product/id?product_id=`


|METHOD|`GET`|
|-------|-----|
|**Description**|GET Product Name By Product ID|


#### Example Request
[/product/id?product_id=40863057445061]

#### Example Response:
```
{
    "Product_Name": "18oz Box Dreamy Dunes + Vase"
}

```

<a id="sales-endpoints"></a>
## Sales Endpoints

<a id="get-sales-by-customer-type"></a>
### `/sales/customertype/`

|METHOD|`GET`|
|-------|-----|
|**Description**|Gets Sales By Customer Type|


#### Example Request
[/sales/customertype/]

#### Example Response:
```json
[
    [
        {
            "Customer Type": "First-time",
            "Total Sales": 3374
        },
        {
            "Customer Type": "Returning",
            "Total Sales": 1235
        }
    ],
    [
        {
            "Customer Type": "First-time",
            "Percentage": "82.00%"
        },
        {
            "Customer Type": "Returning",
            "Percentage": "17.00%"
        },
        {
            "Customer Type": "customer_type",
            "Percentage": "0.00%"
        }
    ]
]
...
```

<a id="get-sales-by-month"></a>
### `/sales/month/`

|METHOD|`GET`|
|-------|-----|
|**Description**|Gets Sales Per Month|


#### Example Request
[/sales/month/]

#### Example Response:
```json
[
    {
        "Month_Num": 7,
        "Monthly_Sales$": "$91414.6400000006",
        "Year": 2023
    },
    {
        "Month_Num": 8,
        "Monthly_Sales$": "$121351.09",
        "Year": 2023
    },
    {
        "Month_Num": 9,
        "Monthly_Sales$": "$57922.7600000001",
        "Year": 2023
    }
]
...
```
<a id="get-sales-qty-product-type"></a>
### `/sales/producttype`

|METHOD|`GET`|
|-------|-----|
|**Description**|Gets Sales Per Product Type|


#### Example Request
[/sales/producttype]

#### Example Response:
```json
[
    {
        "Product type": "18oz candle",
        "Sales Qty": 1536
    },
    {
        "Product type": "2gal bucket",
        "Sales Qty": 366
    },
    {
        "Product type": "55lb bulk bag",
        "Sales Qty": 318
    },
    {
        "Product type": "Sample",
        "Sales Qty": 1185
    },
    {
        "Product type": "Wicks",
        "Sales Qty": 902
    }
]
...
```


<a id="sales-by-product"></a>
### `/SalesPerProduct`

|METHOD|`GET`|
|-------|-----|
|**Description**|All Time Sales Per Product|
|**Parameters**|*limit* (optional) - limits the number of results returned EX. /SalesPerProduct?limit=10|


#### Example Request
[/sales/perproductname]

#### Example Response:
```
Product: 2gal Pail Dreamy Dunes, Total Sales: 2957.90<br>
Product: Duo Dark Emerald / Red, Total Sales: 82.11<br>
Product: Duo Red / Black, Total Sales: 74.99<br>
Product: Duo Nude / Desert Rose, Total Sales: 74.99<br>
Product: Duo Desert Rose / Desert Rose, Total Sales: 74.99<br>
Product: Duo Black / Nude, Total Sales: 74.99<br>
Product: Duo Black / Desert Rose, Total Sales: 74.99<br>
Product: Duo Black / Dark Emerald, Total Sales: 74.99<br>

```

<a id="sales-per-day"></a>
### `/sales/perday`

|METHOD|`GET`|
|-------|-----|
|**Description**|Gets Total Sales Per Day of Week|


#### Example Request
[/SalerPerDay]

#### Example Response:
```json
[
    {
        "total_sales": 36255.84999999999,
        "weekday": "Friday"
    },
    {
        "total_sales": 39387.71999999999,
        "weekday": "Monday"
    },
    {
        "total_sales": 21409.059999999972,
        "weekday": "Saturday"
    },
    {
        "total_sales": 34117.700000000004,
        "weekday": "Sunday"
    },
    {
        "total_sales": 46106.46999999998,
        "weekday": "Thursday"
    },
    {
        "total_sales": 49111.609999999986,
        "weekday": "Tuesday"
    },
    {
        "total_sales": 44300.08,
        "weekday": "Wednesday"
    }
]
...
```



<a id="update-orderid"></a>
### `/Update/Order_Id`

|METHOD|`POST`|
|-------|-----|
|**Description**|This API endpoint allows you to update the quantity (Qty) for a specific order_id and a specific product_ID into the order|


#### Example Request
[/sales/update]

[Headers - Key: Content-Type Value: application/json]

[Body: {
  "order_name": 105221,
  "Product_Id": 42347175903429,
  "new_quantity": 999
} ]

#### Example Input:
```json
{
    "message": "Sales updated successfully"
}
```

<a id="get-orderdetails-by-order-id"></a>
### `/Sales/ordername?order_name=`


|METHOD|`GET`|
|-------|-----|
|**Description**|GET order details from a specific order id|


#### Example Request
[/sales/ordername?ordername=109721]

#### Example Response:
```
{
    "Order_Details": [
        {
            "Date": "9/28/2023",
            "Net_Quantity": 1,
            "Product_ID": 41339626488005,
            "Product_Name": "Scent Sample Misty Monte",
            "customer_type": "First-time",
            "order_id": "109721",
            "total_sales": "$2.54"
        },
        {
            "Date": "9/28/2023",
            "Net_Quantity": 1,
            "Product_ID": 42347138384069,
            "Product_Name": "Scent Sample Mulled Magic",
            "customer_type": "First-time",
            "order_id": "109721",
            "total_sales": "$2.54"
        },
        {
            "Date": "9/28/2023",
            "Net_Quantity": 1,
            "Product_ID": 41200137240773,
            "Product_Name": "18oz Box Scent Free",
            "customer_type": "First-time",
            "order_id": "109721",
            "total_sales": "$29.74"
        }
    ]
}
```







