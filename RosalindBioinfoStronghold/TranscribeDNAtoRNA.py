#!/usr/python

string = input("Enter your string of DNA nucleotides here please: ")

if 0 < len(string) <= 1000:
    print(string.replace("T", "U"))
else:
    print("Your string is too long. Please stick to max. 1000 nucleotides!")