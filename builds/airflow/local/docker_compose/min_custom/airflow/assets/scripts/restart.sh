#!/bin/bash                                                                                                                                                                                                                                                   

. ./utils.sh --source-only

ps_aux

stop_airflow

ps_aux

start_airflow

ps_aux

