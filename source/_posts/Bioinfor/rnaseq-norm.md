---
toc: true
url: rnaseq_norm
covercopy: <a href="https://statquest.org/rpkm-fpkm-and-tpm-clearly-explained/">© StatQuest</a>
priority: 10000
date: 2022-10-04 13:00:32
title: "FPKM, RPKM, CPM, TPM, TMM in RNA-Seq"
ytitle: "FPKM, RPKM, CPM, TPM, TMM in RNA-Seq"
description: "FPKM, RPKM, CPM, TPM, TMM in RNA-Seq"
excerpt: "RNA-seq expression normalization is the process of adjusting the raw gene expression counts to account for differences in sequencing depth and other technical factors. It is important to perform normalization to enable comparisons between samples and increase the accuracy and reproducibility of downstream analyses. Common normalization methods include TPM, FPKM, and DESeq. <a title='ChatGPT'>Who sad this?</a>"
tags: [Bioinformatics, RNA-Seq, NGS]
category: [Biology, Bioinformatics, Protocol, RNA-Seq]
cover: "https://pic1.zhimg.com/v2-d2b4e99108f94080eb1ddf9ade73e947_1440w.jpg?source=172ae18b"
thumbnail: "https://pic1.zhimg.com/v2-d2b4e99108f94080eb1ddf9ade73e947_1440w.jpg?source=172ae18b"
---

## RPKM/FPKM (reads/fragments per kilobase of transcript per million reads mapped)
$$
FPKM_ i = \frac{q_ i}{l_ i × \sum_ i{q_ i}}×10^ 9
$$

$q_i$ is raw read or fragment counts, $l_i$ is feature (i.e., gene or transcript) length

RPKM is for single ends reads, a read is a unit.
FPKM is for paired ends reads, a paired reads is a unit.


## TPM (transcript per million)

$$
TPM_ i = \frac{q_ i/l_ i}{\sum_ j{q_ i/l_ i}}×10^ 6
$$



0 where $q_i$ denotes reads mapped to transcript, $l_i$  is the transcript length, and $\sum_ j{q_ i/l_ i}$

corresponds to the sum of mapped reads to transcript normalized by transcript length.

The TPM measure can easily be converted to FPKM:
$TPM_ i = \frac{FPKM_ i}{\sum_ j{FPKM_ i}}×10^ 6$

## CPM (counts per million reads mapped (CPM)

$$
CPM_ i = \frac{q_ i}{\sum_ i{q_ i}} × 10^ 6
$$


The simplest RNA-seq feature expression unit reports normalized counts, or the number of reads that align to a particular feature after correcting for sequencing depth and transcriptome composition bias. Normalized counts are the most popular unit among differential expression analysis methods (including edgeR). However, feature length normalization is skipped, with the important consequence that within-sample differential feature expression analysis is not possible.

## Shortcomings

Example 1:
We have 2 genes:

| |  Length| Sample1| Sample2|
| :-- | :-- | :-- |:--|
|  Gene1 | 100| 200|200|
| Gene2| 2400| 0| 1200|

```r
CPM <- function(TB) {
}

FPKM <- function(TB) {
}

TPM <- function(TB) {
}

```

## Others

- TMM (trimmed mean of M values frpm edgeR)
- RLE (Relative Log Expression from DESeq)
- MRN (Median Ratio Normalization)




Though, TPM, RPKM, and FPKM are designed to normalize the expression levels of genes, ==it suitable for the comparison within a sample, not cross samples==[^Zhao_Y_21]. According to Dillies[^Dillies_MA_13], normalization algorithms could be divided into two groups: library size concept (TMM and DESeq) or distribution adjustment of read counts (Total Counts, RPKM, Quantile from `limma`). The hypothesis of TMMP and DESeq is that most of genes are not DE and the both propose a scaling factor based on a mean, median, or ratio. Based on Real data and simulated date, TMM and DESeq's performance are acceptable, but RPKM and total counts of genes are not suggested to be used on the down stream analysis[^Dillies_MA_13][^Zhao_Y_21]. On the other hand, RPKM, FPKM, and TPM tend to perform poorly when transcript distribution differ between samples[^Conesa_A_16]. In another reseach, the title is without replicates RNA-Seq, but the data set is triplicates shows that the results from TMM, RLE, and MRN are really similar[^Maza_E_16]. And for more complicated comparison, MRN might be better[^Maza_E_13].

[^Maza_E_16]: Maza E (2016) In Papyro Comparison of TMM (edgeR), RLE (DESeq2), and MRN Normalization Methods for a Simple Two-Conditions-Without-Replicates RNA-Seq Experimental Design. Front. Genet. 7:164. doi: 10.3389/fgene.2016.00164

[^Maza_E_13]: Maza, E., Frasse, P., Senin, P., Bouzayen, M., and Zouine, M. (2013). Comparison of normalization methods for differential gene expression analysis in RNA-Seq experiments: a matter of relative size of studied transcriptomes. Commun. Integr. Biol. 6:e25849. doi: 10.4161/cib.25849

[^Conesa_A_16]: Conesa A, Madrigal P, Tarazona S, Gomez-Cabrero D, Cervera A, McPherson A, Szczesniak MW, Gaffney DJ, Elo LL, Zhang X, Mortazavi A. A survey of best practices for RNA-seq data analysis. Genome Biol. 2016;17:13.
[^Dillies_MA_13]: Dillies MA, Rau A, Aubert J, Hennequet-Antier C, Jeanmougin M, Servant N, Keime C, Marot G, Castel D, Estelle J, et al. A comprehensive evaluation of normalization methods for Illumina high-throughput RNA sequencing data analysis. Brief Bioinform. 2013;14:671–83.
[^Zhao_Y_21]: Zhao, Y., Li, MC., Konaté, M.M. et al. TPM, FPKM, or Normalized Counts? A Comparative Study of Quantification Measures for the Analysis of RNA-seq Data from the NCI Patient-Derived Models Repository. J Transl Med 19, 269 (2021). https://doi.org/10.1186/s12967-021-02936-w


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
