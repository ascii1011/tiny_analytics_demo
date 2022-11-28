#!/usr/local/bin/python3.10

from mongodb_lib import db_dig, onboard_database

db_name = 'client_projects'
collection = 'gen_project_files'

#add_initial_project
doc = {
    "client_id": "lala",
    "project_id": "ctc",
    "file_criteria": {
        "files": (5,10),
        "entries": (20,30),
        "values": (100,50000),
    },
}   

onboard_database(db_name, collection, doc)
db_dig(db_name, collection)
