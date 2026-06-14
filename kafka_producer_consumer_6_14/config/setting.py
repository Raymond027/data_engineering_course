import os

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")

TOPIC_USER_EVENTS = "user-events"

CONSUMER_GROUP_ID = "user-events-group"

AUTO_OFFSET_RESET = "earliest"

ENABLE_AUTO_COMMIT = True