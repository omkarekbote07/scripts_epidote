from Bio import SeqIO
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
input_file = "/media/tanvi/One Touch/SRA_downloads_omkar/code/All_out/subSRR1277193.fasta"
min_length = float('inf') 
max_length = 0
sequence_lengths = []
num_sequences = 0
with open(input_file, "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        num_sequences+=1
        #print(f"ID: {record.id}")
        #print(record)
        #print(f"Length: {len(record)}")
        #print()
        sequence_lengths.append(len(record.seq))
        seq_length=(len(record.seq))
        if seq_length < min_length:
            min_length = seq_length
        if seq_length > max_length:
            max_length = seq_length

print(f"Total Sequences{num_sequences}")
print(f"Min seq length: {min_length}")
print(f"Max seq length: {max_length}")

plt.figure(figsize=(10, 6))
plt.hist(sequence_lengths, bins=410, color='blue', log = 'true')
plt.xscale('log')
plt.xlim(1000)
plt.title('')
plt.xlabel('Sequence Length')
plt.ylabel('Frequency')

plt.grid(True)
plt.show()
