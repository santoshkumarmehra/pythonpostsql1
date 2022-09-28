from distutils.cmd import Command
from sqlite3 import connect
import psycopg2 as p

mydb = p.connect(
    user='santosh1',
    password='postgres',
    dbname='postdatabase',
    host="localhost"    
)
mycursor=mydb.cursor()

# Command="create table student(name text,city text,email text,password text)"
# mycursor.execute(Command)
# mydb.commit()

# while True:
#     name=input("name: ")
#     city=input("city: ")
#     email=input("email: ")
#     password=input("password: ")
#     q="insert into student(name,city,email,password) values('{}','{}','{}','{}')".format(name,city,email,password)
#     mycursor.execute(q)
#     mydb.commit()

# mycursor.execute("select * from student")
# data=mycursor.fetchall()
# for i in data:
#     print(i)

# mycursor.execute("delete from student")
# mydb.commit()
# mycursor.execute("select * from student")
# data=mycursor.fetchall()
# for i in data:
#     print(i)

# mycursor.execute("select * from student")
# data=mycursor.fetchall()