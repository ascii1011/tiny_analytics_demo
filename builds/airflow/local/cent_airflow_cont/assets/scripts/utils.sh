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
    echo "___________________OS________________________"
    echo "PATH:   '${PATH}'"

    echo ""
    echo "___________________AIRFLOW: ${TAG}___________"
    echo "AIRFLOW_HOME:           '${AIRFLOW_HOME}'"
    echo "AIRFLOW_DAGS_PATH:      '${AIRFLOW_DAGS_PATH}'"
    echo "AIRFLOW_LOGS_PATH:      '${AIRFLOW_LOGS_PATH}'"
    echo "AIRFLOW_PKG_EXEC:       '${AIRFLOW_PKG_EXEC}'"
    echo "AIRFLOW_PKG_HOME:       '${AIRFLOW_PKG_HOME}'"
    echo "AIRFLOW_UI_PORT:        '${AIRFLOW_UI_PORT}'"
    echo "AIRLFOW_GPL_UNIDECODE:  '${AIRLFOW_GPL_UNIDECODE}'"
    echo "SLUGIFY_..._UNIDECODE:  '${SLUGIFY_USES_TEXT_UNIDECODE}'"

    echo ""
    echo "___________________PLATFORM__________________"
    echo "INGESTION_ROOT:  '${INGESTION_ROOT}'"
    echo "INGESTION_TMPL:  '${INGESTION_TMPL}'"
    echo "STAGING_ROOT:    '${STAGING_ROOT}'"
    echo "STAGING_TMPL:    '${STAGING_TMPL}'"

    echo ""
    echo "___________________CLIENT____________________"
    echo "CLIENT_BATCH_ROOT:  '${CLIENT_BATCH_ROOT}'"
    echo "CLIENT_BATCH_TMPL:  '${CLIENT_BATCH_TMPL}'"

    echo ""
    echo "___________________CUSTOM____________________"
    echo "BIGDATA_PYLIB:   '${BIGDATA_PYLIB}'"
    echo "PYTHONPATH:      '${PYTHONPATH}'"
    echo "Temp Mods path:  '${OPT_MODS}'"
    echo ""
}

function airflow_create_user {
    echo ""
    echo "Creating user"
    airflow users create \
        --username admin \
        --password airflow \
        --firstname twig \
        --lastname derp \
        --role Admin \
        --email some@gmail.com
}
