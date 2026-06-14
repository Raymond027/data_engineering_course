# Kafka End-to-End Pipeline

## Overview
This project demonstrates a complete Kafka pipeline using Python:
Producer → Kafka Topic → Consumer

## Architecture

Producer (Python)
   ↓
Kafka Topic: user-events
   ↓
Consumer (Python)

## How to Run

### 1. Start Kafka
Make sure Kafka is running locally:

```bash
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties