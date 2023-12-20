---
title: "SNP Calling: samtools"
description: "SNP Calling: samtools"
url: snp_samtools
date: "2020/07/28"
toc: true
excerpt: "SNP Calling: samtools"
tags: [Software, SNP, NGS, Bioinformatics]
category: [Biology, Bioinformatics, Protocol, SNP]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## SNP Calling: samtools


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>

## 1. sort by samtools
```bash
samtools sort bwa.bam -o bwa.sorted.bam > bwa.sorted.bam
samtools faidx genome.fna

##Exp:
samtools sort AJ.bam -o AJ.sorted.bam > AJ.sorted.bam
##Exp:
samtools faidx Apostichopus_japonicus.fna
```

### 2. SNP calling
```bash
samtools mpileup -guSDf genome.fasta abc.bam | bcftools view -cvNg - > abc.vcf
```


Reference: [Kevin Blighe, 2019](https://www.biostars.org/p/150972/)
```bash
bcftools mpileup --redo-BAQ --min-BQ 30 --per-sample-mF \
  --annotate FORMAT/AD,FORMAT/ADF,FORMAT/ADR,FORMAT/DP,FORMAT/SP,INFO/AD,INFO/ADF,INFO/ADR \
  -f "${Ref_FASTA}" \
  "${repBAM1}" "${repBAM2}" "${repBAM3}" "${repBAM4}" | \
bcftools call --multiallelic-caller --variants-only > out.vcf ;
```


## Annotation

1. Convert gtf to bed file

[Alex Reynolds; 20011](https://www.biostars.org/p/56280/)
```bash
# install
# sudo apt install bedops
convert2bed -i gtf <Drosophila_melanogaster.BDGP6.32.104.chr.EGFP.GAL4.mCD8GFP.gtf> Dme.bed
```
There are some problems for the conversion.
<pre>
Error: Potentially missing gene or transcript ID from GTF attributes (malformed GTF at line [1]?)
</pre>

Here is one of the resolution from [russhh; 2019](https://www.biostars.org/p/56280/) and it works for me.

```bash
cat input.gtf.gz | gunzip - | grep transcript_id | grep gene_id | convert2bed --do-not-sort --input=gtf - > output.bed
```

2. bcftools annotate the vcf file

[SemiQuant, 2015](https://www.biostars.org/p/122690/)
```bash
# install bedtools: sudo apt-get install bedtools
bedtools sort -i Dme.bed > Dme_sort.bed
# install bgzip: sudo apt-get install tabix
bgzip Dme_sort.bed
tabix -p bed Dme_sort.bed.gz
bgzip variants.vcf
tabix -s1 -b2 -e3 variants.vcf.gz
bcftools annotate -a Dme_sort.bed.gz \
  -h Header_file.hdr \
  -c CHROM,FROM,TO,TAG,ID variants.vcf.gz

# or

bcftools annotate \
  -a genes.bed.gz \
  -c CHROM,FROM,TO,GENE \
  -h <(echo '##INFO=<ID=GENE,Number=1,Type=String,Description="Gene name">') \
  variants.vcf.gz
```



## Consequence Annotation By SnpEff

Document: [SnpEff](http://pcingola.github.io/SnpEff/)

Chinese Exampel: [牧羊的男孩儿; 2019](https://zhuanlan.zhihu.com/p/72068778)

install snpeff
```bash
conda install -c bioconda snpeff
```

```bash
tree genomes
```

<pre>
genomes
├── Dme
│   └── genesls genes.gtf
└── genes.fa
</pre>

```bash
echo "data.dir = genomes/" >  snpEff.config
echo "Dme.genome:Dme" >> snpEff.config

java -Xmx4G -jar /home/ken/Soft/snpEff/snpEff/snpEff.jar build -gff3 Dme
```

There some reason
```bash
sed -i  "/^EGFP/d"  genomes/Dme/genes.gtf
sed -i  "/^GAL4/d"  genomes/Dme/genes.gtf
sed -i  "/^mCD8GFP/d"  genomes/Dme/genes.gtf
```



Download prebuild database

```bash
# Eeck the database avalable
java -jar snpEff.jar databases| grep Drosophila_melanogaster
# Failed
```



## test from other blog

```bash
mkdir snpEff
cd snpEff  ###进入snpEff目录下
mkdir data   ###新建data目录
cd data    ####进入data目录下
mkdir genomes  ####新建genomes目录
mkdir ecoli  ###新建ecoli目录


cd genomes
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz
gzip -d GCF_000005845.2_ASM584v2_genomic.fna.gz
mv GCF_000005845.2_ASM584v2_genomic.fna ecoli.fa

cd ../ecoli
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.gff.gz
gzip -d GCF_000005845.2_ASM584v2_genomic.gff.gz
mv GCF_000005845.2_ASM584v2_genomic.gff genes.gff
cd ../../ #回到snpEff目录下


echo "ecoli.genome:ecoli" >> snpEff.config
```



### Mu protocol for Drosophila

```bash
tree data
```

<pre>
data
├── Dme
│   └── genes.gtf
└── genomes
    └── Dme.fa
</pre>

```bash
cd data/Dme
# sudo install gffread
gffread -g ../genomes/Dme.fa -x cds.fa genes.gtf
# Using TransDecoder to translate the cds file into protein sequence
TransDecoder.LongOrfs -t cds.fa
TransDecoder.Predict  -t cds.fa

mkdir dir BioSeq
```

TransDecoder installation: [Karobben; 2020](https://karobben.github.io/2020/07/28/Bioinfor/TransDecoder)


There is an interesting conflicate between two fiels I download. The Protine file is starded by Flybase ID. The cds file is started by Gene Name. But The Database was using Transcript id That rediculase.

```bash
mkdir dir BioSeq
```

```bash
for i in $(grep ">" protein.fa| awk '{print $1}'| sed 's/>//');
  do Name=$(grep -w $i genes.gtf| tr ";" "\n" |grep transcript_id|head -n 1| awk '{print $2}'| sed 's/"//g')
  sed -i 's/>'$i'/>'$Name'/' protein.fa
done


for i in $(grep ">" cds.fa| awk '{print $1}'| sed 's/>//');
  do Name=$(grep -w $i genes.gtf| tr ";" "\n" |grep transcript_id|head -n 1| awk '{print $2}'| sed 's/"//g')
  sed -i 's/>'$i'/>'$Name'/' cds.fa
done
```

```python
GTF=pd.read_csv("genes.gtf", header=2, sep='\t')
GTF_list = list(set(GTF.iloc[:,0].to_list()))

from Bio import SeqIO
Seq1='cds.fa'
Name_l = []
for seq_record in SeqIO.parse(Seq1, "fasta"):
  Anot = []
  try:
    # for we can find the flybase id in gtf file
    Anot = [i for i in GTF_list if seq_record.id in i][0].split(";")
  except:
    # try it in the parent id
    Pat_list = [i for i in seq_record.description.split(";") if "parent=" in i][0].replace(" ",'').replace("parent=", "").split(",")
    for P_id in Pat_list:
      try:
        Anot = [i for i in GTF_list if P_id in i][0].split(";")
      except:
        1 == 1
  Tra_ID = [i for i in Anot if "transcript_id" in i][0].split(" ")[-1].replace('"', "")
  Name_l += [Tra_ID]

```


## Test for samplifed Genom

```bash
sed -i  "/^EGFP/d"  genes.gtf
sed -i  "/^GAL4/d"  genes.gtf
sed -i  "/^mCD8GFP/d"  genes.gtf


# Generate the CDS
gffread -g ../genomes/Dme.fa -x cds.fa genes.gtf
```

```python
from Bio import SeqIO
from Bio.Seq import translate

Seq1='cds.fa'
Name_l = []
for seq_record in SeqIO.parse(Seq1, "fasta"):
  seq_record.seq = translate(seq_record.seq)[:-1]
  Name = seq_record.description.split("FlyBase:")[-1].split(",")[0].split(";")[0]
  Name_l += [Name]
  SeqIO.write(seq_record, "BioSeq/"+Name+".fa", "fasta")
```

It works with lots of stop codon in protein fasta file.


## For Real Genome

```bash
conda create -n snpeff python=3.7
# simplify the gtf
sed -i  "/^EGFP/d"  genes.gtf
sed -i  "/^GAL4/d"  genes.gtf
sed -i  "/^mCD8GFP/d"  genes.gtf
snpEff build -gtf22 Dme

snpEff Dme vcf/test.vcf  > test.ann.vcf
```
