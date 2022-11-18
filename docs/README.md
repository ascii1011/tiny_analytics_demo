# Overview


## Project progress
- The progress thus far is still inline with initial intentions.
    - Building a standalone instance with at least one basic ETL DAG has been achieved.
    - The challenges thus far have been how far to plan in the future for changes and how much abstraction.
    - granular implementations:
      - I have chosen not to go the stateless container route so far as it needs supporting resources and I am not there yet.
         - I will eventually be creating another build process for stateless containers.
      - Alternatively, I have built the standalone airflow container to show the following:
        - how central dev resources can be leveraged via mounts
        - how environment variables may be applied, including airflow overrides
        - how to apply custom extensions or mods
      - basic templated bash commands for a client based ETL pattern


## todo
- finish the client-side dag: generates files/zip, sends files, triggers specific target dag
- convert docker to docker-compose for airflow+posgresql only so we can use the next level executor
  - local distributed vs cloud ... hmm... version is a bigger turn around cycle and heavy for local testing at this point
- adding resources... possibly (ldap, mongo, hdfs, hive(pig), juypter)


## Goals
My goal is to eventually have it deployed to AWS EC2 as a resilient piece-meal solution where clients can submit files for consumption(shiny api abstraction, Mr. Liang) and retrieve analytics feedback.
And then promote it to AWS EKS or MWAA...

APIs appear to be the new shiny thing all the kewl kids are using these days, so will this will be




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
 - Data Stores
 - cicd process
 - may including Bash and Docker syntax

### Data Engineer duties
 - create build/deployment of single airflow instance
 - create ETL workflows orchestration
 - may include Python, Bash, and docker syntax

### Software Engineer duties
 - customize libraries, extensions, and access for workflows, security, and access
 - may include Python, Bash, html, jinja, javascript, & CSS




## considerations
For realistic scenarios to be reproduced I do need to provide a reasonable amount of various depths of knowledge, understanding, planning, and implemented.

To repduce such a realistic situation we need to consider the following:
 - the client side of data, which may consider some form of data being sent to the platform
 - the platform will need to have a way of receiving the data from the client and holding it until it can be processed (depends on SLAs)
 - the platform should have a way of then processing the data in an efficient way.  This means that the process should have the lowest resistance possible.
    All linear steps should be quick and direct; all non-linear steps should be able to be broken into many parrallel pieces.
 - the platform should have ways of "transforming" the data.  This could mean things like normalizing, verifying, and validating data
 - the platform will likely use file systems and data stores where data management is needed
    - retention of data at various steps helps to verify, replay, & rebuild results quickly

 - security was paramount regarding my previous experience.  Custom authentication and authorization were applied to various 
    places within a platform.  I will give some examples (keep in mind this is within a secure infrastructure):
    - data transmission: some authorization would need to be create for sending and saving files to a directory
    - triggering dags: after confirmation that data has landed within a specific client area, specific dags would need to be triggered...
       that have access to the landing area, are allowed to trigger their dag and...
       have additional access to create, modifiy, and process data through big data resources (i.e. hdfs, hadoop, hive, spark, juypter, mongo, postgress, etc...)
       and being able to provide those credentials when and where needed...
    - cloud infrastructure: of course this is all run on a cloud service so there needs to be support within the platform account for some authorization process like ldap.
    - airflow (UI only) client and admin access
       - so custom authentication ldap+rbac adapter for UI support
         - extended security rbac (authorization) support for granular access
       - custom authorization (through the adapter) for triggering dags with credentials
       - custom views and all other resources per admin and/or client access
    
How might we:
 - automate onboard client
   - automate onboard project and historical data
   - automate ingestion on regular cycles afterwards
   - what type of processing?

 - build / maintain / migrate in the future...?  appears to be a huge revolving issue as clients ask for increasingly more types of processing

All this stuff is being manually created at the moment with some templating, but boatloads of automation, access, abstraction, and resources still needs to be created and stitched together. 
