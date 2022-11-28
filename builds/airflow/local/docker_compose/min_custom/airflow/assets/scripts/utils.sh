#!/bin/sh                                                                                                                                                                                                                                                     

function init_airflow {
    echo ""
    echo "airflow db init"

    airflow db init
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

function display_platform {
    echo ""
    echo "___________________PLATFORM__________________"
    echo "INGESTION_ROOT:  '${INGESTION_ROOT}'"
    echo "INGESTION_TMPL:  '${INGESTION_TMPL}'"
    echo "STAGING_ROOT:    '${STAGING_ROOT}'"
    echo "STAGING_TMPL:    '${STAGING_TMPL}'"
}

function display_os {
    echo ""
    echo "___________________OS__________________"
    echo "PATH:            '${PATH}'"
    echo "BIGDATA_PYLIB:   '${BIGDATA_PYLIB}'"
    echo "PYTHONPATH:      '${PYTHONPATH}'"
    echo "Temp Mods path:  '${OPT_MODS}'"
}

function display_airflow {
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
}

function display_client {
    echo ""
    echo "___________________CLIENT____________________"
    echo "CLIENT_BATCH_ROOT:  '${CLIENT_BATCH_ROOT}'"
    echo "CLIENT_BATCH_TMPL:  '${CLIENT_BATCH_TMPL}'"
}

function display_mods {
    echo ""
    echo "___________________MODS____________________"
    echo "na:  ''"
}

function display_all_env {
    display_platform

    display_os

    display_airflow

    display_mods

    display_client
}


function apply_platform_resources {
    echo ""
    echo "applying platform resources..."

    cd platform_resources
    chmod +x *.sh
    chmod +x *.py
    
    ./apply.sh
    cd ../
}

function apply_mod_resources {
    echo ""
    echo "applying mods..."

    cd mod_resources
    chmod +x *.sh
    
    ./apply.sh
    cd ../
}

function apply_client_resources {
    echo ""
    echo "applying client..."

    cd client_resources
    chmod +x *.sh
    chmod +x *.py
    
    ./apply.sh
    cd ../
}

function apply_all_resources {
    # this needs to be applied before the db init and services are run
    

    apply_platform_resources
    source ~/.bash_profile
    display_platform
    display_os


    #display_airflow

    #apply_mod_resources
    #display_mods

    apply_client_resources
    display_client
}


function run_airflow {

    init_airflow

    #sleep 2

    airflow_create_user

    #sleep 2

    start_airflow

    display_all_env

    ps_aux
}


function onboard {

    source ~/.bash_profile

    pip install -r requirements.txt

    tree /opt/

    display_all_env


    apply_all_resources

    # resources above have applied and re-sourced the ~/.bash_profile
    # however this level of the bash script is out of that scope
    source ~/.bash_profile

    run_airflow
}

