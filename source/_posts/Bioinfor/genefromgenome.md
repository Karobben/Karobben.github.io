---
toc: true
url: genefromgenome
covercopy: <a href="https://www.smacgigworld.com/blog/principle-dna-extraction.php">© smacgigworld.com</a>
priority: 10000
date: 2022-09-16 11:01:08
title: "Genome Annotation"
ytitle: "Extract Genes from Non-annotated Genome"
description: "Extract Genes from Non-annotated Genome"
excerpt: "Genome annotations help us understand the functions and roles of genes and genomic regions, leading to improved knowledge of biological processes and disease mechanisms. <a title='ChatGPT'>Who sad this?</a>"
tags: [Bioinformatics, blast, Python]
category: [Biology, Bioinformatics, Protocol]
cover: "https://www.smacgigworld.com/assets/blog-img/genomic-dna-extraction.webp"
thumbnail: "https://www.smacgigworld.com/assets/blog-img/genomic-dna-extraction.webp"
---

## Extract Genes from Non-annotated Genome

For de-novo assembled genomes, `gtf` from reference genome is not match the position of de-novo genomes because there are many novel deletions, insertions, etc. So, we can not using than to locate genes, introns, or extrons.

There are a few things we can achieve this goal:
- genome annotation
- align the reference genes into your genome
- call them from the `vcf` file directly

### Call genes from VCF file

This is the trickiest way. Because if we have the variation files, we can call the genes based on the location of reference `gtf`. And we even don't need to assemble our genomes.
Cons:
    - We have only SNP information
    - Structure variation like inversion and duplication cannot be found.


## Genome Annotation

One of easiest way to extract genes from non-annotated Genome is annotate it.

[MITOS WebServer](http://mitos.bioinf.uni-leipzig.de/index.py).
In this server, you just need to submit your `fasta` file and wait. A quick test of mitochondria genome shows it can not only annotate genes, but also annotate tRNA:

| Name |Start     | Stop| Strand| Length| Structure|
| :-: | :-: |:-: |:-: |:-: |:-: |
|trnI(atc) |1 |65 |+ |65 |svg ps|
|nad5-1_a |58 |120 |+ |63 ||
|trnQ(caa) |97 |165 |- |69 |svg ps|
|trnM(atg) |171 |239 |+ |69 |svg ps|

`svg` are secondary structure of the tRNA.

By compaired with the reference `gtf` file, the general quality f this annitations is good. tRNA prediction has a very high positive ratio. Most of genes were annotated as well as  tRNAs. You can download the BED fiel, GFF file, or other type of annotation formats.

All annotated genes:
![](https://s1.ax1x.com/2022/09/17/xSdLz6.png)

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
