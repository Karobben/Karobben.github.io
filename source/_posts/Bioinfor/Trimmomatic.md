---
title: "Trimmomatic"
description: "Trimmomatic"
url: trimmomatic
date: 2020/07/28
toc: true
excerpt: "Trimmomatic is a java tool for cut and filter reads"
tags: [Software, Bioinformatics, RNA-Seq]
category: [Biology, Bioinformatics, Software, Fasta/q]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## Trimmomatic

## Quick start

### Paired End:
```bash
java -jar ~/Biosoft/Trimmomatic-0.38/trimmomatic-0.38.jar PE -threads 8 -phred33 input_forward.fq.gz input_reverse.fq.gz output_forward_paired.fq.gz output_forward_unpaired.fq.gz output_reverse_paired.fq.gz output_reverse_unpaired.fq.gz ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
```

### Single End:
```bash
java -jar  ~/Biosoft/Trimmomatic-0.38/trimmomatic-0.38.jar SE -threads 8 -phred33 SRR771602.fastq 2.fq ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
```

### Args
```bash
HEADCROP:13  #Dorp 13 head base
phred33    设置碱基的质量格式,如果不设置，默认的是-phred64
trimlog file就是产生日志，包括如下部分内容：read的名字，留下来的序列的长度，第一个碱基的起始位置，从开始trimmed的长度，最后的一个碱基位于初始read的位置，最后trimmed的数量，其他步骤产生的日志
LEADING:3   切除首端碱基质量小于3的碱基或者N
TRAILING:3   切除末端碱基质量小于3的碱基或者
ILLUMINACLIP: 1.adapter.lis:2:30:10 1.adapter.list为adapter文件，允许的最大mismatch 数，palindrome模式下匹配碱基数阈值：simple模式下的匹配碱基数阈值
SLIDINGWINDOW:4:15  Windows的size是4个碱基，其平均碱基质量小于15，则切除
MINLEN:36  最低reads长度为36
CROP:  保留的reads长度
HEADCROP: 在reads的首端切除指定的长度
```
