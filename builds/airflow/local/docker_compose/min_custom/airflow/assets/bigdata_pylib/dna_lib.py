

import re
import sys

from pprint import pprint

__all__ = ["transcribe", "translate"]

def transcribe(dna='GAUGCUAGUCGUCGAUGCUGAUGAUCGU'):
	# create a transcription map and use regex to translate
	map = {"A":"U", "T":"A", "C":"G", "G":"C"}
	map = dict((re.escape(k), v) for k, v in map.iteritems())
	pattern = re.compile("|".join(map.keys()))
	DNA = dna.read().strip()
	mRNA = pattern.sub(lambda m: map[re.escape(m.group(0))], DNA)

	return mRNA

def translate(mRNA='MLVVDADD'):
	mRNA = mRNA.read().strip()
	codon_map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

	protein = ''
	# find the start codon and proceed until a 'STOP'
	start = mRNA.find('AUG')
	if start != -1:
		while start+2 < len(mRNA):
			protein += codon_map[mRNA[start:start+3]]
			start += 3
		protein = protein[:protein.find('STOP')]
	return protein



def repeated_dna_sequences(_strand, _freq, _size, log_level=0):
    if log_level > 0: 
        print("\n##### repeated_dna_sequences #####")
    lookup = {}
    all_pairs = []   
    output = []

    for i in range(_freq, _size+1, _freq):
        sub_str = _strand[i-_freq:i+_freq]
        if len(sub_str) != 2*_freq:
            continue

        all_pairs.append(sub_str)
        
        if log_level > 1:
            print(f"{i})_strand[{i}-{_freq}:{i}+5] = sub: {sub_str}")

        if sub_str not in lookup:
            lookup[sub_str] = 0
        lookup[sub_str] += 1

        if lookup[sub_str] > 1 and sub_str not in output:
            output.append(sub_str)

    return output, all_pairs

def get_strand_map(_strand, size, log_level=0):
    if log_level > 0: 
        print("\n##### get_strand_map #####")
    prev_elem = None
    max = 0
    lookup = {
        "A": {},
        "C": {},
        "G": {},
        "T": {},
    }
    order = []
    seq = 0
    for i in range(size):
        if log_level > 1: print(f"\nelem: {i}, {prev_elem}, {_strand[i]}")

        if prev_elem == None:
            if log_level > 1: print('\tfirst')
            # record as first element found
            order.append(_strand[i])

        elif prev_elem != _strand[i]:
            if log_level > 1: 
                print('\tA change has been detected...')
                print("\tlookup[prev_elem][seq]")
                print(f"\tlookup[{prev_elem}][{seq}]: {lookup[prev_elem]} >? max: {max}")
            if lookup[prev_elem][seq] > max:
                if log_level > 1: print(f'\t\tcurr:{lookup[prev_elem][seq]} > max:{max} (updating max)')
                max = lookup[prev_elem][seq]

            # update for new element found
            seq += 1
            # add the newly found element
            order.append(_strand[i])


        if log_level > 1: print(f"\tis '{seq}' in {lookup[_strand[i]]} ?")
        if seq not in lookup[_strand[i]]:
            if log_level > 1: print('\t\tNOT IT IS NOT... creating...')
            lookup[_strand[i]].update({seq: 0})
            if log_level > 1: print(f"\t\tnew dict entry: {lookup[_strand[i]]}")

        lookup[_strand[i]][seq] += 1
        #print(f"\updated seq dict entry: {lookup[_strand[i]]}")

        prev_elem = _strand[i]

        if log_level > 1: 
            print(f'\tsummary: seq={seq}, lookup_seq_total={lookup[_strand[i]][seq]}, max={max}, order={order}')

    def rebuild_pairs(elems, pair_size, lookup):
        pairs = []
        pair = ""
        #print(f'rebuild_pairs:: pair_size: {pair_size}')
        for x, elem in enumerate(elems):
            #print(f"\t-{x}: {elem}")
            
            pair += elem * lookup[elem][x]
            #print(f"\t\t{pair} += {elem} * {lookup[elem][x]}")

            if len(pair) >= pair_size:
                pairs.append(pair)
                pair = ""

        #print(f"pairs: {pairs}")
        return pairs

    cpairs = rebuild_pairs(order, max*2, lookup)

    if log_level > 0: 
        print(f'\n\nSummary: sequences={seq} | freq={max}')
        print(f"order: {order}")
        pprint(lookup)

    return {
        "freq": max,
        "seq": seq,
        "lookup": lookup,
        "order": order,
    }

#def find_repeated_pairs(_strand_map):
#    find_all_pairs = []


def app(strand):
    print("######## APP ########\n")
    #log_level = # 0=None 1=info, 2=debug

    size = len(strand)

    strand_map = get_strand_map(strand, size, log_level=0)

    print('\nstrand_map:')
    pprint(strand_map)

    #resp2 = find_repeated_pairs(strand_map, log_level=2)

    repeats, all_pairs = repeated_dna_sequences(strand, strand_map["freq"], size, log_level=0)

    print(f'\nall_pairs: {all_pairs}')
    print(f'repeats: {repeats}')

    #if log_level > 0: 
    #print(f"restate strand({size}): '{strand}'")

def dev(strand):
    print("######## DEV ########\n\n")

    for i in range(5, 30+1, 5):
        print((i-5,i))
        print(strand[i-5: i+5])

def main():

    print("\n#########################")
    strand = "AAAAACCCCCAAAAACCCCCAAAAAGGTTT"


    app(strand)

    #dev(strand)


    print("\n###### COMPLETE #####\n")

if __name__ == "__main__":
    main()


