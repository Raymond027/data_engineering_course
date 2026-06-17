from app.utils.kafka_client import create_producer
from app.models.signup_event import SignupEvent
from app.config import TOPIC_NAME
from app.utils.logger import logger


def publish_signup_event(event):

    producer = create_producer()

    try:

        message = SignupEvent.to_json(event)

        producer.send(
            TOPIC_NAME,
            value=message
        )

        producer.flush()

        print(
            f"Signup event sent for "
            f"{event['email']}"
        )

        logger.info(
            f"Event published: "
            f"{event['email']}"
        )

    except Exception as e:

        logger.error(
            f"Producer error: {e}"
        )

        print(f"Error: {e}")

    finally:
        producer.close()


if __name__ == "__main__":

    users = [
        {
            "user_id": 1,
            "name": "John Doe",
            "email": "john@example.com"
        },
        {
            "user_id": 2,
            "name": "Alice Smith",
            "email": "alice@example.com"
        },
        {
            "user_id": 3,
            "name": "Bob Johnson",
            "email": "bob@example.com"
        }
    ]

    for user in users:
        publish_signup_event(user)