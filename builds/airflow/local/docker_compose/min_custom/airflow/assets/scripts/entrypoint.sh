#!/bin/bash

. ./utils.sh --source-only

tree /opt/

display_all_env


apply_all_resources

# resources above have applied and re-sourced the ~/.bash_profile
# however this level of the bash script is out of that scope
source ~/.bash_profile

run_airflow

echo 'tailing...'
tail -f /dev/null
