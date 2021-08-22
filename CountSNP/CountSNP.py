#!/usr/bin/env python3

import sys

#command line arguments
fileOneSNP = sys.argv[1]
fileTwoYeast = sys.argv[2]

yeastTable = []

#read the files
with open(fileTwoYeast, "r") as f:
    data = f.readlines()
    for line in data:
        yeastTable.append(line.strip().split("\t")[1])
#print(yeastTable)

snpTable = []
with open(fileOneSNP, "r") as f:
    snp_data = f.readlines()
    for line in snp_data:
        snpTable.append(line.strip().split("\t")[1])
#print(snpTable)

#Get the region frequency
regionCounts = {}
#for eeach snp position check if it is also a part of yeast, if so, then increment counter by 1
for zeile in snpTable:
    if zeile in data[2] or data[3]:
        for region in yeastTable:
            if region not in regionCounts:
                regionCounts[region] = 1
            else:
                regionCounts[region] += 1
#print(regionCounts)

#formatting and print out
for key, value in regionCounts.items():
    print('{} \t {}'.format(key, value))



