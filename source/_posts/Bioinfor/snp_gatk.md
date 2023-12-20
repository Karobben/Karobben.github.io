---
title: "SNP Calling: GATK"
description: "SNP Calling: GATK"
url: snp_gatk
date: "2020/07/28"
toc: true
excerpt: "Denove Prokaryotic Genome with Spader"
tags: [Software, SNP, Protocol, GATK, NGS, Bioinformatics]
category: [Biology, Bioinformatics, Protocol, SNP]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## SNP Calling: GATK


### 1. build bwa index
```bash
bwa index genome.fna
##Exp:
bwa index Apostichopus_japonicus.fna
```
### 2. reads Mapping
```bash
bwa mem -t 4 -R '@RG\tID:foo\tPL:illumina\tSM:E.coli_K12' genome.fna reada_1.fq reads_2.fq | samtools view -Sb - > bwa.bam

##Exp:
bwa mem -t 4 -R '@RG\tID:foo\tPL:illumina\tSM:E.coli_K12' Apostichopus_japonicus.fna SRR771602.fastq | samtools view -Sb - > AJ.bam
```

### 3. sort by samtools
```bash
samtools sort bwa.bam -o bwa.sorted.bam > bwa.sorted.bam
samtools faidx genome.fna

##Exp:
samtools sort AJ.bam -o AJ.sorted.bam > AJ.sorted.bam
##Exp:
samtools faidx Apostichopus_japonicus.fna
```

### 4. Maker PCR repeats
```bash
gatk MarkDuplicates -I bwa.sorted.bam -O bwa.sorted.markdup.bam   -M bwa.sorted.markdup_metrics.txt

##Exp:
gatk MarkDuplicates -I AJ.sorted.bam -O AJ.sorted.markdup.bam   -M AJ.sorted.markdup_metrics.txt

samtools index bwa.sorted.markdup.bam
```

### 5. Prepare a dict file
```bash
gatk CreateSequenceDictionary -R genome.fna -O genome.dict

##Exp:
gatk CreateSequenceDictionary -R Apostichopus_japonicus.fna -O Apostichopus_japonicus.dict
```

### 6. Build intermidia file, gvcf file
```bash
gatk HaplotypeCaller -R genome.fna --emit-ref-confidence GVCF -I bwa.sorted.markdup.bam -O  bwa.g.vcf

##Exp:
gatk HaplotypeCaller -R Apostichopus_japonicus.fna --emit-ref-confidence GVCF -I AJ.sorted.markdup.bam -O  AJ.g.vcf
```

### 7. Finally
```bash
gatk GenotypeGVCFs -R genome.fna -V bwa.g.vcf -O bwa.vcf

##Exp:
gatk GenotypeGVCFs -R Apostichopus_japonicus.fna -V AJ.g.vcf -O AJ.vcf
```

Another Example:

[炎季宏, 2018](https://y570pc.github.io/%E5%9F%BA%E4%BA%8EGATK%E6%A3%80%E6%B5%8B%E5%9F%BA%E5%9B%A0%E7%BB%84SNP%E5%92%8Cindel/)
