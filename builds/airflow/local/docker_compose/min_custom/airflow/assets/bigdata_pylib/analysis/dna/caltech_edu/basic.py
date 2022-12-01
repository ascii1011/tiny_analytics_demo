##!/usr/local/bin/python3.10

import os
import pathlib
from itertools import combinations

import Bio.SeqIO

from pprint import pprint

##### sequence analysis #####
# https://bi1.caltech.edu/code/t01_sequence_analysis.html
# http://www.rpgroup.caltech.edu/bige105/tutorials/t01/t01_sequence_analysis.html

RAW_DATA_ROOT = '/opt/mnt/raw_data/dna'

__all__ = [
    "sequence_analysis",
    "get_dna_pair_compute_similarity_scores", "get_dna_map_combination_pairs", 
    "map_dna_files", "to_graph_edges"
    ]



def compute_similarity(seq_1, seq_2):
    """
    ref: bi1.caltech.edu
    Computes the percent similarity between two sequences ignoring gaps. 
    
    Parameters
    ----------
    seq_1, seq_2 : strings
        DNA sequences to compare. These must be the same length.
        
    Returns
    -------
    score : float
        The percent similarity between the two sequences. 
    """
    # Make sure they are the same length. 
    if len(seq_1) != len(seq_2):
        raise ValueError('Sequences must be the same length!')
        
    # Make both sequences lowercase.
    seq_1 = seq_1.lower()
    seq_2 = seq_2.lower()
        
    # Set up counters of length and similarity.
    comp_length = 0
    num_sim = 0
    
    # Iterate through each position in the sequences.
    for base in range(len(seq_1)):
        
        # Ensure we are not comparing gaps.
        if (seq_1[base] != '-') and (seq_2[base] != '-'):
            
            # Increase the counter for compared length.
            comp_length += 1
            
            # Compare the two positions.
            if seq_1[base] == seq_2[base]:
                
                # Increase the similarity counter.
                num_sim += 1
                
    # Compute and return the percent similarity.
    score = float(num_sim  / comp_length)
    return score

def to_graph_edges(dna_pair_score, debug=False):
    """
    scores.update({f"{dna1}___{dna2}": score_value})
    to..

    edges = {
        'A': [('B', 6), ('D', 1)],
        'B': [('A', 6), ('C', 5), ('D', 2), ('E', 2)],
        'C': [('B', 5), ('E', 5)],
        'D': [('A', 1), ('B', 2), ('E', 1)],
        'E': [('B', 2), ('C', 5), ('D', 1)],
    }
    """
    edges = {}
    for key, score in dna_pair_score.items():
        if debug: print(f"{key=} = {score=}")
        seq1, seq2 = key.split('___')

        if seq1 not in edges:
            edges.update({seq1:[]})
        if (seq2,score) not in edges[seq1]:
            edges[seq1].append((seq2,score))

        if seq2 not in edges:
            edges.update({seq2:[]})
        if (seq1,score) not in edges[seq2]:
            edges[seq2].append((seq1,score))

    return edges

def map_dna_files(files, debug=False):
    if debug: print(f"\nmap_dna_files():")
    dna_map = {}
    for _file in files:
        with open(_file, 'r') as seq:
            basename = pathlib.Path(_file).stem

            if debug: print(f'\n### {basename} ###')

            fileobj = Bio.SeqIO.parse(seq, 'fasta')
            if debug: print(f'\t{fileobj=}')

            for record in fileobj:
                if debug: 
                    print(f'\n\t{record=}')
                    print(f'\t{record.description=}')
                    print(f'\t{record.seq=}')
                dna_map.update({str(record.description): str(record.seq)})

    if debug: print(f"\tEND<< {dna_map=}")
    return dna_map

def get_dna_map_combination_pairs(dna_map={}, debug=False):
    if debug: print(f"\nget_dna_map_combination_pairs():")
    combo_pairs = []
    for tpl in combinations(dna_map.keys(), 2):
        if debug: print(f"{tpl}")
        if len(tpl) == 2:
            dna1, dna2 = tpl
            combo_pairs.append((dna1, dna2))

    if debug: print(f"\tEND<< {combo_pairs=}")
    return combo_pairs

def get_dna_pair_compute_similarity_scores(combos, dna_map, debug=False):
    if debug: print(f"\nget_dna_pair_compute_similarity_scores():")
    scores = {}
    for dna1, dna2 in combos:
        score_key = f"{dna1}___{dna2}"
        #print(f"key({type(score_key)}): {score_key}")

        score_value = compute_similarity(dna_map[dna1], dna_map[dna2])
        #print(f"key({type(score_value)}): {score_value}")

        scores.update({score_key: score_value})

        if debug: print(f">> {dna1} vs {dna2} == {score_value}")

    if debug: print(f"\tEND<< {scores=}")
    return scores

"""
def cache_dna_from_files(path, files):
    raw_seqs = {}
    for _file in files:
        with open(os.path.join(path, _file), 'r') as seq:
            noronha_file = Bio.SeqIO.parse(seq, 'fasta')
            noronha_sequences = [record for record in noronha_file]
            #noronha_seq = noronha_sequences[0].seq
            #noronha_desc = noronha_sequences[0].description
            raw_seqs.update({pathlib.Path(_file).stem: noronha_sequences[0].seq})

    return raw_seqs


def sequence_analysis(list_of_files=[], debug=False):

    #path = RAW_DATA_ROOT + "/bige105/mabuya_atlantica"
    #files = ['mabuya_aln.fasta', 'noronha_mabuya.txt', 'world_mabuya.txt']
    #files2 = ['mabuya_aln.fasta',]

    def compute_similarity(seq_1, seq_2):
        #""
        #ref: bi1.caltech.edu
        #Computes the percent similarity between two sequences ignoring gaps. 
        #
        #Parameters
        #----------
        #seq_1, seq_2 : strings
        #    DNA sequences to compare. These must be the same length.
        #    
        #Returns
        #-------
        #score : float
        #    The percent similarity between the two sequences. 
        #""
        # Make sure they are the same length. 
        if len(seq_1) != len(seq_2):
            raise ValueError('Sequences must be the same length!')
            
        # Make both sequences lowercase.
        seq_1 = seq_1.lower()
        seq_2 = seq_2.lower()
            
        # Set up counters of length and similarity.
        comp_length = 0
        num_sim = 0
        
        # Iterate through each position in the sequences.
        for base in range(len(seq_1)):
            
            # Ensure we are not comparing gaps.
            if (seq_1[base] != '-') and (seq_2[base] != '-'):
                
                # Increase the counter for compared length.
                comp_length += 1
                
                # Compare the two positions.
                if seq_1[base] == seq_2[base]:
                    
                    # Increase the similarity counter.
                    num_sim += 1
                    
        # Compute and return the percent similarity.
        score = num_sim  / comp_length
        return score


    def display_output(files, debug=False):
        seqs = {}
        for _file in files:
            with open(_file, 'r') as seq:
                basename = pathlib.Path(_file).stem

                if debug: print(f'\n### {basename} ###')

                fileobj = Bio.SeqIO.parse(seq, 'fasta')
                if debug: print(f'\tfileobj: {fileobj}')

                for record in fileobj:
                    #print(f'\n\trecord: {record}')
                    if debug: print(f'\tdesc: {record.description}')
                    #print(f'\tseq: {record.seq}')
                    seqs.update({record.description: record.seq})

        for tpl in combinations(seqs.keys(), 2):
            #print(f"{tpl}")
            score = compute_similarity(seqs[tpl[0]], seqs[tpl[1]])
            print(f">> {tpl[0]} vs {tpl[1]} == {score}")

        #sequences = [record for record in fileobj]
        #print(f'\tsequences: {sequences}')

        #desc = sequences[0].description
        #print(f'\tdesc: {desc}')

        #seq = sequences[0].seq
        #print(f'\tseq: {seq}')
        #raw_seqs.update({pathlib.Path(_file).stem: noronha_sequences[0].seq})

    display_output(list_of_files, debug)

"""

