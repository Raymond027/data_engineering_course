import json

from kafka import KafkaProducer
from kafka import KafkaConsumer

from config.settings import (
    KAFKA_BOOTSTRAP_SERVERS,
    CONSUMER_GROUP
)


def create_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )


def create_consumer(topic):
    return KafkaConsumer(
        topic,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=CONSUMER_GROUP,
        auto_offset_reset="earliest",
        value_deserializer=lambda m: json.loads(
            m.decode("utf-8")
        )
    )