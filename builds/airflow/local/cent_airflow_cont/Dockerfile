FROM c8py3_airflow24_base

LABEL name="airflow24_cont" \
      build-date="2022-10-01"

### Override airflow.cfg ###
ENV AIRFLOW__CORE__LOAD_EXAMPLES="False"
ENV AIRFLOW__API__AUTH_BACKENDS="airflow.api.auth.backend.basic_auth"
ENV BIGDATA_PYLIB="/opt/mnt/bigdata/pylib"
ENV PYTHONPATH=$PYTHONPATH:$BIGDATA_PYLIB

COPY assets/root/.bash_profile /root/.bash_profile

# copy over big data central dev support (usually already available through mnt or copied into each container for stateless)
RUN mkdir -p /opt/mnt/bigdata/pylib
COPY assets/bigdata_pylib/*.* /opt/mnt/bigdata/pylib

# copy over all dags
RUN mkdir -p /opt/airflow/dags
COPY assets/dags/*.py /opt/airflow/dags

COPY assets/packages/airflow/api/common/experimental/tapd_trigger.py /usr/local/lib/python3.10/site-packages/airflow/api/common/experimental/
COPY assets/packages/airflow/models/taskinstance.py                  /usr/local/lib/python3.10/site-packages/airflow/models/
COPY assets/packages/airflow/www/api/experimental/endpoints.py       /usr/local/lib/python3.10/site-packages/airflow/www/api/experimental/

# copy over utils and tools
COPY assets/scripts/*.sh /opt/scripts/
RUN chmod +x /opt/scripts/*.sh

WORKDIR /opt/scripts
CMD /opt/scripts/entrypoint.sh
