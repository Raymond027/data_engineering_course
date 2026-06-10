# Kafka Producer Consumer System

## Goal

Run Apache Kafka locally using Docker Compose.

## Stack

- Apache Kafka 4.0
- Docker Desktop
- Docker Compose
- KRaft Mode

## Commands

Start:

docker compose up -d

Stop:

docker compose down

Logs:

docker compose logs -f

Status:

docker ps

## Verification

Create Topic:

docker exec kafka kafka-topics.sh \
--create \
--topic test-topic \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1

List Topics:

docker exec kafka kafka-topics.sh \
--bootstrap-server localhost:9092 \
--list