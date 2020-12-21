
## manage query results
class QueryObject:

    # initialize a new QueryObject
    def __init__(self,queryData):
        self.queryData = queryData
     
    # return first record from queryObject
    def first(self):
        FIRST = 0
        first_record = self.queryData[FIRST]
        return first_record

    # return last record from queryObject
    def last(self):
        LAST = -1
        last_record = self.queryData[LAST]
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