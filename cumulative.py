from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np

def get_cumulative_lengths(fasta_file):
    contig_lengths = []
    with open(fasta_file, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            contig_lengths.append(len(record.seq))
    contig_lengths.sort(reverse=True)
    cumulative_lengths = np.cumsum(contig_lengths)
    return cumulative_lengths

file1 = "QUAST_files/MegERR479014.fa"
file2 = "QUAST_files/MspERR479014.fasta"
file3 = "QUAST_files/Meg478989.fa"
file4 = "QUAST_files/Msp478989.fasta"

cumulative_lengths1 = get_cumulative_lengths(file1)
cumulative_lengths2 = get_cumulative_lengths(file2)
cumulative_lengths3 = get_cumulative_lengths(file3)
cumulative_lengths4 = get_cumulative_lengths(file4)

plt.figure(figsize=(10, 6))
plt.plot(range(1, len(cumulative_lengths1) + 1), cumulative_lengths1, marker='o', label='MegERR479014')
plt.plot(range(1, len(cumulative_lengths2) + 1), cumulative_lengths2, marker='o', label='MspERR479014')
plt.plot(range(1, len(cumulative_lengths3) + 1), cumulative_lengths3, marker='o', label='MegERR478989')
plt.plot(range(1, len(cumulative_lengths4) + 1), cumulative_lengths4, marker='o', label='MspERR478989')

plt.xlabel('Scaffold Index')
plt.ylabel('Cumulative Length (bp)')
plt.title('Cumulative Length vs. Scaffold Index')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()