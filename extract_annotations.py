from BCBio import GFF
from Bio import SeqIO
import csv
import sys

in_gff_file = sys.argv[1]
out_file = sys.argv[2]

#Add annotations to sequences
print("Parsing .gff file...")
in_handle = open(in_gff_file)
limit_info = dict(gff_type = ["mRNA"])

protnames = []
protanno = []

for rec in GFF.parse(in_handle, limit_info = limit_info, target_lines = 1):
	feat = rec.features[0]
	protnames.append(feat.qualifiers["Name"][0])
	protanno.append(feat.qualifiers["Note"][0])
in_handle.close()

#Write lists of sequences and annotations to .tsv file
print("Writing annotations to %s ..." % out_file)
with open(out_file, "w") as f:
	for protname, protan in zip(protnames, protanno):
		entry = [protname, protan]
		f.write("\t".join(entry) + "\n")
	f.close()

print("Extraction complete.")

