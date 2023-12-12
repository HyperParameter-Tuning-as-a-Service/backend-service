from backend_server import app, session, constants
from flask import request, redirect, url_for

@app.route('/')
def index():
    if 'user_id' in session:
        return f'Logged in as {session["user_id"]}'
    else:
        return '<a class="button" href="/login">Google Login</a>'
    
