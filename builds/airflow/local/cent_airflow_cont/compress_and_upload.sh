#!/bin/bash        

source env_vars.sh

#tar -zcvf tmp/airflow_packages_mods.tar.gz assets/packages/airflow/
#docker cp tmp/airflow_packages_mods.tar.gz $CONTAINER_NAME:/opt/scripts

# copy custom modules
#docker cp assets/packages/airflow/api/common/experimental/tapd_trigger.py $CONTAINER_NAME:/usr/local/lib/python3.10/site-packages/airflow/api/common/experimental/
#docker cp assets/packages/airflow/models/taskinstance.py                  $CONTAINER_NAME:/usr/local/lib/python3.10/site-packages/airflow/models/
#docker cp assets/packages/airflow/www/api/experimental/endpoints.py       $CONTAINER_NAME:/usr/local/lib/python3.10/site-packages/airflow/www/api/experimental/

docker cp assets/packages/airflow/api/common/experimental/tapd_trigger.py $CONTAINER_NAME:$OPT_MODS
docker cp assets/packages/airflow/models/taskinstance.py                  $CONTAINER_NAME:$OPT_MODS
docker cp assets/packages/airflow/www/api/experimental/endpoints.py       $CONTAINER_NAME:$OPT_MODS

