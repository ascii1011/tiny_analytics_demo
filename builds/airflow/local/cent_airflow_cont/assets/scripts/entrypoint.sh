#!/bin/bash                                                                                                                                                                                                                                              

. ./utils.sh --source-only

ls -alht /usr/local/lib/python3.10/site-packages/airflow/api/common/experimental/

display_env

init_airflow

sleep 2

airflow_create_user

sleep 2

start_airflow

ps_aux

echo 'tailing...'
tail -f /dev/null
