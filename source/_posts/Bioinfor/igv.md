---
title: "IGV"
description: "IGV"
url: igv
date: 2020/07/28
toc: true
excerpt: "IGV, and free reads map visualization"
tags: [Software, Bioinformatics]
category: [Biology, Bioinformatics, Software, Visualization]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>

## IGV

## Dowload

https://software.broadinstitute.org/software/igv/download

open:
```bash
bash igv.sh
```

## build index
```bash
bowtie2-build --threads 8 genome.fa genome.fa
```
## build sam file

```bash
bowtie2 -p 8 -q --no-unal -k 20 -x genome.fa -U reads.fq   -S  bowtie2.sam
bowtie2 -p 8 -q --no-unal -k 20 -x genome.fa -1 reads_1.fq -2 reads_2.fq  -S  bowtie2.sam

##Exp:
bowtie2 -p 8 -q --no-unal -k 20 -x Trinity.fasta -U SRR771602.fastq   -S  bowtie2.sam
```
### sam to bam
```bash
samtools view -b -S bowtie2.sam > bowtie2.bam
samtools sort bowtie2.bam -o bowtie2.coordSorted.bam > bowtie2.coordSorted.bam
samtools index bowtie2.coordSorted.bam
samtools faidx Trinity.fasta
```

## IGV

```bash
~/Biosoft/IGV_2.4.10/igv.sh -g Trinity.fasta bowtie2.coordSorted.bam
```
