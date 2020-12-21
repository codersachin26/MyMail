from query_manager import QuerySet


# create new my mail id for new user account

def generate_mymail_id(username):
    Q = f"SELECT name FROM user WHERE name REGEXP '^{username}[0-9]@mymail.com' OR name REGEXP '^{username}@mymail.com'"
    my_mail_id = QuerySet.make_query(Q).queryData
    print(my_mail_id)
    if len(my_mail_id) == 0:
        new_mail_id = f'{username}@mymail.com'
        return new_mail_id

    my_mail_count = len(my_mail_id)
    new_mail_id = f'{username}{my_mail_count}@mymail.com'
    return new_mail_id
    
    
