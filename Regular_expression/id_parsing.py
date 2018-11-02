#!/usr/bin/env python3

import re
# process the celegans_gene_names.no_dot.txt file

infile = "celegans_gene_names.txt"

count_alleles = {}
with open(infile, "r") as fh:
    for line in fh:
        line = line.strip()
        # print(line)

        # aaz-2.3
        # aaz-2
        
        match = re.search("([a-zA-Z]+)-(\d+)",line)
        if match:
            gene_name = match.group(1)
            gene_number = match.group(2)
            # print(gene_name,gene_number)
            if not gene_name in count_alleles:
                count_alleles[gene_name] = 1
            else:
                count_alleles[gene_name] += 1

print("==")
# convert / sort the dictionary so that it is sorted by 
sorted_counts = sorted(count_alleles, reverse=True,key=count_alleles.__getitem__)
print(sorted_counts)
for gene in sorted_counts:
    print(gene,count_alleles[gene])

