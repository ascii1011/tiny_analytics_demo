FROM c8py3_airflow24_base

LABEL name="airflow24_cont" \
      build-date="2022-10-01"

ENV AIRFLOW__TAPD__ENHANCED_TRIGGER_XCOM_KEY_PREFIX="tapd_"
ENV AIRFLOW__TAPD__ENHANCED_TRIGGER_XCOM_TASK_ID="tapd_args"
ENV AIRFLOW__CORE__LOAD_EXAMPLES="False"
#ENV AIRFLOW__API__ENABLE_EXPERIMENTAL_API="True"
#ENV AIRFLOW__API__AUTH_BACKENDS="airflow.api.auth.backend.default"
ENV AIRFLOW__API__AUTH_BACKENDS="airflow.api.auth.backend.basic_auth"

RUN mkdir /usr/local/lib/python3.10/site-packages/airflow/utils/tapd
COPY assets/packages/airflow/api/common/experimental/tapd_trigger.py /usr/local/lib/python3.10/site-packages/airflow/api/common/experimental/
COPY assets/packages/airflow/models/taskinstance.py                  /usr/local/lib/python3.10/site-packages/airflow/models/
COPY assets/packages/airflow/www/api/experimental/endpoints.py       /usr/local/lib/python3.10/site-packages/airflow/www/api/experimental/

RUN mkdir -p /opt/airflow/dags
COPY assets/dags/*.py /opt/airflow/dags

COPY assets/scripts/*.sh /opt/scripts/
RUN chmod +x /opt/scripts/*.sh

WORKDIR /opt/scripts
CMD /opt/scripts/entrypoint.sh
