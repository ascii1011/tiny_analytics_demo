from pymongo import MongoClient

def connect_to_database(uri):
    # Connect to the database
    client = MongoClient(uri)
    return client

def create_collection(client, db_name, coll_name):
    # Get a reference to the database
    db = client[db_name]

    # Create the collection
    coll = db[coll_name]
    return coll

def insert_data(coll, data):
    # Insert the data into the collection
    coll.insert_one(data)

def close_connection(client):
    # Close the connection
    client.close()
