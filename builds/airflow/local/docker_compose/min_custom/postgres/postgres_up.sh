#!/bin/bash

echo ""
echo "________________"
echo "docker-compose up -d"
docker-compose up -d

./add_server_to_pgadmin.sh
