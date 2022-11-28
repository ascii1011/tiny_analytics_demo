#!/usr/local/bin/python3.10

from mongodb_lib import db_dig, onboard_database

doc = {"name": "lala", "projects": ["ctc2"]}
onboard_database('platform2', 'customers', doc)
db_dig('platform2', 'customers')
