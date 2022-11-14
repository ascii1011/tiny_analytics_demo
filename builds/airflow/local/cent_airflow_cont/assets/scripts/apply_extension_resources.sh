#!/bin/bash

### airflow mods ###
# Add custom kwargs to airflow.cfg for enhanced_trigger_dag
AIRFLOW__TAPD__ENHANCED_TRIGGER_XCOM_KEY_PREFIX="tapd_"
AIRFLOW__TAPD__ENHANCED_TRIGGER_XCOM_TASK_ID="tapd_args"

mkdir -p $OPT_MODS

# create custom utils subfolder
#mkdir /usr/local/lib/python3.10/site-packages/airflow/utils/tapd
mkdir $AIRFLOW_PKG_HOME/utils/$TAG
