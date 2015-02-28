from __future__ import division
import re

#finding how long the gene is to determine how to go about calculating codon
def antibiotic(dna):
	gene_length = len(dna)
	a_count = dna.upper().count('A')
	t_count = dna.upper().count('T')
	c_count = dna.upper().count('G')
	g_count = dna.upper().count('C')
	return a_count, t_count, c_count, g_count

#complementing the strand
def complement_RNA(dna):
	base = 'A', 'T', 'G', 'C'
	for base in complement
	a_complement_replacement = dna.replace('A', 'U')
	t_complement_replacement = dna.replace('T', 'A')
	c_complement_replacement = dna.replace('C', 'G')
	g_complement_replacement = dna.replace('G', 'C')
	final_rna = a_complement_replacement
	return final_rna

#translation of dna to protein, refer to for loop later on	
def translate_dna(dna):
	last_codon_start = len(dna) - 2
	protein = ""	

#creates a description output file just for a list of bacteria
description_output = open(description_output + ".fasta", "w")
description_output.write(description)

#creates a library of dna sequences
sequence_output = open(sequence_output + ".fasta", "w")
sequence_output.write(sequence)

#reading the fasta file, splitting into multiple lines
resistance_read = open("testgenes.fa").read().splitlines()

#conditional statement for seperating the DNA sequence from the description
for line in resistance_read:
	if line.startswith(">"):
		description = line
	else: 
		sequence = line

# calculate the start position for the final codon
last_codon_start = len(dna) – 2
# process the dna sequence in three base chunks
for start in range(0,last_codon_start,3):
codon = dna[start:start+3]

#dictionary for a list of codons
codon_dict = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

#creates the code from a list of dna sequences, need to write append for loop later
for start in range(0,last_codon_start,3):
	codon = dna[start:start+3]
	aa = codon_dict.get(codon.upper(), 'X')
	protein = protein + aa
	return protein

	
#calculation of the number of ATGC


#converting the strand of every 3 RNA sequence into an amino acid
#def amino_acid(RNA):


#matching specific proteins
#def RNA(protein):

#plan to list all the bacteria

#retrieve information on all the types of antibiotics

#formula for dn/ds

#create a user input to search for type of bacteria
