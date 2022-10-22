# tiny_analytics_demo

Author: Christopher Harty

The contents of this repository are meant to display talent and not meant for production use.
Use at your own risk.

## project overview

The project will consist of a small analytics platform.
The base finished product will have Airflow kicking off ETL jobs to itself.

The basic tech stack will compose of at least Apache Airflow, Python, Bash & AWS services (like RDS).
I am aspiring to expand it so that tenant level DAGs will run workflows with simple analytics.

Security, resiliency, scalability, big data stores, and advanced queries or analytics are beyond the scope of this demo.

### requirements
 - Airflow on AWS
 
### specifications
 - Create Airflow locally and test
 - Duplicate for AWS + RDS
 - create deployment of airflow for AWS