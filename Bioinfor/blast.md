---
url: blast
---

# Blast+


[latest release](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)


# Installation
For Ubuntu or Debian (Deepin, like me)
```bash
sudo apt-get install ncbi-blast+
```

# Quick Start

## make blast base
```bash
makeblastdb -in db.fasta -dbtype prot/nucl -parse_seqids -out dbname
```

## model of uniprot annotation
```bash
blastx -query T0.05.fa -out blast.out -db /media/ken/Base/blastdb/uniprot_sprot.fasta -outfmt "6 qacc sacc evalue stitle sblastname" -evalue 1e-5 -max_target_seqs 1 -num_threads 8 -max_hsps 1
```

# Output format
```bash
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
```
---  
[Github](https://github.com/Karobben)  
[Blog](http://Karobben.github.io)  
[Bilibili](https://space.bilibili.com/393056819)  
[R 语言画图索引](https://karobben.github.io/R/R-index.html)
