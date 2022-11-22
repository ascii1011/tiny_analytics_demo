#!/bin/bash

source env.sh

echo ""
echo "Creating ${NETWORK} network bridge."
docker network create --attachable --driver=bridge ${NETWORK}

#docker network create --gateway 10.5.0.1 --subnet 10.5.0.0/16 ${NETWORK}

