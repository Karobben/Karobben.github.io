---
title: "sratools"
description: "sratools"
url: sratools
---

# sratools

# SRA data download
```bash
prefetch  --ascp-path "/usr/bin/ascp|/home/ken/.aspera/connect/etc/asperaweb_id_dsa.putty" ERR025599
```
# For trinity
```bash
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files file.sra

Trinity --seqType fq --max_memory 55G --single Seq.fastq --CPU 8 --full_cleanup
```

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
