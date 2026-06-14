from kafka_client.producer import EventProducer

if __name__ == "__main__":
    producer = EventProducer()
    producer.generate_test_events(count=10)