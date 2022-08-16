import mysql.connector as cntr
import datetime as __dt
from random import shuffle
from tempfile import mktemp
from os import system , startfile

db = cntr.connect(host = 'localhost' , user = 'root' , passwd = 'root' , database = 'lib_management')
cur = db.cursor(buffered=True)
db.autocommit = True

def add_user(username,password):
    cur.execute("insert into users values('{}' , '{}')".format(username , password))


def login(username,password):
    cur.execute("Select * from users where (username = '{}' and password = '{}')".format(username , password))
    if cur.rowcount : return True
    else: return False


