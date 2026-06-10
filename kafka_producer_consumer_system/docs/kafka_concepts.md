# Apache Kafka Concepts

## What is Apache Kafka?

Apache Kafka is a distributed event streaming platform
used for building real-time data pipelines and event-driven
applications.

Kafka allows systems to:

- Publish events
- Store events
- Process events
- Consume events

at extremely high throughput.

Originally developed by LinkedIn and later donated to
the Apache Software Foundation.

---

# Why Kafka Exists

Traditional systems often communicate directly.

Example:

Application A
    ↓
Application B

Problems:

- Tight coupling
- Difficult scaling
- Message loss
- Poor fault tolerance

Kafka introduces an event streaming layer.

Application A
    ↓
Kafka
    ↓
Application B

Benefits:

- Decoupling
- Scalability
- Reliability
- Replayability

---

# Producer

A Producer is an application that writes messages
into Kafka.

Examples:

- Website
- Mobile App
- Payment System
- IoT Device

Producer responsibilities:

- Generate events
- Send events to topics
- Select partition

Example event:

{
  "order_id": 101,
  "amount": 250
}

Producer publishes event to:

orders_topic

---

# Topic

A Topic is a logical stream of events.

Think of a topic as:

- Database table
or
- Folder of messages

Examples:

orders
payments
user_clicks
sensor_data

Topics store records in order.

---

# Partition

A Topic is divided into partitions.

Example:

orders_topic

Partition 0
Partition 1
Partition 2

Benefits:

- Parallel processing
- Higher throughput
- Scalability

Each message receives an offset.

Example:

Offset 0
Offset 1
Offset 2
Offset 3

Offsets uniquely identify messages inside a partition.

---

# Consumer

Consumer reads data from Kafka topics.

Examples:

- Spark Job
- Flink Job
- Data Warehouse Loader
- Fraud Detection Service

Consumer responsibilities:

- Subscribe to topics
- Read messages
- Process messages
- Commit offsets

---

# Consumer Group

Multiple consumers can work together.

Consumer Group:

Consumer A
Consumer B
Consumer C

Kafka distributes partitions across consumers.

Benefits:

- Scalability
- Load balancing
- Fault tolerance

---

# Broker

Kafka server is called a Broker.

Broker responsibilities:

- Store messages
- Serve consumers
- Handle replication

Production clusters contain multiple brokers.

Example:

Broker 1
Broker 2
Broker 3

This improves reliability.

---

# Offset

Offset is the position of a message within a partition.

Example:

Offset 0
Offset 1
Offset 2
Offset 3

Consumers track offsets to know what has been processed.

Benefits:

- Replay data
- Recovery
- Fault tolerance

---

# Retention

Kafka keeps messages for a configured period.

Examples:

1 day
7 days
30 days

Even after consumers read messages,
Kafka can retain them.

Benefits:

- Reprocessing
- Debugging
- Auditing
