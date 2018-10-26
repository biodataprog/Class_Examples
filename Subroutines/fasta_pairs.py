#!/usr/bin/env python3
# try and get a file like this one
# curl -O https://downloads.yeastgenome.org/sequence/S288C_reference/orf_protein/orf_trans.fasta.gz
# gunzip orf_trans.fasta.gz

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

def sum_list_numbers(input_numbers):
    # this is the subroutine code
    running_total = 0
    for num in input_numbers:
        running_total += num
    return running_total

def average(input_numbers):
    avg = sum_list_numbers(input_numbers) / len(input_numbers)
    return avg


# here is my program
# get the filename from the cmdline      
filename = sys.argv[1]
with open(filename,"r") as f:
   seqs = dict(aspairs(f))

# iterate through the sequences
n=0
seq_lengths = []
for k,v in seqs.items():
#   print( "id is",k,"seq is",v)
    print( "id is",k,"length is",len(v))
    seq_lengths.append(len(v))
    n += 1
   
print("There are",n,"sequences")
print("Avg sequence length is", average(seq_lengths))
