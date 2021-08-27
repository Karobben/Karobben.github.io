---
title: "sratools"
description: "sratools"
url: sratools
date: 2020/07/28
toc: true
excerpt: "sratools for manage SRA Files"
tags: [Software, Bioinformatics, MateGenome]
category: [Biology, Bioinformatics, Software, Download]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## sratools

## SRA data download
```bash
prefetch  --ascp-path "/usr/bin/ascp|/home/ken/.aspera/connect/etc/asperaweb_id_dsa.putty" ERR025599
```
## For trinity
```bash
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files file.sra

Trinity --seqType fq --max_memory 55G --single Seq.fastq --CPU 8 --full_cleanup
```
