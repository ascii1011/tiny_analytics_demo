
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

export INGESTION_ROOT=/opt/mnt/workflows/ingest/
export INGESTION_TMPL=/opt/mnt/workflows/ingest/{client_id}/{project_id}/{batch_id}

export STAGING_ROOT=/opt/mnt/workflows/staging/
export STAGING_TMPL=/opt/mnt/workflows/staging/{client_id}/{project_id}/{batch_id}

export CLIENT_BATCH_ROOT=/opt/mnt/client_side/batch_jobs/
export CLIENT_BATCH_TMPL=/opt/mnt/client_side/batch_jobs/{batch_id}

export BIGDATA_PYLIB=/opt/mnt/bigdata/pylib

export PYTHONPATH=$PYTHONPATH:/opt/airflow:/opt/mnt/bigdata/pylib

