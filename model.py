## import Query Executer Function for execute SQL Queries
from db import query_Executer


class QueryObject:
    def __init__(self,queryData,tableName):
        self.queryData = queryData
        self.tableName = tableName

    def first(self):
        first_record = self.queryData[0]
        return first_record

    def last(self):
        last_record = self.queryData[-1]
        return last_record

    def count(self):
        total_record = len(self.queryData)
        return total_record

    def exist(self,**kwarg):
        record = self.queryData[0]
        for key,value in kwarg:
            if record[key] == value:
                pass
            else:
                return False
        return True



class QuerySet:

    def get(table_name,**kwarg):
        pass

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
     



