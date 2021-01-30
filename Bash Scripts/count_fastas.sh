#!/bin/bash

# Author: Janith Weeraman
# Date : 12/01/2021
#
# Script to find the total number of fasta files in a folder
#
# Input : folder of fasta files
# Output: console output

cd ./fastas
lis=$(ls)
num=$(cat $lis | grep -c ">")

echo "Total number of fasta files: $num"


