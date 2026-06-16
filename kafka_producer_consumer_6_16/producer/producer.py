import json

from kafka import KafkaProducer

from config.settings import (
    KAFKA_BOOTSTRAP_SERVERS,
    TOPIC_NAME,
    RETRY_ATTEMPTS,
    RETRY_DELAY_SECONDS
)

from utils.retry import retry_operation
from utils.logger import logger
from utils.json_utils import serialize_event
from models.event_schema import validate_event


def create_producer():

    def connect():

        logger.info(
            "Connecting producer to Kafka..."
        )

        return KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: v.encode("utf-8")
        )

    return retry_operation(
        connect,
        RETRY_ATTEMPTS,
        RETRY_DELAY_SECONDS
    )


def load_events():

    with open(
        "sample_data/events.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def main():

    try:

        producer = create_producer()

        events = load_events()

        for event in events:

            try:

                validate_event(event)

                payload = serialize_event(event)

                producer.send(
                    TOPIC_NAME,
                    value=payload
                )

                logger.info(
                    f"Message sent: {event}"
                )

            except Exception as error:

                logger.error(
                    f"Event failed validation/send: {error}"
                )

        producer.flush()

        logger.info(
            "Producer completed successfully."
        )

    except Exception as error:

        logger.error(
            f"Producer terminated: {error}"
        )


if __name__ == "__main__":
    main()