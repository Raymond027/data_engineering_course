from config.settings import KAFKA_BROKER

class KafkaBase:
    def __init__(self):
        self.bootstrap_servers = KAFKA_BROKER