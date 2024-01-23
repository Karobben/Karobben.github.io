---
title: "Blast+"
description: "Blast+"
url: blast
date: "2020/07/28"
toc: true
excerpt: "The Basic Local Alignment Search Tool (BLAST) finds regions of local similarity between sequences. The program compares nucleotide or protein sequences to sequence databases and calculates the statistical significance of matches. BLAST can be used to infer functional and evolutionary relationships between sequences as well as help identify members of gene families."
tags: [Software, Database, Align]
category: [Biology, Bioinformatics, Software, Align]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## Blast+


[latest release](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)


## Installation
For Ubuntu or Debian (Deepin, like me)
```bash
sudo apt-get install ncbi-blast+
```

For other distributions:
```bash
wget -c https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.12.0+-x64-linux.tar.gz
tar -zxvf ncbi-blast-2.12.0+-x64-linux.tar.gz
cd ncbi-blast-2.12.0+/bin
```

## Quick Start

### make blast base
```bash
makeblastdb -in db.fasta -dbtype prot/nucl -parse_seqids -out dbname
```

### model of uniprot annotation
```bash
blastx -query T0.05.fa -out blast.out -db /media/ken/Base/blastdb/uniprot_sprot.fasta -outfmt "6 qacc sacc evalue pident qcovs" -evalue 1e-5 -max_target_seqs 1 -num_threads 8 -max_hsps 1
```

Output explanation for "6 qacc sacc evalue pident qcovs":
- "qacc": Query ID
- "sacc": Subject ID
- "evalue": Evalue
- "pident": Identity (Percentage)
- "qcovs": Query coverage

## Different Commands

- `BLASTP`: For comparing Protein sequences to Protein databases.
- `BLASTN`: For comparing Nucleotide sequences to Nucleotide databases.
- `BLASTX`: For comparing a Nucleotide query sequence translated in all reading frames to a Protein database.
- `TBLASTN`: For comparing a Protein sequence to a Nucleotide database that is translated in all reading frames.
- `TBLASTX`: For comparing the six-frame translations of a Nucleotide query sequence against the six-frame translations of a Nucleotide database.

## Output format

<pre>
Options 6, 7 and 10 can be additionally configured to produce
a custom format specified by space delimited format specifiers.
The supported format specifiers are:
     qseqid means Query Seq-id
        qgi means Query GI
       qacc means Query accesion
    qaccver means Query accesion.version
       qlen means Query sequence length
     sseqid means Subject Seq-id
  sallseqid means All subject Seq-id(s), separated by a ';'
        sgi means Subject GI
     sallgi means All subject GIs
       sacc means Subject accession
    saccver means Subject accession.version
    sallacc means All subject accessions
       slen means Subject sequence length
     qstart means Start of alignment in query
       qend means End of alignment in query
     sstart means Start of alignment in subject
       send means End of alignment in subject
       qseq means Aligned part of query sequence
       sseq means Aligned part of subjecnit sequence
     evalue means Expect value
   bitscore means Bit score
      score means Raw score
     length means Alignment length
     pident means Percentage of identical matches
     nident means Number of identical matches
   mismatch means Number of mismatches
   positive means Number of positive-scoring matches
    gapopen means Number of gap openings
       gaps means Total number of gaps
       ppos means Percentage of positive-scoring matches
     frames means Query and subject frames separated by a '/'
     qframe means Query frame
     sframe means Subject frame
       btop means Blast traceback operations (BTOP)
     staxid means Subject Taxonomy ID
   ssciname means Subject Scientific Name
   scomname means Subject Common Name
 sblastname means Subject Blast Name
  sskingdom means Subject Super Kingdom
    staxids means unique Subject Taxonomy ID(s), separated by a ';'
      (in numerical order)
  sscinames means unique Subject Scientific Name(s), separated by a ';'
  scomnames means unique Subject Common Name(s), separated by a ';'
 sblastnames means unique Subject Blast Name(s), separated by a ';'
      (in alphabetical order)
 sskingdoms means unique Subject Super Kingdom(s), separated by a ';'
      (in alphabetical order)
     stitle means Subject Title
 salltitles means All Subject Title(s), separated by a '<>'
    sstrand means Subject Strand
      qcovs means Query Coverage Per Subject
    qcovhsp means Query Coverage Per HSP
     qcovus means Query Coverage Per Unique Subject (blastn only)
</pre>


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
