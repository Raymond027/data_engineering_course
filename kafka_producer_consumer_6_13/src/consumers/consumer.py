from confluent_kafka import Consumer, KafkaError
import signal
import sys

from config.settings import Settings
from utils.logger import get_logger

logger = get_logger("KafkaConsumer")


class KafkaConsumerService:
    def __init__(self):
        self.running = True

        self.consumer = Consumer({
            "bootstrap.servers": Settings.KAFKA_BOOTSTRAP_SERVERS,
            "group.id": Settings.KAFKA_GROUP_ID,
            "auto.offset.reset": Settings.AUTO_OFFSET_RESET,
            "enable.auto.commit": True
        })

        self.topic = Settings.KAFKA_TOPIC

    def start(self):
        logger.info(f"Subscribing to topic: {self.topic}")
        self.consumer.subscribe([self.topic])

        while self.running:
            msg = self.consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    logger.info("End of partition reached")
                else:
                    logger.error(f"Kafka error: {msg.error()}")
                continue

            self.process_message(msg)

        self.shutdown()

    def process_message(self, msg):
        try:
            key = msg.key().decode("utf-8") if msg.key() else None
            value = msg.value().decode("utf-8")

            logger.info(f"Received message | key={key} | value={value}")

        except Exception as e:
            logger.error(f"Error processing message: {e}")

    def shutdown(self):
        logger.info("Shutting down consumer...")
        self.consumer.close()


# Graceful shutdown handler
def shutdown_handler(consumer_service):
    def handler(sig, frame):
        logger.info("Shutdown signal received")
        consumer_service.running = False
    return handler