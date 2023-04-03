import mysql.connector 

# menghubungkan mysql
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

# Create a cursor object
cursorObject = dataBase.cursor()

# membuat database dengan nama d3_ti_2023
cursorObject.execute("CREATE DATABASE d3_ti_2023")