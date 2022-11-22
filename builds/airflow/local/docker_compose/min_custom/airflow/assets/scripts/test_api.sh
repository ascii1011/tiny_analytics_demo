
curl -X POST -d '{"execution_date": "2021-11-10T20:00:01Z","conf": {}}' \
    'http://localhost:8080/api/v1/dags/example_02_custom/dagRuns' \
    -H 'content-type: application/json' \
    --user "admin:airflow"
