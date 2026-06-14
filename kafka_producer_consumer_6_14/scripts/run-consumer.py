from kafka_client.consumer import EventConsumer

if __name__ == "__main__":
    consumer = EventConsumer()
    consumer.start_listening()