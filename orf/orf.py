# import sys
# dna = sys.argv[1]
# path_to_triplets = sys.argv[2]

def get_reverse_complement(dna_sequence):
    rev_compl = ''
    # get reverse complement
    # TODO
    return rev_compl


# get codon table (file from excerxise 4, triplets.csv)
def read_codon_sun(file):
    codon_table = {}

    with open(path_to_triplets, mode='r') as infile:
        for line in infile:
            fields = line.strip().split("\t")
            # strip(): Entfernt Zeilenumbrüche am Ende von Zeile, split: splittet line am abgegeben String
            codon_table[fields[0]] = fields[1]
    return codon_table


def get_prot_from_orf(rna_string, codon_sun):
    protein_candidates = []
    for pos in range(len(rna_string) - 2):
        if rna_string[pos:pos + 3] == 'AUG':
            pos_tmp = pos
            prot = ''
            codon = rna_string[pos_tmp:pos_tmp + 3]
            while codon_sun[codon] != '$':
                prot += codon_sun[codon]
                pos_tmp += 3
                if pos_tmp > len(rna_string) - 3:
                    break
                codon = rna_string[pos_tmp:pos_tmp + 3]
            if codon_sun[codon] == '$' and prot not in protein_candidates:
                protein_candidates.append(prot)

    return protein_candidates


# transcribe dna to rna
rna = dna.replace('T', 'U')

# get reverse complement from rna
rev_complement = get_reverse_complement(rna)

# read codon_sun
codon_sun = read_codon_sun(path_to_triplets)

# get all protein candidates
proteins = get_prot_from_orf(rna, codon_sun)
proteins.extend(get_prot_from_orf(rev_complement, codon_sun))

print('\n'.join(set(proteins)))  # set filters only unique values from proteins