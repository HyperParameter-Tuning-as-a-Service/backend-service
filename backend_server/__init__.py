from flask import Flask, session
from flask_cors import CORS
from minio import Minio

from backend_server import constants

app = Flask(__name__)
app.secret_key = constants.FLASK_SECRET
CORS(app)

minio_client = None
try:
    minio_client = Minio(constants.minioHost, access_key=constants.minioUser, secret_key=constants.minioPasswd, secure=False)
except Exception as exp:
    print(f'Exception raised in while starting minio: {str(exp)}')

from backend_server import home, auth, submit_job