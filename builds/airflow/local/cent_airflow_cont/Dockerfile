FROM c8py3_airflow24_base

LABEL name="airflow24_cont" \
      build-date="2022-10-01"

COPY assets/scripts/*.sh /opt/scripts/
RUN chmod +x /opt/scripts/*.sh

WORKDIR /opt/scripts
CMD /opt/scripts/entrypoint.sh
