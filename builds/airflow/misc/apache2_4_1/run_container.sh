#!/bin/bash

source env_vars.sh

./stop_remove_container.sh

# run new container from iamge
echo "sudo docker run -d ${PORT_MAP} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
echo "sudo docker exec -it ${CONTAINER_NAME} /bin/bash"
sudo docker run -d $PORT_MAP --name $CONTAINER_NAME $IMAGE_NAME

echo ""
echo "docker top:"
sudo docker top $CONTAINER_NAME

echo ""
echo "docker logs:"
sudo docker logs $CONTAINER_NAME
