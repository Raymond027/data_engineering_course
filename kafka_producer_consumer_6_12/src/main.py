from datetime import datetime

from config.settings import KAFKA_TOPIC
from src.producers.producer import UserEventProducer


def main():

    producer = UserEventProducer()

    try:

        for i in range(1, 11):

            message = {
                "event_id": i,
                "event_type": "test_event",
                "timestamp": datetime.utcnow().isoformat(),
                "message": f"Kafka test message {i}"
            }

            producer.send_message(
                topic=KAFKA_TOPIC,
                message=message
            )

    finally:
        producer.close()


if __name__ == "__main__":
    main()