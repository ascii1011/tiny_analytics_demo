
import os
import pathlib

"""
https://github.com/sbg/sevenbridges-python
"""
##### sequence analysis #####
# https://bi1.caltech.edu/code/t01_sequence_analysis.html
# http://www.rpgroup.caltech.edu/bige105/tutorials/t01/t01_sequence_analysis.html
# https://catalog.data.gov/dataset/dna-data1
#

RAW_DATA_ROOT = '/opt/mnt/raw_data/dna'


def sequence_analysis():

    import Bio.SeqIO

    path = RAW_DATA_ROOT + "/bige105/mabuya_atlantica"
    files = ['mabuya_aln.fasta', 'noronha_mabuya.txt', 'world_mabuya.txt']

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



    def display_output(path, files):
        for _file in files:
            with open(os.path.join(path, _file), 'r') as seq:
                basename = pathlib.Path(_file).stem

                print(f'\n### {basename} ###')

                fileobj = Bio.SeqIO.parse(seq, 'fasta')
                print(f'\tfileobj: {fileobj}')

                sequences = [record for record in noronha_file]
                print(f'\tsequences: {sequences}')

                desc = sequences[0].description
                print(f'\tdesc: {desc}')

                seq = sequences[0].seq
                print(f'\tseq: {seq}')
                #raw_seqs.update({pathlib.Path(_file).stem: noronha_sequences[0].seq})

    display_output(path, files)

sequence_analysis