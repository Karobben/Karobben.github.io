---
toc: true
url: annotation
covercopy: <a href="https://www.cshlpress.com/">© cshlpress.com</a>
priority: 10000
date: 2021-07-21 16:05:37
title: "RNA-Seq, Annotation and Enrichment"
ytitle: "RNA-Seq, 注释和富集"
description: "RNA-Seq annotation, GO, KEGG"
excerpt: "RNA-Seq annotation, GO, KEGG"
tags: [Biology, Bioinformatics, Protocol, NGS]
category: [Biology, Bioinformatics, Protocol, Annotation]
cover: "https://www.cshlpress.com/productgraphics/big/RNAManual_f.jpg"
thumbnail: "https://www.cshlpress.com/productgraphics/big/RNAManual_f.jpg"
---

## Swiss-Prot Annotation

### prerequisite

**Prepare Softwares**
downloads latest [blast+](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)
```bash
wget -c https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.12.0+-x64-linux.tar.gz
tar -zxvf ncbi-blast-2.12.0+-x64-linux.tar.gz
cd ncbi-blast-2.12.0+/bin
```


**Prepare Database**
Download the latest version from [Uniport](https://www.uniprot.org/downloads)

for example, we'd like to download the reviewed database:
```bash
wget -c https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
gzip -d uniprot_sprot.fasta.gz
du -h uniprot_sprot.fasta
```

<pre>268M	uniprot_sprot.fasta</pre>

```bash
~/Bio/blast/ncbi-blast-2.12.0+/bin/makeblastdb -in uniprot_sprot.fasta  -dbtype prot -parse_seqids -out Swiss
ls
```
<pre>
Swiss.pdb  Swiss.pin  Swiss.pos  Swiss.psq  Swiss.pto
Swiss.phr  Swiss.pog  Swiss.pot  Swiss.ptf  uniprot_sprot.fasta
</pre>

### Blast
```bash
mkdir Annotation
cd Annotation
blastx -query ../trinity_out_dir.Trinity.fasta -out blast.out -db /run/media/ken/BackUP/blastdb/Swiss -outfmt "6 qacc sacc evalue stitle sblastname" -evalue 1e-5 -max_target_seqs 1 -num_threads 8 -max_hsps 1

head blast.out
```
|qacc|sacc|evalue|stitle|sblastname|
|:-|:-|:-|:-|:-|
TRINITY_DN1_c0_g1_i1|P31792|4.12e-31|Pol polyprotein (Fragment) OS=Feline endogenous virus ECE1 OX=11766 GN=pol PE=3 SV=1|N/A
TRINITY_DN10_c0_g1_i1|P63088|3.52e-16|Serine/threonine-protein phosphatase PP1-gamma catalytic subunit OS=Rattus norvegicus OX=10116 GN=Ppp1cc PE=1 SV=1|N/A
TRINITY_DN12_c0_g1_i1|Q61092|0.0|Laminin subunit gamma-2 OS=Mus musculus OX=10090 GN=Lamc2 PE=1 SV=2|N/A
TRINITY_DN13_c0_g1_i1|P09405|1.17e-14|Nucleolin OS=Mus musculus OX=10090 GN=Ncl


## Module Species

For example, this group of transcripts is belongs to Mus musculus (house mouse), we can find well annotated protein from [NCBI Genome](https://www.ncbi.nlm.nih.gov/genome/?term=txid10090[orgn])

We can using this from NCBI ([Link](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/635/GCF_000001635.27_GRCm39/GCF_000001635.27_GRCm39_protein.faa.gz))

```bash
gzip -d GCF_000001635.27_GRCm39_protein.faa.gz
~/Bio/blast/ncbi-blast-2.12.0+/bin/makeblastdb -in GCF_000001635.27_GRCm39_protein.faa  -dbtype prot -parse_seqids -out Mus_musculus

~/Bio/blast/ncbi-blast-2.12.0+/bin/blastx -query ../trinity_out_dir.Trinity.fasta -out blast.out_Mus -db /run/media/ken/BackUP/blastdb/Swiss -outfmt "6 qacc sacc evalue stitle sblastname" -evalue 1e-5 -max_target_seqs 1 -num_threads 8 -max_hsps 1

```



```r
TB <- read.table("G5M_S45_Unmap/RSEM.isoforms.results", header = T)
TB2 <- TB[TB$expected_count>0,]
TB2 <- TB2[TB2$length >= 200,]
TB2 <- TB2[order(TB2$FPKM),]
TB2 <- TB2[TB2$expected_count>100,]
write.table(TB2$transcript_id, "tmp.id", row.names = F, col.names = F, quote = F)
```
```bash
for i in $(cat tmp.id); do echo $i $(samtools depth G50-FE_TUMOR-a_S37_Unmap/sorted.bam -r $i|wc -l ); done > tmp.cs
```
```r
Len_TB <- read.table("tmp.csv")
TB2$T_len <- Len_TB$V2[match(TB2$transcript_id, Len_TB$V1)]
TB3 <- TB2[TB2$T_len / TB2$length > 0.7,]
paste(TB3$transcript_id[grep("_i1$", TB3$transcript_id)], collapse =   "|")










```
























---
