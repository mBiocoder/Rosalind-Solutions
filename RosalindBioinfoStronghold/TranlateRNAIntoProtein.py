#!/usr/python
import sys

#Variante 1:
with open(sys.argv[1], "r") as f:
    mRNA = f.read()

#Variante 2:
#mRNA = input("Enter your mRNA string here: ")

"""
In case -not needed for this exercise though-here is the code to build the anticodon of a given MRNA string

anticodon = ''
for base in mRNA:
    if base == 'A':
        anticodon += 'U' # not 'T' because we are dealing with mRNA here!
    elif base == 'C':
        anticodon += 'G'
    elif base == 'G':
        anticodon += 'C'
    elif base == 'U': # not 'T' because we are dealing with mRNA here!
        anticodon += 'A'
    else:
        print("This is not a base.")
print(anticodon)
"""

codontabelle = {'UUU':'F', 'CUU' :  'L', 'AUU': 'I', 'GUU': 'V','UUC': 'F','CUC': 'L','AUC': 'I', 'GUC': 'V','UUA': 'L','CUA': 'L','AUA': 'I','GUA': 'V', 'UUG': 'L','CUG': 'L','AUG': 'M','GUG': 'V', 'UCU': 'S','CCU': 'P','ACU': 'T','GCU': 'A',
                'UCC': 'S','CCC': 'P','ACC': 'T','GCC': 'A','UCA': 'S','CCA': 'P','ACA': 'T','GCA': 'A','UCG': 'S','CCG': 'P','ACG': 'T','GCG': 'A', 'UAU': 'Y','CAU': 'H','AAU': 'N','GAU': 'D','UAC':'Y','CAC': 'H','AAC': 'N','GAC':'D','UAA': 'Stop',
                'CAA': 'Q', 'AAA': 'K','GAA': 'E','UAG': 'Stop','CAG': 'Q','AAG': 'K','GAG': 'E','UGU': 'C','CGU': 'R','AGU': 'S','GGU': 'G','UGC': 'C', 'CGC': 'R', 'AGC': 'S','GGC': 'G','UGA': 'Stop','CGA': 'R','AGA': 'R','GGA': 'G','UGG': 'W',
                'CGG': 'R','AGG': 'R','GGG': 'G'}


def getAminoacidSequence(mRNA):
    peptidkette = ''
    for i in range(0,len(mRNA),3):
        if codontabelle[mRNA[0:3]] == 'M' and mRNA[i:i+3] in codontabelle and codontabelle[mRNA[i:i+3]] != 'Stop':
            peptidkette += codontabelle[mRNA[i:i+3]]
        elif codontabelle[mRNA[i:i+3]] == 'Stop':
            print("Das Stopcodon wurde erreicht.")
        else:
            print("Es gibt einen Fehler.")
            exit()
    print("Unsere Peptidkette: "+peptidkette)

getAminoacidSequence(mRNA)

