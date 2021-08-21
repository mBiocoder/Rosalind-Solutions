#!/usr/python3

#Through inputs
#a = input("Enter here for a: ")
#b = input("Enter here for b: ")
f = open("C:\Bachelor Bioinformatik\Bachelor Bioinformatik\ProPra\RosalindPythonProblems\VariablesFile.txt", "rt")
line = f.read()
values = line.split()
a = int(values[0])
b = int(values[1])

if 1 <= int(a) <= 1000:
    c = pow(int(a), 2) + pow(int(b), 2)
    print(c)
else:
   print("Enter values in proper range!")

