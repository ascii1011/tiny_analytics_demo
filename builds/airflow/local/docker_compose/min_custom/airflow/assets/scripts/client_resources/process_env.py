#!/usr/local/bin/python3.10

__ENV__ = "dev"
__MODULE__ = "process_env.py"

"""
Purpose: To persist environment variables within a specific account
Note: This module is specific to development purposes.

WARNING: Production stateless machines should not need persisted environment variables as it is a security risk.
"""

import sys
from env_vars import envs

def process(_envs, src_file):
    #print("\nProcessing envs...")
    with open(src_file, 'a+') as f:
        f.write("\n")
        f.write("### adding client envs ###\n")
        for k, v in _envs.items():
            f.write("export {}={}\n".format(k, v))

def read_source_file(src_file):
    print("\nReading file...")
    with open(src_file, 'r') as f:
        print(f'#{src_file}')
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        for _line in f.readlines():
            print("> {}".format(_line.strip()))
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

def main():
    src_file = sys.argv[1]
    print(f'\n\nProcessing Environmental Variables to {src_file}')

    #read_source_file(src_file)
    process(envs, src_file)
    read_source_file(src_file)

if __name__ == "__main__":
    main()