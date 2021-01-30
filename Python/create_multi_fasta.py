"""

Author: Janith Weeraman
Date: 19/12/2020

A script to create multiple FASTA files from a list of accession numbers

"""

from Bio import Entrez
from Bio import SeqIO

# The sequences needed
sequences = ["AAK43967.1","AED90870.1","NP_567720.1","AAK59861.1"]

Entrez.email = 'arrerex580@gmail.com' # Letting Entrez know who I am :)

# Loop through sequence accession numbers
for id in sequences:
	# Fetching the FASTA data from Entrez protein database
	with Entrez.efetch(db='protein',rettype='fasta',retmode='text',id=id) as handle:
		filename = 'fastas/' + id + 'fasta' # To save each FASTA file with their accession 			numbers
		with open(filename,'w') as file:
			file.writelines(handle.readlines()) # Writing data to file
