#!/bin/bash

#. ./envs.sh --source-only

# create custom utils subfolder
#mkdir /usr/local/lib/python3.10/site-packages/airflow/utils/tapd
CUSTOM_AIRFLOW_UTILS_PATH=$AIRFLOW_PKG_HOME/utils/$TAG
mkdir CUSTOM_AIRFLOW_UTILS_PATH
export CUSTOM_AIRFLOW_UTILS_PATH


### airflow mods ###

function apply__airflow_settings__mod {
    cp /opt/tmp/artifacts/packages/airflow/settings.py /usr/local/lib/python3.10/site-packages/airflow/settings.py
}

function apply__enhanced_trigger__ext {
    # """
    # This mod allows for dags to leverage xcom transformed params from an 'enhanced trigger' dag api call
    #
    # How it works:
    #    1) api call: host/experimental/api/enhanced_trigger_dag/dag_workflow1&tapd_varx=99?tapd_pig=555
    #        - the tapd_trigger.py module is called and then
    #          - transforms the passed url params into xcom pairs varx=99 and pig=555 while being linked to the 
    #            dag_run that was triggered via the dag and execution_date
    #    2) create a dag that calls the `all_args = ti.xcom_pull_params()`
    # """
    # Add custom kwargs to airflow.cfg for enhanced_trigger_dag

    ### create custom airflow.cfg key/val pairs
    # export AIRFLOW__TAPD__ENHANCED_TRIGGER_XCOM_KEY_PREFIX="tapd_"
    # export AIRFLOW__TAPD__ENHANCED_TRIGGER_XCOM_TASK_ID="tapd_args"


    # copy over the experimental api module.
    # this needs to be in place before the endpoints.py endpoint is created

    # apply api module
    cp /opt/tmp/artifacts/packages/airflow/api/common/experimental/tapd_trigger.py /usr/local/lib/python3.10/site-packages/airflow/api/common/experimental/
    # apply taskinstance.py update
    cp /opt/tmp/artifacts/packages/airflow/models/taskinstance.py                  /usr/local/lib/python3.10/site-packages/airflow/models/
    # apply endpoint update
    cp /opt/tmp/artifacts/packages/airflow/www/api/experimental/endpoints.py       /usr/local/lib/python3.10/site-packages/airflow/www/api/experimental/

}

apply__airflow_settings__mod
apply__enhanced_trigger__ext

