"""

Author: Janith Weeraman
Date 16/02/2021

A program to test the NetCandPred package

"""

import NetCandPred as ncp
import os,sys

# Code to change the working directory to the location where the script is
cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(cwd)

# Test files that are in the current working directory
infofile = "3702.protein.info.v11.0.txt"
proteingraph = "Arabidopsis.protein.links.v11.0.txt.gz"
seedfolder = "seed_folder"
singleseed = "flower_development.txt"

graph = ncp.NetCandPred(proteingraph,infofile)
proteins,interactions = graph.proteins_interactions()
print(f"Number of proteins: {proteins} \nNumber of interactions: {interactions}")
print('\n\n')
# testing the hishigaki and majority voting algorithms for a single seed protein list
result = graph.hishigaki_single_function_predictor(singleseed)
print("Best proteins for flower development (Hishigaki algorithm):")
for key,value in result.items():
    print(f"{key} : ({value})")

print('\n\n')
result = graph.majority_single_function_predictor(singleseed)
print("Best proteins for flower development (majority voting algorithm):")
for key,value in result.items():
    print(f"{key} : ({value})")
print('\n')

# Testing the algorithms for a folder with seed proteins for multiple functions
result = graph.hishigaki_multi_function(seedfolder)
print("Best proteins for flower development from multiple seed lists (Hishigaki algorithm):")
for key1,value1 in result.items():
    print(f"{key1}:")
    for key2,value2 in value1.items():
        print(f"{key2} : ({value2})")
    print('')
print('')

result = graph.majority_multi_function(seedfolder)
print("Best proteins for flower development from multiple seed lists (Majority voting algorithm):")
for key1,value1 in result.items():
    print(f"{key1}:")
    for key2,value2 in value1.items():
        print(f"{key2} : ({value2})")
    print('')
print('\n')

# Testing the program for an unknown protein
result = graph.majority_best_function_predictor('ACT12',seedfolder)
print(f"The most likely function of ACT12 according to the majority voting algorithm is: {result}")
result = graph.hishigaki_best_function_predictor('SEP3',seedfolder)
print(f"The most likely function of SEP3 according to the hishigaki algorithm is: {result}")

input()