#!/usr/python

string = input("Enter your string of nucleotides here please: ")

nuc_A = 0
nuc_C = 0
nuc_T = 0
nuc_G = 0

if 0 < len(string) <= 1000:
    for i in string:
        if i == "A":
            nuc_A +=1
        elif i == "C":
            nuc_C +=1
        elif i == "T":
            nuc_T +=1
        elif i == "G":
            nuc_G +=1
        else:
            print("Invalid base.")
    print(str(nuc_A) + " " +  str(nuc_C) + " " + str(nuc_G) + " " + str(nuc_T))
else:
    print("Your string is too long. Please stick to max. 1000 nucleotides!")
