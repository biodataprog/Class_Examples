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
codon_lookup = {} # dictionary to lookup a codon and find the AA

with open(codon_table,"r") as ct:
    for line in ct:
        line = line.strip()
        codoninfo = line.split()
        # turn the list of codons (AAA,AAT,.. into an array)
        codons = codoninfo[0].split(",")
        aminoacid = codoninfo[1] # store the amino acid from col 2
        # for each codon, assign it the value of the current amino acid
        # by storing it in the dictionary 'codon_lookup'
        for codon in codons:
#            print('codon ',codon,'translates to',aminoacid)
            codon_lookup[codon] = aminoacid
        
#        print(codoninfo)
#        print(line)

filename = sys.argv[1]

# can run either way
# python translate_protein.py orf_coding.fasta > orf_coding.pep
# ./translate_protein.py orf_coding.fasta > orf_coding.pep
with open(filename,"r") as f:
   seqs = dict(aspairs(f))
#   print(seqs)
   for seqid in seqs.keys():
       #print("seqid is",seqid)
       cdsseq = seqs[seqid]
       #print('length of sequence is',len(cdsseq))
       proteinseq = ""
       for start in range(0,len(cdsseq), 3):
           #print("starting base is",start)
           codon = cdsseq[start:start + 3]

           AA = codon_lookup[codon]
           #print("codon is",codon, " AA is",AA)
           proteinseq += AA
# also can be written
#           proteinseq = (proteinseq + AA)
       print(">%s"%(seqid))
       print(proteinseq)
