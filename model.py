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
     
    # return only one record from table
    def get(table_name,**kwarg):
        conditions = ''
        for key,value in kwarg.items():
            conditions = conditions + f'{key}={value}'
        SQLquery = f'SELECT * FROM {table_name} WHERE {conditions}'
        sql_query_result = query_Executer(SQLquery)
        query_object = QueryObject(sql_query_result,table_name)
        return query_object
    
    # return more than one record from table
    def filter(table_name,**kwarg):
        condition_len = len(kwarg)
        conditions = ''
        condition_val = []
        for key,value in kwarg.items():
            conditions = conditions + f'{key}=%s {"AND " if condition_len > 1 else "" }'
            condition_val.append(value)
            condition_len -= 1
        condition_val = tuple(condition_val)
        SQLquery = f'SELECT * FROM {table_name} WHERE {conditions}'
        sql_query_result = query_Executer(SQLquery,val=condition_val)
        query_object = QueryObject(sql_query_result,table_name)
        return query_object

    # return all record from table
    def all(table_name,**kwarg):
        SQLquery = f'SELECT * FROM {table_name}'
        sql_query_result = query_Executer(SQLquery)
        query_object = QueryObject(sql_query_result,table_name)
        return query_object        
    

    # update record from table
    def update(table_name,Set=None,**kwarg):
        condition_len = len(kwarg)
        conditions = ''
        condition_val = []
        for key,value in kwarg.items():
            conditions = conditions + f'{key}=%s {"AND " if condition_len > 1 else "" }'
            condition_val.append(value)
            condition_len -= 1
        condition_val = tuple(condition_val)
        
        update_val = [] 
        Set_values_len = len(Set)
        Set_values = ''
        for key,value in Set.items():
            Set_values = Set_values + f'{key}=%s{"," if Set_values_len > 1 else "" }'
            update_val.append(value)
            Set_values_len -= 1
        update_val = tuple(update_val)
        values = update_val + condition_val

        SQLquery = f'UPDATE {table_name} SET {Set_values} WHERE {conditions}'
        sql_query_result = query_Executer(SQLquery,val=values)
        query_object = QueryObject(sql_query_result,table_name)
        return query_object


     # remove record from table
    def delete(table_name,**kwarg):
        condition_len = len(kwarg)
        conditions = ''
        values = []
        for key,value in kwarg.items():
            conditions = conditions + f'{key}=%s {"AND " if condition_len > 1 else "" }'
            values.append(value)
            condition_len -= 1
        values = tuple(values)
        SQLquery = f'DELETE FROM {table_name} WHERE {conditions}'
        sql_query_result = query_Executer(SQLquery,val=values)
        query_object = QueryObject(sql_query_result,table_name)
        return query_object
        
    # insert new record into table
    def save(table_name,**kwarg):
        no_of_column = len(kwarg)
        column_name = ''
        format_specifier = ''
        values = []
        for key,value in kwarg.items():
            column_name      = column_name + f'{key} {"," if no_of_column > 1 else ""}'
            format_specifier = format_specifier +  f'%s {"," if no_of_column > 1 else ""}'
            values.append(value)
            no_of_column -= 1
        values = tuple(values)
        SQLquery = f'INSERT INTO {table_name}({column_name})VALUES({format_specifier})'
        print(SQLquery)
        sql_query_result = query_Executer(SQLquery,val=values)
        query_object = QueryObject(sql_query_result,table_name)
        return query_object

     

