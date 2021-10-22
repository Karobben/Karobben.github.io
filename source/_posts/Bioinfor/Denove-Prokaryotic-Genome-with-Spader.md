---
title: "Denove Prokaryotic Genome with Spader"
description: "Denove Prokaryotic Genome with Spader"
url: genom_spider
date: "2020/07/28"
toc: true
excerpt: "Denove Prokaryotic Genome with Spader"
tags: [Software, Genome, Protocol]
category: [Biology, Bioinformatics, Protocol, Genome]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## Denove Prokaryotic Genome with Spader


## Data Download
```bash
a paired fastq file:
  ERS011978_pass_1.fastq
  ERS011978_pass_2.fastq
```
## Filter low quality reads
```bash
fastp -u 15 -i ERS011978_pass_1.fastq -I ERS011978_pass_2.fastq -o cut_ERS011978_pass_1.fastq -O cut_ERS011978_pass_2.fastq
```
## cut adapter on the end
```
##java -jar ~/Biosoft/Trimmomatic-0.38/trimmomatic-0.38.jar PE \
-threads 8 -phred33 input_forward.fq.gz input_reverse.fq.gz   \
output_forward_paired.fq.gz output_forward_unpaired.fq.gz     \
output_reverse_paired.fq.gz output_reverse_unpaired.fq.gz     \
ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3       \
SLIDINGWINDOW:4:15 MINLEN:36
```

## Quick Through

### cut the adapter tail on the 1.fastq
```bash
java -jar  ~/Biosoft/Trimmomatic-0.38/trimmomatic-0.38.jar SE -threads 8 -phred33 cut_ERS011978_pass_1.fastq cut2_ERS011978_pass_1.fastq CROP:76
mv cut2_ERS011978_pass_1.fastq cut_ERS011978_pass_1.fastq
```

### spade:
```bash
sudo /home/ken/Biosoft/SPAdes-3.12.0-Linux/bin/spades.py -1 fastq/cut_ERS011978_pass_1.fastq -2 fastq/cut_ERS011978_pass_2.fastq -o /home/ken/ComGE/assembly3
```

### state information
```bash
~/Biosoft/bbmap/stats.sh assembly3/scaffolds.fasta
```

### Predicted the genes by prodigal
```bash
prodigal -i scaffolds.fasta -o my.genes -a Protein.fa
```
### Predicted the rRNA by barrnap
```bash
barrnap --quiet scaffolds.fasta
```




## Other Pipeline

[Whole genome assembly workshop; © cornell EDU; 2019](https://biohpc.cornell.edu/doc/assembly_2019_exercise.pdf)

```bash
# Prepare
mkdir /workdir/$USER
cd /workdir/$USER
cp /shared_data/assembly_workshop_2019/*fastq.gz ./

# Trim
java -jar /programs/trimmomatic/trimmomatic-0.39.jar PE -phred33
SRR1982238_1.fastq.gz SRR1982238_2.fastq.gz r1.fastq.gz u1.fastq.gz r2.fastq.gz
u2.fastq.gz ILLUMINACLIP:/programs/trimmomatic/adapters/TruSeq3-PE-2.fa:2:30:10
LEADING:10 TRAILING:10 SLIDINGWINDOW:4:15 MINLEN:150

# assembly
export OMP_NUM_THREADS=6
/programs/spades/bin/spades.py -t 6 --careful --s1 u1.fastq.gz --pe1-1
r1.fastq.gz  --pe1-2 r2.fastq.gz -o spades_run

# Assessment
cp -r /shared_data/assembly_workshop_2019/spades_results ./
cd spades_results
grep "=====" spades.log
grep "genome size" spades.log
/programs/quast-5.0.2/quast.py contigs.fasta
/programs/quast-5.0.2/quast.py scaffolds.fasta
tail quast_results/*/report.txt
# Evaluate
wget https://busco.ezlab.org/datasets/bacillales_odb9.tar.gz
tar xvfz bacillales_odb9.tar.gz
cp /programs/busco-3.1.0/config/config.ini /workdir/$USER/
cp -r /programs/Augustus-3.3.2/config /workdir/$USER/
export AUGUSTUS_CONFIG_PATH=/workdir/$USER/config
export BUSCO_CONFIG_FILE=/workdir/$USER/config.ini

export PYTHONPATH=/programs/busco-3.1.0/lib/python3.6/site-packages
export PATH=/programs/busco-3.1.0/scripts:/programs/Augustus-
3.3.2/bin:/programs/Augustus-3.3.2/scripts:$PATH
run_BUSCO.py --in ./contigs.fasta --lineage_path ./bacillales_odb9 --mode genome
--out busco_bacillales --cpu 8
cat run_busco_bacillales/short_summary_busco_bacillales.txt

# Assemble PacBio
cd /workdir/$USER
cp /shared_data/assembly_workshop_2019/SRR10405213.fastq.gz ./
/programs/canu-1.8/Linux-amd64/bin/canu  useGrid=false maxThreads=8
maxMemory=24g -p ecoli -d /workdir/$USER/ecoli genomeSize=4.6m  -pacbio-raw
SRR10405213.fastq.gz
cp -r /shared_data/assembly_workshop_2019/ecoli/ ./
programs/minimap2-2.17/minimap2 -a ecoli/ecoli.contigs.fasta  
SRR10405213.fastq.gz | samtools view -b - > ecoli.bam
samtools sort -@ 6  -m 5G -T ./ -o ecoli.sorted.bam ecoli.bam
samtools index ecoli.sorted.bam
java -jar /programs/pilon-1.23/pilon-1.23.jar --genome ecoli/ecoli.contigs.fasta
--pacbio  ecoli.sorted.bam --output ecoli.pilon
```
