---
toc: true
url: BSgenome
covercopy: © Karobben
priority: 10000
date: 2022-07-23 14:53:41
title: "Build BSgenome by youself"
ytitle: "创建一个 BSgenome"
description: "Build BSgenome by youself in OS environment"
excerpt: "Build BSgenome by youself in OS environment"
tags: [R, Bioinformatic]
category: [R, Bio]
cover: "https://opengraph.githubassets.com/29fa5a85e707b696f7e0b31cc2d5ba825d24e4ede70215ee41130905b184fd45/Bioconductor/BSgenome"
thumbnail: "https://opengraph.githubassets.com/29fa5a85e707b696f7e0b31cc2d5ba825d24e4ede70215ee41130905b184fd45/Bioconductor/BSgenome"
---

## Build a BSgenome by youself

Reference: [Tom Guest](https://tomguest.netlify.app/tutorial/bsgenome/)


In this tutorial, I'll show how to create a BSgenome library with Linux commands. The main steps for doing this are to prepare the fasta files and the configure files.

## Preparing the sequence files and configuring file
We'd like to store each chromosome into an independent file and record them in a configuring file so the BSgenome can find them. Here I use `awk` to remove useless information in the name and `seqkit` to extract seqs.
Prepare: `Genome.fa` and `seqkit`
`conda install -c bioconda seqkit`
```bash
mkdir BSgenome # make a new directory
cd BSgenome    # Enter the directory
awk '{print $1}' ../Genome.fa > sample.fa   # samplify the name of each sequence
grep ">" sample.fa | sed 's/>//'> list.txt               # Get the name sequences

for i in $(cat list.txt)
do echo -e $i"\n"$i"\n"$i"\n"$i"\n" > tmp
    seqkit grep -n -f tmp  sample.fa > $i.fa
done

rm sample.fa  list.txt tmp

echo 'Package: BSgenome.dme.BDGP6.32
Title: Full genome sequence
Description: Full genome sequence
Version: 1.0.0
organism: drosophila melanogaster
common_name: fruit fly
provider: BDGP
provider_version: 6.32
release_date: ?
release_name: ?
source_url: ?
organism_biocview: ?
BSgenomeObjname: dme
seqnames: c("2L", "2R", "3L", "3R", "4", "EGFP", "GAL4", "mCD8GFP", "mitochondrion_genome", "test", "X", "Y")
seqs_srcdir: /media/ken/BackUP/Drosophila/BSgenome
' > BSgenome.dme.BDGP6.32-seed
```


R
```r
library(BSgenome)
forgeBSgenomeDataPkg("BSgenome.dme.BDGP6.32-seed")
```
If everything is right, you would see the codes below and a directory `BSgenome.dme.BDGP6.32` was created. Now, we need to package it and install it.

<pre>
Creating package in ./BSgenome.dme.BDGP6.32
Loading '2L' sequence from FASTA file '/media/ken/BackUP/Drosophila/BSgenome/2L.fa' ... DONE
Loading '2R' sequence from FASTA file '/media/ken/BackUP/Drosophila/BSgenome/2R.fa' ... DONE
Loading '3L' sequence from FASTA file '/media/ken/BackUP/Drosophila/BSgenome/3L.fa' ... DONE
Loading '3R' sequence from FASTA file '/media/ken/BackUP/Drosophila/BSgenome/3R.fa' ... DONE
Loading '4' sequence from FASTA file '/media/ken/BackUP/Drosophila/BSgenome/4.fa' ... DONE
Loading 'EGFP' sequence from FASTA file '/media/ken/BackUP/Drosophila/BSgenome/EGFP.fa' ... DONE
Loading 'GAL4' sequence from FASTA file '/media/ken/BackUP/Drosophila/BSgenome/GAL4.fa' ... DONE
Loading 'mCD8GFP' sequence from FASTA file '/media/ken/BackUP/Drosophila/BSgenome/mCD8GFP.fa' ... DONE
Loading 'mitochondrion_genome' sequence from FASTA file '/media/ken/BackUP/Drosophila/BSgenome/mitochondrion_genome.fa' ... DONE
Loading 'test' sequence from FASTA file '/media/ken/BackUP/Drosophila/BSgenome/test.fa' ... DONE
Loading 'X' sequence from FASTA file '/media/ken/BackUP/Drosophila/BSgenome/X.fa' ... DONE
Loading 'Y' sequence from FASTA file '/media/ken/BackUP/Drosophila/BSgenome/Y.fa' ... DONE
Writing all sequences to './BSgenome.dme.BDGP6.32/inst/extdata/single_sequences.2bit' ... DONE
</pre>


```bash
R CMD build BSgenome.dme.BDGP6.32
R CMD INSTALL BSgenome.dme.BDGP6.32_1.0.0.tar.gz
```

Now, you can load your Genome
