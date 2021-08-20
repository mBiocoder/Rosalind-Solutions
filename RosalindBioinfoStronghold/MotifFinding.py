#!/usr/python

dataset = open("Rosalind_motif.txt").read()
s = dataset.splitlines()
#print(s) print the list
string = s[0]
substring = s[1]
print(string)
print(substring)
"""for elem in s:
    print(elem)"""

all_positions=[]
if len(substring)<len(string):
    for i in range(0, len(string)):
        if string[i: i+len(substring)] == substring[:]:
            all_positions.append(i+1)
            #print(i+1) #Ausgehend von Indexbeginn bei 1 nicht 0
    #print(all_positions) #simply print list as is
    #print(str(all_positions).strip('[]')) #have results comma-seperated
    print(' '.join(map(str, all_positions)))

else:
    print("Substring muss kleiner sein als String!")
