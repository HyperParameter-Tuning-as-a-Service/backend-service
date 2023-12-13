import os
import secrets

# Flask configs
FLASK_SECRET = os.getenv('FLASK_SECRET') or secrets.token_hex()
ALLOWED_EXTENSIONS = ['csv']

# Google Oauth configs
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET") 
GOOGLE_DISCOVERY_URL =  "https://accounts.google.com/.well-known/openid-configuration"

# Minio configs
minioHost = os.getenv("MINIO_HOST") or "localhost:9000"
minioUser = os.getenv("MINIO_USER") or "minioadmin"
minioPasswd = os.getenv("MINIO_PASSWD") or "minioadmin"

# Confluent Kafka configs
KAFKA_USERNAME = os.getenv("KAFKA_USERNAME")
KAFKA_SECRET = os.getenv("KAFKA_SECRET")
KAFKA_BOOTSTRAP_SERVER = "pkc-4r087.us-west2.gcp.confluent.cloud"
KAFKA_SUBMIT_JOB_TOPIC = 'demo'
