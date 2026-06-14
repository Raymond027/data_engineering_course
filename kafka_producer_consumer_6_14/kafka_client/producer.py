from kafka import KafkaProducer
from kafka_client.base import KafkaBase
from utils.json_serializer import serialize_message
from utils.logger import get_logger
from config.settings import TOPIC_USER_EVENTS

import time
import uuid

logger = get_logger("producer")


class EventProducer(KafkaBase):
    def __init__(self):
        super().__init__()

        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=serialize_message,
            acks="all",
            retries=3,
            linger_ms=10,
        )

    def send_event(self, event: dict):
        try:
            future = self.producer.send(TOPIC_USER_EVENTS, value=event)

            record_metadata = future.get(timeout=10)

            logger.info(
                f"Sent event to {record_metadata.topic} "
                f"partition={record_metadata.partition} offset={record_metadata.offset}"
            )

        except Exception as e:
            logger.error(f"Failed to send event: {e}")

    def generate_test_events(self, count=10):
        for i in range(count):
            event = {
                "event_id": str(uuid.uuid4()),
                "user_id": f"user_{i}",
                "event_type": "click",
                "timestamp": time.time(),
            }

            self.send_event(event)
            time.sleep(0.5)