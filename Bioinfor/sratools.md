---
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
[Github](https://github.com/Karobben)  
[Blog](http://Karobben.github.io)  
[Bilibili](https://space.bilibili.com/393056819)  
[R 语言画图索引](https://karobben.github.io/R/R-index.html)
