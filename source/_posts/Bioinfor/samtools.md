---
title: "samtools"
description: "samtools"
url: samtools
date: 2020/07/28
toc: true
excerpt: "Samtools"
tags: [Software, Bioinformatics, RNA-Seq]
category: [Biology, Bioinformatics, Software, Sam]
cover: 'https://s1.ax1x.com/2020/06/26/Nro4d1.png'
thumbnail: 'https://s1.ax1x.com/2020/06/26/Nro4d1.png'
priority: 10000
---

## samtools

- [x] s

<style>
span
    .tag {
      background-color:#38393d;
      color: #5fd381;
    }
</style>

## Quick start
```bash
samtools tview sorted.bam Trinity.fasta   -p "ID:35" -d T > result

samtools tview sorted.bam ../../2-Trinity/Trinity.fasta   -p "comp0_c0_seq1:35" -d H > 123.html
```
```
*.bam file *.fasta file  -p  posation, fasta name and star posation of the fasta :
```

## Install

```bash
wget -c https://github.com/samtools/samtools/releases/download/1.12/samtools-1.12.tar.bz2
tar -xjf samtools-1.12.tar.bz2
cd samtools-1.12
ls
./configure
make & make install
```

### Install through conda

```bash
conda install sra-tools
```

## Sorting by bam files
```bash
samtools sort bwa.bam -o bwa.sorted.bam > bwa.sorted.bam
```

## Index
```bash
samtools faidx genome.fna
```


## Depth count

```bash
samtools depth -r 2R:24687896-24687900 out.bam
```
<pre>
2R	24687896	41
2R	24687897	41
2R	24687898	41
2R	24687899	41
2R	24687900	41
</pre>

## Reads counts in bam


```bash
# counting all reads
samtools view -c SAMPLE.bam
# or
samtools view SAMPLE.bam |wc
# counting only mapped reads
samtools view -c -F 260 SAMPLE.bam
```

Time cousts for `-c` and `wc`
| `-c` | `|wc -l`     |
| :--: | :--: |
| 0m16.497s     |   0m44.720s     |
