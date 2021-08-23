#!/usr/bin/env python3

import sys

#command line arguments
fastaFile = sys.argv[1]
basepairs = str(sys.argv[2])

#Method for reading fasta files
def parserForFasta(inputFile):
    seqs = []
    headers = []
    with open(inputFile) as f:
        sequence = " "
        header = None
        for line in f:
            #Fasta files always start with '>' as their header
            if line.startswith('>'):
                headers.append(line[1:-1])
                if header:
                    seqs.append([sequence])
                sequence = ""
                header = line[1:]
            else:
                #The rstrip() method returns a copy of the string with trailing characters removed
                sequence += line.rstrip()
        seqs.append([sequence])
    return headers, seqs

headers, seqs = parserForFasta(fastaFile)

item_seq = [item for sublist in seqs for item in sublist]

#count nucleotides in fasta
def nucleotideCount(inputString):
    #count upper and lower case sequences
    for base in basepairs:
        if base == 'G':
            g = inputString.upper().count('G')
        elif base == 'C':
            c = inputString.upper().count('C')
        elif base == 'A':
            a = inputString.upper().count('A')
        elif base == 'T':
            t = inputString.upper().count('T')

    #Account for any order of ATCG in sys.arv[2] -> 4! = 24 possibilities
    if basepairs[0] == 'G' and basepairs[1] == 'C' and basepairs[2] == 'A' and basepairs[3] == 'T':
        return '{} \t {} \t {} \t {}'.format(g, c, a, t)
    elif basepairs[0] == 'G' and basepairs[1] == 'C' and basepairs[2] == 'T' and basepairs[3] == 'A':
        return '{} \t {} \t {} \t {}'.format(g, c, t, a)
    elif basepairs[0] == 'C' and basepairs[1] == 'G' and basepairs[2] == 'A' and basepairs[3] == 'T':
        return '{} \t {} \t {} \t {}'.format(c, g, a, t)
    elif basepairs[0] == 'A' and basepairs[1] == 'G' and basepairs[2] == 'C' and basepairs[3] == 'T':
        return '{} \t {} \t {} \t {}'.format(a, g, c, t)
    elif basepairs[0] == 'G' and basepairs[1] == 'A' and basepairs[2] == 'C' and basepairs[3] == 'T':
        return '{} \t {} \t {} \t {}'.format(g, a, c, t)
    elif basepairs[0] == 'C' and basepairs[1] == 'A' and basepairs[2] == 'G' and basepairs[3] == 'T':
        return '{} \t {} \t {} \t {}'.format(c, a, g, t)
    elif basepairs[0] == 'A' and basepairs[1] == 'C' and basepairs[2] == 'G' and basepairs[3] == 'T':
        return '{} \t {} \t {} \t {}'.format(a, c, g, t)
    elif basepairs[0] == 'T' and basepairs[1] == 'C' and basepairs[2] == 'G' and basepairs[3] == 'A':
        return '{} \t {} \t {} \t {}'.format(t, c, g, a)
    elif basepairs[0] == 'C' and basepairs[1] == 'T' and basepairs[2] == 'G' and basepairs[3] == 'A':
        return '{} \t {} \t {} \t {}'.format(c, t, g, a)
    elif basepairs[0] == 'C' and basepairs[1] == 'A' and basepairs[2] == 'G' and basepairs[3] == 'T':
        return '{} \t {} \t {} \t {}'.format(c, a, g, t)
    elif basepairs[0] == 'G' and basepairs[1] == 'T' and basepairs[2] == 'C' and basepairs[3] == 'A':
        return '{} \t {} \t {} \t {}'.format(g, t, c, a)
    elif basepairs[0] == 'T' and basepairs[1] == 'G' and basepairs[2] == 'C' and basepairs[3] == 'A':
        return '{} \t {} \t {} \t {}'.format(t, g, c, a)
    elif basepairs[0] == 'C' and basepairs[1] == 'G' and basepairs[2] == 'T' and basepairs[3] == 'A':
        return '{} \t {} \t {} \t {}'.format(c, g, t, a)
    elif basepairs[0] == 'G' and basepairs[1] == 'A' and basepairs[2] == 'T' and basepairs[3] == 'C':
        return '{} \t {} \t {} \t {}'.format(g, a, t, c)
    elif basepairs[0] == 'G' and basepairs[1] == 'T' and basepairs[2] == 'A' and basepairs[3] == 'C':
        return '{} \t {} \t {} \t {}'.format(g, t, a, c)
    elif basepairs[0] == 'A' and basepairs[1] == 'T' and basepairs[2] == 'G' and basepairs[3] == 'C':
        return '{} \t {} \t {} \t {}'.format(a, t, g, c)
    elif basepairs[0] == 'A' and basepairs[1] == 'G' and basepairs[2] == 'T' and basepairs[3] == 'C':
        return '{} \t {} \t {} \t {}'.format(a, g, t, c)
    elif basepairs[0] == 'A' and basepairs[1] == 'C' and basepairs[2] == 'T' and basepairs[3] == 'G':
        return '{} \t {} \t {} \t {}'.format(a, c, t, g)
    elif basepairs[0] == 'A' and basepairs[1] == 'T' and basepairs[2] == 'C' and basepairs[3] == 'G':
        return '{} \t {} \t {} \t {}'.format(a, t, c, g)
    elif basepairs[0] == 'T' and basepairs[1] == 'G' and basepairs[2] == 'A' and basepairs[3] == 'C':
        return '{} \t {} \t {} \t {}'.format(t, g, a, c)
    elif basepairs[0] == 'T' and basepairs[1] == 'A' and basepairs[2] == 'G' and basepairs[3] == 'C':
        return '{} \t {} \t {} \t {}'.format(t, a, g, c)
    elif basepairs[0] == 'T' and basepairs[1] == 'A' and basepairs[2] == 'C' and basepairs[3] == 'G':
        return '{} \t {} \t {} \t {}'.format(t, a, c, g)
    elif basepairs[0] == 'T' and basepairs[1] == 'C' and basepairs[2] == 'A' and basepairs[3] == 'G':
        return '{} \t {} \t {} \t {}'.format(t, c, a, g)
    elif basepairs[0] == 'C' and basepairs[1] == 'T' and basepairs[2] == 'A' and basepairs[3] == 'G':
        return '{} \t {} \t {} \t {}'.format(c, t, a, g)
    elif basepairs[0] == 'C' and basepairs[1] == 'A' and basepairs[2] == 'T' and basepairs[3] == 'G':
        return '{} \t {} \t {} \t {}'.format(c, a, t, g)

#print the result in Stdout
for header, sequence in zip(headers, item_seq):
    print(header + '\t' + nucleotideCount(sequence))
