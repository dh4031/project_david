from __future__ import division
import re

resistance_read = open("testgenes.fa").read()
resistance_data = re.findall(r"[>\w+.+]",resistance_read)
print resistance_data
#calculation of the number of ATGC
def antibiotic(resistance_data):
	gene_length = len(resistance)
	a_count = resistance_A.upper().count('A')
	t_count = resistance_T.upper().count('T')
	c_count = resistance_G.upper().count('G')
	g_count = resistance_C.upper().count('C')
	return round (a_count, t_count, c_count, g_count)
#---print gene_length
#complementing the strand
def complement_RNA(resistance):
	a_complement = resistance
	a_complement_replacement = a_complement_replacement.replace('A', 'U')
	t_complement_replacement = t_complement_replacement.replace('T', 'A')
	c_complement_replacement = c_complement_replacement.replace('C', 'G')
	g_complement_replacement = g_complement_replacement.replace('G', 'C')


#converting the strand of every 3 RNA sequence into an amino acid
#def amino_acid(RNA):


#matching specific proteins
#def RNA(protein):

#plan to list all the bacteria

#retrieve information on all the types of antibiotics

#
