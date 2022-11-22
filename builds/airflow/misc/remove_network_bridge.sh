#!/bin/bash

source env.sh

echo ""
echo "Removing ${NETWORK} network bridge."
docker network rm ${NETWORK}

