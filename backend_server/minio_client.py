from backend_server import constants
from minio import Minio


def get_minio_client():
    minio_client = None
    try:
        minio_client = Minio(constants.minioHost, access_key=constants.minioUser, secret_key=constants.minioPasswd, secure=False)
    except Exception as exp:
        print(f'Exception raised in while starting minio: {str(exp)}')
    return minio_client