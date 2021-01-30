"""
Author: Janith Weeraman
Date: 30/11/2020

A set of methods to process fasta files
input: fasta file
outputs: [see in method description]
"""


def at_calc(sequence):
    """
    Method to calculate AT content of a sequenct
    :param sequence as a single string:
    :return AT content in the sequence:
    """

    # Read sequence -> sequence (Done outside of method)
    # Remove header line if exists
    start = sequence.find('\n') + 1
    sequence = sequence[start:].replace('\n', '')  # in addition, removes \n characters
    # Define counter for A/T bases
    counter = 0
    # For each nucleotide in sequence
    if sequence[0] == 'M': return 0
    for i in sequence:
        # If nucleotide is A or T then add 1 to counter
        if i == 'A' or i == 'T': counter += 1
    # Output
    return counter


def split_fasta(filename):
    """
    Method that takes in a multi-fasta and returns a dictionary with headers
    as keys and sequences as values

    :param filename:
    :return dict with headers as keys and sequences as values:
    """
    fastas = {}
    with open(filename, 'r') as file:
        seqs = file.read().split('>')
        for i in seqs[1:]:
            split_mark = i.find('\n')
            key = i[:split_mark]
            value = i[split_mark + 1:].replace('\n', '')
            fastas[key] = value

    return fastas


def what_type(sequence):
    start = sequence.find('\n') + 1
    if sequence[start] == 'M': return "Amino acid"
    if 'U' in sequence[start:start + 10]:
        return "mRNA"
    else:
        return "DNA"


filename = "OSDREB_sequences.fasta"
fastas = split_fasta(filename)
for key,value in fastas.items():
    print(key + ":")
    base = at_calc(value)
    base = base if base != 0 else "N/A"
    print("AT content:",base)
    print("Type:",what_type(value))
    print()

