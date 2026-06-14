from kafka import KafkaConsumer
from kafka_client.base import KafkaBase
from utils.json_serializer import deserialize_message
from utils.logger import get_logger
from config.settings import TOPIC_USER_EVENTS, CONSUMER_GROUP_ID, AUTO_OFFSET_RESET

logger = get_logger("consumer")


class EventConsumer(KafkaBase):
    def __init__(self):
        super().__init__()

        self.consumer = KafkaConsumer(
            TOPIC_USER_EVENTS,
            bootstrap_servers=self.bootstrap_servers,
            group_id=CONSUMER_GROUP_ID,
            auto_offset_reset=AUTO_OFFSET_RESET,
            enable_auto_commit=True,
            value_deserializer=deserialize_message,
        )

    def start_listening(self):
        logger.info("Consumer started listening...")

        try:
            for message in self.consumer:
                event = message.value

                logger.info(
                    f"Received event | partition={message.partition} "
                    f"offset={message.offset} | data={event}"
                )

        except Exception as e:
            logger.error(f"Consumer error: {e}")

        finally:
            self.consumer.close()