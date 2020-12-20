# import MySQL Connector
import mysql.connector as MySQLConnector

# Create a MySQL Connection Object
db_connection = MySQLConnector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'my_mail'
)

# initiate a MySQLCursor Object
MySQL_cursor = db_connection.cursor()



