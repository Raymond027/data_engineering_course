from models.signup_event import SignupEvent
from utils.kafka_client import create_producer
from config.settings import TOPIC_NAME
from utils.logger import get_logger

logger = get_logger(__name__)


def send_signup_event(event):
    producer = create_producer()

    producer.send(
        TOPIC_NAME,
        value=event.to_dict()
    )

    producer.flush()

    logger.info(
        f"Signup Event Sent: {event.username}"
    )


def main():

    users = [
        SignupEvent(
            1,
            "alice",
            "alice@example.com"
        ),
        SignupEvent(
            2,
            "bob",
            "bob@example.com"
        ),
        SignupEvent(
            3,
            "charlie",
            "charlie@example.com"
        )
    ]

    for user in users:
        send_signup_event(user)


if __name__ == "__main__":
    main()