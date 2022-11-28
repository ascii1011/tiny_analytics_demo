#!/usr/local/bin/python3.10

from pprint import pprint
from pymongo import MongoClient

__all__ = ["db_dig", "onboard_db"]

client = MongoClient('mongodb://mgadmin:mgpass@mongo:27017/?authSource=admin', directConnection=True)

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