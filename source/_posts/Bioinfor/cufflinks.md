---
title: "cufflinks"
description: "cufflinks"
url: cufflinks
date: "2020/07/28"
toc: true
excerpt: "Capt to merger transcripts"
tags: [Software, Bioinformatics, RNA-Seq]
category: [Biology, Bioinformatics, Software, De nove]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## cufflinks

### run cufflinks
the result of tophat is needed
```bash
~/Biosoft/cufflinks-2.2.1.Linux_x86_64/cufflinks -p 8 -b ../tophat/erecta.fna -u -o sample1 ../tophat/tophat_out/accepted_hits.bam
```
### gtf merging
(without fasta.file result)
```bash
cuffmerge -o merged_asm -p 8 -s ../../tophat/erecta.fna list
```

### cuffquant
(For count the reads)
```bash
cuffquant -o cuffquant2 -p 8 -b Genome.fna -u Genome.gff tophat.bam

##Exp:
cuffquant -o cuffquant2 -p 8 -b ../../data/Genome/A.japonicus/Apostichopus_japonicus.fna -u ../../data/Genome/A.japonicus/Apostichopus_japonicus.gff 2dpe/accepted_hits.bam                                      (the result of cuffquant is binary file you can run cuffnorm to transfor this binary file to readable file.)
```

### cuffcompare
for stattistics (useless)
```bash
cuffcompare -o cuffcmp -r genome.gtf -s genome.fasta sample1.gtf

##Exp:
cuffcompare -o cuffcmp2 -r ../../data/Genome/A.japonicus/Apostichopus_japonicus.gff -s ../../data/Genome/A.japonicus/Apostichopus_japonicus.fna cufflinks2/transcripts.gtf
```
### merge the fpkm
```bash
cuffnorm -L 0dpe,3dpe,7dpe,14dpe,21dpe -p 8 ../../data/Genome/A.japonicus/Apostichopus_japonicus.gff cuffquant2/abundances.cxb cuffquant3/abundances.cxb cuffquant4/abundances.cxb cuffquant5/abundances.cxb cuffquant6/abundances.cxb  -o cuffnorm
```

### cuffdiff
 .... similar to the same as the cuffnorm.
```bash
cuffdiff -L A1,B2 -o cuffdiff2 -p 8 -u -b ../../data/Genome/A.japonicus/Apostichopus_japonicus.fna ../../data/Genome/A.japonicus/Apostichopus_japonicus.gff cuffquant2/abundances.cxb cuffquant2/abundances.cxb
```
