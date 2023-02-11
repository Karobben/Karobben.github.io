---
title: "WGCNA: an R package for weighted correlation network analysis"
description: "WGCNA: an R package for weighted correlation network analysis"
url: paper_wgcna
date: 2020/07/07
toc: true
excerpt: "WGCNA: an R package for weighted correlation network analysis"
tags: [Papers, Bioinformatics, WGCNA]
category: [Notes, Paper, Biology]
cover: "https://i.loli.net/2020/06/08/UWBD5CLEcsvd6Fl.png"
thumbnail: "https://i.loli.net/2020/06/08/UWBD5CLEcsvd6Fl.png"
priority: 10000
---

## WGCNA: an R package for weighted correlation network analysis

Peter Langfelder1 and Steve Horvath*2

## Abstract
Weighted gene co-expression network analysis is a method for describing the **correlation patterns among genes across samples**.
WGCNA can find **clusters** (modules) of high correlated genes.
Those gene clusters are called as ***module eigengene*** or ***intramodular hub gene***.
And WGCNA can masure the **correlation of modules to one another or external traits**.
It can be used to identify candidate **biomarkers** or **therapeutic targets**.

## Background
**Functions of WGCNA**:
1. <span style="background:lightgreen">Cluster co-expression genes</span>
2. <span style="background:lightgreen">Correlation of modules to traits identification</span>
3. <span style="background:lightgreen">Significant modules identification</span>
4. <span style="background:lightgreen">Module annotation</span>
5. <span style="background:lightgreen">Define the network neighborhood</span>
6. <span style="background:lightgreen">Screen of nodes</span>
7. <span style="background:lightgreen">Contract network</span>

## Results

**Overview of typical analysis steps and the rational behind them:**

![DeepinScreenshot_select-area_20200608133456](https://i.loli.net/2020/06/08/UWBD5CLEcsvd6Fl.png)
© Peter Langfelder 2008

1. co-expression
2. Using dynamic tree cut to idnetify modules.
3. Correlation with traits:
    - Clinical data, SNPs, proteomics
    - ontology, functional enrichment
    - find biology interest modules
4. Module relationships
5. Find the Key drivers in ***interesting*** modules

### 1. Gene Cluster
<span style="background:red;color:white">Question: Soft Threadhold power????</span>
### 2. Module Detection

#### 2.1 Algorithm
<span style="background:salmon">Modules are defined as clusters of **densely interconnected genes**.</span>
***hierarhical cluster*** is used to cluster the genes.
<span style="background:lightgreen">Short Coming</span> of this algorithm:
 - Difficult determines how many clusters present in the data set.
 [About how to determines the numbers of cluster [1]](#paper1)

#### 2.2 Biological Meaning
It could reflect:
  1. Biological signal
  2. Noise

So, gene ontology information can be used.

Algorithms of Modules detection
- Fuzzy measure of module membership
- Automatic block-wise module detection
- Consensus module detection

### 3. Module and Gene Selection
ummmm....
 = =

### 4. Topological Properties

To study about network concept.
1. Whole Network Connectivity (degree)
2. Intramodular Connectivity
3. Topological Overlap
4. Clustering Coefficient

### ...Skip

## Mouse Data Application
For computational reason, only 3600 most related genes are selected.
18 modules...
![img](https://media.springernature.com/full/springer-static/image/art%3A10.1186%2F1471-2105-9-559/MediaObjects/12859_2008_Article_2544_Fig4_HTML.jpg?as=webp)
© Peter Langfelder 2008

As is how in Graph D above, weight is mostly correlated to brown, red, and salmon.
By GO enrichment result, we can find that brown is significantly enriched in categories "glycoprotein" and "signal", red is enriched in "cell cycle", and "salmon" is enriched in "chromosome". Overall, it is biological meaningful.

Figure E shows body weight between genes significant...


























 ---
 <li id="paper1">1. Dudoit S, Fridlyand J: A prediction-based resampling method for estimating the number of clusters in a dataset. Genome Biol 2002, 3(7):RESEARCH0036.

 
