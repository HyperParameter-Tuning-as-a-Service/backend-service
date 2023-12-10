import os
import secrets

FLASK_SECRET = os.getenv('FLASK_SECRET') or secrets.token_hex()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET") 
GOOGLE_DISCOVERY_URL =  "https://accounts.google.com/.well-known/openid-configuration"