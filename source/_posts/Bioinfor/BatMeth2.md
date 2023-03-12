---
title: "BatMeth2"
description: "BatMeth2| DNA Methylation Sequencing analysis"
url: "batmeth2"
date: "2020/07/28"
toc: true
excerpt: "An Integrated Package for Bisulfite DNA Methylation Data Analysis with Indel-sensitive Mapping."
tags: [Software, Bioinformatics, NGS]
category: [Biology, Bioinformatics, Software, Dna Methylation]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---


## BatMeth2

Citation: Zhou Q, Lim J-Q, Sung W-K, Li G: An integrated package for bisulfite DNA methylation data analysis with Indel-sensitive mapping. BMC Bioinformatics 2019, 20:47.

More information is in [Github](https://github.com/GuoliangLi-HZAU/BatMeth2), [中文](https://www.dna-asmdb.com/tools/batmeth2-tutorial/batmeth2.html)

<span style='background:salmon'>I just tried the pipeline but I don't know exactly how those all work. Maybe I'll update this later</span>

## Install

**Requirement**
1. gcc (v4.8) , gsl library, zlib
2. R (ggplot2, pheatmap, xtable)
3. samtools (suggest: v1.3.1)
4. fastp, raw reads as input need

```bash
## gsl install: sudo apt-get install libgsl0ldbl libgsl0-dev
./configure
make
make copy
```

### Example Data
You can download the test data on [here](https://drive.google.com/open?id=1SEpvJbkjwndYcpkd39T11lrBytEq_MaC)

It contain files:
- input fastq.gz (paired end)
- genome file
- usage code and details
- gene annotation file

## BUILDING INDEX

```bash
mkdir batmeth2index
cd batmeth2index
BatMeth2 build_index GENOME.fa # WGBS Data set
BatMeth2 build_index rrbs GENOME.fa # RRBS Data set
cd ../
```

## Pipline



---

### Quick pipeline
`BatMeth2 pipel --aligner=no -1 R1.fq.gz -2 R2.fq.gz -g ./batmeth2index/genome.fa -o meth -p 6 --gff ./gene.gff -f 1
`

### Step by Step
```bash
mkdir batmeth2index
cd batmeth2index
BatMeth2 build_index genome.fa # WGBS Data set
cd ../

BatMeth2 align -g ./batmeth2index/genome.fa -i R1.fq.gz -i R2.fq.gz -p 6 -o meth.sam

## Caculate DNA methylation level
BatMeth2 calmeth -g ./batmeth2index/genome.fa -i meth.sam -m meth

## DNA methylation level distribution on gene/TE etc
BatMeth2 annoation -o meth -G ./batmeth2index/genome.fa -gff ./gene.gff -m meth.methratio.txt -B -P --TSS --TTS --GENE

## DNA methylation differential analysis example
BatMeth2 batDMR -g ./batmeth2index/genome.fa -o_dm DM.txt -1 meth_loci.CG.txt -2 mutant_loci.CG.txt -L


```

### Visualization
```bash
BatMeth2 methyPlot meth.methBins.txt meth.Methygenome.pdf 0.025 meth.Methylevel.1.txt meth.function.pdf TSS TTS meth.AverMethylevel.1.txt meth.Methenrich.pdf meth.annoDensity.1.txt meth.density.pdf meth meth.mCdensity.txt meth.mCdensity.pdf  meth.mCcatero.txt jcmeth.mCcatero.pdf 0.6 0.1 0.1
```
