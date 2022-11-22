#!/bin/bash

TAG=tapd
IMAGE_NAME="img_min_airflow24"
CONTAINER_NAME="con_min_airflow24"
PORT="8080"
PORT_MAP=" -p 8080:8080 "
OPT_MODS=/opt/mods

AIRFLOW__CORE__LOAD_EXAMPLES=False
