FROM c8py3_airflow24_base

LABEL name="airflow24_cont" \
      build-date="2022-10-01"

### Override airflow.cfg ###
ENV AIRFLOW__CORE__LOAD_EXAMPLES="False"
ENV AIRFLOW__API__AUTH_BACKENDS="airflow.api.auth.backend.basic_auth"

# client data source folder
ENV CLIENT_SRC_FOLDER="/opt/mnt/client_side/batch_jobs"

# platform folder structure
ENV CLIENT_INGESTION_FOLDER="/opt/mnt/workflows/clients/{client_id}/instances/ingestion"
ENV CLIENT_STAGING_FOLDER="/opt/mnt/workflows/clients/{client_id}/instances/staging"

### airflow mods ###
# Add custom kwargs to airflow.cfg for enhanced_trigger_dag
ENV AIRFLOW__TAPD__ENHANCED_TRIGGER_XCOM_KEY_PREFIX="tapd_"
ENV AIRFLOW__TAPD__ENHANCED_TRIGGER_XCOM_TASK_ID="tapd_args"

# create custom utils subfolder
RUN mkdir /usr/local/lib/python3.10/site-packages/airflow/utils/tapd

# copy custom modules
COPY assets/packages/airflow/api/common/experimental/tapd_trigger.py /usr/local/lib/python3.10/site-packages/airflow/api/common/experimental/
COPY assets/packages/airflow/models/taskinstance.py                  /usr/local/lib/python3.10/site-packages/airflow/models/
COPY assets/packages/airflow/www/api/experimental/endpoints.py       /usr/local/lib/python3.10/site-packages/airflow/www/api/experimental/


### create tenant based structure and content ###
#RUN mkdir -p $CLIENT_SRC_FOLDER

# ingestion folder structure
RUN mkdir -p $CLIENT_INGESTION_FOLDER
COPY test_data/*.txt $CLIENT_INGESTION_FOLDER

# staging folder structure
RUN mkdir -p $CLIENT_STAGING_FOLDER


# copy over all dags
RUN mkdir -p /opt/airflow/dags
COPY assets/dags/*.py /opt/airflow/dags

# copy over utils and tools
COPY assets/scripts/*.sh /opt/scripts/
RUN chmod +x /opt/scripts/*.sh

WORKDIR /opt/scripts
CMD /opt/scripts/entrypoint.sh
