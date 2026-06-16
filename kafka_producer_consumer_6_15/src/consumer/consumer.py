import json
from kafka import KafkaConsumer

from config.settings import KAFKA_BROKER, TOPIC_NAME, CONSUMER_GROUP
from src.utils.logger import get_logger

logger = get_logger("consumer")


consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BROKER,
    group_id=CONSUMER_GROUP,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)


def process_event(event: dict):
    event_type = event.get("event_type")

    if event_type == "user_signup":
        logger.info(f"🆕 USER SIGNUP: {event}")

    elif event_type == "user_login":
        logger.info(f"🔐 USER LOGIN: {event}")

    elif event_type == "order_created":
        logger.info(f"🛒 ORDER CREATED: {event}")

    else:
        logger.warning(f"Unknown event: {event}")


if __name__ == "__main__":
    logger.info("Consumer started...")

    for message in consumer:
        event = message.value
        process_event(event)