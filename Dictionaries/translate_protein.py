#!/usr/bin/env python3

import itertools
import sys
import re
# based on post here
# https://drj11.wordpress.com/2010/02/22/python-getting-fasta-with-itertools-groupby/
# define what a header looks like in FASTA format
def isheader(line):
    return line[0] == '>'

# this function reads in fasta file and returns pairs of data
# where the first item is the ID and the second is the sequence
# it isn't that efficient as it reads it all into memory
# but this is good enough for our project
def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence


# here is my program
# get the filename from the cmdline      
# The way to run this program will be
# translate_protein.py coding_sequences.fasta > protein_sequences.fasta

codon_table = "codon_table_compact.txt"

filename = sys.argv[1]

with open(filename,"r") as f:
   seqs = dict(aspairs(f))
   print(seqs)
   for seqid in seqs.keys():
       print("seqid is",seqid)
