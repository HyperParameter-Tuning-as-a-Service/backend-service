from flask import Flask, session
from flask_cors import CORS

from backend_server import constants
from backend_server.minio_client import get_minio_client
from backend_server.kafka_producer import get_kafka_producer

app = Flask(__name__)
app.secret_key = constants.FLASK_SECRET
CORS(app)

minio_client = get_minio_client()

producer = get_kafka_producer()

from backend_server import home, auth, submit_job