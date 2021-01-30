#!/bin/bash

python3 cds_seq_retrieve.py
python3 transcribe.py
python3 translate.py
python3 aa_seq_analyze.py

mkdir -p ./intermediate_files
mkdir -p ./output

mv cds_seq.fasta ./intermediate_files
mv mRNA_seq.fasta ./intermediate_files
mv aa_seq.fasta ./intermediate_files
mv aa_stats.txt ./output/aa_stats.txt
