import mysql.connector

# Connect to MySQL connector.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssw0rd12!")

mycursor = mydb.cursor()


# Create database for products.
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
