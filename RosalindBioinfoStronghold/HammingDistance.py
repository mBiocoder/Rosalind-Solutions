#!/usr/python

#Inputs
#string1 = input("Enter your first string of DNA seq here: ")
#string2 = input("Enter your second string of DNA seq here: ")

large_dataset = open('C:\Bachelor Bioinformatik\Bachelor Bioinformatik\ProPra\RosalindBioinfoStronghold\HammingDistance.txt').read()
s, t = large_dataset.split()

counter = 0
hammingDistance = 0
if len(s) == len(t):
    for i in s:
        if i != t[counter]:
            hammingDistance += 1
        counter +=1
else:
    print("The strings must be of equal length!")

print(hammingDistance)
