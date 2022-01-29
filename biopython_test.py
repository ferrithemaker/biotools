from Bio import SeqIO
from Bio.SeqUtils import GC  # (G + C) * 100 / (A + C + G + T)



records = SeqIO.parse("multipleSeqs.fa", "fasta")
list_records = []
print(records)


# transformem FastaIterator object en una llista
for seq_record in records:
    list_records.append(seq_record)

print(list_records[0].seq.count("A"))
print(GC(list_records[0].seq))
print(list_records[0].seq)
print(list_records[0].seq.reverse_complement())
print(list_records[0].seq.transcribe())
mRNA = list_records[0].seq.transcribe()
print(mRNA.translate())
print(list_records[0].seq.translate())

# Tener en cuenta dos funcionalidades: encontrar motivos y distancia de hamming
