from backend_server import constants
from confluent_kafka import Producer


kafka_producer_config = {
    'bootstrap.servers': constants.KAFKA_BOOTSTRAP_SERVER,
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': constants.KAFKA_USERNAME,
    'sasl.password': constants.KAFKA_SECRET
}

producer = Producer(kafka_producer_config)

def push_to_topic():
    pass