
curl -X PATCH 'http://localhost:8080/api/v1/dags/example_02_custom?update_mask=is_paused' \
    -H 'Content-Type: application/json' \
    --user "admin:astrov" \
    -d '{
        "is_paused": true
    }'
