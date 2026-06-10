#!/bin/bash

docker ps

docker inspect kafka \
--format='{{json .State.Health}}'