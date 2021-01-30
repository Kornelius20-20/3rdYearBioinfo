"""
Author: Janith Weeraman
Date: 24/11/2020
Version: 3.0

Takes in a multi-fasta file and outputs single fasta files while converting any
DNA sequences into RNA sequences and appending "mRNA" to mRNA files and "translated"
to protein files
Input: multi-fasta file
output: separate fasta files containing one sequence each labeled as "mRNA" or
"translated" based on what type of sequence
"""

import os

# Get name of fasta file to open -> name
while True:
    name = input("What's the fasta file you want opened?")
    if name[-6:] == '.fasta':
        break
    else:
        print("You didn't enter a valid fasta file!")

# Read the fasta file into variable -> lines
with open(name, 'r') as fasta1:
    lines = fasta1.read()

# Separate lines into individual fastas
fastas = lines.split('>')

# For each individual sequence
for seq in fastas[1:]:
    line = seq.find('\n')

    # Open a new fasta file and write sequence to file where
    name2 = ''.join(x for x in seq[:line] if x.isalnum()) + ".fasta"
    with open(name2, 'w') as f:

        #       if file is a protein sequence (starts with 'M') then it is written as is
        if seq[line + 1] == 'M':
            f.write(seq)

        #       otherwise all 'T's in the sequence are replaced with 'U' and then written
        else:
            f.write(seq[0:line] + seq[line:].replace('T', 'U'))

    # The file with the protein sequence is called “[original fasta name]_transcribed” and
    if seq[line + 1] == 'M':
        os.rename(name2, name[:-6] + '_transcibed.fasta')
    #   The file with the mRNA sequence is called ““[original fasta name]_mRNA”
    else:
        os.rename(name2, name[:-6] + '_mRNA.fasta')
