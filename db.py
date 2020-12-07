# import MySQL Connector
import mysql.connector as MySQLConnector

# Create a MySQL Connection Object
db_connection = MySQLConnector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'my_mail'
)

# initiate a MySQLCursor
query_cursor = db_connection.cursor()
q = 'select * from my_mail where id = 2'

# for query Executing
def query_Executer(query):
    query_cursor.execute(query)
    queryData = query_cursor.fetchall()
    db_connection.commit()
    return queryData

query_Executer(q)
