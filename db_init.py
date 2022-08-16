import mysql.connector as cntr
db = cntr.connect(host = 'localhost' , user = 'root' , passwd = 'root')
db.autocommit = True
cur = db.cursor()
cur.execute("create database if not exists lib_management")
cur.execute("use lib_management")
cur.execute("create table IF NOT EXISTS stock\
            (Book_No bigint primary key,\
Book_Name varchar(255),\
Author varchar(255),\
Publisher varchar(255),\
Cost_per_Book float,\
Available_Stock bigint,\
qty_purchased bigint,\
purchased_on date)")
cur.execute("create table IF NOT EXISTS users(username varchar(255) , password varchar(255))")
cur.execute("create table IF NOT EXISTS purchased (Book_no bigint , purchased_on date , foreign key(Book_no) references stock(Book_No))")

cur.execute("insert into users values('admin' , 'admin')")
print("Database and Tables created successfully")
cur.close()
db.close()
