import mysql.connector

# Establish connection
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234'
)

# Prepare cursor object
cursorObject = dataBase.cursor()

# Create the database
cursorObject.execute("CREATE DATABASE elderco")

print("All done")
