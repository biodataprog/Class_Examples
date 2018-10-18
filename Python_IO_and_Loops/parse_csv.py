#!/usr/bin/env python3
import csv
file2 = "test.csv"
with open(file2) as csvfile:
    reader = csv.reader(csvfile,delimiter=",",quotechar='|')
    for row in reader:
        print("\t".join(row))
        print("color is ",row[2])
