"""

Author: Janith Weeraman
Date: 17/01/2020

python file to transcribe a sequence in a fasta file
named cds_seq.fasta into mRNA and save it as a fasta file

"""

# Dictionary containing base translations
code = { 'G':'C', 'C':'G', 'A':'U', 'T':'A' }

# Ask for the fasta file to transcribe
filename = 'cds_seq.fasta'

# Open the fasta file and read it line by line into a variable ->lines
with open(filename,'r') as file:
	temp = file.readlines()
	header = temp[0]
	# Code to convert sequence into one continuous string 
	line =  ''.join([line.strip() for line in temp[1:]])

# Code to check if the sequence is mRNA
if len(set(line).difference('ACTG')) > 0: raise Exception("The file isn't a DNA file!")

# add "transcribed" to the end of the header
header = header.strip() + '_transcribed\n'

# Open the output file and write header
file = open('mRNA_seq.fasta','w')
file.write(header)

# Write the transcribed bases into the file and close it
for base in line:
	file.write(code[base])
file.close()
