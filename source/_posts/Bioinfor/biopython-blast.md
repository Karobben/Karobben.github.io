---
toc: true
url: biopython_blast
covercopy: © Karobben
priority: 10000
date: 2021-10-15 11:41:48
title: "Online Blast with Biopython"
ytitle: "在Biopython里面完成在线blast"
description: "Blast hundreds of sequence with Biopython scripts"
excerpt: "Blast hundreds of sequence with Biopython scripts"
tags: [Bioinformatic, Scripts, Biopython, Python]
category: [Biology, Bioinformatics, Protocol]
cover: "https://s1.ax1x.com/2020/07/27/aFEKqH.png"
thumbnail: "https://biopython.org/assets/images/biopython_logo_white.png"
---

## Quick Start

source: [© Biopython](https://www.tutorialspoint.com/biopython/biopython_overview_of_blast.htm)

```python
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

sequence_data = open("blast_example.fasta").read()
result_handle = NCBIWWW.qblast("blastn", "nt", sequence_data)
E_VALUE_THRESH = 1e-20

with open('results.xml', 'w') as save_file:
  blast_results = result_handle.read()
  save_file.write(blast_results)

print(sequence_data)
E_VALUE_THRESH = 1e-20
for record in NCBIXML.parse(open("results.xml")):
    if record.alignments:
       print("\n")
       print("query: %s" % record.query[:100])
       for align in record.alignments:
                print("match: %s " % align.title[:100])
```

<pre>
  >gnl|alu|X55502_HSAL000745 (Alu-J)
  TGCCTTCCCCATCTGTAATTCTGGCACTTGGGGAGTCCAAGGCAGGATGATCACTTATGC
  CCAAGGAATTTGAGTACCAAGCCTGGGCAATATAACAAGGCCCTGTTTCTACAAAAACTT
  TAAACAATTAGCCAGGTGTGGTGGTGCGTGCCTGTGTCCAGCTACTCAGGAAGCTGAGGC
  AAGAGCTTGAGGCTACAGTGAGCTGTGTTCCACCATGGTGCTCCAGCCTGGGTGACAGGG
  CAAGACCCTGTCAAAAGAAAGGAAGAAAGAACGGAAGGAAAGAAGGAAAGAAACAAGGAG
  AG

  query: gnl|alu|X55502_HSAL000745 (Alu-J)
  match: gi|120310614|gb|AC190318.8| Rhesus Macaque BAC CH250-278P13 () complete sequence
  match: gi|149944763|gb|AC204073.5| Rhesus Macaque BAC CH250-450C10 () complete sequence
  match: gi|218436709|dbj|AP007219.1| Macaca fuscata fuscata DNA, clone: MSB2-167F16, complete sequence
  match: gi|1777294620|ref|XM_009195938.4| PREDICTED: Papio anubis SEC14 like lipid binding 5 (SEC14L5), tran
</pre>


## Tricks

Blast Sequence from Uniprot with Organism Option

From: [zorbax; Biostars 2020](https://www.biostars.org/p/439571/)

```python
import urllib.request
from Bio import SeqIO
from Bio.Blast import NCBIWWW

url = 'https://www.uniprot.org/uniprot/Q9LZP9.fasta'
urllib.request.urlretrieve(url, "chain_N.faa")

record = SeqIO.read("chain_N.faa", format="fasta")
result_handle = NCBIWWW.qblast('blastp', 'nr', record.seq,
                               entrez_query="txid3702[ORGN]")

```


## Download best matched seq from the blast result

```python
from Bio import Entrez

# Tell NCBI who you are
Entrez.email="example@outlook.com"

# Acquire the sequences
# If you are searching for DNA sequences, then db="nucleotide"

handle = Entrez.efetch( db="protein", id="NP_172363.1", rettype="fasta", retmode="text")
print(handle.read())
```

### Esearch in terminal

We can use esearch to dwonload the fast file
source: [NCBI Book](https://www.ncbi.nlm.nih.gov/books/NBK179288/)

```bash
conda install -c bioconda entrez-direct

# for nucleotide
esearch -db nucleotide -query "KAG7629426.1" | efetch -format fasta
# for protein sequences
esearch -db protein -query "KAG7629426.1" | efetch -format fasta
```


## Practices

Find the homologs gene from 10 different species by blast

organism information: [NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Tree&id=38039&lvl=3&lin=f&keep=1&srchmode=1&unlock)

1. Find a list of organism
```python
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
from Bio import Entrez
import urllib.request



Organ_list = ["9527",
  "499232",
  "9597",
  "9601",
  "61851",
  "716690",
  "9480",
  "9521",
  "174599",
  "37295",
  "1861701",
  "1812036",
  "30596",
  "9604",
  "9504",
  "9480"]

for i in Organ_list:
    record = SeqIO.read("chain_N.faa", format="fasta")
    result_handle = NCBIWWW.qblast('blastp', 'nr', record.seq,
                                   entrez_query="txid"+ i +"[ORGN]")

    with open('results.xml', 'w') as save_file:
      blast_results = result_handle.read()
      save_file.write(blast_results)
    E_VALUE_THRESH = 1e-20
    Num = 0
    for record in NCBIXML.parse(open("results.xml")):
        Num += 1
        if record.alignments:
           print("\n")
           print("query: %s" % record.query[:100])
           for align in record.alignments:
                    align.title.split("|")[1]
                    if Num < 4:
                        A = align.title
                        handle = Entrez.efetch( db="protein", id=A.split("|")[1], rettype="fasta", retmode="text")
                        print(handle.read())

```




for(i in c("BLOSUM62", "PAM250")){
  seq_1 <- "MRSSPGNMERIVICLMVIFLGTLVHKSSSQGQDRHMIRMRQLIDIVDQLKNYVNDLVPEFLPAPEDVETNCEWSAFSCFQKAQLKSANTGNNERIINVSIKKLKRKPPSTNAGRRQKHRLTCPSCDSYEKKPPKEFLERFKSLLQKMIHQHLSSRTHGSEDS"
  seq_2 <- "MERTLVCLVVIFLGTVAHKSSPQGPDRLLIRLRHLIDIVEQLKIYENDLDPELLSAPQDVKGHCEHAAFACFQKAKLKPSNPGNNKTFIIDLVAQLRRRLPARRGGKKQKHIAKCPSCDSYEKRTPKEFLERLKWLLQKMIHQHLS"
  globalAlign_CHRNA2 <- pairwiseAlignment(seq_1, seq_2, substitutionMatrix = i, gapOpening = -12, gapExtension = -2, scoreOnly = FALSE)
  substr(globalAlign_CHRNA2@pattern, 1, nchar(globalAlign_CHRNA2@pattern))
  substr(globalAlign_CHRNA2@subject, 1, nchar(globalAlign_CHRNA2@subject))
  print(globalAlign_CHRNA2@score)
}
