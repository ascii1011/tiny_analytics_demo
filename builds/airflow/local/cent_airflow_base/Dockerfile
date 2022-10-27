FROM cent8py310_base

LABEL name="airflow" \
      build-date="2022-10-01"

ARG PYTHON_VERSION=3.10
ARG AIRFLOW_VERSION=2.4.2
ARG AIRFLOW_HOME_PATH=/opt/airflow
ARG AIRFLOW_UI_PORT=8080
ARG AIRFLOW_LOGS_PATH=$AIRFLOW_HOME_PATH/logs
ARG AIRFLOW_DAG_PATH=$AIRFLOW_HOME_PATH/dags
ARG AIRFLOW_PKG_EXEC="/usr/local/bin/airflow"
ARG AIRFLOW_PKG_HOME="/usr/local/lib/python$PYTHON_VERSION/site-packages/airflow/"

ENV AIRFLOW_HOME=$AIRFLOW_HOME_PATH \
    AIRFLOW_UI_PORT=$AIRFLOW_UI_PORT \
    AIRFLOW_LOGS_PATH=$AIRFLOW_LOGS_PATH \
    AIRFLOW_DAGS_PATH=$AIRFLOW_DAGS_PATH \
    AIRFLOW_PKG_EXEC=$AIRFLOW_PKG_EXEC \
    AIRFLOW_PKG_HOME=$AIRFLOW_PKG_HOME \
    AIRLFOW_GPL_UNIDECODE=yes \
    SLUGIFY_USES_TEXT_UNIDECODE=yes \
    PYTHONPATH=$PYTHONPATH:$AIRFLOW_HOME_PATH

RUN mkdir -p $AIRFLOW_LOGS_PATH \
    mkdir -p $AIRFLOW_DAGS_PATH

RUN echo "Installing utils and dev tools." \
    && yum -y install git wget curl bzip2 unzip ca-certificates openssh-server \
    && yum -y install emacs vim nano screen multitail tree \
    && yum -y clean all

RUN pip3.10 install "apache-airflow[celery]==$AIRFLOW_VERSION" \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-$AIRFLOW_VERSION/constraints-$PYTHON_VERSION.txt"

