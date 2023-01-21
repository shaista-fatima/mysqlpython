import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydb2"
)
cur=mydb.cursor()
s="UPDATE student SET name='sofi' WHERE name='safa'"
cur.execute(s)
mydb.commit()