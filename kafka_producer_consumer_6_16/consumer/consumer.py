from kafka import KafkaConsumer

from config.settings import (
    KAFKA_BOOTSTRAP_SERVERS,
    TOPIC_NAME,
    CONSUMER_GROUP,
    RETRY_ATTEMPTS,
    RETRY_DELAY_SECONDS
)

from utils.retry import retry_operation
from utils.logger import logger
from utils.json_utils import deserialize_event


def create_consumer():

    def connect():

        logger.info(
            "Connecting consumer to Kafka..."
        )

        return KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            group_id=CONSUMER_GROUP,
            auto_offset_reset="earliest"
        )

    return retry_operation(
        connect,
        RETRY_ATTEMPTS,
        RETRY_DELAY_SECONDS
    )


def process_message(message):

    event = deserialize_event(
        message.value.decode("utf-8")
    )

    if event is None:

        logger.warning(
            "Skipping invalid JSON message."
        )

        return

    logger.info(
        f"Processed Event: {event}"
    )

    print("\nReceived Event")
    print("-" * 40)

    for key, value in event.items():
        print(f"{key}: {value}")

    print("-" * 40)


def main():

    try:

        consumer = create_consumer()

        logger.info(
            "Consumer started."
        )

        for message in consumer:

            try:

                process_message(message)

            except Exception as error:

                logger.error(
                    f"Message processing failed: {error}"
                )

    except Exception as error:

        logger.error(
            f"Consumer terminated: {error}"
        )


if __name__ == "__main__":
    main()