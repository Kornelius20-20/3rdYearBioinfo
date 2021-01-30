"""
Author: Janith Weeraman
Date: 4/12/2020

A class to represent DNA/mRNA/Amino acid sequences
"""

global seq_count
seq_count = 0
class Sequences:
    # Sequences features represented as variables to enable easy access
    seq_id: str
    seq_name: str
    seq_type: str
    seq_len: int
    sp_name: str
    subsp_name: str
    sequence: str

    def __init__(self, seq_name, seq_id, sp_name, subsp_name, sequence):
        global seq_count
        self.seq_id = seq_id
        self.seq_name = seq_name
        self.seq_len = len(sequence)
        self.seq_type = Sequences.get_Seq_Type(sequence)
        seq_count += 1
        self.sp_name = sp_name
        self.subsp_name = subsp_name

    def fasta_split(filename):
        """
        Method that takes in a multi-fasta and returns a dictionary with gene name
        as keys and a list containing hyphen-separated fields including the sequence
        as elements

        :param filename:
        :return dict with headers as keys and sequences as values:
        """
        fastas = {}
        with open(filename, 'r') as file:
            seqs = file.read().split('>')
            for i in seqs[1:]:
                # Find index of sequence start
                seq_start = i.find('\n')
                # get header and separate it on hyphens and add values except
                # gene name into the value list
                header = i[:seq_start]
                key = header.split('-')
                value = key[1:]
                # add sequence to value list
                value.append(i[seq_start + 1:].replace('\n', ''))
                # assign key and value pair in dictionary
                fastas[header] = value

        return fastas

    def get_Seq_Type(sequence):
        """
        Method that takes in a sequence and outputs a string mentioning whether
        it is a DNA,mRNA or Amino acid sequence
        :param sequence:
        :return String:
        """
        AA_CODES = ['R', 'N', 'D', 'B', 'E', 'Q', 'Z', 'H', 'I', 'L', \
                    'K', 'M', 'F', 'P', 'S', 'W', 'Y', 'V']

        # computationally efficient implementation
        if 'U' in sequence[0:20] or 'U' in sequence[20:]:
            return "mRNA"
        else:
            for i in sequence:
                # Determines if Amino acid specific letters are in sequence to check if protein
                if i in AA_CODES:
                    return "Amino acid"
                else:
                    return "DNA"

    def get_Character_Count(self,sequence):
        """
            Method to calculate base/amino acid content of a sequence
            :param sequence as a single string:
            :return AT content in the sequence:
            """
        # Read sequence -> sequence (Done outside of method)
        # Remove header line if exists
        start = sequence.find('\n') + 1
        sequence = sequence[start:].replace('\n', '')  # in addition, removes \n characters
        # Define counter for species
        counter = {}
        # For each species in sequence
        for i in sequence:
            # creaate a counter for each species and count how many iterations it has
            counter[i] = counter.get(i, 0) + 1

        # Output
        return counter


"""
A subclass to store DNA data specifically along with its AT content
and the transcribed mRNA sequence 
"""


class DNAseq(Sequences):
    AT_content: int
    trans_seq: str

    def __init__(self, seq_name, seq_id, sp_name, subsp_name, sequence):
        global seq_count
        seq_count += 1
        super().__init__(seq_name, seq_id, sp_name, subsp_name, sequence)
        self.AT_content = self.get_AT_content(sequence)
        self.trans_seq = self.transcribe_sequence(sequence)

    def transcribe_sequence(self, sequence):
        """
        Method to transcribe a given DNA sequence into its mRNA form and
        store it in the object's trans_seq variable. Storing is done as part of
        the object constructor

        :param sequence:
        :return None:
        """
        return sequence.replace('T', 'U')

    def get_AT_content(self, sequence):
        """
        Class Method to calculate AT content of a sequence, store it in the object
        variable and also return the value. Storing is done as part of the object
        constructor

        :param sequence:
        :return AT_content:
        """
        bases = self.get_Character_Count(sequence)
        at_content = bases['A'] + bases['T']
        return at_content


"""
A subclass to store mRNA data specifically along with its AT_content,
a codon table generator and the translated sequence 
"""


class MRNAseq(Sequences):
    AT_content: int
    aa_codons: str
    transl_seq: str

    def __init__(self, seq_name, seq_id, sp_name, subsp_name, sequence):
        global seq_count
        seq_count += 1
        self.seq_id = seq_id
        self.seq_name = seq_name
        self.seq_type = "mRNA"
        self.seq_len = len(sequence)
        self.sequence = sequence
        self.sp_name = sp_name
        self.subsp_name = subsp_name
        self.AT_content = self.get_ATcontent(sequence)
        self.transl_seq = self.translate_Sequence(sequence)

    def get_ATcontent(self, sequence):
        """
        Class method to Calculate AT content of mRNA sequence
        :param sequence:
        :return AT_content:
        """
        at_con = {}
        for base in sequence:
            if base == "A" or base == "U":
                at_con[base] = at_con.get(base, 0) + 1

        at = at_con['A'] + at_con['U']

        return at

    def upload_Codons(MRNAseq, filename):
        """
        Class method to return a dictionary to store codon-amino acid pairs from
        a text file that has codon table data

        :param filename:
        :return codon:
        """
        pattern = '([ACGU]{3})\t...\t(\w)'
        # Reading the codon file
        with open(filename, 'r') as f:
            lines = f.readlines()
            codonDict = {}
            # For each line in the codon table
        for line in lines:

            # 	Find codon pattern and corresponding Amino acid code
            # I know this isn't technically good coding practice but there's no
            # reason to import it if you're not running this specific method so I put it here
            import re
            matches = re.search(pattern, line)
            if matches:
                # Add it to a codon table dictionary -> codonDict
                codonDict[matches.group(1)] = matches.group(2)
        return codonDict

    def translate_Sequence(self, sequence, codons='codon_table.txt'):
        """
        Method that takes a sequence and an optional filename for a codon table
        and outputs the translated sequence
        :param sequence:
        :param codons:
        :return Amino acid sequence:
        """
        seq_prot = []
        codonDict = self.upload_Codons(codons)

        # Starting from first start codon (UAG) till a stop codon is reached,
        seq_mrna = sequence[sequence.find('AUG'):]
        i = 0
        while True:
            if codonDict[sequence[i:i + 3]] == 'O': break
            # Get nucleotide triplet and compare to codon table to get relevant Amino acid
            # Add amino acid to protein sequence

            seq_prot.append(codonDict[sequence[i:i + 3]])
            i += 3

        return seq_prot


class Proteinseq(Sequences):
    uniprot_id: int
    reviewed: bool
    hydrophobicity: float

    def __init__(self, seq_name, seq_id, sp_name, subsp_name, sequence,\
                 uniprot_id, reviewed):
        super().__init__(seq_name, seq_id, sp_name, subsp_name, sequence)
        global seq_count
        seq_count += 1
        self.sequence = sequence
        self.uniprot_id = uniprot_id
        self.hydrophobicity = self.get_Hydrophobicity(sequence)
        self.reviewed = reviewed

    def get_Hydrophobicity(self, sequence):
        """
        Method that takes in a sequence and calculates its hydrophobicity
        :param sequence:
        :return hydrophobicity:
        """
        amino_acids = self.get_Character_Count(sequence)
        total = sum(amino_acids.values())
        hydro = amino_acids.get('A',0) + amino_acids.get('I',0) + amino_acids.get('L',0) + \
                amino_acids.get('M',0) + amino_acids.get('F',0) + amino_acids.get('W',0) + \
                amino_acids.get('Y',0) + amino_acids.get('v',0)

        return hydro / total * 100
