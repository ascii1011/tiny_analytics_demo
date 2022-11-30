#!/usr/local/bin/python3.10

from pprint import pprint
from pymongo import MongoClient


platform_side_db_name = 'platform'
platform_side_collection = 'clients'

client_side_db_name = 'client_projects'
client_side_collection = 'gen_project_files'

__all__ = ["db_dig", "onboard_db", "client_get_file_criteria", "platform_get_project_meta"]

# IMPORTANT NOTE: the 'mongo' within '@mongo:27017' is a container name reference from within the airflow container
client = MongoClient('mongodb://mgadmin:mgpass@mongo:27017/?authSource=admin', directConnection=True)

def platform_get_project_meta(_client, _project):
    _db = platform_side_db_name
    _collection = platform_side_collection
    print(f"\ndb_dig(client: {_client})")
    print(f"#db:{_db}, coll:{_collection}")
    meta = {}
    try:
        with client:

            db = client[_db]
            #print('\tcollecting...')
                       
            docs = db[_collection].find({"name": _client}, {"project_meta": {_project:1},"_id": False})
            #print(f"docs: {docs}")
            doc = docs.next()
            
            meta = dict(doc["project_meta"][_project])
            #print(f"meta: {meta}")
            
    except Exception as e:
        print(f"error: {e}")
    finally:
        return meta

def client_get_file_criteria(_client):
    """
    
    return: dict
    """

    _db = client_side_db_name
    _collection = client_side_collection
    print(f"\ndb_dig(client: {_client})")
    print(f"#db:{_db}, coll:{_collection}")
    fc = {}
    try:
        with client:

            db = client[_db]
            print('\tcollecting...')
            docs = db[_collection].find_one({"client_id": _client}, {"file_criteria":1,"_id": False})
            fc = dict(docs["file_criteria"])
            
    except Exception as e:
        print(f"error: {e}")
    finally:
        return fc


def db_dig(_db, _collection, _limit=5):
    print(f"\ndb_dig(db:{_db}, coll:{_collection}, limit:{_limit})")
    
    with client:

        db = client[_db]
        print('\tcollecting...')
        docs = db[_collection].find().limit(_limit)

        print('\tdocs:')
        for doc in docs:
            print("\t- {}".format(doc))

    print('\n === dig complete ===\n')

    
def onboard_database(_dbname, _collection, doc):
    """
    doc::dict: (ex: {"name":"ma name swaz"})
    """
    
    try:
        print('\ncreate db')
        db = client[_dbname]

        print('\ncreate collection')
        client_col = db[_collection]

        print('\ninserting doc')
        x = client_col.insert_one(doc)
        print(f"\tinserted_id: {x.inserted_id}")

        collist = db.list_collection_names()
        if _collection in collist:
            print(f"collection '{_collection}' exists :)")
        else:
            print(f"'{_collection}' collection was not found :(")

    except Exception as e:
        print(f"error: {e}")
        return False

    dblist = client.list_database_names()
    if _dbname in dblist:
        print(f"the database {_dbname} exists :)")
    else:
        print(f"db {_dbname} was not found :(")

    return True
    


if __name__ == "__main__":
    pass