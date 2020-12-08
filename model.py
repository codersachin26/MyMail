## import Query Executer Function for execute SQL Queries
from db import query_Executer

class QueryObject:

    # initialize a new QueryObject
    def __init__(self,queryData,tableName):
        self.queryData = queryData
        self.tableName = tableName
     
    # return first record from queryObject
    def first(self):
        first_record = self.queryData[0]
        return first_record

    # return last record from queryObject
    def last(self):
        last_record = self.queryData[-1]
        return last_record
    
    # return total numbers of record in queryObject
    def count(self):
        total_record = len(self.queryData)
        return total_record
    
    # check, is given record exist or not
    def exist(self,**kwarg):
        record = self.queryData[0]
        for key,value in kwarg:
            if record[key] == value:
                pass
            else:
                return False
        return True



class QuerySet:
     
    # return only one record from db
    def get(table_name,**kwarg):
        conditions = ''
        for key,value in kwarg.items():
            conditions = conditions + f'{key}={value}'
        SQLquery = f'SELECT * FROM {table_name} WHERE {conditions}'
        print(SQLquery)
        sql_query_result = query_Executer(SQLquery)
        query_object = QueryObject(sql_query_result,table_name)
        return query_object
    
    # return more than one record from db
    def filter(table_name,**kwarg):
        pass


    def all(table_name,**kwarg):
        pass

    def update(table_name,**kwarg):
        pass

    def delete(table_name,**kwarg):
        pass

    def save(table_name,**kwarg):
        pass
     