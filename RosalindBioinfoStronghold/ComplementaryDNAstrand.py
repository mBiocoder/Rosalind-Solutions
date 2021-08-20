#!/usr/python

string = input("Enter your string of DNA nucleotides here please: ")
#Create dictionary with complements
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

if 0 < len(string) <= 1000:
    reverse_complement = "".join(complement.get(base, base) for base in reversed(string))
    print(reverse_complement)

else:
    print("Your string is too long. Please stick to max. 1000 nucleotides!")
