
"""
a local module to dist load between N number of tasks
"""

__all__ = ["persist_to_raw", "persist_raw_to_bronze"]

def persist_to_raw(**context):
    """
    - cycle through all files
      - normalize values
        - save to collection 'platform__ingest__{client_id}_{project_id}_raw
    """
    pass

def persist_raw_to_bronze():
    #"normalize, transform, filter, validate"
    # could be stored procedures, py, sh, rs, etc...
    pass

def process(func):
    """
    - get db record count
    - divide amoung available branch tasks
      - save raw db collection
    """
    pass