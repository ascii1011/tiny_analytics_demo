FROM c8py3_airflow24_base

ARG TMP_DUMP=/opt/tmp/dump
ARG AIRFLOW__CORE__LOAD_EXAMPLES=FALSE

ENV AIRLFOW_GPL_UNIDECODE="yes"
ENV SLUGIFY_USES_TEXT_UNIDECODE="yes"
ENV AIRFLOW__CORE__LOAD_EXAMPLES=$AIRFLOW__CORE__LOAD_EXAMPLES

ENV TMP_DUMP=$TMP_DUMP
RUN mkdir -p $TMP_DUMP

# install ocr lib
RUN yum -y install tesseract

# installing for spark/pyspark
RUN yum -y install java-11-openjdk java-11-openjdk-devel

# copy over utils and tools
COPY assets/scripts/ /opt/scripts/
RUN chmod +x /opt/scripts/*.sh

RUN pip3.10 install -r /opt/scripts/requirements.txt

# tmp mounting dags from host.
# copy general dags files
#COPY assets/dags/ /opt/airflow/dags

# copy general dags files
COPY assets/mods/ /opt/tmp/artifacts

WORKDIR /opt/scripts
CMD /opt/scripts/entrypoint.sh
