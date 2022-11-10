# tiny_analytics_demo

Author: Christopher Harty / Date: Oct 2022

## Warning
This repository is meant to be a demo to show talent only and not meant for production use.
Use at your own risk.

## Purpose of this project
To showcase a good portion of my abilities by working through a project at all levels.
So, it will be a project within a project.  

## My overall approach
Because I will be the client as well as the staff that brings the project to life, I am 
going to try to keep this as simple as possible although the possibilites are endless.

I will kick this all off by stating: We somehow have a client(me) wanting a solution.
I ask myself to describe the concept of the project, as it can give indicators for expectations. 


==================== The project ====================

## client(me) concept 
"A flexible project that provides insights into my management, 
design, archectural, and coding abilities."


After serveral meetings with the client(myself) I gathered additional high-level requirements

## client requirements
 - limited budget and time
 - basic solution expectations:
    - a small analytics platform locally hosted for now
        - Should be able to test ETL jobs.
        - Assume knowledge of data and ignore historical element for now (i.e. onboarding client data)
 - target audience: Recruiters, engineers, and even CTOs
 - cloud build possible in future

 
## specifications
 - localhost platform: docker-compose
 - ETL Scheduler: Apache Airflow + postgres image (POC only, not scaled out yet)
 - file process/location TBD (local)
 - Staging scenario only for now



==================== The Team ====================

## Roles
A translation of the specifications could be broken down to the following roles:

### Technical project manager 
 - Use open source and off the shelf solutions while possible
 - Possibly use clickup.com as the project management.
 - Possibly use Jenkins as CICD tool.

### Platform Engineer duties
 - local/AWS environment
 - Database
 - cicd process
 - may including Bash and Docker syntax

### Data Engineer duties
 - create build/deployment of single airflow instance
 - create ETL workflows orchestration
 - may include Python, Bash, and docker syntax

### Software Engineer duties
 - customize libraries, extensions, and access for workflows, security, and access
 - may include Python, Bash, html, jinja, javascript, & CSS




