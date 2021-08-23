
#!/usr/bin/python3
import sys

#Accounting for the flags
sequence = sys.argv[2]
k = int(sys.argv[4])
L = int(sys.argv[6])
t = int(sys.argv[8])

#Read the file
file_path = sequence
with open(file_path) as f_obj:
    s = f_obj.read()

#Mthod called clumpFinding
def clumpFinding( s, k, L, t ):
	#Initialize a list called out 
    out = []
    for start in range(len(s)-L+1):
        window = s[start:start+L]
        counts = {}
		#Same as in 'Präsenzaufgabe'
        for i in range(len(window)-k+1):
            if window[i:i+k] not in counts:
                counts[window[i:i+k]] = 0
            counts[window[i:i+k]] += 1
		#chech if kmer counts are above the threshold t, if so, then append it to list out
        for kmer in counts:
            if counts[kmer] >= t and kmer not in out:
                out.append(kmer)
    return out

#Format the result
new = ' '.join(clumpFinding(s,k,L,t))
list = new.split(" ")
print(list)
