#!/usr/python

file = open('Rosalind_ConsensusFasta.txt', 'r')
stringarray = []
for DNA in file.readlines():
	stringarray.append(DNA.rstrip())
file.close()

DNAlength = len(stringarray[1])
profileA = []
profileC = []
profileG = []
profileT = []

for x in range(0, DNAlength):
	#print(x)
	profileG.append(0)
	profileT.append(0)
	profileA.append(0)
	profileC.append(0)


n = 1
while n <= len(stringarray):
	string = stringarray[n]
	letters = list(string)
	c = 0
	while c < len(string):
		char = letters[c]
		if char == 'A':
			profileA[c] = profileA[c] + 1
		if char == 'C':
			profileC[c] = profileC[c] + 1
		if char == 'G':
			profileG[c] = profileG[c] + 1
		if char == 'T':
			profileT[c] = profileT[c] + 1
		c = c+1
	n = n+2

consensus = []
for char in range(0, len(profileA)):
	d = {profileA[char]:'A', profileC[char]:'C', profileG[char]:'G', profileT[char]:'T'}
	maximum = max(k for k, v in d.items())
	consensus.append(d[maximum])

print (''.join(consensus))

strA ='A: ' + ' '.join(str(e) for e in profileA)
strC ='C: ' + ' '.join(str(e) for e in profileC)
strG ='G: ' + ' '.join(str(e) for e in profileG)
strT ='T: ' + ' '.join(str(e) for e in profileT)
print (strA.strip() + '\n' + strC.strip() + '\n' + strG.strip() + '\n' + strT.strip())














