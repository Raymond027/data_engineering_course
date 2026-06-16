# Kafka JSON Event Pipeline

## Overview
A production-style Kafka pipeline that sends structured JSON events.

## Event Types
- user_signup
- user_login
- order_created

## Run Kafka

docker-compose -f docker/docker-compose.yml up -d

## Run Consumer

python -m src.consumer.consumer

## Run Producer

python -m src.producer.producer