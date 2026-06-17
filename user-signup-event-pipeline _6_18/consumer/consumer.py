from utils.kafka_client import create_consumer
from config.settings import TOPIC_NAME
from utils.logger import get_logger

logger = get_logger(__name__)


def process_signup_event(event):

    print("\nNew User Signup")
    print("-" * 30)
    print(f"User ID : {event['user_id']}")
    print(f"Username: {event['username']}")
    print(f"Email   : {event['email']}")

    print(
        f"Sending welcome email to "
        f"{event['email']}"
    )

    print("-" * 30)


def main():

    consumer = create_consumer(
        TOPIC_NAME
    )

    logger.info(
        "Consumer started..."
    )

    for message in consumer:

        try:
            process_signup_event(
                message.value
            )

        except Exception as error:
            logger.error(
                f"Processing Error: {error}"
            )


if __name__ == "__main__":
    main()