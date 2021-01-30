"""
Author: Janith Weeraman
Date: 4/12/2020

Code to read a fasta file and run a blastn using the nucleotide database.
The script then outputs an xml file containing the blast result

input: fasta file
outptut: xml file containing blast result
"""

from Bio.Blast import NCBIWWW

# Read fasta file into variable
with open("ATdreb2a.fasta",'r') as file:
    seq = file.read()

# Run a BLAST against the nucleotide database
result = NCBIWWW.qblast('blastn','nt',seq)

# Write the BLAST result into an xml file
with open('dreb2a_blast.xml','w') as file:
    file.write(result.read())

