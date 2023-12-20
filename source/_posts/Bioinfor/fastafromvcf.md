---
toc: true
url: fastafromvcf
covercopy: <a href="https://www.sepmag.eu/blog/choosing-the-appropriate-dna-extraction-protocol">© Lluis M. Martínez</a>
priority: 10000
date: 2022-09-16 11:40:36
title: "Extract Fasta from VCF"
ytitle: "Extract Fasta from VCF"
description: "Extract Fasta from VCF"
excerpt: "To create a fasta file from a VCF file, use a script or software that can extract the genomic sequence information from the VCF file and format it into the fasta format. This allows you to generate a sequence-based representation of the genetic variation data stored in the VCF file, making it easier to visualize, analyze, and compare the variants. The fasta file can then be used as input for various bioinformatics tools and pipelines. <a title='ChatGPT'>Who sad this?</a>"
tags: [Bioinformatics, Fasta, VCF]
category: [Biology, Bioinformatics, Protocol]
cover: "https://www.sepmag.eu/hubfs/DNA%20extraction%20protocol.jpg"
thumbnail: "https://www.sepmag.eu/hubfs/DNA%20extraction%20protocol.jpg"
---


## Extract only a part of genes


In this part, we'll try to extract specific region of sequence from genome and substitute the SNP sites in python

Basic Tech:

Let's assume:
- 1: A → C
- 4: TAT → TA
- 5: A → C
- 10: C → AC,G

!!! warning There are two things we have to highlight:
    1. Conflict between 4:TAT and 5: A→C
        - In this situation, we simply select the TA because it can reduce the calculation.
    2. 10: C→ AC,G
        - we simply select the first one.


```python
import pandas as pd

VCF = pd.DataFrame([[1,"A","C"],
            [4, "TAT", "TA"],
            [5,"A","C"],
            [10, "G", "AC,C"]],
            columns=["Pos", "Ref", "Alt"])

STR = 'ATCTATCACGCATAGCTAGCTAGTCA'

TB = pd.DataFrame([*STR])
TB['Ref'] = ""
TB['Alt'] = ""

TB.iloc[VCF.Pos-1,1] = VCF.Ref.to_list()
TB.iloc[VCF.Pos-1,2] = [i.split(",")[0] for i in VCF.Alt.to_list()]
TB.head()
```
<pre>
   0  Ref Alt
0  A    A   C
1  T         
2  C         
3  T  TAT  TA
4  A    A   C
</pre>


!!! Now, we can fill the blank in `Alt` with Reference:

```python
TB.Alt[TB.Alt==""] =  TB[0][TB.Alt==""].to_list()
TB.head()
```

<pre>
   0  Ref Alt
0  A    A   C
1  T        T
2  C        C
3  T  TAT  TA
4  A    A   C
</pre>

!!! Last but not least step is fold the table based on the Ref (Exp, 4:TAT)

```python
TB["Len"] = [len(i)-1 for i in TB.Ref]
TB.Len[TB.Len<0]=0

TB["DEL"] = 0
TB["DEL_mark"] = 0

TB.DEL =TB.Len.to_list()[:1] +TB.Len.to_list()[:-1]
TB.DEL_mark += TB.DEL
TB.DEL[TB.DEL>1] = TB.DEL_mark[TB.DEL>1]-1


while TB.DEL.max()!=0:
    TB.DEL =TB.DEL.to_list()[:1] +TB.DEL.to_list()[:-1]
    TB.DEL_mark += TB.DEL
    TB.DEL[TB.DEL>0] = TB.DEL[TB.DEL>0]-1

STR2 = "".join(TB.Alt[TB.DEL_mark==0].to_list())

# Print Alignment results
from Bio.pairwise2 import format_alignment
alignments = pairwise2.align.globalxx(STR, STR2)
print(format_alignment(*alignments[0]))
```

<pre>
A-TCTATCACG-C-ATAGCTAGCTAGTCA
  |||| |||  | |||||||||||||||
-CTCTA-CAC-ACCATAGCTAGCTAGTCA
  Score=23
</pre>

```diff index.js
-let strRegExp = '(?<=^\n)(^!!! *)(note|info|todo|warning|attention|caution|failure|missing|fail|error)(.*\n)((^ {4}.*\n|^\n)+)';
+let strRegExp = '(?<=^\n)(^!!! *)(note|info|todo|warning|attention|caution|failure|missing|fail|error|question)(.*\n)((^ {4}.*\n|^\n)+)';

```


!!! note Why pandas?
    Because we can now extract any part of sequence based on the annotation information from `gtf` file.

Prepare a csv file which contains the information of location you want:
<pre>
CHROM	START	END	NAME Dirc
mitochondrion_genome	1480	2988	COX1	+
mitochondrion_genome	3083	3754	COX2	+
</pre>

This script only works on specific example (Drosophila mitochondria Genes in genome V6.39 from Flybase)

```bash
echo -e "CHROM\tSTART\tEND\tNAME\tDirc" > Target.csv
grep -i "^mitochondrion_genome" genes.gtf|  \
    grep -v transcript_symbol|              \
    awk '{OFS="\t"; print $1,$4,$5,$12,$7}'|   \
    sed 's/[";]//g' >> Target.csv
```

An script could be like:

```python
import gzip
import pandas as pd
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def get_vcf_names(vcf_path):
    with gzip.open(vcf_path, "rt") as ifile:
          for line in ifile:
            if line.startswith("#CHROM"):
                  vcf_names = [x for x in line.split('\t')]
                  break
    ifile.close()
    return vcf_names

VCF_file = "G1FFH.vcf.gz"
Genome = "../Mito.fa"
Target = "Target.csv"
SAMPLE = VCF_file.replace(".vcf.gz", "")
names = get_vcf_names(VCF_file)
vcf = pd.read_csv('G1FFH.vcf.gz', compression='gzip', comment='#',  header=None, names=names, sep='\t')

TARGET = pd.read_csv(Target, sep='\t')

for seq_record in SeqIO.parse(Genome, "fasta"):
    if seq_record.id in TARGET.CHROM.unique():
        print("Chrom:", seq_record.id)
        TB = pd.DataFrame([*seq_record.seq])
        TB['REF'] = ""
        TB['ALT'] = ""
        TB.iloc[vcf.POS-1,1] = vcf.REF.to_list()
        TB.iloc[vcf.POS-1,2] = [i.split(",")[0] for i in vcf.ALT.to_list()]
        TB.ALT[TB.ALT==""] =  TB[0][TB.ALT==""].to_list()
        TB.head()
        TB["Len"] = [len(i)-1 for i in TB.REF]
        TB.Len[TB.Len<0]=0

        TB["DEL"] = 0
        TB["DEL_mark"] = 0

        TB.DEL =TB.Len.to_list()[:1] +TB.Len.to_list()[:-1]
        TB.DEL_mark += TB.DEL
        TB.DEL[TB.DEL>1] = TB.DEL_mark[TB.DEL>1]-1
        while TB.DEL.max()!=0:
            TB.DEL =TB.DEL.to_list()[:1] +TB.DEL.to_list()[:-1]
            TB.DEL_mark += TB.DEL
            TB.DEL[TB.DEL>0] = TB.DEL[TB.DEL>0]-1

        TMP = TB.ALT[TB.DEL_mark==0]
        F = open(SAMPLE + "_" + seq_record.id +".fa", "w")
        F.close()

        F = open(SAMPLE + "_" + seq_record.id +".fa", "a")
        LIST = []
        for i in range(len(TARGET[TARGET.CHROM==seq_record.id])):
            FROM =TARGET.START[TARGET.CHROM==seq_record.id][i]
            END = TARGET.END[TARGET.CHROM==seq_record.id][i]
            print(FROM,END)
            STR1 = "".join(TB[0][TB.index.isin(range(FROM-1,END))].to_list())
            STR2 = "".join(TMP[TMP.index.isin(range(FROM-1,END))].to_list())
            F.write(">"+TARGET.NAME[TARGET.CHROM==seq_record.id][i] + "_" + SAMPLE + "\n" + STR2 + "\n" )
            LIST += range(FROM-1,END)

        #F.write(">NonHit_" + SAMPLE + "\n" + "".join(TMP[~TMP.index.isin(LIST)]) + "\n" )

        F.close()

```

reference: [d.vitale199, 2021](https://www.biostars.org/p/416324/), how to read the VCF files with python pandas.

This script was uploaded into GitHub:[Karobben/Bio_tools](https://github.com/Karobben/Bio_tools)
A demo would be like:

```bash
python vcf2fasta.py -g Genome.fa -v File.vcf.gz -t Target.csv
```


## Other Methods

### For a whole chromosome

#### vcf2fasta
 [rlebron88, 2016](https://github.com/rlebron88/vcf2fasta)
```bash
git clone https://github.com/rlebron88/vcf2fasta.git
python vcf2fasta/vcf2fasta.py -v <VCF file from the sample> -f <reference FASTA file> -o <FASTA file from the sample>
```
Limitations:
- ONLY ONE SEQUENCE/CHROMOSOME PER VCF.
- USE "X" TO REFER TO THE SEQUENCE OF REF IN THE VCF FILE.
- IF THERE IS MORE THAN ONE ALT, THE FIRST IS USED.
- DO NOT USE multiFASTA.

#### vcftools


[MatthewP, 2018](https://www.biostars.org/p/360900/): vcftools has a command vcf-consensus which can convert VCF to FASTA file if you got the reference

```bash
bgzip -c file.vcf > file.vcf.gz
tabix -fp vcf file.vcf.gz
cat Reference.fasta | vcf-consensus file.vcf.gz > file.fa
```

#### Python scripts

[Python Scripts](https://www.researchgate.net/publication/354169060_FASTA_files_generator_for_TABULAR_BLAST_HITS_and_Non_HITS_using_Python): -- Didn't be test.
[Peal scripte](https://github.com/lh3/samtools/blob/master/bcftools/vcfutils.pl): -- Didn't be test.

Python code from [Jared Andrews, 2017](https://bioinformatics.stackexchange.com/questions/2825/converting-a-vcf-into-a-fasta-given-a-reference-with-python-r):

```python
consensus = FastaVariant('yourgenome.fasta', 'variants.vcf.gz', het=True, hom=True)

out = open("variants.fasta", "w")

for chrom in consensus.keys:
    for var in consensus[chrom].variants_sites:
        record = consensus[chrom][var-1:var]
        print(record, file=out)

out.close()
```






<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}

</style>
