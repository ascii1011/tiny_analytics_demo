#!/usr/local/bin/python3.10

""""
https://www.mongodb.com/docs/drivers/java/sync/v4.3/fundamentals/builders/projections/?_ga=2.179217062.348092994.1669646335-33691716.1669646335
https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html?highlight=find#pymongo.collection.Collection.find_one
https://mongoplayground.net/
https://stackoverflow.com/questions/70590047/projection-on-nested-object-mongodb-find-query
"""

from pprint import pprint
from pymongo import MongoClient

from .client_side import TenantProject
from .platform_side import PlatformTenants

DEBUG = False

# IMPORTANT NOTE: the 'mongo' within '@mongo:27017' is a container name reference from within the airflow container
client = MongoClient('mongodb://mgadmin:mgpass@mongo:27017/?authSource=admin', directConnection=True)

__all__ = ["client_get_file_criteria", "platform_get_project_meta"]

def client_get_file_criteria(tenant, debug=None):
    collection_target = 'gen_project_batch'
    if debug == None:
        debug = DEBUG

    Project = TenantProject(client, debug)
    return Project.get_file_criteria(tenant, collection_target)

def platform_get_project_meta(tenant, project, debug=None):
    collection_target = 'tenant_project_settings'
    if debug == None:
        debug = DEBUG

    Platform = PlatformTenants(client, debug)
    return Platform.get_project_meta(tenant, project, collection_target)