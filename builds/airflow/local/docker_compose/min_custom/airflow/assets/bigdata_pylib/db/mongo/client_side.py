#!/usr/local/bin/python3.10

project_conf = {
    "gen_project_batch": {
        "desc": "bad initial labeling here... meant to hold dynamic batch criteria to generate random data",
        "db_name": "client_projects",
        "collection": "gen_project_files",
        }
}

__all__ = ["TenantProject"]


class TenantProject:

    project_conf = project_conf

    def __init__(self, client_mongo, debug=False):
        self.client_mongo = client_mongo
        self.debug = debug

        if self.debug:
            print("\n### TenantProject ###")
            print(f"debug: {self.debug}")
            print(f"MongoClient: {self.client_mongo}")


    def get_file_criteria(self, tenant, collection_target):
        """
        
        return: dict
        """
        if self.debug: 
            print(f"::get_file_criteria(tenant:{tenant}, col_target:{collection_target}):")
        fc = {}

        _db = self.project_conf[collection_target]["db_name"]
        _collection = self.project_conf[collection_target]["collection"]
        if self.debug:
            print(f"# db:{_db}, coll:{_collection}")
        
        try:
            #print('# attempting client_mongo...')
            with self.client_mongo:

                #print('#\t within...')
                db = self.client_mongo[_db]
                #print('\tcollecting...')
                docs = db[_collection].find_one({"client_id": tenant}, {"file_criteria":1,"_id": False})
                fc = dict(docs["file_criteria"])
                
        except Exception as e:
            print(f"error: {e}")
        finally:
            return fc

if __name__ == "__main__":
    pass