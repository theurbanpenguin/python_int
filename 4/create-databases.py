import mysql.connector

#Connect to MySQL connector.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd12!")

mycursor = mydb.cursor()


# Create database for products.
mycursor.execute("CREATE DATABASE IF NOT EXISTS wwproducts")

print("wwproducts database created.")

# Create database for orders.
mycursor.execute("CREATE DATABASE IF NOT EXISTS wworders")

print("wworders database created.")

mydb.close()

#Connect to wwproducts database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd12!",
    database="wwproducts")

mycursor = mydb.cursor()

#Create products table.
mycursor.execute("CREATE TABLE IF NOT EXISTS products (product VARCHAR(255), "
                 "price DECIMAL(12,2), PRIMARY KEY(product))")
mydb.close()

print("products table created in the wwproducts database.")

#Connect to wworders database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd12!",
    database="wworders")

mycursor = mydb.cursor()

#Create ordersummary table.
mycursor.execute("CREATE TABLE ordersummary (ordernumber "
                 "INT AUTO_INCREMENT PRIMARY KEY, orderdate DATE, "
                 "shipmethod VARCHAR(255), totalprice DECIMAL(12,2))")
mydb.close()

print("ordersummary table created in the wworders database.")