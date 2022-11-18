# tiny_analytics_demo

Author: Christopher Harty / Date: Oct 2022

!!! UNDER CONSTRUCTION !!!

## Warning (do not run this unless you know what your doing)
* This repository is meant to be a demo to show talent only and not meant for production use.
* This project will grow rapidly and so will resource requirements.
* Running this project may cause unwanted results if resources are not carefully considered.
* I make no guarantees and am not claiming this will work for anyone else.  Use at your own risk.

## Purpose of this repo
To showcase a good portion of my abilities by working through a project at all levels, (from basic local to cloud distributed).
So, it will be a project within a project.  Cadence may vary :)  

## Basic plan of attack
Continuously gather requirements, build, test, deploy... all while documenting the goal (moving target), roles, process/methods, etc.

Containers currently run locally on the following ports:
 - airflow @ http://localhost:8080/


## Stand it up
This will change over time.  
 - current: 
    - stand-a-lone docker for airflow POC
    - basic pass through args/envs, applying basic customizations, and POC workflow concept
 - next phase
    - airflow + postgres within docker compose
    - add bigger workflow (TDB)

### centos base image
`
$ project_root
$ cd builds/airflow/local/centos8_base
$ ./rebuild_image.sh
`

### airflow base image (extends centos base)
`
$ project_root
$ cd builds/airflow/local/cent_airflow_base
$ ./rebuild_image.sh
`

### airflow custom image/container (extends airflow base)
`
$ project_root
$ cd builds/airflow/local/cent_airflow_cont
$ ./rebuild_image.sh
$ ./run_container.sh
`

- Check out the docs for more information


