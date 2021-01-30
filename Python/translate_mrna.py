"""
Author: Janith Weeraman
Date: 24/11/2020
Version: 1.0

Takes in an mRNA file and translates it using a codon table for reference ("codon.txt")
and outputs a translated protein sequence in one reading frame

Input: mRNA fasta file
output: translated protein sequence fasta file
"""

import re

# Read the mRNA file and codon table -> mRNA, codon
file_cod = 'codon_table.txt'
file_mrna = 'OSDREB1A_mRNA.fasta'
file_prot = file_mrna[:-10] + 'tranlation.fasta'
seq_prot = []
pattern = '([ACGU]{3})\t...\t(\w)'

"""
# Temporary comment for testing
while True:
    file_mrna = input("What's the fasta file you want opened?")
    if (file_mrna[-6:] == '.fasta'):
        break
    else:
        print("You didn't enter a valid fasta file!")
"""

# Reading the codon file
with open(file_cod, 'r') as f:
    lines = f.readlines()
    codonDict = {}

    # For each line in the codon table
    for line in lines:

        # 	Find codon pattern and corresponding Amino acid code
        matches = re.search(pattern, line)
        if matches:
            # Add it to a codon table dictionary -> codonDict
            codonDict[matches.group(1)] = matches.group(2)


tmp = None # variable to hold the original fasta header of mRNA file

# Reading the mRNA file
with open(file_mrna, 'r') as f:
    data = f.read()
    seq_mrna = data[data.find('\n') + 1:] .replace('\n','') # Slicing out the header and remove newlines
    tmp = data[:data.find('\n')]

    # Starting from first start codon (UAG) till a stop codon is reached,
    seq_mrna = seq_mrna[seq_mrna.find('AUG'):]
    i = 0
    while True:
        if codonDict[seq_mrna[i:i + 3]] == 'O': break
        # Get nucleotide triplet and compare to codon table to get relevant Amino acid
        # Add amino acid to protein sequence
        print(codonDict[seq_mrna[i:i + 3]])
        seq_prot.append(codonDict[seq_mrna[i:i + 3]])
        i +=3

# Store the protein sequence in its own fasta file named “[mRNA file name]_translation.fasta”
with open(file_prot,'w') as f:
    f.write(tmp + '\n')
    f.write(''.join(seq_prot))