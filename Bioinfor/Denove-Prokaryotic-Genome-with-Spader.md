---
url: wwgswq
---

# Denove Prokaryotic Genome with Spader


```bash
a paired fastq file:
  ERS011978_pass_1.fastq
  ERS011978_pass_2.fastq

#fileter low quality reads
fastp -u 15 -i ERS011978_pass_1.fastq -I ERS011978_pass_2.fastq -o cut_ERS011978_pass_1.fastq -O cut_ERS011978_pass_2.fastq

#cut adapter on the end
#java -jar ~/Biosoft/Trimmomatic-0.38/trimmomatic-0.38.jar PE -threads 8 -phred33 input_forward.fq.gz input_reverse.fq.gz output_forward_paired.fq.gz output_forward_unpaired.fq.gz output_reverse_paired.fq.gz output_reverse_unpaired.fq.gz ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
####cut the adapter tail on the 1.fastq
java -jar  ~/Biosoft/Trimmomatic-0.38/trimmomatic-0.38.jar SE -threads 8 -phred33 cut_ERS011978_pass_1.fastq cut2_ERS011978_pass_1.fastq CROP:76
mv cut2_ERS011978_pass_1.fastq cut_ERS011978_pass_1.fastq

spade:
sudo /home/ken/Biosoft/SPAdes-3.12.0-Linux/bin/spades.py -1 fastq/cut_ERS011978_pass_1.fastq -2 fastq/cut_ERS011978_pass_2.fastq -o /home/ken/ComGE/assembly3

#state information
~/Biosoft/bbmap/stats.sh assembly3/scaffolds.fasta

#### Predicted the genes by prodigal
prodigal -i scaffolds.fasta -o my.genes -a Protein.fa

#### Predicted the rRNA by barrnap
barrnap --quiet scaffolds.fasta

```

