#!/bin/bash

echo "AIRFLOW_HOME: {$AIRFLOW_HOME}"
echo "AIRFLOW_PKG_EXEC: {$AIRFLOW_PKG_EXEC}"
echo "AIRFLOW_PKG_HOME: {$AIRFLOW_PKG_HOME}"
echo "AIRFLOW_LOGS_PATH: {$AIRFLOW_LOGS_PATH}"
echo "AIRFLOW_UI_PORT: {$AIRFLOW_UI_PORT}"

echo "airflow db init"
airflow db init

echo "Creating user"
airflow users create \
    --username admin \
    --password airflow \
    --firstname Chris \
    --lastname Harty \
    --role Admin \
    --email ascii1011@gmail.com

echo "starting webserver"
#airflow webserver &
nohup airflow webserver --port $AIRFLOW_UI_PORT 0<&- &> $AIRFLOW_LOGS_PATH/webserver.log &

echo "starting scheduler"
#airflow scheduler &
nohup airflow scheduler 0<&- &> $AIRFLOW_LOGS_PATH/scheduler.log &

echo 'tailing...'
tail -f /dev/null
