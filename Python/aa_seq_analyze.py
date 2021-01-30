"""

Author: Janith Weeraman
Date: 17/01/2020

Python code to analyze the aa_seq.fasta file and calculate the length, molecular weight,
alanine percentage(A%), and glycine percentage(G%). The calculated parameters in a new
text file called aa_stats.txt

"""

from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Reading the aa_seq.fasta file and getting the sequence
with open('aa_seq.fasta','r') as file:
	# Get only the sequence of the fasta and turn it into 
	# a string without the newline
	seq = ''.join([line.strip() for line in file.readlines()[1:]])

prot_seq = ProteinAnalysis(seq)

with open('aa_stats.txt','w') as file:
	l = sum(prot_seq.count_amino_acids().values())
	file.writelines(f"Length of protein: {l}\n")
	percents = prot_seq.get_amino_acids_percent()
	file.writelines(f"Alanine percentage: {percents['A']}\n")
	file.writelines(f"Glycine percentage: {percents['G']}\n")
	weight = prot_seq.molecular_weight()
	file.writelines(f"Molecular weight: {weight}\n")
	

