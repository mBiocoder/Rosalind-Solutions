#!/usr/python

#As called in Rosalind
# k  = number of homozygous dominant organisms
# n = number of heterozygous organisms
# m  = number of homozygous recessive organisms

def dominant_probability(num_homozygous_dominant, num_heterozygous, num_homozygous_recessive):
	total_population = num_homozygous_dominant + num_heterozygous + num_homozygous_recessive

# Mindestens ein dominantes Allel bedeutet 1 minus alle rezessive Allele
#Calculate the probability of two recessive organisms mating:
	recessive_probability = (num_homozygous_recessive / total_population) * ((num_homozygous_recessive - 1) / (total_population - 1))
#Now heterozygous organisms mating:
	heterozygous_probability = (num_heterozygous / total_population) * ((num_heterozygous - 1) / (total_population - 1))
#Now the hetero + recessive matings:
	hetero_recessive_probability = (num_heterozygous / total_population) * (num_homozygous_recessive / (total_population - 1)) + (num_homozygous_recessive / total_population) * (num_heterozygous / (total_population - 1))
#Now incorporate the fractions from the punnet squares:
#Return the output for dominant
	recessive_total = recessive_probability + heterozygous_probability * (.25) + hetero_recessive_probability * (.5)
	return (1 - recessive_total)

if __name__ == "__main__":

	result = round(dominant_probability(18, 29, 22), 5)
	print (result)

	# new dataset output
	f = open('workfile.txt', 'w')
	f.write(str(result))


