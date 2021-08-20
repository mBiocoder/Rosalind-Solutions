#!/usr/python
import sys

ContentFasta = [x.strip() for x in open(sys.argv[1]).readlines()]
#print(ContentFasta)
fasta = {}
for line in ContentFasta:
    if not line:
        continue
    # create the sequence name in the dict and a variable
    if line.startswith('>'):
        sname = line
        if line not in fasta:
            fasta[line] = ''
        continue
    # add the sequence to the last sequence name variable
    fasta[sname] += line

#print(fasta)

# get keys and values from dict and print it as a list but without brackets
#lst = list(fasta.items())
#print(str(lst).replace("[", "").replace("]", ""))

#print header and values in appropriate fashion
for k, v in fasta.items():
    print(k + "\n", v)
print("-------------------------------------------------------------------------------------------------------------")


final = []
value = []
for i in range(len(ContentFasta)):
    if ContentFasta[i][0] == '>':
        final.append(value)
        value = [ContentFasta[i][1:]]
    else:
        value.append(ContentFasta[i])
final.append(value)
#remove first in final
final.pop(0)
countTotal = []

for i in range(len(final)):
    dnaString = ''
    for j in range(1,len(final[i])):
        dnaString += final[i][j]
    countTotal.append([final[i][0], dnaString])
GC_content = []
for i in range(len(countTotal)):
    record = "%.6f" % round((countTotal[i][1].count('C') + countTotal[i][1].count('G')) / len(countTotal[i][1]) * 100, 6)
    GC_content.append([record, countTotal[i][0]])

print(GC_content)
MaximumGC_Content = max(GC_content)

print(MaximumGC_Content[1])
print(MaximumGC_Content[0])

print("-------------------------------------------------------------------------------------------------------------")










