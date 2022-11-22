#!/bin/bash

#cd pgadmin
#./pgadmin_down.sh
#cd ..

cd postgres
./postgres_down.sh
cd ..


./remove_network_bridge.sh


./docker_info.sh
