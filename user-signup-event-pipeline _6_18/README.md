# Kafka User Signup Event Pipeline

A simple event-driven data pipeline built using Apache Kafka and Python.

This project demonstrates:

- Kafka Producer
- Kafka Topic
- Kafka Consumer
- JSON Event Messages
- Event Processing
- Error Handling
- Clean Project Architecture

---

## Architecture

Producer → Kafka Topic → Consumer → Welcome Email Processing

---

## Tech Stack

- Python 3.11+
- Apache Kafka
- kafka-python

---

## Project Structure

```text
kafka-user-signup-pipeline/
├── producer/
├── consumer/
├── config/
├── models/
├── utils/
├── diagrams/
├── screenshots/
└── README.md
```

---

## Setup

### Start Zookeeper

```bash
zookeeper-server-start.sh config/zookeeper.properties
```

### Start Kafka

```bash
kafka-server-start.sh config/server.properties
```

### Create Topic

```bash
kafka-topics.sh \
--create \
--topic user-signup-events \
--bootstrap-server localhost:9092
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Consumer

```bash
python consumer/consumer.py
```

### Run Producer

```bash
python producer/producer.py
```

---

## Sample Event

```json
{
  "user_id": 1,
  "username": "alice",
  "email": "alice@example.com"
}
```

---

## Learning Outcomes

This project demonstrates understanding of:

- Event-driven architecture
- Producer/Consumer communication
- Kafka Topics
- JSON serialization
- Error handling
- Project organization
- GitHub portfolio standards