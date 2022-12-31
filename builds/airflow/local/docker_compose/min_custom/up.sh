#!/bin/bash 

docker-compose --env-file ~/dev/.env up -d --force-recreate

#sleep 1

# container is not automatically onboarding js files, so need to manually apply changes
#docker exec mongodb mongosh platform /docker-entrypoint-initdb.d/init-mongo-js -u mgadmin -p mgpass --authenticationDatabase admin

