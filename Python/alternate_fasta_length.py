'''
Author: Janith
Date: 10/11
Uses len() to find length of sequence
input: fasta file named 'sequence.fasta'
output: length of file
'''

# Open file and store the sequence for reading
with open('sequence.fasta','r') as fasta:
    sequence = fasta.readlines()

# create counter for sequence length and initialize with 0
length = 0

# Count length of each line except for first line
for line in sequence[1:]:
    # Remove newline characters from each line
    line = line.strip()
    # Add length of line of bases to total length
    length += len(line)

# Output final total
print("The length of the sequence is: " + str(length))