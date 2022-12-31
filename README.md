# tiny_analytics_demo

Author: Christopher Harty / Date: Oct 2022

!!! UNDER CONSTRUCTION !!!

## Warning (do not run this unless you know what your doing)
* This repository is meant to be a demo to show talent only and not meant for production use.
* This project will grow rapidly and so will resource requirements.
* Running this project may cause unwanted results if resources are not carefully considered.
* I make no guarantees and am not claiming this will work for anyone else.  Use at your own risk.
* DON'T FORGET TO CREATE THE HOST SIDE MOUNTS :)

## Purpose of this repo
To showcase a good portion of my abilities by working through a project at all levels, (from basic local to cloud distributed).
So, it will be a project within a project.  Cadence may vary :)  

## Basic plan of attack
Continuously gather requirements, build, test, deploy... all while documenting the goal (moving target), roles, process/methods, etc.

Major milestones regarding apache airflow infra:
  1) standalone
  2) min local multi-task (with bells) [currently here]
  3) full local multi-task (just has everything scaled out locally; rough on resources and build/deploy)
  4) kubernetes full local
  5) cloud based CICD for infra, container, and dev

## current and future plots/plans
### current evolving phases
This will change over time.  
 - [done] phase 1: 
    - stand-a-lone docker for airflow POC
    - basic pass through args/envs, applying basic customizations, and POC workflow concept
 - [done-mostly] phase 2
    - airflow + postgres within docker compose ("local/min_custom")
    - add bigger workflow (have a client-side, platform-size, and shared libs / mnts)
      - [pending] finish platform-side etl dag
      - [pending] extra: nice to have: client-side generating data files manifest... 
          create manifest with file count, line count, etc... to validate against on platform-side etl dag
 - [inprogress]phase 3.* (I am thinking diverse workflows)
    - [done]3.a: create DNA case
      - simple dna workflow (found caltech course 01 regarding 'Mabuya atlantica' dna samples and simple analysis)
         - discovered 4 samples of dna, found score through tutorial code.
            - thinking of using combinations to find how scores might find migration patterns and leverage dijkstra or A* to find best guess weighted relationships
            - thought briefly about using graphql, but a bit overkill for now.  will stick to local scripts for now.
- [done] ML       # added simple ML-based langauge detection and ocr dags
- [done] Dijkstra # added to the end of dna analysis dag as a base for back tracing human lineage
- [done] Qiskit   # added really basic api usage within a dag

### planning to build
- spark + scala
- fastapi API as a proxy for admin, client, and downstream workflow features, etc...
### really nice to haves
- openai, openml, protobuf, pubsub, dijkstra, q, openrgb
- translate files/strings into different encoded output
- spark (additional 3 containers)
   - dags: split and process work
   - streaming workflows - similar to databricks
   - jupyter
### lofty or on-the-fence stuff
- graph db - relationships
- hdfs/hive (min 5 containers)
- kubernetes + etcd and deploy everything as resilient (need more power!!)
- crypto/blockchain triggering tasks
- leadgen platform
- stock/crypto trading
- anaconda3

## Stand it up local custom airflow 2.4.2

* Local Prerequisites:
 - local volumes and mounts
 - ~/.env (for overriding env vars and creds)
   - openai credentials


>>> Step 1 - Create the images
 - centos base image
`
 // from project root
$ cd builds/airflow/local/centos8_base
$ ./rebuild_image.sh (builds image: cent8py310_base)
`

 - airflow base image (extends centos base)
`
 // from project root
$ cd builds/airflow/local/cent_airflow_base
$ ./rebuild_image.sh (builds image: c8py3_airflow24_base)
`

>>> Step 2 - Pick a deploy option

### [option 1] "custom standalone" (Dockerfile - 1 container)
 -- airflow[8080] + sqlite + some customizations (minimal) (airflow custom image/container - extends airflow base)
`
 // from project root
$ cd builds/airflow/local/cent_airflow_cont
$ ./rebuild_image.sh (builds image: img_airflow24)
$ ./run_container.sh (deploys container: con_airflow24, port: 8080, db: sqlite, SequentialExecutor)
`
UI: `http://localhost:8080/`

### [option 2] "min_custom" (docker-compose - 4 containers)
 -- airflow+pgsql+mongodb+mongo express+custom dev
 `
 // from project root
 cd builds/airflow/local/docker_compose/min_custom
 docker-compose -d up
 `
Airflow         UI: http://localhost:8251/
MongoDB       URL: mongodb://mgadmin:mgpass@mongo:27017/
Mongo-express  UI: http://localhost:8081



* Check out the docs for more information


