---
title: "Denove Prokaryotic Genome with Spader"
description: "Denove Prokaryotic Genome with Spader"
url: genom_spider
---

# Denove Prokaryotic Genome with Spader


# Data Download
```bash
a paired fastq file:
  ERS011978_pass_1.fastq
  ERS011978_pass_2.fastq
```
# Filter low quality reads
```bash
fastp -u 15 -i ERS011978_pass_1.fastq -I ERS011978_pass_2.fastq -o cut_ERS011978_pass_1.fastq -O cut_ERS011978_pass_2.fastq
```
# cut adapter on the end
```
#java -jar ~/Biosoft/Trimmomatic-0.38/trimmomatic-0.38.jar PE \
-threads 8 -phred33 input_forward.fq.gz input_reverse.fq.gz   \
output_forward_paired.fq.gz output_forward_unpaired.fq.gz     \
output_reverse_paired.fq.gz output_reverse_unpaired.fq.gz     \
ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3       \
SLIDINGWINDOW:4:15 MINLEN:36
```
# cut the adapter tail on the 1.fastq
```bash
java -jar  ~/Biosoft/Trimmomatic-0.38/trimmomatic-0.38.jar SE -threads 8 -phred33 cut_ERS011978_pass_1.fastq cut2_ERS011978_pass_1.fastq CROP:76
mv cut2_ERS011978_pass_1.fastq cut_ERS011978_pass_1.fastq
```

# spade:
```bash
sudo /home/ken/Biosoft/SPAdes-3.12.0-Linux/bin/spades.py -1 fastq/cut_ERS011978_pass_1.fastq -2 fastq/cut_ERS011978_pass_2.fastq -o /home/ken/ComGE/assembly3
```

# state information
```bash
~/Biosoft/bbmap/stats.sh assembly3/scaffolds.fasta
```

# Predicted the genes by prodigal
```bash
prodigal -i scaffolds.fasta -o my.genes -a Protein.fa
```
# Predicted the rRNA by barrnap
```bash
barrnap --quiet scaffolds.fasta
```

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
