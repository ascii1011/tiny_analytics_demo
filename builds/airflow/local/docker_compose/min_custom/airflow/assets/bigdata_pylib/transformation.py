




def tranform(db='mongo', task_dest='local', workflow_step='extract'):
    if db == 'mongo':
        if task_dest == 'local':

            if workflow_step == 'extract':

                from local_unordered import persist_to_raw, persist_raw_to_bronze




