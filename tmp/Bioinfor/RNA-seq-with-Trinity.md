---
title: "RNA-seq with Trinity"
description: "RNA-seq with Trinity"
url: trinity_rna_seq
---

# RNA-seq with Trinity


![Nro4d1.png](https://s1.ax1x.com/2020/06/26/Nro4d1.png)

```bash
#### Downloading the RNA-seq
prefetch  --ascp-path "/usr/bin/ascp|/home/ken/.aspera/connect/etc/asperaweb_id_dsa.putty" ERR025599

#### Split SSR to fastq
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files SRR77600*

#### cut the low quality reads
#basic command
#fastp -u 15 -w 8 -i SRR7760055_1.fastq -o cut_SRR7760055_1.fastq
for i in $(ls *.fastq);do  fastp -u 15 -w 8 -i $i -o cut_$i; mv fastp.html $i.html;done

#### Trimmomatic cut the lower grade head or tail jodged by the quality report
java -jar  trimmomatic-0.38.jar SE -threads 8 -phred33 SRR771602.fastq 2.fq ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 HEADCROP:10 CROP:87
for i in $(ls cut_SRR77600*);do
  java -jar  trimmomatic-0.38.jar SE -threads 8 -phred33 $i 2_$i ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 HEADCROP:10 CROP:87
done


#Trnity
Trinity --seqType fq --max_memory 55G --single ../cut_SRR7760072_1.fastq --CPU 8 --full_cleanup
Trinity --seqType fq --max_memory 55G --single 2_cut_SRR7760055_1.fastq --CPU 8 --full_cleanup

for i in $(ls 2_cut_SRR77600*); do
Trinity --seqType fq --max_memory 40G --single $i --CPU 8 --full_cleanup
mv trinity_out_dir.Trinity.fasta $i.fa
done
```

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
