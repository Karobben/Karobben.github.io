---
toc: true
url: paper_edger
covercopy: <a href ="https://academic.oup.com/bioinformatics/article/26/1/139/182458">© Mark D. Robinson</a>
priority: 10000
date: 2021-04-07 12:19:56
title: "edgeR"
ytitle: "edgeR"
description: "Paper reading notes for edgeR, the algorithms"
excerpt: "Paper reading notes for edgeR"
tags: [R]
category: [Notes]
cover: "https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/bioinformatics/26/1/10.1093/bioinformatics/btp616/2/m_btp616f1.jpeg?Expires=1620175077&Signature=wJVzw5pXEdGzipZWAV2yxMYFN9lnFDO8jGnetOyJAKJWlbVjmABpdn0x3gFSabuDfyEGhcJykPAV9OJJ-p2dZh3vk0drXGXBwHrbigmfVYYz3wZT2Bg-z7BRHkniuZTXXj1Y5Id~DDbKdNvtbz8ApT0N6FtO--fQI7MYl7ZUYb399P3IBvwWlvr9-YpyfizJkYdz3ISBSsZFgjoC0xowariAqSw7gogZVFxnQYW2FtHjmtEUo8T6x1l-~ia~V9Ueb16y0~OhpbgTW8wK5XLoN8x~xNfzs1qc07ZlUTEawf4EkGr8YVIYi4WCbSV5mFnsugbbo2f6k3hWD92FRgNnag__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA"
thumbnail: "https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/bioinformatics/26/1/10.1093/bioinformatics/btp616/2/m_btp616f1.jpeg?Expires=1620175077&Signature=wJVzw5pXEdGzipZWAV2yxMYFN9lnFDO8jGnetOyJAKJWlbVjmABpdn0x3gFSabuDfyEGhcJykPAV9OJJ-p2dZh3vk0drXGXBwHrbigmfVYYz3wZT2Bg-z7BRHkniuZTXXj1Y5Id~DDbKdNvtbz8ApT0N6FtO--fQI7MYl7ZUYb399P3IBvwWlvr9-YpyfizJkYdz3ISBSsZFgjoC0xowariAqSw7gogZVFxnQYW2FtHjmtEUo8T6x1l-~ia~V9Ueb16y0~OhpbgTW8wK5XLoN8x~xNfzs1qc07ZlUTEawf4EkGr8YVIYi4WCbSV5mFnsugbbo2f6k3hWD92FRgNnag__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA"
---

## edgeR: empirical analysis of DGE in R

cite: [Mark D. Robinson, Davis J. McCarthy, Gordon K. Smyth, edgeR: a Bioconductor package for differential expression analysis of digital gene expression data, Bioinformatics, Volume 26, Issue 1, 1 January 2010, Pages 139–140, https://doi.org/10.1093/bioinformatics/btp616](https://academic.oup.com/bioinformatics/article/26/1/139/182458)

> -  An ==overdispersed Poisson model== is used to account for both biological and technical variability.
> - ==Empirical Bayes methods== are used to moderate the degree of overdispersion across transcripts, improving the reliability of inference.
> - The methodology can be used even with the **most minimal levels of replication**, provided at least one phenotype or experimental condition is replicated.


## Why EdgeR

> - ==For microarrays==, the abundance of a particular transcript is measured as ==afluorescence intensity==, effectively a continuous response
> - [**Digital gene expression (DGE)**](#DGE) data the abundance is observed as a ==count==
> - Therefore, procedures that are successful for microarray data are ==not directly applicable== to DGE data
> - . edgeR is designed for the analysis of replicated count-based expression data and is an implementation of methology developed by Robinson and Smyth[^Robinson_MD1][^Robinson_MD2].
> - It initially developed for [**serial analysis of gene expression (SAGE)**](#SAGE)
> As a result, edgeR may also be useful in other experiments that generate counts, such as ChIP-seq, in proteomics experiments where spectral counts are used to summarize the peptide abundance[^Andersson_2008] or in barcoding experiments where several species are counted [^Wong_2008].
---

<p id="DGE"></p>

==Digital gene expression==: Digital gene expression (DGE) is a sequence-based approach for gene expression analyses, that generates a digital output at an unparalleled level of sensitivity[^Rodríguez-Esteban].

<p id="SAGE"></p>

==Serial analysis of gene expression (SAGE)==: Serial analysis of gene expression, or SAGE, is an experimental technique designed to gain a direct and quantitative measure of gene expression. The SAGE method is based on the isolation of unique sequence tags (9-10 bp in length) from individual mRNAs and concatenation of tags serially into long DNA molecules for a lump-sum sequencing[^Yamamoto_2001].

<span> Spam test</span>
<span class="mjx-chtml"> Spam test2</span>

---

## Method

In limma (Smyth, 2004), where an ==empirical Bayes model== is used to moderate the probe-wise variances.

In edgeR:
We ==assume== the data can be summarized into a table of counts
We ==model== the data as negative binomial (NB) distributed
$$
Y_ {gi} \sim NB(M_ i p_ {gj},\phi_g)
$$

For gene $_ g$ and sample $_ i$:
$M_i$: the library size (total number of reads),
$ϕ_g$: the dispersion
$p _{gj}$: is the relative abundance of gene $_g$ in experimental group $_j$ to which sample $_i$ belongs.

We use the *NB* parameterization where:
- the **mean** is $\mu_ {gi} = M_ i p_ {gj}$
- the **variance** is $μ_ {gi}(1+ \mu _ {gi} \phi _g)$

For differential expression analysis:
- the parameters of interest are $p_ {gj}$.


The NB distribution is reduced to Poisson when $ \phi_g = 0$.

In some DGE applications, technical variation can be treated as Poisson.
In general, $\phi_g$ represents the coefficient of variation of biological variation between the samples. In this way, our model is able to separate biological from technical variation.


`limma`: dispersion estimates ->  `topTags`: tabulate the top differentially expressed genes
                     -> `plotSmear`: MA plot


## More

There are a few terms and algorithms I do not understand. So, I'll update this page later.

[^Andersson_2008]: Andersson AF, et al. Comparative analysis of human gut microbiota by barcoded pyrosequencing, PLoS ONE, 2008, vol. 3 pg. e2836

[^Wong_2008]: Wong JWH, et al. Computational methods for the comparative quantification of proteins in label-free LCn-MS experiments, Brief. Bioinform., 2008, vol. 9 (pg. 156-165)

[^Yamamoto_2001]: [Yamamoto M, Wakatsuki T, Hada A, Ryo A. Use of serial analysis of gene expression (SAGE) technology. J Immunol Methods. 2001 Apr;250(1-2):45-66. doi: 10.1016/s0022-1759(01)00305-2. PMID: 11251221.](https://www.sciencedirect.com/science/article/abs/pii/S0022175901003052)


[^Rodríguez-Esteban]: Rodríguez-Esteban, G., González-Sastre, A., Rojo-Laguna, J.I. et al. Digital gene expression approach over multiple RNA-Seq data sets to detect neoblast transcriptional changes in Schmidtea mediterranea . BMC Genomics 16, 361 (2015). https://doi.org/10.1186/s12864-015-1533-1

[^Robinson_MD1]: [Robinson MD,  Smyth GK. Moderated statistical tests for assessing differences in tag abundance, Bioinformatics, 2007, vol. 23 (pg. 2881-2887)](https://academic.oup.com/bioinformatics/article/23/21/2881/372869)

[^Robinson_MD2]: [Robinson MD,  Smyth GK. Small sample estimation of negative binomial dispersion, with applications to SAGE data, Biostatistics, 2008, vol. 9 (pg. 321-332)]
