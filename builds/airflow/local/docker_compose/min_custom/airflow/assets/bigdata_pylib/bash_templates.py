
__all__ = ['extract_bash_cmd_tmpl', 'load_bash_cmd_tmpl', 'compress_bash_cmd_tmpl']

tmpl = """
echo "[ENV] $INGESTION_ROOT: '${INGESTION_ROOT}'"
echo "[param] client_id: '{{ params.client_id }}'"
echo "[xcom] workflow: '{{ ti.xcom_pull(task_ids=\'context\', key=\'workflow\') }}'"
"""

compress_bash_cmd_tmpl="""
#tar -zcvf airflow_extensions.tar.gz extensions/
TARGET_FILENAME="{{ params.client_id }}_{{ params.project_id }}_{{ params.batch_id }}.tar.gz"

SRC_PATH={{ ti.xcom_pull(task_ids=['create_batch_folder']) }}

echo "tar -zcvf ${TARGET_FILENAME} ${SRC_PATH}"
tar -zcvf $SRC_PATH/$TARGET_FILENAME.tar.gz $SRC_PATH/
ls -alht $SRC_PATH/
"""

extract_bash_cmd_tmpl="""
FILE="{{ params.client_id }}_{{ params.project_id }}_{{ params.batch_id }}.tar.gz"
echo "file: ${FILE}"

INGEST="${INGESTION_ROOT}/{{ params.client_id }}/{{ params.project_id }}/{{ params.batch_id }}"
echo "ingest: ${INGEST}"

INGEST_FILE_PATH="${INGEST}/${FILE}"
echo "INGEST_FILE_PATH: ${INGEST_FILE_PATH}"

STAGING="${STAGING_ROOT}/{{ params.client_id }}/{{ params.project_id }}/{{ params.batch_id }}"
echo "staging: ${STAGING}"

DEST_FILE_PATH="${STAGING}/extract"
echo "DEST_FILE_PATH: ${DEST_FILE_PATH}"
"""

extract_bash_cmd_tmpl_test="""
INGEST_ROOT=/opt/mnt/workflows/ingestion/{{ ti.xcom_pull(task_ids=['client_id']) }}/{{ ti.xcom_pull(task_ids=['project_id']) }}/{{ ti.xcom_pull(task_ids=['batch_id'])[0] }}
echo "ingest root: ${INGEST_ROOT}"
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