import json
from kafka import KafkaProducer

from config.settings import (
    KAFKA_BOOTSTRAP_SERVERS
)
from src.utils.logger import logger


class UserEventProducer:

    def __init__(self):

        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

        logger.info(
            f"Connected to Kafka: {KAFKA_BOOTSTRAP_SERVERS}"
        )

    def send_message(self, topic, message):

        future = self.producer.send(
            topic,
            value=message
        )

        record_metadata = future.get(timeout=10)

        logger.info(
            f"Message sent to "
            f"{record_metadata.topic} "
            f"partition={record_metadata.partition} "
            f"offset={record_metadata.offset}"
        )

        print(
            f"✓ Sent -> "
            f"partition={record_metadata.partition}, "
            f"offset={record_metadata.offset}"
        )

    def close(self):
        self.producer.flush()
        self.producer.close()
        logger.info("Producer closed")