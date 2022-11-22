#!/bin/bash

# build and apply envs
./process_env.py ~/.bash_profile

source ~/.bash_profile

# ingestion folder structure
# all new files land under this root path
echo ""
echo "ingestion root: ${INGESTION_ROOT}"
mkdir -p $INGESTION_ROOT

# staging folder structure
# transformed data lives here
mkdir -p $STAGING_ROOT
