#!/bin/bash

source env_vars.sh

# remove previous containers first
echo "sudo docker ps -a | grep $CONTAINER_NAME"
sudo docker ps -a | grep $CONTAINER_NAME
AF_CONT=$(sudo docker ps -a | grep $CONTAINER_NAME)
echo "AF_CONT: [$AF_CONT]"
if [ -z "$AF_CONT" ]; then
    echo "Container not found"
else
    ARR=($AF_CONT)
    echo "ARR: $ARR"
    CONTAINER_ID=${ARR[0]}
    echo "CONT ID: $CONTAINER_ID"
    if [ -z CONTAINER_ID ]; then
        echo "container id not found"
    else
    echo "attempting to stop and rum container"
    sudo docker stop $CONTAINER_ID
    sudo docker rm $CONTAINER_ID
    fi
fi
