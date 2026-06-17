from app.utils.kafka_client import create_consumer
from app.models.signup_event import SignupEvent
from app.services.email_service import send_welcome_email
from app.config import TOPIC_NAME
from app.utils.logger import logger


def start_consumer():

    consumer = create_consumer(TOPIC_NAME)

    print("Consumer started...")
    print("-" * 50)

    try:

        for message in consumer:

            try:

                json_message = (
                    message.value.decode("utf-8")
                )

                user = SignupEvent.from_json(
                    json_message
                )

                print("New Signup Event")
                print(
                    f"User ID : {user['user_id']}"
                )
                print(
                    f"Name    : {user['name']}"
                )
                print(
                    f"Email   : {user['email']}"
                )
                print("-" * 50)

                send_welcome_email(user)

                logger.info(
                    f"Processed signup: "
                    f"{user['email']}"
                )

            except Exception as e:

                logger.error(
                    f"Message processing failed: {e}"
                )

                print(
                    f"Processing error: {e}"
                )

    except KeyboardInterrupt:

        print("\nConsumer stopped.")

    finally:

        consumer.close()


if __name__ == "__main__":
    start_consumer()