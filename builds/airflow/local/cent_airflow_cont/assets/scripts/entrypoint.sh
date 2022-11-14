#!/bin/bash

. ./utils.sh --source-only

display_env


./apply_extension_resources.sh
./apply_platform_resources.sh
./apply_client_resources.sh


init_airflow

#sleep 2

airflow_create_user

#sleep 2

start_airflow

display_env

#ps_aux

echo 'tailing...'
tail -f /dev/null
