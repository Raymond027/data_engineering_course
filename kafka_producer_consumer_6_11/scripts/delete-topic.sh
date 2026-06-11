#!/bin/bash

TOPIC=$1

kafka-topics.sh \
--delete \
--topic $TOPIC \
--bootstrap-server localhost:9092