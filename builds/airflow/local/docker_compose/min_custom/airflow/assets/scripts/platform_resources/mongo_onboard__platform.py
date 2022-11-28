#!/usr/local/bin/python3.10

"""pip install pymongo"""
from pprint import pprint
from pymongo import MongoClient

DBNAME='platform'
#client = MongoClient('mongodb://mgadmin:mgpass@localhost:27017/local?authSource=admin&retryWrites=True', directConnection=True)
#client = MongoClient('mongodb://mgadmin:mgpass@localhost:27017/local?authSource=admin', directConnection=True)
#client = MongoClient('mongodb://mgadmin:mgpass@localhost:27017/local?directConnection=true&serverSelectionTimeoutMS=6000&appName=mongosh+1.6.0')

platform_client = MongoClient('mongodb://mgadmin:mgpass@mongo:27017/?authSource=admin', directConnection=True)

def test():
    client = MongoClient('mongodb://mgadmin:mgpass@mongo:27017/local?authSource=admin', directConnection=True)

    db = client.local
    collection = db.startup_log
    print(f"coll: {list(collection.find())}")

def display_platform(_client):
    
    with _client:
        db = _client.platform
        clients = db.clients.find()

        pprint(list(clients))

    
def create_platform_database(_client):
    """DB will only be created once a collection and data have been inserted!!!"""
    
    try:
        print('\ncreate db')
        platformdb = _client[DBNAME]

        print('\ncreate collection')
        client_col = platformdb["clients"]

        print('\ninsert record')
        # insert into collection
        client_info = {
            "name": "lala", "projects": ['ctc'],
        }
        x = client_col.insert_one(client_info)

        print(f"inserted_id: {x.inserted_id}")

        #check if collection exists
        collist = platformdb.list_collection_names()
        if 'clients' in collist:
            print(f"collection 'clients' exists :)")
        else:
            print(f"'clients' collection was not found :(")

    except Exception as e:
        print(f"error: {e}")

    dblist = _client.list_database_names()
    if DBNAME in dblist:
        print(f"the database {DBNAME} exists :)")
    else:
        print(f"db {DBNAME} was not found :(")

    return platformdb
    
def main():
    #test()
    
    create_platform_database(platform_client)
    display_platform(platform_client)
    #create_client_collections()
    #create_project_collections()

    #onboard_client(name='lala')
    #onboard_client_project(name='lala', project='ctc')


if __name__ == "__main__":
    main()