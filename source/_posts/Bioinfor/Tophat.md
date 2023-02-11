---
title: "Tophat"
description: "Tophat"
url: tophat
date: 2020/07/28
toc: true
excerpt: "Tophat"
tags: [Software, Bioinformatics, RNA-Seq]
category: [Biology, Bioinformatics, Software, De nove]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## Tophat


## build a index
```bash
bowtie2-build seaGenome.fna seaGenome.fna
```

##run tophat2
```bash
tophat2 -p 8 -i 20 -I 4000 --min-segment-intron 20 --max-segment-intron 4000 --min-coverage-intron 20 --max-coverage-intron 4000 --coverage-search --microexon-search -G Apostichopus_japonicus.gff --library-type fr-firststrand seaGenome.fna SRR771602.fastq

~/Biosoft/cufflinks-2.2.1.Linux_x86_64/cufflinks -p 8 -b ../tophat/erecta.fna -u -o sample1 ../tophat/tophat_out/accepted_hits.bam
```

## merge the transcripts.gtf
```bash
cuffmerge -o merged_asm -p 8 -s ../../tophat/erecta.fna list
```
