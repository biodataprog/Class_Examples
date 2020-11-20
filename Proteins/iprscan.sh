#!/usr/bin/bash
#SBATCH -p short -N 1 -n 16 --mem 4gb --out iprscan.%A.log

module load iprscan
iprscan.sh --goterms --pathways -f tsv --cpu 8 -i examples.fa -f tsv > examples.iprscan.out
