import mysql.connector

from mysql.connector import errorcode
try:
    db_connection = mysql.connector.connect(host='localhost', user='root', password='nenem', database='DB_EMPRESA')
    print("Database connection made!")
except mysqql.connector.Error as error:
    if error.errnr == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
    elif error.errnr == errorcode.ER_ACCESS_DENIED_ERROR:
            print ("User name or password is wrong")
    else:
        print (error)
else:
    db_connection.close()