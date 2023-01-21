import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydb2"
)
cur=mydb.cursor()
s="DELETE FROM student WHERE name='shaista'"
cur.execute(s)
mydb.commit()