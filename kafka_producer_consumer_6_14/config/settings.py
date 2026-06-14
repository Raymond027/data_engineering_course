import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
    KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "user-events")
    KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "default-group")
    AUTO_OFFSET_RESET = os.getenv("AUTO_OFFSET_RESET", "earliest")