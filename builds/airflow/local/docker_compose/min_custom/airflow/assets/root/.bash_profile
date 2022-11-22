
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin

export PATH

export AIRFLOW_HOME=/opt/airflow
export AIRFLOW_UI_PORT=8080
export AIRFLOW_LOGS_PATH=/opt/airflow/logs
export AIRFLOW_DAGS_PATH=/opt/airflow/dags
export AIRFLOW_PKG_EXEC=/usr/local/bin/airflow
export AIRFLOW_PKG_HOME=/usr/local/lib/python3.10/site-packages/airflow/
export AIRLFOW_GPL_UNIDECODE=yes
export SLUGIFY_USES_TEXT_UNIDECODE=yes

export AIRFLOW__WEBSERVER__EXPOSE_CONFIG=False
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
# For backward compatibility, with Airflow <2.3
export AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
export AIRFLOW__CORE__EXECUTOR=LocalExecutor
export AIRFLOW__CORE__FERNET_KEY=''
export AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=True
export AIRFLOW__CORE__LOAD_EXAMPLES=False
export AIRFLOW__API__ENABLE_EXPERIMENTAL_API=True
export AIRFLOW__API__AUTH_BACKENDS=airflow.api.auth.backend.basic_auth

export PYTHONPATH=$PYTHONPATH:/opt/airflow

