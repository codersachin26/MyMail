from flask import session,redirect,request
from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(**arg):
        if session.get('userID'):
            return func(arg)
        else:
            return redirect('/login')
            
    return wrapper