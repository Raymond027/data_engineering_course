from kafka import KafkaProducer, KafkaConsumer
from app.config import (
    KAFKA_BOOTSTRAP_SERVERS,
    CONSUMER_GROUP
)


def create_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: v.encode("utf-8")
    )


def create_consumer(topic):
    return KafkaConsumer(
        topic,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=CONSUMER_GROUP,
        auto_offset_reset="earliest"
    )