#!/bin/bash

docker-compose down

docker rmi min_custom_airflow

#rm -f ~/dev/mnt_data/tiny_analytics_platform/min_custom/airflow/logs/*.log
#rm -rf ~/dev/mnt_data/tiny_analytics_platform/min_custom/airflow/logs/*.*

./mongodb/teardown_mongodb.sh
