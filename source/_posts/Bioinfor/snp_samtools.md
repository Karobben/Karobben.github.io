---
title: "SNP Calling: samtools"
description: "SNP Calling: samtools"
url: snp_samtools
date: "2020/07/28"
toc: true
excerpt: "SNP Calling: samtools"
tags: [Software, SNP, Bioinformatics]
category: [Biology, Bioinformatics, Protocol, SNP]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## SNP Calling: samtools


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
