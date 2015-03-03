#reading the fasta file, splitting into multiple lines
resistance_read = open("testgenes.fa").read().splitlines()

for line in resistance_read:
	if line.startswith(">"):
		description_output = line
	else: 
		sequence_output = line

description_output = open(description_output + ".fasta", "w")
description_output.write(description)

#creates a library of dna sequences
sequence_output = open(sequence_output + ".fasta", "w")
sequence_output.write(sequence)