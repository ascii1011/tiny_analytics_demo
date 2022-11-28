#!/bin/bash

chmod +x *.sh
chmod +x *.py

# build and apply envs
./process_env.py ~/.bash_profile

source ~/.bash_profile


# ingestion folder structure
echo ""
echo "client batch root: ${CLIENT_BATCH_ROOT}"
mkdir -p $CLIENT_BATCH_ROOT


### typical general onboarding of clients
# ldap auth add creds
# db entries mongo, etc
# onboard client + project ingestion, staging, prod

### onboarding data varies 

### onboard client_id: lala, project_id: ctc
echo ""
echo "ingestion: ${INGESTION_ROOT}/lala/ctc"
mkdir -p $INGESTION_ROOT/lala/ctc

echo ""
echo "staging: ${STAGING_ROOT}/lala/ctc"
mkdir -p $STAGING_ROOT/lala/ctc

### tmp mounting dags folder from host
#echo ""
#echo "copying client dags..."
#cp client_data_generation_dag.py /opt/airflow/dags
#cp lala_workflow_dags/client__lala__ctc__etl.py /opt/airflow/dags

./mongo_onboard__client__lala.py