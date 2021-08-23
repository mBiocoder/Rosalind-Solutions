#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import sys



#command line arguments
file = sys.argv[1]

# Read the file
f=open(file,"r")
lines=f.readlines()
#print(lines)
Avec = []
Cvec = []
Tvec = []
Gvec = []

for x in lines:
    g = x.split('\t')[-1]
    t = x.split('\t')[-2]
    c = x.split('\t')[-3]
    a = x.split('\t')[-4]
    Avec.append(int(a))
    Cvec.append(int(c))
    Tvec.append(int(t))
    Gvec.append(int(g))

f.close()
#print(Avec, Cvec, Tvec, Gvec)



# adapted from https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py

N = 11
ind = np.arange(N)  # the x locations for the groups
width = 0.8     # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, Avec, width/4, label='Adenosine', color='r')
rects2 = ax.bar(ind + width/4, Cvec, width/4, label='Cytosine', color='g')
rects3 = ax.bar(ind + width/2, Tvec, width/4, label='Thyamine', color='b')
rects4 = ax.bar(ind + 3*width/4, Gvec, width/4, label='Guanine', color='c')

#ax.set_title('Organisms')
ax.set_ylabel('Nucleotide count')
ax.set_xticks(ind)
ax.set_xticklabels(('Bacillus_subtilis', 'Escherichia_coli', 'Haemophilus_influenzae', 'Helicobacter_pylori', 'Hyperthermus_butylicus', 'Mycobacterium_tuberculosis', 'Mycobacterium_tuberculosis_v2', 'Salmonella_enterica', 'Thermotoga_petrophila', 'Vibrio_cholerae_chrI', 'Vibrio_cholerae_chrII') )
plt.xticks(rotation=90)
ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('A', 'C', 'T', 'G'))

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation='vertical')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
fig.tight_layout()
plt.show()