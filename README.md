# tiny_analytics_demo

Author: Christopher Harty / Date: Oct 2022

## Warning
This repository is meant to be a demo to show talent only and not meant for production use.
Use at your own risk.

## Purpose of this project
Is to showcase a good portion of my abilities by working through a project at all levels.
So, it will be a project within a project.

## My overall approach
Because I will be the client as well as the staff that brings the project to life, I am 
going to try to keep this as simple as possible although the possibilites are endless.

I will kick this all off by stating: We somehow have a client(me) wanting a solution.
I ask myself to describe the concept of the project, as it can give indicators for expectations. 

## client(my) concept 
"A flexible project that provides insights into my management, 
design, archectural, and coding abilities."


After serveral meetings with the client(myself) I gathered additional high-level requirements

## client requirements
 - limitations: 
    - limited budget
    - limit time - a few weeks
 - basic solution expectations:
    - a small analytics platform based in AWS
        - Should be able to test ETL jobs.
        - ignore historical element for now
 - target audience: Recruiters, engineers, and even CTOs

 
## specifications
 - Cloud platform: Amazon AWS
 - ETL Scheduler: Apache Airflow + DB AWS image
 - file process/location TBD (local/S3/other)
 - Staging image for translation and processing of workflows
 - Route 53
 - Security: As needed defined access per AWS instance 

## Roles
A translation of the specifications could be broken down to the following roles:

### Technical project manager 
 - Use open source and off the shelf solutions unless unable to
 - Possibly use clickup.com as the project management.
 - Possibly use Jenkins as CICD tool.

### Platform Engineer duties
 - AWS environment
 - Database
 - cicd process
 - may including Bash and Docker syntax

### Data Engineer duties
 - create build/deployment of airflow AWS
 - create ETL workflows orchestration
 - may include Python, Bash, and docker syntax

### Software Engineer duties
 - customize libraries, extensions, and access for workflows, security, and access
 - may include Python, Rust, Bash, html, jinja, javascript, & CSS