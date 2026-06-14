# Kafka Producer Consumer System

## Topics

1. user-events
2. order-events
3. test-topic

## Commands

Create Topics

./scripts/create-topics.sh

List Topics

./scripts/list-topics.sh

Delete Topic

./scripts/delete-topic.sh test-topic

## Verification

docker ps

kafka-topics.sh --list --bootstrap-server localhost:9092