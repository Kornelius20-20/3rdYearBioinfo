from sequence_objects_oop import *

fastas = Sequences.fasta_split('OSDREB_sequences.fasta')
print(fastas)
seq_objects = []
for key,value in fastas.items():
    key = key.split('-')[0]
    if Sequences.get_Seq_Type(value[-1]) == 'mRNA':
        seq_objects.append(MRNAseq(key,value[0],value[1],value[2],value[3]))
    elif Sequences.get_Seq_Type(value[-1]) == 'DNA':
        seq_objects.append(DNAseq(key, value[0], value[1], value[2], value[3]))
    else:
        seq_objects.append(Proteinseq(key, value[0], value[1], value[2], value[3],value[5],True if value[4].lower() == 'reviewed' else False))

for obj in seq_objects:
    if obj.seq_type == "DNA" and "DREB1A" in obj.seq_name:
        print('i')
        print("Gene ID: ",obj.seq_id)
        print("Sequence length: ", obj.seq_len)
        print("Sequence type: ", obj.seq_type)
        print("AT content: ", obj.AT_content)
        print()

    if obj.seq_type == "DNA" and "DREB2B" in obj.seq_name:
        print('ii')
        transcribed = obj.trans_seq # code auto transcribes when creating object
        mRNA = MRNAseq(obj.seq_name,obj.seq_id,obj.sp_name,obj.subsp_name,transcribed)
        print("Sequence length: ", mRNA.seq_len)
        print("Sequence type: ", mRNA.seq_type)
        print("AT content: ", mRNA.AT_content)
        print("Sequence: ",mRNA.sequence)
        print()

        print('iii')
        prot = mRNA.transl_seq
        print("protein: ", prot)
        print("length: ",len(prot))
        print()

    if obj.seq_type == "Amino acid" and "DREB2A" in obj.seq_name:
        print('iv')
        print("Uniprot ID: ",obj.uniprot_id)
        print("reviewed: ","yes" if obj.reviewed else "no")
        print("Composition: ", obj.get_Character_Count(obj.sequence))
        print("hydrophobicity: ",obj.hydrophobicity)
        print()

print(seq_count)


