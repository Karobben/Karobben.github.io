---
title: "SNP Calling: samtools"
description: "SNP Calling: samtools"
url: snp_samtools
---

# SNP Calling: samtools


# 1. sort by samtools
```bash
samtools sort bwa.bam -o bwa.sorted.bam > bwa.sorted.bam
samtools faidx genome.fna

#Exp:
samtools sort AJ.bam -o AJ.sorted.bam > AJ.sorted.bam
#Exp:
samtools faidx Apostichopus_japonicus.fna
```

## 2. SNP calling
```bash
samtools mpileup -guSDf genome.fasta abc.bam | bcftools view -cvNg - > abc.vcf
```

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
