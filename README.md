# extract-annotations
Use Biopython to extract functional gene annotations from a GFF file and output them as a tab-delimited text file.

In some bioinformatic analyses, it can be helpful to create a list of all the functional annotations (i.e. short statements on the function of potential gene products), often as an intermediary step to adding such annotations to a fasta file. 

## USAGE

The syntax for this script is as follows:

`python3 extract_annotations.py <GFF FILE> <NAME YOU WANT FOR OUTPUT FILE>`

For example, this code:

`python3 extract_annotations.py my_example_genes.gff my_example_annotations.txt`

will extract the annotations in my_example_genes.gff and save the results to the my_example_annotations.txt file. The first column in the text file will be the mRNA feature id associated with each annotation and the second column will be the actual functional annotation.

## FORMAT NOTES

The functional annoations are assumed to be in the dictionary entry "Note" under the mRNA features of the GFF file, like in this entry from the my_example_genes.gff file:

```
SL4.0ch00       maker_ITAG      gene    93750   94430   .       +       .       ID=gene:Solyc00g500001.1;Alias=Solyc00g500001;Name=Solyc00g500001.1;length=680
SL4.0ch00       maker_ITAG      mRNA    93750   94430   .       +       .       ID=mRNA:Solyc00g500001.1.1;Parent=gene:Solyc00g500001.1;Name=Solyc00g500001.1.1;Note=Retrovirus-related Pol polyprotein from transposon TNT 1-94 (AHRD V3.3 *-* A0A2I0VJ33_9ASPA);_AED=0.01;_QI=0|-1|0|1|-1|0|1|0|227;_eAED=0.01
SL4.0ch00       maker_ITAG      exon    93750   94430   .       +       .       ID=exon:Solyc00g500001.1.1.1;Parent=mRNA:Solyc00g500001.1.1
SL4.0ch00       maker_ITAG      CDS     93750   94430   .       +       0       ID=CDS:Solyc00g500001.1.1.1;Parent=mRNA:Solyc00g500001.1.1
```

## DEPENDENCIES

1. Biopython. Install with:

`pip install biopython`

If that doesn't work, see [here](https://biopython.org/wiki/Download).

2. The GFF file parser for Biopython. Install with:

`pip install bcbio-gff`

If that doesn't work, see [here](https://github.com/chapmanb/bcbb/tree/master/gff).

3. Python3 - I tested this script with Python v3.8.2

## REFERENCES

I acquired the example gff file from the [Sol Genomics Network](https://solgenomics.net/organism/Solanum_lycopersicum/genome).
