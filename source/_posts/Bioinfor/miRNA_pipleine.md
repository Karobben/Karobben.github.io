---
title: "miRNA pipeline"
description: "miRNA pipeline"
url: mirna_pip
date: "2020/07/28"
toc: true
excerpt: "An standard pipeline for miRNA-Seq data processing. "
tags: [Software, miRNA-Seq, NGS, Protocol]
category: [Biology, Bioinformatics, Protocol, miRNA]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## miRNA pipeline


## 1 fastq dum
fastq-dump *

### reads length distribution
from intetnet  
python scripts
```python
from collections import Counter
Seq_read = "fastp_cut.fq"
output = "fastp.distribution"
with open(Seq_read,'r') as Fileout, open('srg1.r1.paired.results.txt','w') as Filein:
  i = 4
  dic, arr = {}, []
  while True:
    line = Fileout.readline()
    i += 1
    if i%4 == 2:
      arr.append(len(str(line)))
    if not line:
      break
  dic = Counter(arr)

result = ''
for k,v in dic.items():
  result = result +str(k)+"\t"+str(v)+"\n"

fo = open(output, "w")
fo.write(result)
```
R scripts
```R
save_name="fastp.pdf"
table_name = "fastp.distribution"
library(ggplot2)
A <- read.table(table_name)
ggplot(A,aes(x=V1,y=V2)) +geom_bar(stat="identity")
ggsave(save_name)
```


## 2 fastQC
```bash
for i in $(ls *.fastq);do
mkdir QC_$i
~/Biosoft/FastQC/fastqc -o QC_$i -t 7 $i
done

mkdir 2-QC
mv QC* 2-QC/
mkdir 1-reads
mv E* 1-reads/
```
## 3 alignment
```bash
mkdir 3-align
cd 3-align
for i in $(ls ../1-reads/ERR219785*.fastq);do
bowtie2 -p 8 -x /media/ken/Data/CrippsLab/DB_D.melanogaster/Genome -U ../1-reads/$i   -S $i.Genome.sam
done
mv ../1-reads/*.sam .
cd ..

for i in $(ls ERR219785*.fastq);do
bowtie2 -p 8 -x /media/ken/Data/DB/miRNA/hairpin -U $i   -S $i.hairpin.sam
done
mv *.sam 3-align

for i in $(ls ERR219785*.fastq);do
bowtie2 -p 8 -x /media/ken/Data/DB/miRNA/mature -U $i   -S $i.hairpin.sam
done
mv *.sam 3-align
```
### 4 counts
```bash
samtools view  -SF 4 2.sam |perl -alne '{$h{$F[2]}++}END{print "$_\t$h{$_}" foreach sort keys %h }'  > 2-hairpin.counts
```
