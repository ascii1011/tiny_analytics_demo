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
- 
- convert docker to docker-compose for airflow+posgresql only so we can use the next level executor
  - local distributed vs cloud ... hmm... version is a bigger turn around cycle and heavy for local testing at this point
- adding resources... possibly (ldap, mongo, hdfs, hive(pig), juypter)

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


All this stuff is being manually created at the moment with some templating, but boatloads of automation, access, abstraction, and resources still needs to be created and stitched together. 
