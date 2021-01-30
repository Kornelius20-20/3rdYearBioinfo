"""
Author: Janith Weeraman
Date: 13/12/2020

A script to parse a blast output xml file and return the hits with an e-value below
a certain threshold.
The script outputs the hit title, alignment length, e-value, score, hit sequence,
and hit sequence length

input: BLAST output file in xml format
output: console output of information about hits (mentioned in description)
"""
from Bio.Blast import NCBIXML
import re

thresh_value = 0.05
file = open('dreb2a_blast.xml')
search = re.compile('ACGT[GT]C')
counter = 0 # Counter to count number of blast hits with ABRE present

blast_rec = NCBIXML.read(file)

for alignment in blast_rec.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < thresh_value:
            print("Title: ", alignment.title)
            print("Alignment length: ", alignment.length)
            print("E-value: ", hsp.expect)
            print("Score: ", hsp.score)
            print("Sequence: ",hsp.sbjct)
            print("Sequence length:", len(hsp.sbjct))

            # Find ABRE elements present, and if present print which one and where in the sequence
            factors = re.finditer(search,hsp.sbjct)
            print("ABRE element present: ",end='')

            isEmpty = True # Ugly workaround becaus python doesn't have an isEmpty for iterators ¬_¬

            for match in factors:
                print(match.group(0),end=' ')
                print(match.span())
                isEmpty = False

            # If no ABRE elements present, then just print N/A. If there was then add 1 to counter
            if isEmpty: print("N/A")
            else: counter += 1
            print('\n')
    # Print the number of hits in the sequence that contained ABRE
    print("No. of hits with ABRE = ",counter)