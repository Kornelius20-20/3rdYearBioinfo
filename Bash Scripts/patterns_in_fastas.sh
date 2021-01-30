#!/bin/bash

# Author: Janith Weeraman
# Date : 12/01/2021
#
# Script to search fasta files in a folder names 'fastas'
# and then return a file with headers that contain a specific pattern
#
# Input : folder of fasta files
# Output: text file of headers containing pattern

files=$(ls ./fastas)
cd ./fastas
for file in $files
  do
    regexes=$(grep -E -c "(WGKWV|AAEIR)" $file)
    if [ $regexes -eq 1 ]
      then
	line=$(head -n 1 $file)
        echo "$line" >> ../AP2_advanced_headers.txt
    fi
  done
