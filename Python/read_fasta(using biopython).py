"""
Author: Janith Weeraman
Date: 4/12/2020

Code to read a fasta file and output the sequence ID,description, sequence and
length

input: fasta file
outptut: console output of values mentioned above
"""
from Bio import SeqIO

# Read fasta file using SeqIO
for record in SeqIO.parse('ATdreb2a.fasta', 'fasta'):
    # Output sequence info
    print("ID: ", record.id)
    print("Description: ", record.description)
    print("Sequence: ", record.seq)
    print("Length: ", len(record))
