#!/bin/sh

#pip install -r requirements.txt

#function airflow_create_user {
#    echo ""
#    echo "Creating user"
#    airflow users create \
#        --username admin \
#        --password airflow \
#        --firstname twig \
#        --lastname derp \
#        --role Admin \
#        --email some@gmail.com
#}

#echo ""
#echo "airflow db init"

#airflow db reset

#airflow db init

#airflow_create_user

#echo ""
#echo "starting webserver"
#nohup airflow webserver --port 8080 0<&- &> /opt/airflow/logs/webserver.log &

#echo "starting scheduler"
#nohup airflow scheduler 0<&- &> /opt/airflow/logs/scheduler.log &

#echo 'tailing...'
#tail -f /dev/null
