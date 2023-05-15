import argparse
from Bio import SeqIO

# Handle user input and automate help message (out of scope for this course)
parser = argparse.ArgumentParser()
parser.add_argument("input", help = "Path to input file", type = str)
parser.add_argument("output", help = "Path to results file", type = str)
args = parser.parse_args()

# Import fasta file is Biopython object
sequence_file = SeqIO.parse(args.input, format = "fasta")

# Reset Seq count
seqs = 0

# Iterate over all items
for seq in sequence_file:
    seqs += 1

# Generate output file
with open(args.output, "w") as outfile:
	outfile.write("Sequences\n%s" %seqs)

