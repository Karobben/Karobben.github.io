---
title: "Tophat"
description: "Tophat"
url: tophat
---

# Tophat


# build a index
```bash
bowtie2-build seaGenome.fna seaGenome.fna
```

#run tophat2
```bash
tophat2 -p 8 -i 20 -I 4000 --min-segment-intron 20 --max-segment-intron 4000 --min-coverage-intron 20 --max-coverage-intron 4000 --coverage-search --microexon-search -G Apostichopus_japonicus.gff --library-type fr-firststrand seaGenome.fna SRR771602.fastq

~/Biosoft/cufflinks-2.2.1.Linux_x86_64/cufflinks -p 8 -b ../tophat/erecta.fna -u -o sample1 ../tophat/tophat_out/accepted_hits.bam
```

# merge the transcripts.gtf
```bash
cuffmerge -o merged_asm -p 8 -s ../../tophat/erecta.fna list
```

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
