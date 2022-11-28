#!/usr/local/bin/python3.10

from mongodb_lib import db_dig, onboard_database

db_name = 'platform'
collection = 'clients'

#add_initial_project
doc = {
    "name": "lala", 
    "org": "LaLA LLC.",
    "dag_owner": "lala",
    "project_meta": {
        "ctc": {
            "file_format": {
                "extension": ".txt",
                "headers": ["id","project","desc","data","date"],
                "header_exists": True,
                "field_types": ["increment", "str-5", "str-20, int-10, dtef"],
            },
            "workflow_action_order": {
                "etl": ["extract"],
            },
            "actions": {
                "extract": {
                    "unzip": True,
                    "tar_file_format": "{client_id}_{project_id}_{batch_id}.tar.gz",
                    "dest": "hdfs",
                },
                "validate": {
                    "field": "project",
                }
            },
        }
    }
}

onboard_database(db_name, collection, doc)
db_dig(db_name, collection)
