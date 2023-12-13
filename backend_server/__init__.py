from flask import Flask, session
from flask_cors import CORS

from backend_server import constants
from backend_server import minio_utils
from backend_server import kafka_utils

app = Flask(__name__)
app.secret_key = constants.FLASK_SECRET
CORS(app)

from backend_server import home, auth, submit_job