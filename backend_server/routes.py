from backend_server import app

@app.route("/")
def hello_world():
    return "<p>Hello, Anush!</p>"