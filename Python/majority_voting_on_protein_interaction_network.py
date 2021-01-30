"""
Author: Janith Weeraman
Date 14/12/2020

A script to implement the majority voting algorithm on a protein interaction network and output
the result to a txt file in descending order of voting score (based on number of known neighbours)

input: text files for known stress proteins and interaction network
output: text file containing predicted scores in descending order
"""

import networkx as nx
from collections import OrderedDict

# Read the list of stress proteins -> stress_prot
with open('AT_stress_proteins.txt', 'r') as file:
    stress_prot = file.readlines()
    # Code to split each line in file to a list of values according to tabs
    for i in range(len(stress_prot)): stress_prot[i] = stress_prot[i].strip().split('\t')

# Read the tsv of protein-protein interactions - > interactions
with open('lab4_2.tsv', 'r') as file:
    interactions = file.readlines()[1:]
    # Code to split each line in file to a list of values according to tabs
    for i in range(len(interactions)): interactions[i] = interactions[i].strip().split('\t')

# Create an interactions graph of the proteins from the tsv
gr = nx.Graph()

for line in interactions:
    gr.add_edge(line[0], line[1], weight=line[-1])

# Find the proteins in the interaction database whose functions aren’t already know (ie, they aren’t in stress_prot)
# -> unknowns
st_prot_names = [stress_prot[i][1].upper() for i in range(len(stress_prot))]  # Get stress protein names
nt_prot_names = [interactions[i][0] for i in range(len(interactions))]  # Get names of proteins making up nodes

unknowns = [i for i in nt_prot_names if i not in st_prot_names]
unknowns = dict.fromkeys(unknowns)

# For each of these unknown proteins,
for protein in unknowns.keys():
    score = 0
    # determine how many of their neighbors are known proteins
    # And assign them a score based on the number of known neighbours.
    for neighbour in gr.neighbors(protein):
        if neighbour.upper() in st_prot_names: score += 1
    unknowns[protein] = score

# Arrange the unknown proteins in descending order of neighbours
ordered = OrderedDict()
keys = list(unknowns.keys())
values = list(unknowns.values())
sorted_values = sorted(values, reverse=True)
maxim = 0

for i in sorted_values:
    # Find the key corresponding to a certain value
    key = keys[values.index(i)]
    # Add that key into an OrderedDict
    ordered[key] = i

# Output the ordered list of unknown proteins to a text file.
with open('PredictedScores.txt', 'w') as file:
    for key, val in ordered.items():
        file.write(str(key) + "\t" + str(val) + "\n")

# Code to get the answers for part i
print(gr.degree('DREB2A'))
print(len(keys))
