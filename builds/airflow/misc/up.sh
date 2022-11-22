#!/bin/bash

./docker_info.sh

./create_network_bridge.sh
sleep 5

#cd pgadmin
#./pgadmin_up.sh
#cd ..

#echo "sleeping for 90 seconds... waiting for pgadmin"
#sleep 90

cd postgres
./postgres_up.sh
cd ..
sleep 5

./docker_info.sh
