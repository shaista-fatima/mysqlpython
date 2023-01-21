import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydb2"
)
cur=mydb.cursor()
s="INSERT INTO student(id,name) Values (%s,%s)"
mul=[(2,'shazz'),(3,'shaista')]
cur.executemany(s,mul)
mydb.commit()