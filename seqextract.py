from Bio import SeqIO

# Read the sequence IDs classified as E. coli
with open("subSRR12277193_seqid_ecoli.txt") as f:
    ecoli_ids = set(line.strip() for line in f)

# Extract sequences from the original FASTA file
input_fasta = "/media/tanvi/One Touch/SRA_downloads_omkar/code/All_out/subSRR12277193.fasta"
output_fasta = "home/omkar/Desktop/ecoli_subSRR12277193.fasta"

with open(output_fasta, "w") as output_handle:
    for record in SeqIO.parse(input_fasta, "fasta"):
        if record.id in ecoli_ids:
            SeqIO.write(record, output_handle, "fasta")