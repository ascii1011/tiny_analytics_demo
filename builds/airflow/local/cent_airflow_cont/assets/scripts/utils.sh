#!/bin/sh                                                                                                                                                                                                                                                     

function init_airflow {
    echo ""
    echo "airflow db init"

    airflow db init
}

function start_airflow {
    echo ""
    echo "starting webserver"
    nohup airflow webserver --port $AIRFLOW_UI_PORT 0<&- &> $AIRFLOW_LOGS_PATH/webserver.log &

    echo "starting scheduler"
    nohup airflow scheduler 0<&- &> $AIRFLOW_LOGS_PATH/scheduler.log &
}

function stop_airflow {
    echo ""
    echo "stopping airflow"
    #kill $(cat $AIRFLOW_HOME/airflow-webserver.pid)
    ps -ef | egrep 'airflow|scheduler|webserver|master|gunicorn' | grep -v grep | awk '{print $2}' | xargs kill
}

function ps_aux {
    echo ""
    echo "ps -ef"
    ps -ef | egrep 'airflow|scheduler|webserver|master|gunicorn' | grep -v grep 
    #ps -ef | egrep 'airflow|scheduler|webserver|master|gunicorn' | grep -v grep | awk '{print $2}'
}

function display_env {
    echo ""
    echo "__________________________________________"
    echo "AIRFLOW_HOME:      '${AIRFLOW_HOME}'"
    echo "AIRFLOW_PKG_EXEC:  '${AIRFLOW_PKG_EXEC}'"
    echo "AIRFLOW_PKG_HOME:  '${AIRFLOW_PKG_HOME}'"
    echo "AIRFLOW_LOGS_PATH: '${AIRFLOW_LOGS_PATH}'"
    echo "AIRFLOW_UI_PORT:   '${AIRFLOW_UI_PORT}'"
}

function airflow_create_user {
    echo ""
    echo "Creating user"
    airflow users create \
        --username admin \
        --password airflow \
        --firstname Chris \
        --lastname Harty \
        --role Admin \
        --email ascii1011@gmail.com
}
