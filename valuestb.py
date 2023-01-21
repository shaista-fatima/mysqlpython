import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydb2"
)
cur=mydb.cursor()
s="INSERT INTO student(id,name)VALUES(%s,%s)"
v=(1,"safa")
cur.execute(s,v)
mydb.commit()