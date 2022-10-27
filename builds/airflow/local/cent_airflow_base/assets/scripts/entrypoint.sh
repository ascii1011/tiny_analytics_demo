#!/bin/bash

echo "AIRFLOW_HOME: {$AIRFLOW_HOME}"
echo "AIRFLOW_PKG_EXEC: {$AIRFLOW_PKG_EXEC}"


#AIRFLOW_EXEC"/usr/local/bin/airflow"
#AIRFLOW_LOGS_FOLDER="/opt/airflow/logs"
#AIRFLOW_UI_PORT="8080"


#echo "airflow db init"
#airflow db initdb

#echo "airflow init"

#echo "Creating user"
#airflow users create \
#    --username admin \
#    --firstname Chris \
#    --lastname Harty \
#    --role Admin \
#    --email ascii1011@gmail.com


#echo "starting webserver"
#nohup airflow webserver --port 8080 0<&- &> $AIRFLOW_LOGS_PATH/webserver.log &

#echo "starting scheduler"
#nohup airflow scheduler 0<&- &> $AIRFLOW_LOGS_PATH/scheduler.log &

echo 'tailing...'
tail -f /dev/null
