#!/bin/bash

docker-compose down

docker rmi min_custom_airflow

./mongodb/teardown_mongodb.sh
