## do authentication here

from flask import session
from hashlib import sha256
from query_manager import QuerySet


# start user session
def login(user_id):
    session['userID'] = user_id


# remove user session
def logout():
    session.pop('userID',None)


# user Authentication
def authenticate(user_Email_Id,passwd):
    user = QuerySet.get('my_mail',email_Id=user_Email_Id)
    if user is None:
        return False
    if sha256(passwd.encode()).hexdigits() == user.passwd:
        return True
    return False







