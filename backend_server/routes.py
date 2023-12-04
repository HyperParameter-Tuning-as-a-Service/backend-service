from backend_server import app, session

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    else:
        return '<a class="button" href="/login">Google Login</a>'