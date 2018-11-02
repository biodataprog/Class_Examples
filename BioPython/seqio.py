import sys
#import Bio
from Bio import SeqIO
from Bio.Seq import Seq
# seqfile 
filename = sys.argv[1]

#seqio = SeqIO.parse( filename , "fasta"):
#for seq_record in seqio:

for seq_record in SeqIO.parse( filename , "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(seq_record.seq)
    print(len(seq_record))

filename = sys.argv[2]
for seq_record in SeqIO.parse( filename , "genbank"):
    print(seq_record.id)
    for feature in seq_record.features:
        print("\t",feature.type,feature.location)
        print("\t",feature.type,
              feature.location.start, 
              feature.location.end, 
              feature.location.strand)
