
import os

import string
import random
from time import sleep

from pprint import pprint

from workflow_lib import gen_batch_id, display_dir_content

__all__ = ['generate_files',]

BASE_TEST_DIR = '/opt/mnt/raw_data/test'
GENERATED_DIR = os.path.join(BASE_TEST_DIR, 'generated')

max_retries = 3

def generate_files(file_count=2, row_count=3, cols=[], row_delim=',', file_ext='txt', path=GENERATED_DIR, context={}, debug=False):
    # statically set for now, will build out later
    # random file_count and row_count will be modified later
    # manifest options
    # precalulations for validation downstream
    if debug: print(f'\n##### generate_files ({debug=}) #####')

    batch_id = gen_batch_id(4)

    # build filename + path template
    target_path = path
    filename_tmpl = f"generated_{batch_id}" + '_{file_num}.' + file_ext
    
    if context != {} and 'client' in context and 'project' in context:
        target_path = os.path.join(path, 'client', context["client"], context["project"], batch_id)
        filename_tmpl = f'{context["client"]}_{context["project"]}_{batch_id}' + '_{file_num}.' + file_ext

    if debug:
        print(f"\n#{target_path=}\n#{filename_tmpl=}\n\n")
    
    if not os.path.exists(target_path):
        print('path does not exist...')

        os.makedirs(target_path)

        if not os.path.exists(target_path):
            print(f'Error, folder {target_path} does not exist.  Exiting...')
            return False

        else:
            print('now it exists!!!!!')
    
    ### simple assumption of how cols might be defined for automating the generating of column values
    # will use this for now
    #cols[0] = {"col_name": "rand_chars", "pattern": "random", "type": "ascii_lowercase", "len": 6}
    headers = [c["col_name"] for c in cols]
    report = {
        "files": [],
        "file_count": file_count,
        "total_line_count": 0,
        "path": target_path,
    }

    for file_num in range(file_count):
        filename = filename_tmpl.format(file_num=file_num)
        full_file_path = os.path.join(target_path, filename)
        if debug: print(f"working on file '{full_file_path}'...")

        with open(full_file_path, "w+") as f:

            report["files"].append(filename)
            report["total_line_count"] += row_count

            for i in range(row_count):
                if debug: print(f"{i}) {cols=}")
                elem_values = []
                for col in cols:
                    if debug: print(f"\t{col=}")

                    value = '1'
                    if col["pattern"] == "random":
                        if col["type"] == "ascii_lowercase":
                            if debug: print('ascii_lower')
                            value = ''.join(random.choices(string.ascii_lowercase, k=col["len"]))
                        elif col["type"] == "int":
                            if debug: print('int')
                            value = random.randint(1,col["len"])
                        else:
                            if debug: print('else...')
                            value = random.randint(5,9)

                    if debug: print(f"\t{value=}")

                    elem_values.append(str(value))
                
                values = row_delim.join(elem_values)
                if debug: print(f"{i}) line: {values}")

                line = "{}\n".format(values)
                f.write(line)

    display_dir_content(target_path)

    return report
        
def gen_files():
    """
    one off case for generating data files with strings
    """
    print("\n==================== generating files ====================")
    enable_combinations = False

    file_count = 2
    lines_per_file = 100000
    string_len = 12
    s1 = []
    s2 = []

    for file_id in range(1,file_count+1):

        file_path = os.path.join('/opt', f"generated_strings_{file_id}.txt")
        with open(file_path, "w+") as f:
            #print(f"\nstrings_{file_id}.txt")
            
            for l in range(lines_per_file):
                #_str = random.randint(1,3)
                _str = ''.join(random.choices(string.ascii_lowercase, k=string_len))
                if file_id == 1:
                    #print(f"adding {_str} to s1")
                    s1.append(_str)
                else:
                    #print(f"adding {_str} to s2")
                    s2.append(_str)
                #print(f"\t> {_str}")
                f.write("{}\n".format(_str))

    #print(f"s1: {s1[:20]}")
    #print(f"==> {sorted(s1)}")
    #print(f"s2: {s2[:20]}")
    #print(f"==> {sorted(s2)}")


    def get_unique(s1, s2):
        ss1 = set(s1)
        ss2 = set(s2)
        set_out = ss1.intersection(ss2)
        del(ss1)
        del(ss2)

        set_len = len(set_out)
        print(f"Unique: {set_len}")
        return set_len

    def get_combinations(s1, s2, enabled=False):
        if enabled == False:
            return

        print("\ndiscovering combos:")
        combos = {}
        for s in s1:
            #print(f"\ts: {s}")
            if s not in combos:
                combos[s] = {"in":0, "out": 0}
            combos[s]["in"] += 1
            for ts in s2:
                #print(f"\t\ts: {ts}")
                if s == ts:
                    #print(f"\t\t\t{s}==={ts}")
                    combos[s]["out"] += 1

        """
        possible_combos = {k:v["out"] for k,v in combos.items()}
        c_total = 0
        for _k,_v in possible_combos.items():
            if _v > 0:
                #print(f"{_k}:{_v} ({combos[_k]})")
                c_total += _v

        print(f"total combos: {c_total}\n\n")
        """
        c_total = 0
        for k,v in combos.items():
            c_total += v["out"]

        print(f"Combinations: {c_total} ")

    get_combinations(s1, s2, enable_combinations)
    return get_unique(s1, s2)
    


def test__gen_files():
    for i in range(max_retries):
        if gen_files() > 0:
            break
        sleep(1)

def test__generate_files(debug=False):
    path = '~/dev/mnt_data/tiny_analytics_platform/raw_data/test/generated'
    path = "/opt/mnt/raw_data/test/generated"

    args = {
        "context": {"client": "moomoo", "project": "ube"},
        "file_count": 3,
        "row_count": 4,
        "cols": [
            {"col_name": "rand_chars", "pattern": "random", "type": "ascii_lowercase", "len": 3},
        ],
        "path": path,
        "debug": debug,
    }
    
    report = generate_files(**args)
    print('\nreport:')
    pprint(report)


def main():
    debug = True
    
    test__generate_files(debug)
    #test__gen_files(debug)

if __name__ == "__main__":
    main()
                        
