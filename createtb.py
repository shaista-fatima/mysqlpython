import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydb2"
)
cur=mydb.cursor()
s="CREATE TABLE student(id integer(4), name varchar(20))"

cur.execute(s)