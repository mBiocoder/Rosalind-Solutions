#!/bin/env python3
import itertools

"""
The most elegant way:
"""

seq = {}
with open('./overlap.fa', 'r') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('>'):
            seqname = line[1:]
            seq[seqname] = ''
            continue
        seq[seqname] += line.upper()

for key, value in seq.items():
    for key2, value2 in seq.items():
        if key != key2 and value[-3:] == value2[:3]:
            print(key + '\t' + key2)

"""
lines = [x.strip() for x in open('Rosalind_OverlapGraphs.txt').readlines()]
#print(lines)

fasta = {}

for line in lines:
    if not line:
        continue
    if line.startswith('>'):
        header = line
        if line not in fasta:
            fasta[line] = ""
        continue
    fasta[header] += line

prefix = []
suffix = []
for k, v in fasta.items():
    matrix = " ".join(fasta.get(k).strip(' ')).splitlines()
    #print(v[-3:])
    prefix.append(v[:3])
    suffix.append(v[-3:])

#print(prefix)
#print(suffix)


def is_k_overlap(s1, s2, k):
    return s1[-k:] == s2[:k]


def k_edges(data, k):
    edges = []
    for u,v in itertools.combinations(data, 2):
        u_dna, v_dna = data[u], data[v]

        if is_k_overlap(u_dna, v_dna, k):
            edges.append((u + " " +v))

        if is_k_overlap(v_dna, u_dna, k):
            edges.append((v + " " + u))

    return edges

print('\n'.join(map(str,k_edges(fasta, 3))).replace(">", "").replace("(", ""). replace(")", ""))
"""

"""
Variante 2:
"""

"""
from collections import defaultdict

def overlap(seq,name):
    pref = seq[:FL]
    suff = seq[-FL:]
    if suff in prefixes:
        for i in prefixes[suff]:
            print name, i
    if pref in suffixes:
        for i in suffixes[pref]:
            print i, name

FL = 3
suffixes = defaultdict(list)
prefixes = defaultdict(list)
seq = ""
olist = []
filename = 'rosalind_grph.txt'

with open(filename, "r") as f:
    for line in f:
        if line[0] == ">":
            if seq:
                overlap(seq,name)
                prefixes[seq[:FL]].append(name)
                suffixes[seq[-FL:]].append(name)
                seq = ""
            name = line.rstrip()[1:]
        else:
            seq += line.rstrip()
    overlap(seq,name)"""
