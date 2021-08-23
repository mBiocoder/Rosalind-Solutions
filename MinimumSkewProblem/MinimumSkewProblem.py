#!/usr/bin/env python3
import matplotlib.pyplot as plt
import os
import sys

#Read the commandline arguments
genome_path = sys.argv[1]
output_folder = sys.argv[2]

#Read the file
lines=[]
with open(genome_path, 'r') as genome_path:
    for line in genome_path:
        lines.append(line)
genome= ''.join(lines)

#Count the number of 'C' and 'G' and put each Skew in the skews list
c=0
g=0
skews = [0]
min = 0
min_skew_indices = []

#iterate genome over index and character
for index, nucl in enumerate(genome):
    if nucl == 'C':
        c+=1
    elif nucl == 'G':
        g+=1
    difference =g-c
    skews.append(difference)

    #Test if difference is smaller than the minimal value
    if difference < min:
        min = difference
        #clear list because miniml skew value has changed
        min_skew_indices.clear()
    if difference == min:
        min_skew_indices.append(index+1) #add the index to list

#print indices for min skew
for i in min_skew_indices:
    print(i, end= " ")

#plot the skew values
plt.plot(skews, color='green')
plt.xlabel('Genome position')
plt.ylabel('Skew value')

#For plot title use input path to get organism name
#os.path.basename(path) returns the tail of the path
#then split the 'filename.txt' using deliminator


#organism = Escherichia_coli.split('.')[1]
plt.title('Skew diagram')
#plt.tight_layout()

plt.savefig(output_folder + "/SkewDiagram.png")
plt.show()