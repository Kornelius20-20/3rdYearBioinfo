'''
Author: Janith
Date: 10/11
Calculates length of DNA sequence in FASTA format
Input: fasta file name
Output: length value
'''

# Assign variable as counter and set it to 0
# Assign variable to start count as start and set it to false
counter = 0
start = False

# Get name of fasta file to open -> name
while True:
    name = input("What's the fasta file you want opened?")
    if (name[-6:] == '.fasta'):
        break
    else:
        print("You didn't enter a valid fasta file!")

# Open the FASTA file and read it into a variable -> dna
with open(name,'r') as fasta:
    dna = fasta.readlines()

# For each line in dna except the first line
for line in dna[1:]:
# 	For each character in line except for newline character
    for character in line.strip():
#		Counter = counter +1
        counter +=1
#	endfor

# output total length
print("Length of sequence is:" + str(counter))

