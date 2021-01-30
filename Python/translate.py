"""

Name: Janith Weeraman
Author: 17/01/2020

A python file to translate a sequence in a fasta file and save the translated amino acid sequence
in another fasta file

"""
from Bio.Seq import Seq

# Open the mRNA sequence file and split it into the header and sequence
with open('mRNA_seq.fasta','r') as file:
	temp = file.readlines()
	header = temp[0].strip()
	# Code to remove the newline files and turn the sequence lines into
	# a single string
	seq = ''.join([line.strip() for line in temp[1:]])


# Check to see if sequence is mRNA
if len(set(seq).difference('ACGU')) > 0: raise Exception("File isn't an mRNA!")

# Update header and add into a new file
header = header + '_translated\n'
file = open('aa_seq.fasta','w')
file.write(header)

# Adding Ns until the final sequence is a multiple of 3 so that the biopython translate
# function can work properly
seq = seq + (len(seq)%3-1)*'N'
# Translate sequence using Biopython and write to file
protein = Seq(seq).translate()
file.write(str(protein))

file.close()


