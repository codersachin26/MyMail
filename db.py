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


# for query Executing
def query_Executer(query,val=None):
    query_cursor.execute(query,val)
    try:
        queryData = query_cursor.fetchall()
    except:
        queryData = None
    db_connection.commit()
    return queryData

