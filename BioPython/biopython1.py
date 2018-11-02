import Bio
from Bio.Seq import Seq
my_seq = Seq("ATGAGTACACTAGGGTAA")
print my_seq
rc = my_seq.reverse_complement()
pep = my_seq.translate()
print "revcom is", rc
print pep

print 'first 2 amino acids are ', pep[0]
