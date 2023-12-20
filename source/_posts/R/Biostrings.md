---
title: "Biostrings"
url: biostrings2
date: 2020/05/01
excerpt: "R library for fasta sequences handling."
toc: true
tags: [R, Bioinformatics, NGS, Fasta]
category: [R, Bio, Fasta]
cover: 'https://imgur.com/JsTmbyM.png'
thumbnail: 'https://www.r-project.org/Rlogo.png'
priority: 10000
---

## Biostrings

source("[http://bioconductor.org/biocLite.R](http://bioconductor.org/biocLite.R)")<br />
```r
## Install
BiocManager::install('Biostrings')
```
## Quick Start
[test.txt](https://www.yuque.com/attachments/yuque/0/2020/txt/691897/1579800839293-b28e0f1a-1088-4c56-ba2a-1a910f827db0.txt?_lake_card=%7B%22uid%22%3A%221579800839229-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Ftxt%2F691897%2F1579800839293-b28e0f1a-1088-4c56-ba2a-1a910f827db0.txt%22%2C%22name%22%3A%22test.txt%22%2C%22size%22%3A6581%2C%22type%22%3A%22text%2Fplain%22%2C%22ext%22%3A%22txt%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22umG5T%22%2C%22card%22%3A%22file%22%7D)
```r
library(Biostrings)
s = readDNAStringSet("test.txt")

length(s) #Numbers of seq
nchar(s)  #length of each seq
reverse(s)
translate(s)
dna2rna(s)
cDNA(dna2rna(s))
tolower(s)  # = = I don't know
letterFrequency(s, DNA_BASES)  # Frq with A,T,G,C
letterFrequency(s, DNA_ALPHABET)  # Frq with A, C, G, T, M, R, W, S, Y, K, V, H, D, B, N, -, +, .
letterFrequency(s, DNA_BASES, as.prob = TRUE) # Frq with A T G C
letterFrequency(s, "GC", as.prob = TRUE) # Frq with GC
```

## 1. Fasta Calculate

```r
library(Biostrings)
## Reading a fasta file
A <-readDNAStringSet('predict.coding.fa.transdecoder.pep.sel.fa')
head(DNAStringSet(A))
```

<pre>
  width seq names               
[1]   604 ASSVASTASSAHHHASAASTGTV...  TRINITY_DN100000_...
[2]   616 MDYMDSGRYTKSDKDWDTNVASD...  TRINITY_DN100001_...
[3]   157 SRAKKVKKDSKKGGGGGGGGSSW...  TRINITY_DN100002_...
</pre>


## Get the Distance Matrix from the Tree

[Raw post](https://yulab-smu.top/treedata-book/chapter13.html?q=distance%20matrix)

```bash
library(TDbook) # example data
library(Biostrings)

tree <- tree_HPV58


tl <- tree$tip.label
acc <- sub("\\w+\\|", "", tl)
names(tl) <- acc

tipseq <- ape::read.GenBank(acc) %>% as.character %>% 
    lapply(., paste0, collapse = "") %>% unlist %>% 
    Biostrings::DNAStringSet

tipseq_aln <- muscle::muscle(tipseq)
tipseq_aln <- DNAStringSet(tipseq_aln)

tipseq_dist <- stringDist(tipseq_aln, method = "hamming")
as.matrix(tipseq_dist)[1:5, 1:5]
```

|           | FJ385264 | D90400 | FJ385265 | FJ385263 | FJ385261 |
|-----------|----------|--------|----------|----------|----------|
| FJ385264  |        0 |     15 |       16 |       18 |       20 |
| D90400    |       15 |      0 |        7 |        7 |        9 |
| FJ385265  |       16 |      7 |        0 |        8 |       12 |
| FJ385263  |       18 |      7 |        8 |        0 |       12 |
| FJ385261  |       20 |      9 |       12 |       12 |        0 |




























<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>