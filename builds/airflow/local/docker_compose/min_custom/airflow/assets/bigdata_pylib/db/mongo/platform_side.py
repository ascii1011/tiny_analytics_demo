#!/usr/local/bin/python3.10


platform_tenant_conf = {
    "tenant_project_settings": {
        "desc": "bad initial labeling here... meant to hold dynamic batch criteria to generate random data",
        "db_name": "platform",
        "collection": "clients",
        }
}

__all__ = ["PlatformTenants"]


class PlatformTenants:

    conf = platform_tenant_conf

    def __init__(self, client_mongo, debug=False):
        self.client_mongo = client_mongo
        self.debug = debug

        if self.debug:
            print("\n### PlatformTenants ###")
            print(f"debug: {self.debug}")
            print(f"MongoClient: {self.client_mongo}")

    def get_project_meta(self, tenant, project, collection_target):

        if self.debug: 
            print(f"::get_project_meta(tenant:{tenant}, project:{project}, col_target:{collection_target}):")

        _db = self.conf[collection_target]["db_name"]
        _collection = self.conf[collection_target]["collection"]

        if self.debug: 
            print(f"#db:{_db}, coll:{_collection}")

        meta = {}
        try:
            #print('# attempting client_mongo...')
            with self.client_mongo:

                #print('#\t within...')
                db = self.client_mongo[_db]
                #print('\tcollecting...')
                        
                docs = db[_collection].find({"name": tenant}, {"project_meta": {project:1},"_id": False})
                #print(f"docs: {docs}... next()")
                doc = docs.next()
                
                meta = dict(doc["project_meta"][project])
                #print(f"meta: {meta}")
                
        except Exception as e:
            print(f"error: {e}")
        finally:
            return meta


if __name__ == "__main__":
    pass