#!/usr/bin/env python3
import sys

infile = sys.argv[1]


# some functions here

# this is a function which takes a list of numbers
# returns a number
def mysum(number_list):
    sum = 0
    for i in number_list:
        sum += int(i)
    return sum


# dictionary to keep track of chromosome lengths
chrom_sizes = {}
feature_counts    = {}
feature_lengths   = {}

with open(infile,"r") as gff_fh:
    for line in gff_fh:
        line = line.strip()
#        print(line) # print every line
        if line.startswith("##sequence-region"):
            # print(line) # print the sequnce regions
            seqinfo = line.split()
            chrname = seqinfo[1]
            chrlen  = seqinfo[3]
            # store chrom lengths
            chrom_sizes[chrname] = int(chrlen)
        elif line.startswith("#"):
            continue
        else:
            # now we are in GFF land
            gffdata = line.split("\t")
            type = gffdata[2]
            if type in feature_counts:
                feature_counts[type] += 1
            else:
                feature_counts[type] = 1

            feat_len = abs(int(gffdata[4]) - int(gffdata[3])) + 1
            
            if type in feature_lengths:                
                feature_lengths[type] += feat_len
            else:
                feature_lengths[type] = feat_len
                
# this program will
# print out
# - the % of the genome which is coding
# - the number of genes, exons, and coding exons
# - number and length of UTR regions (combine 5' and 3')

total_genome_size = mysum( chrom_sizes.values() )

print("Total genome size is %d\n"%(total_genome_size))
for ftype in feature_counts.keys():
    print("Feature %s: %d"%(ftype,feature_counts[ftype])) 

print("")
for ftype in feature_lengths.keys():
    print("Feature length %s: %d %.2f%%"%(ftype,feature_lengths[ftype],
                                         100 * feature_lengths[ftype] / total_genome_size))
