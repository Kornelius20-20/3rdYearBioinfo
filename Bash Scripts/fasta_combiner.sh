#!/bin/bash

# Author: Janith Weeraman
# Date : 12/01/2021
#
# Script to combine multiple fasta files into a single fasta file
#
# Input : folder of fasta files
# Output: single fasta file named 'combined.fasta'

cd ./fastas

files=$(ls)
for file in $files
do 
	cat $file >> ../combined.fasta
done
