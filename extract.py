import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydb2"
)
cur=mydb.cursor()
s="SELECT * from student"
cur.execute(s)
result=cur.fetchall()
for r in result:
    print(r)