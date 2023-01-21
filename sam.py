import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='root',database='db1')
cur=mydb.cursor()
# to delete
s="DELETE FROM book WHERE title='python'"
# to  update
# s="UPDATE book SET price=price+10 WHERE price>200"
cur.execute(s)
mydb.commit()
# result=cur.fetchall()
# for rec in result:
#     print(rec)
# s="INSERT INTO book (bookid, title,price) VALUES(%s,%s,%s)"
# # v=(1,'python',654)#for single
# v=[(2,'java',500),(3,'html',250),(4,'css',200)]
# cur.executemany(s,v)
# mydb.commit()
# t="CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,2))"
# cur.execute(t)
# cur.execute("CREATE DATABASE db1")