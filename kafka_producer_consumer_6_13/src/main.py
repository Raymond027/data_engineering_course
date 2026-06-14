from consumers.consumer import KafkaConsumerService, shutdown_handler
import signal


def main():
    service = KafkaConsumerService()

    signal.signal(signal.SIGINT, shutdown_handler(service))
    signal.signal(signal.SIGTERM, shutdown_handler(service))

    service.start()


if __name__ == "__main__":
    main()