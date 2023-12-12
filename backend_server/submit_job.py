from backend_server import app, session, constants, minio_client
from flask import request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
import json

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in constants.ALLOWED_EXTENSIONS

def train_job_paylod_validator(req):
    if not req.files:
        return 'Valied csv file needs to be uploaded', False
    if 'user_file' not in req.files:
        return 'Invalid key for uploading user file', False
    file = request.files['user_file']
    filename = secure_filename(file.filename)
    if not(allowed_file(filename)):
        return 'User can only upload valid csv files', False
    model_meta_data = ['task_type', 'hyperparams', 'model_name']
    for key in model_meta_data:
        if key not in request.form:
            return f'{key} not found in request payload', False
    return 'Valid Payload', True

def upload_file_to_minio(file):
    filename = secure_filename(file.filename)
    user_bucket = get_user_bucket(session['user-id'])
    size = os.fstat(file.fileno()).st_size
    minio_client.put_object(user_bucket, f'datasets/{filename}', file, size)


@app.route('/submit-job', methods=['POST'])
def submit_training_job():
    if 'user-id' not in session:
        return redirect(url_for("index"))
    
    msg, is_payload_valid = train_job_paylod_validator(request)
    if not is_payload_valid:
        return jsonify({'message':msg}), 400
    
    upload_file_to_minio(request.files['user_file'])
    return jsonify({'message':msg}), 200


        
def get_user_bucket(user_id):
    user_bucket = f'{user_id.replace("@",".")}.bucket'
    return user_bucket