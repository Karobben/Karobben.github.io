---
title: "WGCNA"
description: "WGCNA"
url: wgcna
date: 2020/07/28
toc: true
excerpt: "WGCNA introduction and Q&S"
tags: [Software, Bioinformatics, WGCNA]
category: [Notes, Biology]
cover: 'https://i.loli.net/2020/06/10/9Rw23KCBXcIOMNz.png'
thumbnail: 'https://i.loli.net/2020/06/10/9Rw23KCBXcIOMNz.png'
priority: 10000
---

## WGCNA

## Lecture by Steven Horvath 2013, UCLA

Though, it was designed for microarray data, but it applied in DNA methylation  data, RNA-seq, miRNA-seq, Peptide Count data...

1. NetWork: the value between notes is either 0 or 1
2. weighted network: the value is variable between notes (Connection is weighted).

### Unsigned Network and Signed Network
1. Unsigned network:
  - The value is from -1 to 1. (Both -1 and 1 means adjacent is 0, strongly correlated)
  - Both high value and low (nagetive) value are correlated because of adjacent.
2. Singed network:
  - The correlation value is form 0-1.

From unsigned correlation to singed network,

## Q&A
Reference: [Peter 2017](https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/faq.html)

### Data Analysis Questions

1. **How many samples** do I need?
At least for <span style="background:salmon">**15 samples**</span>. More samples could robust and refined results. Noises may can't be removed if you have less samples.
<br>

2. Should I filter **probesets or genes**?
- <span style="background:salmon">**Filtering genes by DEGs**</span> is not recommended since it **completely** <span style="background:salmon">invalidates</span> the **scale-free topology assumption**, which is the indicator of the **soft thresholding power**.
- On the other hand, filtering gene by DE will lead to a set of correlated genes that will essentially form a single (or few high correlated) module respectively.
<br>

3. What **argument** (option) settings are recommended?
In general, we attempt to select suitable default which feat multiple applications and also, it is high reproducible.
While for new calculations, you can customize argument.
- **Signed Network**
    The choice of ***Signed*** or ***Unsigned*** network is complicate, but generally, we prefer the <span  style="color:darkred">Signed network</span>.
    To construct *Signed Networks*, we usring:
    `type = "signed"` or `type = "signed hybrid"` in function such as `accuracyMeasures`, `adjacency`, `chooseOneHubInEachModule`, `chooseTopHubInEachModule`, `nearestNeighborConnectivity`, `nearestNeighborConnectivityMS`, `orderBranchesUsingHubGenes`, `softConnectivity`. Some functions useing `networkType` to select the `signed`.
- **Robust correlation**
    Generaly, we recommend to using default arguments to detect the correlation unless you have enough reason to believe there is no outlier measurment. You can using `corFnc`, `cor`, et al. to customizing your own detective. For more, please go to [Tutorial](https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/faq.html)

4. Can WGCNA be used to analyze **RNA-Seq data**?
  **Peter**： <span style="background:salmon">Yes</span>. As far as WGCNA is concerned, working with (**properly normalized**) RNA-seq data isn't really any different from working with (**properly normalized**) microarray data.
  **Suggestion**:
  - Removing **low hits** transcripts.
    Low counting transcripts tend to reflect noise. (for example, removing all features that have a count of less than say 10 in more than 90% of the samples)
  - **Normalization**
    `varianceStabilizingTransformation` from *DESeq2* is really useful.
    RPKM and FPKM is helpful, too.
    We can also using `log2(x+1)`.
    <span style="color:salmon"><b>Notions</b></span>:
    1. Different algorithms have huge impact on the result of expression change, but have limit affect on WGCNA.
    2. Id data comes from different batch, We can use `ComBat` (Exp: [木头的博客](http://blog.sina.com.cn/s/blog_70a5f5210102wibx.html)) for batch effect removal.
    3. Finally, we usually check quantile scatterplots to make sure there are no **systematic shifts** between samples; if sample quantiles show correlations (which they usually do), quantile normalization can be used to remove this effect.
5. Data heterogeneous
  Data heterogeneous can effect any statistical analysis. (Skip)

6. **Soft-thresholding power**
  can't get a good scale-free topology index no matter how high I set the soft-thresholding power.
  1. First, the user should ensure that <span style='background:salmon'> variables (probesets, genes etc.) have not been filtered by differential expression</span> with respect to a sample trait.
  Probability: Checking the clustering tree ([exp](https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/Tutorials/FemaleLiver-01-dataInput.pdf)); strong clusters in the tree indicates globally different groups of sample. It may caused by batch effects or heterogenous. Carefully adjust the samples before building topology index.

  If the one causing heterogenous you don't remove, you can still chosen the soft thresholding power by the number of samples at table below.

|Number of samples|Unsigned and signed hybrid networks|Signed networks|
|:--:|:--:|:--:|
|Less than 20|9|18|
|20-30|8|16|
|30-40|7|14|
|more than 40|6|12|
