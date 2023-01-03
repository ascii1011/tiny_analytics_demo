# minimal localexecutor airflow + postgres

## Content
Build and deploys (different container names and ports):
 - [staging] docker-compose up -d
 - [dev] cd ./airflow
    - ./rebuild.sh && ./run_container.sh

platform resources:
 - big data pylib
 - templated client dag

Airflow resources:
 - custom api
 - Other containers in the same network can use http://airflow:8080/api/v1/{endpoint} to access the API
 - resources outside of the same network will need to use http://localhost:8251/api/v1/{endpoint} to access the API

Client side resources:
 - generate data dag

### Staging version
Meant to imitate distributed workflow behavior with minimal 
    resources for quick cicd
Airflow is connected to postgres and leverages the LocalExecutor 
    in order to spawn off multiple dag_runs at once.
There are volumes for central resources(db, logs, bigdata pylib, 
    dags(for now), etc.), but other assets like customization are 
    copied into the container.