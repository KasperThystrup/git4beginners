import argparse
from Bio import SeqIO

# Handle user input and automate help message (out of scope for this course)
parser = argparse.ArgumentParser()
parser.add_argument("input", help = "Path to input file", type = str)
parser.add_argument("output", help = "Path to results file", type = str)
args = parser.parse_args()


# Import fasta file is Biopython object
sequence_file = SeqIO.parse(args.input, format = "fasta")

# Reset base counts
bases = 0

# Iterate over all items
for record in sequence_file:
    bases += len(record.seq)

# Generate output file
with open(args.output, "w") as outfile:
	outfile.write("Base count\n%s" %bases)


