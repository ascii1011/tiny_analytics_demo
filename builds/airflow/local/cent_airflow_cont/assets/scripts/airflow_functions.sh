#!/bin/bash

function update_login_env_variables {
    # these will come from the openshift configmap
    echo "export AIRFLOW_GPL_UNIDECODE=$AIRFLOW_GPL_UNIDECODE" >> /etc/profile.d/airflow-env.sh
    #all other airflow, anaconda, hdfs, hadoop, hive, kerb, LC_ALL, mongo, sendgrid, spark, kub_node, webserver_config.py
    # and PATH from dockerfile

}

function stop_airflow {
    ps -ef | egrep 'airflow scheduler|airflow-webserver|airflow webserver' awk '{ print $2 }' | while read x; do kill -9 $x; done
}

function airflow_initialize {
    echo "updating /opt/airflow/airflow.cfg..."
    sed -i "s|@AIRFLOW_DAGS_FOLDER@|$AIRFLOW_DAGS_FOLDER|" $AIRFLOW_HOME/airflow.cfg
    # logs, pgsql(db_user, server, port, db_name, port), ui_port, ssl crt/key, ip filter
    echo "Escape special characters in pass"
    AIRFLOW_DB_PASSWORD=`echo ${AIRFLOW_DB_PASSWORD} | sed 's/!/\\!/g'`
    # then pass db_password

    airflow initdb
}

function start_airflow {
    WEB_LOG=$AIRFLOW_LOGS_FOLDER/webserver.log
    SCHED_LOG=$AIRFLOW_LOGS_FOLDER/scheduler.log

    echo "starting webserver"

    nohup $ANACONDA_HOME/bin/airflow webserver -p $AIRFLOW_UI_PORT 0<&- &> $WEB_LOG &

    echo "starting scheduler.."

    nohup $ANACONDA_HOME/bin/airflow scheduler 0<&- &> $SCHED_LOG &

    echo "done"
}



AIRFLOW_EXEC"/usr/local/bin/airflow"
AIRFLOW_LOGS_FOLDER="/opt/airflow/logs"
AIRFLOW_UI_PORT="8080"


WEB_LOG=$AIRFLOW_LOGS_FOLDER/webserver.log
SCHED_LOG=$AIRFLOW_LOGS_FOLDER/scheduler.log

echo "starting webserver"

nohup $AIRFLOW_EXEC webserver -p $AIRFLOW_UI_PORT 0<&- &> $WEB_LOG &

echo "starting scheduler.."

nohup $AIRFLOW_BIN scheduler 0<&- &> $SCHED_LOG &

echo "done"