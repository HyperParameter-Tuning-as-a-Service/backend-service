from backend_server import constants
import pymongo
from pymongo import MongoClient


mongo_cluster = MongoClient(constants.MONGO_ATLAS_URL)
mongo_db = mongo_cluster['HypTAAS']
mongo_collection = mongo_db['userinfo']

def create_user_doc(user_id):
    mongo_collection.insert_one({'user_id': user_id,'runs': []})

def find_or_create_user_doc(user_id):
    user_doc = mongo_collection.find_one({'user_id': user_id})
    if not user_doc:
        create_user_doc(user_id)

def record_train_meta_data(user_id, train_meta_data, exp_name):
    train_meta_data['accuracy'] = 0.0
    train_meta_data['training'] = True
    update_key = f'runs.{exp_name}'
    mongo_collection.update_one(
        {'user_id': user_id},
        {'$push': {
            update_key: train_meta_data
        }}
    )


