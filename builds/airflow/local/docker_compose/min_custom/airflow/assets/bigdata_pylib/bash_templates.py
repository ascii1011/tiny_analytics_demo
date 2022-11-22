
__all__ = ['extract_bash_cmd_tmpl', 'load_bash_cmd_tmpl']

extract_bash_cmd_tmpl="""
echo ""
echo "===========>>"
INGEST_ROOT=/opt/mnt/workflows/ingestion/{{ params.client_id }}/{{ params.project_id }}/{{ ti.xcom_pull(task_ids=['batch_id'])[0] }} 
echo "ingest root: ${INGEST_ROOT}"
echo "(this folder and content should already exist)"
echo ""
STAGING_ROOT=/opt/mnt/workflows/staging/{{ params.client_id }}/{{ params.project_id }}/{{ ti.xcom_pull(task_ids=['batch_id'])[0] }}
echo "staging root: ${STAGING_ROOT}"
echo "(need to create this folder)"
echo ""
echo "mkdir ${STAGING_ROOT}"
echo ""
echo "cp ${INGEST_ROOT}/client_upload.tar.gz ${STAGING_ROOT}"
echo "ls -alht ${STAGING_ROOT}"
echo ""
echo "tar -xzvf ${STAGING_ROOT}/client_upload.tar.gz -C ${STAGING_ROOT}/extract"
echo "ls -alht ${STAGING_ROOT}/extract"
echo "<<=========="
echo ""
"""

load_bash_cmd_tmpl="""
echo ""
echo " LOAD ===========>>"
STAGING_ROOT=/opt/mnt/workflows/staging/{{ params.client_id }}/{{ params.project_id }}/{{ ti.xcom_pull(task_ids=['batch_id'])[0] }} 
echo "ingest root: ${STAGING_ROOT}"
echo ""
FINAL_ROOT=/opt/mnt/workflows/final/{{ params.client_id }}/{{ params.project_id }}/{{ ti.xcom_pull(task_ids=['batch_id'])[0] }}
echo "staging root: ${FINAL_ROOT}"
echo "(need to create this folder)"
echo ""
echo "mkdir ${FINAL_ROOT}"
echo ""
echo "cp ${STAGING_ROOT}/*.* ${FINAL_ROOT}"
echo "ls -alht ${FINAL_ROOT}"
echo "<<========== LOAD"
"""

if __name__ == "__main__":
    pass