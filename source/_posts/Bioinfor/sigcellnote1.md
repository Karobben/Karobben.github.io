---
toc: true
url: sigcellnote1
covercopy: © Karobben
priority: 10000
date: 2021-10-31 10:13:25
title: "Single Cell RNA-Seq Notes"
ytitle: "单细胞笔记"
description: "Single Cell RNA-Seq Notes from Seminal"
excerpt: "Single Cell RNA-Seq Notes from Seminal"
tags: [Bioinformatics, RNA-Seq, NGS, scRNA-Seq]
category: [Biology, Bioinformatics, Single Cell]
cover: "https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fncomms14049/MediaObjects/41467_2017_Article_BFncomms14049_Fig1_HTML.jpg?as=webp"
thumbnail: "https://d33wubrfki0l68.cloudfront.net/abc16e23a8293f1b0961651473861345c5a019b8/92ccd/img/icons/network.svg"
---

## Single Cell RNA-Seq Notes

Video materials: [Human Cell Atlas: Day 1: HCA Latin America Single-Cell RNA-SEQ Data Analysis Workshop (Virtual)](https://www.youtube.com/watch?v=QaqBzilH5LE)

## Challenges

### Barcodes errors

|![Barcode errors](https://z3.ax1x.com/2021/10/31/Ip7vlt.png)|
|:-:|
|[© Dana Pe'er 2021](https://www.youtube.com/watch?v=QaqBzilH5LE)|

5000 cells in, but get 200,000 barcides identified.

### Sbarcity

Sbarcity makes the noise is high and the protocols for bulk RNA-seq are not compectable for scRNA-Seq.

### Demension

|![Barcode errors](https://z3.ax1x.com/2021/10/31/IpH7j0.png)|
|:-:|
|[© Dana Pe'er 2021](https://www.youtube.com/watch?v=QaqBzilH5LE)|

Reduce demention based on linear projection (PCA) is not compectable for hide dementional data

|![Barcode errors](https://z3.ax1x.com/2021/10/31/Ipblb8.png)|
|:-:|
|[© Dana Pe'er 2021](https://www.youtube.com/watch?v=QaqBzilH5LE)|


###  Batch effects

|![Barcode errors](https://z3.ax1x.com/2021/10/31/IpbDVU.png)|
|:-:|
|[© Dana Pe'er 2021](https://www.youtube.com/watch?v=QaqBzilH5LE)|



### Path walk: psudotime

|![Barcode errors](https://z3.ax1x.com/2021/10/31/Ipqjp9.png)|
|:-:|
|![Barcode errors](https://z3.ax1x.com/2021/10/31/IpqzOx.png)|
|![Barcode errors](https://z3.ax1x.com/2021/10/31/IpL8pj.png)|
|![Barcode errors](https://z3.ax1x.com/2021/10/31/IpLgnx.png)|
|![Barcode errors](https://z3.ax1x.com/2021/10/31/IpLbut.png)|
|[© Dana Pe'er 2021](https://www.youtube.com/watch?v=QaqBzilH5LE)|


## Nuclear RNS-Seq

Different between single cell RNA-Seq and single Nuclear RNA-Seq

|![Barcode errors](https://z3.ax1x.com/2021/11/01/IpOOMR.png)|
|:-:|
|[© Dana Pe'er 2021](https://www.youtube.com/watch?v=QaqBzilH5LE)|



## Chromium Next GEM Single Cell 5' Reagent Kits v2 (Dual Index)

From: [X10 Genomics](https://www.10xgenomics.com/support/single-cell-immune-profiling/documentation/steps/library-prep/chromium-single-cell-5-reagent-kits-user-guide-v-2-chemistry-dual-index)





|![](https://imgur.com/NdIbWMF.png)|
|:-:|
|[© X10 Genomics](https://cdn.10xgenomics.com/image/upload/v1666737555/support-documents/CG000331_ChromiumNextGEMSingleCell5-v2_UserGuide_RevE.pdf)|

Gel Bead-<font style="background-color: black" color= "white">&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Read 1&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</font><font style="background-color: MediumSeaGreen">&#160;&#160;&#160; Barcode×16 &#160;&#160;&#160;</font><font style="background-color: DarkOrange" color= "white">&#160;&#160;UMI×10&#160;&#160;</font><font style="background-color: LightSeaGreen" color= "white">&#160;&#160;&#160;TSO ×13&#160;&#160;&#160;</font>rGrGrG


- an Illumina R1 sequence (read 1 sequencing primer)
- a 16 nt 10x Barcode.
- a 10 nt unique molecular identifier (UMI)
- 13 nt unique molecular identifier (TSO) are released and mixed with the cell lysate and a Master Mix containing reverse transcription (RT) reagents and poly(dT) RT primers. Incubation of the GEMs produces 10x Barcoded, full-length cDNA from polyadenylated mRNA.

### What are UMI and TSO? (Chat4)

In single-cell sequencing, both Unique Molecular Identifiers and Template Switch Oligos (TSOs) play vital roles. Let's explore what they do and why they are important:

#### Unique Molecular Identifiers (UMI)

1. **Error Reduction**: Unique Molecular Identifiers (UMIs) are unique sequences added to each molecule before amplification. They help in distinguishing genuine sequences from PCR duplicates, allowing for accurate quantification and detection of DNA or RNA molecules.

2. **Quantification**: UMIs allow for the absolute quantification of nucleic acid molecules in a sample, crucial for understanding gene expression levels in single-cell studies.

3. **Reducing Amplification Bias**: By identifying original molecules, UMIs mitigate PCR amplification biases, leading to more representative sequencing data.

#### Template Switch Oligos (TSOs)

1. **cDNA Synthesis and Amplification**: In single-cell RNA sequencing, TSOs are used during the reverse transcription of mRNA to cDNA. They have a unique sequence that attaches to the 3' end of the cDNA. When the reverse transcriptase enzyme reaches the end of the mRNA template, it switches templates to this oligo, effectively adding a known sequence to the cDNA.

2. **Full-Length cDNA**: TSOs facilitate the generation of full-length cDNA, especially important for accurately characterizing the transcriptome of a single cell.

3. **Tagging for Sequencing**: The known sequence added by TSOs serves as a universal priming site for subsequent PCR amplification and sequencing, ensuring that all cDNA molecules are uniformly represented.

#### Why are They Needed?

1. **Accuracy**: Both MIs and TSOs improve the accuracy of single-cell sequencing by reducing errors and biases, crucial in studies where detecting low-abundance transcripts or minor genetic variations is essential.

2. **Representativeness**: They help ensure that the sequencing data is representative of the original cellular content, which is vital for understanding cellular heterogeneity and the function of individual cells within tissues.

3. **Enhanced Detection**: These elements enhance the detection of rare transcripts and genetic variations, which might otherwise be lost or misinterpreted in the noise of sequencing errors and biases.

4. **Quantitative Analysis**: They enable quantitative analysis of gene expression, which is crucial for comparing different cells or understanding dynamic processes within cells.

In summary, Molecular Identifiers and Template Switch Oligos are integral to the reliability, fidelity, and comprehensiveness of single-cell sequencing, enabling researchers to delve deeper into the complexities of cellular biology at an individual cell level.



|![](https://imgur.com/uarbCYv.png)|
|:-:|
|5ʹ Gene Expression (GEX) Library Construction|


