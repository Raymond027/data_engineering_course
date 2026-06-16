import json
from kafka import KafkaProducer

from config.settings import KAFKA_BROKER, TOPIC_NAME
from src.utils.logger import get_logger
from src.producer.event_factory import generate_event

logger = get_logger("producer")


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=json_serializer,
    acks="all",              # reliability
    retries=3
)


def send_event():
    event = generate_event()

    future = producer.send(TOPIC_NAME, value=event)

    record_metadata = future.get(timeout=10)

    logger.info(f"Sent event: {event}")
    logger.info(
        f"Topic: {record_metadata.topic}, Partition: {record_metadata.partition}"
    )


if __name__ == "__main__":
    for _ in range(10):
        send_event()