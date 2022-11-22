#!/bin/bash

CONTAINER=pgadmin4
USER=pgadmin
PASS=pgadmin
PGPASS_DIR=/var/lib/pgadmin/storage/some_gmail.com/
PASS_FILE=postgres_pgpass

echo ""
echo "_________________________________"
echo "Adding postgres server to pgadmin"

# create the anticipated landing dir for server.json files.  This dir is generated by the email in the container.
docker exec -u $USER:$PASS -it $CONTAINER mkdir -m 700 $PGPASS_DIR
# need to copy to tmp in order to chown it, in order to move it
docker cp $PASS_FILE $CONTAINER:/tmp/$PASS_FILE
# chown it
docker exec -it -u root $CONTAINER chown $USER:$PASS /tmp/$PASS_FILE
docker exec -it $CONTAINER mv /tmp/$PASS_FILE $PGPASS_DIR
docker exec -it $CONTAINER chmod 600 $PGPASS_DIR/$PASS_FILE


SERV_FILE=postgres_servers.json
docker cp $SERV_FILE $CONTAINER:/tmp/$SERV_FILE
docker exec -it $CONTAINER /venv/bin/python3 /pgadmin4/setup.py --load-servers /tmp/$SERV_FILE --user some@gmail.com
