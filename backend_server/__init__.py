from flask import Flask
from flask import session

from backend_server import constants

app = Flask(__name__)
app.secret_key = constants.FLASK_SECRET

from backend_server import auth, routes