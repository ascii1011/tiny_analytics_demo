
"""

        client_id = 
        project_id = 
        batch_id = ti.xcom_pull(task_id="context", key="batch_id")
        file_criteria = ti.xcom_pull(task_id="context", key="file_criteria")
"""
__all__ = ['extract_bash_cmd_tmpl', 'load_bash_cmd_tmpl', 'compress_bash_cmd_tmpl']

tmpl = """
echo "[ENV] $INGESTION_ROOT: '${INGESTION_ROOT}'"
echo "[param] client_id: '{{ params.client_id }}'"
echo "[xcom] workflow: '{{ ti.xcom_pull(task_ids=\'context\', key=\'workflow\') }}'"
"""

compress_bash_cmd_tmpl="""
#tar -zcvf airflow_extensions.tar.gz extensions/
TARGET_FILENAME={{ ti.xcom_pull(task_ids="context", key="targz_file") }}

SRC_PATH={{ ti.xcom_pull(task_ids='context', key='batch_src_path') }}

cd $SRC_PATH
echo "tar -zcvf ${SRC_PATH}/${TARGET_FILENAME} *.txt"
tar -zcvf $SRC_PATH/$TARGET_FILENAME *.txt
#echo "tar -C ${SRC_PATH} -zcvf ${TARGET_FILENAME} ${SRC_PATH}"
#tar -C $SRC_PATH -zcvf $SRC_PATH/$TARGET_FILENAME $SRC_PATH/
ls -alht $SRC_PATH/

echo $SRC_PATH
"""

extract_bash_cmd_tmpl=""" 
FILE="{{ ti.xcom_pull(task_ids='context', key='targz_filename') }}"
echo "file: ${FILE}"

echo "======"
INGEST="{{ ti.xcom_pull(task_ids='context', key='ingestion_path') }}"
echo "ingest: ${INGEST}"

echo "======"
INGEST_FILE_PATH="${INGEST}/${FILE}"
echo "INGEST_FILE_PATH: ${INGEST_FILE_PATH}"

echo "======"
echo "mkdir ${INGEST}/extract"
mkdir $INGEST/extract

echo "======"
echo "tar -xzvf ${INGEST_FILE_PATH} --strip-components=1 -C ${INGEST}/extract"
tar -xzvf $INGEST_FILE_PATH -C $INGEST/extract

echo "======"
ls -alht $INGEST/extract

echo ""===done===""
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