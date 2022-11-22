#!/bin/bash                                                                                                                                                                                                                                                   

tail -f $AIRFLOW_LOGS_PATH/webserver.log $AIRFLOW_LOGS_PATH/scheduler.log

