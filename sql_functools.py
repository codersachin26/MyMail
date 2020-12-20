## query helper functions

from sql_query import QueryObject
from db_connect import MySQL_cursor,db_connection

# for query Executing
def query_Executer(query,val=None):
    MySQL_cursor.execute(query,val)
    try:
        queryData = MySQL_cursor.fetchall()
    except:
        queryData = None
    table_col = tuple([d[0] for d in MySQL_cursor.description])
    db_connection.commit()
    return queryData,table_col


def return_queryObj(records,columns):
    query_data = []
    for raw in records:
        raw_data = {k:v for k,v in zip(columns,raw)}
        query_data.append(raw_data)
    query_obj = QueryObject(query_data)
    return query_obj
        