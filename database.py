import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
cur=mydb.cursor()
cur.execute("CREATE DATABASE mydb2")