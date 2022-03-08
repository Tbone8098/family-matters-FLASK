from functools import wraps
from flask import session, redirect

def checkLogin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'uuid' not in session:
            return redirect('/')

        return func(*args, **kwargs)
    return wrapper