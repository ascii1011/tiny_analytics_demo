#!/bin/bash

source env_vars.sh

./stop_remove_container.sh

echo ""
echo "building image '$IMAGE_NAME' ..."
sudo docker build --tag $IMAGE_NAME .
