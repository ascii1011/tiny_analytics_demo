
curl -X POST -d '{"execution_date": "2021-10-09T20:00:00Z","conf": {}}' \
    'http://localhost:8080/api/v1/dags/example_02_custom/dagRuns' \
    -H 'content-type: application/json' \
    --user "admin:airflow"
