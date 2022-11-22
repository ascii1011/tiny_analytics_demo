
envs = {
    "TAG": "tapd",
    "INGESTION_ROOT": "/opt/mnt/workflows/ingest",
    "INGESTION_TMPL": "/opt/mnt/workflows/ingest/{client_id}/{project_id}/{batch_id}",
    "STAGING_ROOT": "/opt/mnt/workflows/staging",
    "STAGING_TMPL": "/opt/mnt/workflows/staging/{client_id}/{project_id}/{batch_id}",
    "BIGDATA_PYLIB": "/opt/mnt/bigdata/pylib",
    "PYTHONPATH": "$PYTHONPATH:$BIGDATA_PYLIB",
}
