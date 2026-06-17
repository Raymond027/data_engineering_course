# User Signup Event Pipeline

Mini Kafka Event-Driven Application

## Architecture

Producer
    |
    v
Kafka Topic (user-signup-events)
    |
    v
Consumer
    |
    v
Welcome Email Service

## Run Kafka

Start Zookeeper

bin/zookeeper-server-start.sh config/zookeeper.properties

Start Kafka

bin/kafka-server-start.sh config/server.properties

## Run Consumer

python -m app.consumer.signup_consumer

## Run Producer

python -m app.producer.signup_producer

## Expected Output

Consumer started...

--------------------------------------------------

New Signup Event

User ID : 1

Name    : John Doe

Email   : john@example.com

--------------------------------------------------

Welcome email sent to John Doe (john@example.com)

New Signup Event

User ID : 2

Name    : Alice Smith

Email   : alice@example.com

--------------------------------------------------

Welcome email sent to Alice Smith (alice@example.com)