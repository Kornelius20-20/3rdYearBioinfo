'''
Author: Janith
Date 11/11
Program to count the bases in a sequence
input: Sequence as fasta file named 'sequence.fasta'
output: The counts of each base for the 4 bases
'''

# Open file and read into a variable
with open('sequence.fasta','r') as fasta:
    sequence = fasta.readlines()
# Set 4 counters as A,C,T,G -> 0
bases = {
    'A': 0,
    'C': 0,
    'T': 0,
    'G': 0
}
# Skip first line in file
# For each line
for line in sequence[1:]:
#	For each character in line
    for character in line:
#		Append 1 to the counter which the character belongs to
        try:
            bases[character] += 1
        except KeyError:
            # For debugging purposes, following line should be commented out
            # print(ord(character))
            None

#	Endfor
# Endfor
# Output results of counters
print(f"""The sequence has,
        {bases['A']} A bases
        {bases['C']} C bases
        {bases['T']} T bases
        {bases['G']} G bases """)
