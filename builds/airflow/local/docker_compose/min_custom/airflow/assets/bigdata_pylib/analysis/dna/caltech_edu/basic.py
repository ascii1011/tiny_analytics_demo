##!/usr/local/bin/python3.10

import os
import pathlib
from itertools import combinations

from pprint import pprint

##### sequence analysis #####
# https://bi1.caltech.edu/code/t01_sequence_analysis.html
# http://www.rpgroup.caltech.edu/bige105/tutorials/t01/t01_sequence_analysis.html

RAW_DATA_ROOT = '/opt/mnt/raw_data/dna'

__all__ = ["sequence_analysis"]

def sequence_analysis():

    import Bio.SeqIO

    path = RAW_DATA_ROOT + "/bige105/mabuya_atlantica"
    files = ['mabuya_aln.fasta', 'noronha_mabuya.txt', 'world_mabuya.txt']
    files2 = ['mabuya_aln.fasta',]

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
        score = num_sim  / comp_length
        return score


    def display_output(path, files):
        seqs = {}
        for _file in files:
            with open(os.path.join(path, _file), 'r') as seq:
                basename = pathlib.Path(_file).stem

                print(f'\n### {basename} ###')

                fileobj = Bio.SeqIO.parse(seq, 'fasta')
                print(f'\tfileobj: {fileobj}')

                for record in fileobj:
                    #print(f'\n\trecord: {record}')
                    print(f'\tdesc: {record.description}')
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

    display_output(path, files2)

