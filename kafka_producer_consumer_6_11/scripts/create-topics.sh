#!/bin/bash

BOOTSTRAP_SERVER=localhost:9092

kafka-topics.sh \
--create \
--topic user-events \
--bootstrap-server $BOOTSTRAP_SERVER \
--partitions 3 \
--replication-factor 1

kafka-topics.sh \
--create \
--topic order-events \
--bootstrap-server $BOOTSTRAP_SERVER \
--partitions 3 \
--replication-factor 1