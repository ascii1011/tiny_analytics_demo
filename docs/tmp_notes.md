tmp_notes.md

# possible future stuff

AIRFLOW_PKG_EXEC="/usr/local/bin/airflow"

    environment:
      AIRFLOW__CORE__EXECUTOR: LocalExecutor
      AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
      # For backward compatibility, with Airflow <2.3
      AIRFLOW__CORE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
      AIRFLOW__CORE__FERNET_KEY: ''
      AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION: 'true'
      AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
      AIRFLOW__API__AUTH_BACKENDS: 'airflow.api.auth.backend.basic_auth'


 - airflow @ http://localhost:8080/
 - jenkins @ http://localhost:8100/ (instructions under docs/)
 - spark @ http://localhost:8081/home (yet to be applied)

 move these to:

 ## management/power user 8200 - 8299
 jenkins    8201
 airflow    8251 - 8270 (~20)

 # base infra
 kubernetes
   hdfs
   ldap
   etcd

 # data stores 8400 - 8499
 postgres   8401
 mongo      8411
 mysql      8421
 hadoop     8431
 hive       8441
 hbase      8451
 ES         8461
 surrealdb  8471
 graphql    8475
 redis      8480

 ## infra (processing) 8500 - 8700
 spark      8501 - 8550 (35+)
 kafka      8551 - 8570
 queue


bootcamp

cover letter

## project overview
The project will consist of a small analytics platform.
The base finished product will have Airflow kicking off ETL jobs to itself.
I will assume the historical engagement, onboarding, and confirmation of transfer methods, 
data types, and data has alrady been confirmed.

The basic tech stack will compose of at least Apache Airflow, Python, Bash & AWS services.
I will aspire to expand it so that tenant level DAGs will run workflows with simple analytics.


## My approach
Even as I write this I am thinking about how to not only approach this, but how to explain my process
while professionally delivering an exhibit.

See I don't just think with a linear mind... 
I think about how to make this appear efficient while limiting the amount of work I need to do.

how to effectively break this a part as a manager into different sections and sprints, while
my platform experience tells me focus on building a fl

As with interview situations this project is under a time constraint as it may determine how quickly I get a new job.


My approach is simple.  Figure out what is to be build and what audience and purpose it will serve.
When engaging in projects it is important understand what is expected.
My approrach to this project depends on context and requirements can 
play a big part when realizing expectations.

The context for this project could be the following:
 - Who is the customer?
    me.  
 - what do I want, at a high level?  
    I want a demo showcasing some of my skills, but I do not want a huge monthly cost.
    I will want an option to add more robust features while keeping cost low as well.
 - target audiences: 
    could be Recruiters, engineers, and even CTOs


### requirements
 - Use open source and off the shelf solutions unless I am unable to
 - Possibly use clickup.com as the project management.
 - Possibly use Jenkins as CICD tool.
 - Use Airflow on a single AWS intance
 
### specifications
 - Create Airflow locally and test
 - Duplicate on AWS with RDS
 - create deployment of airflow for AWS

======================================================================

My approach here is different from real-world sitautions.

Requirements and expectations can be vastly different as expression of thoughts differ 
from actual available techical solutions.

In real client-facing project scenarios can vary wildly in the process and ideally would 
be over the course of 3 or more meetings with stakeholders.  Initial meetings involve a meet and greet
allowing everyone to establish high level (or more) understanding of the expectations and how to communicate.

This may result in an estimate being provided that the client agrees they are in line with.

Additional meetings are likely to be intensely more technical to get well defined specifications.

Which lead into logistics of bringing those specifications to a successful project efficacy stage.  
Logistics of how the projects success is measured can get further broken down into budgetting, 
division of labor, and project processes (Scrum, Waterfall, etc...)

Caveats:
Depending on the scope of projects I might have a learning curve when it comes to either project 
management or the processing space (ML, AI, neural networks, or Analytics)

With appropriate resources and time a project manager would be able to start to 
 - Set goals milestones
 - build out basic timelines with various staggered sprints within them as per the different roles/milestones
 - 



ocr stuff:

 - what I used in some dags: https://builtin.com/data-science/python-ocr 

 - For big picture pipeline overview, think this is a good start
   - url: https://link.springer.com/article/10.1007/s10032-020-00359-9


