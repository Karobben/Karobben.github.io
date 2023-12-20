---
toc: true
url: sigcell1
covercopy: © Karobben
priority: 10000
date: 2021-10-30 22:10:13
title: "Single cell RNA-Seq Practice: Seurat"
ytitle: "scRNA-Seq 数据分析练习"
description: "Bioinformatics: scRNA-seq data processing practices, protocol from seurat"
excerpt: "Bioinformatics: scRNA-seq data processing practices, protocol from seurat"
tags: [Bioinformatics, RNA-Seq, NGS, scRNA-Seq]
category: [Biology, Bioinformatics, Single Cell]
cover: "https://z3.ax1x.com/2021/10/31/IpH7j0.png"
thumbnail: "https://d33wubrfki0l68.cloudfront.net/abc16e23a8293f1b0961651473861345c5a019b8/92ccd/img/icons/network.svg"
---

## Single cell RNA-seq Data processing

This is my first time to learn siRNA-Seq. The protocol are based on [Seurat](https://satijalab.org/seurat/index.html). Please go and reading more information from Seurat. The codes are derectly copied from Seurat and so, if you are confuzed about my moves, please go to the link below and check by yourselves.


> For new users of Seurat, we suggest starting with a guided walk through of a dataset of 2,700 Peripheral Blood Mononuclear Cells (PBMCs) made publicly available by 10X Genomics. This tutorial implements the major components of a standard unsupervised clustering workflow including QC and data filtration, calculation of high-variance genes, dimensional reduction, graph-based clustering, and the identification of cluster markers.
> --[Seurat](https://satijalab.org/seurat/articles/get_started.html)

Source code: [© Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)

## Downlaod Practice Data

Data set: Peripheral Blood Mononuclear Cells (PBMC) freely available from 10X Genomics.

```bash
wget https://cf.10xgenomics.com/samples/cell/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz
tar -zxvf pbmc3k_filtered_gene_bc_matrices.tar.gz

tree filtered_gene_bc_matrices/hg19
```

<pre style="color:lightgreen; background-color: rgb(65, 65, 65);">
filtered_gene_bc_matrices/hg19
├── barcodes.tsv
├── genes.tsv
└── matrix.mtx
</pre>

```bash
head -n 4 filtered_gene_bc_matrices/hg19/*
```
<pre style="color:lightgreen; background-color: rgb(65, 65, 65);">
==> filtered_gene_bc_matrices/hg19/barcodes.tsv <==
AAACATACAACCAC-1
AAACATTGAGCTAC-1
AAACATTGATCAGC-1
AAACCGTGCTTCCG-1

==> filtered_gene_bc_matrices/hg19/genes.tsv <==
ENSG00000243485	MIR1302-10
ENSG00000237613	FAM138A
ENSG00000186092	OR4F5
ENSG00000238009	RP11-34P13.7

==> filtered_gene_bc_matrices/hg19/matrix.mtx <==
%%MatrixMarket matrix coordinate real general
%
32738 2700 2286884
32709 1 4
</pre>


## Data loading

```r
library(dplyr)
library(Seurat)
library(patchwork)

# Load the PBMC dataset
pbmc.data <- Read10X(data.dir = "filtered_gene_bc_matrices/hg19/")
# Initialize the Seurat object with the raw (non-normalized data).
pbmc <- CreateSeuratObject(counts = pbmc.data, project = "pbmc3k", min.cells = 3, min.features = 200)
pbmc
```
<pre style="color:lightgreen; background-color: rgb(65, 65, 65);">
An object of class Seurat
13714 features across 2700 samples within 1 assay
Active assay: RNA (13714 features, 0 variable features)
</pre>

<details>
  <summary style="color:salmon"><strong>What does data in a count matrix look like?</strong></summary>

  ```r
  # Lets examine a few genes in the first thirty cells
  pbmc.data[c("CD3D", "TCL1A", "MS4A1"), 1:30]
  ```
  <pre style="color:lightgreen; background-color: rgb(65, 65, 65);">
  3 x 30 sparse Matrix of class "dgCMatrix"

  CD3D  4 . 10 . . 1 2 3 1 . . 2 7 1 . . 1 3 . 2  3 . . . . . 3 4 1 5
  TCL1A . .  . . . . . . 1 . . . . . . . . . . .  . 1 . . . . . . . .
  MS4A1 . 6  . . . . . . 1 1 1 . . . . . . . . . 36 1 2 . . 2 . . . .
  </pre>

  ```r
  dense.size <- object.size(as.matrix(pbmc.data))
  dense.size
  sparse.size <- object.size(pbmc.data)
  sparse.size
  dense.size/sparse.size
  ```
  <pre style="color:lightgreen; background-color: rgb(65, 65, 65);">
  709591472 bytes
  29905192 bytes
  23.7 bytes
  </pre>
</details>

## Standard pre-processing workflow
### QC and selecting cells for further analysis
```r
# The [[ operator can add columns to object metadata. This is a great place to stash QC stats
pbmc[["percent.mt"]] <- PercentageFeatureSet(pbmc, pattern = "^MT-")
VlnPlot(pbmc, features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3)
```

<details>
  <summary style="color:salmon"><strong>Where are QC metrics stored in Seurat?</strong></summary>

  ```r
  head(pbmc@meta.data, 5)
  ```
  <pre style="color:white; background-color: salmon">
  <table class="dataframe">
  <thead>
  	<tr><th></th><th scope="col">orig.ident</th><th scope="col">nCount_RNA</th><th scope="col">nFeature_RNA</th><th scope="col">percent.mt</th></tr>
  	<tr><th></th><th scope="col">&lt;fct&gt;</th><th scope="col">&lt;dbl&gt;</th><th scope="col">&lt;int&gt;</th><th scope="col">&lt;dbl&gt;</th></tr>
  </thead>
  <tbody>
  	<tr><th scope="row">AAACATACAACCAC-1</th><td>pbmc3k</td><td>2419</td><td> 779</td><td>3.0177759</td></tr>
  	<tr><th scope="row">AAACATTGAGCTAC-1</th><td>pbmc3k</td><td>4903</td><td>1352</td><td>3.7935958</td></tr>
  	<tr><th scope="row">AAACATTGATCAGC-1</th><td>pbmc3k</td><td>3147</td><td>1129</td><td>0.8897363</td></tr>
  	<tr><th scope="row">AAACCGTGCTTCCG-1</th><td>pbmc3k</td><td>2639</td><td> 960</td><td>1.7430845</td></tr>
  	<tr><th scope="row">AAACCGTGTATGCG-1</th><td>pbmc3k</td><td> 980</td><td> 521</td><td>1.2244898</td></tr>
  </tbody>
  </table>
  </pre>
</details>

|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/qc2-1.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|

At here, we filter cells that have:
- unique feature counts over 2,500 or less than 200
- \>5% mitochondrial counts

```r
plot1 <- FeatureScatter(pbmc, feature1 = "nCount_RNA", feature2 = "percent.mt")
plot2 <- FeatureScatter(pbmc, feature1 = "nCount_RNA", feature2 = "nFeature_RNA")
plot1 + plot2
```
|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/qc2-2.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|

```r
dim(pbmc)
pbmc <- subset(pbmc, subset = nFeature_RNA > 200 & nFeature_RNA < 2500 & percent.mt < 5)
dim(pbmc)
```

<pre style="color:lightgreen; background-color: rgb(65, 65, 65);">
[1] 13714  2700
[1] 13714  2638
</pre>

## Data Normalization

By default, we employ a global-scaling normalization method “LogNormalize” that normalizes the feature expression measurements for each cell by the total expression, multiplies this by a scale factor (10,000 by default), and log-transforms the result. Normalized values are stored in pbmc[["RNA"]]@data.

```r
# pbmc <- NormalizeData(pbmc, normalization.method = "LogNormalize", scale.factor = 10000)
pbmc <- NormalizeData(pbmc)
```

<pre style="color:lightgreen; background-color: rgb(65, 65, 65);">
Performing log-normalization
0%   10   20   30   40   50   60   70   80   90   100%
[----|----|----|----|----|----|----|----|----|----|
**************************************************|
</pre>



## Identify of highly variable features (feature selection)

Seurat believe that "focusing on these genes in downstream analysis helps to highlight biological signal in single-cell datasets"

Identification argorithm details: [Comprehensive Integration of Single-Cell Data](https://doi.org/10.1016/j.cell.2019.05.031)

```r
pbmc <- FindVariableFeatures(pbmc, selection.method = "vst", nfeatures = 2000)

# Identify the 10 most highly variable genes
top10 <- head(VariableFeatures(pbmc), 10)

# plot variable features with and without labels
plot1 <- VariableFeaturePlot(pbmc)
plot2 <- LabelPoints(plot = plot1, points = top10, repel = TRUE)
plot1 + plot2
```


## Scaling the data

Next, we apply a linear transformation (‘scaling’) that is a standard pre-processing step prior to dimensional reduction techniques like PCA. The ScaleData() function:

    Shifts the expression of each gene, so that the mean expression across cells is 0
    Scales the expression of each gene, so that the variance across cells is 1
        This step gives equal weight in downstream analyses, so that highly-expressed genes do not dominate
    The results of this are stored in pbmc[["RNA"]]@scale.data


```r
all.genes <- rownames(pbmc)
pbmc <- ScaleData(pbmc, features = all.genes)

```

## Why The order of the Normalization → Variable Finding → Scaling matters

1. **Normalization**: This step is necessary to account for differences in sequencing depth across cells. ==Without normalization, cells with more total reads would dominate any downstream analysis.==

2. **Finding Variable Features**: The primary goal of this step is to identify genes that vary ==significantly across cells==, as these genes can be **informative** for <u>clustering or other downstream analyses</u>. If you scale the data before this step, you would be artificially ==inflating the variance of lowly expressed genes and diminishing the variance of highly expressed ones==, which might impact the accuracy of variable feature detection.

3. **Scaling**: Scaling is performed on the variable features to ensure that they have a ==mean of 0== and a ==standard deviation of 1==. This step is crucial for ==dimensionality reduction== techniques like PCA, where you don't want the magnitude of gene expression values to influence the results. If a gene has a high magnitude of expression (let's say in the thousands) compared to another gene (with values in the tens), without scaling, the gene with higher magnitude values would disproportionately influence the PCA, even if its variance across cells is not particularly informative.

The reason `ScaleData` is performed after `FindVariableFeatures` is to ensure that the detection of variable features is based on the actual biological variance in the data, not on the artificial variance introduced by scaling. Once variable features are identified based on their true variance, then we scale them so that no ==single gene dominates== the downstream analyses due to its magnitude.

In simpler terms:
- We want to identify variable features based on "real" biological differences, not differences introduced by scaling.
- Once we've identified the truly variable features, we scale them so that each has an equal opportunity to influence downstream analyses like PCA or clustering, regardless of its absolute expression level.

Scaling before identifying variable features might lead to a situation where genes that aren't truly variable (in a biological sense) are given undue importance in the analysis.




## Perform linear dimensional reduction

```r
pbmc <- RunPCA(pbmc, features = VariableFeatures(object = pbmc))
# Examine and visualize PCA results a few different ways
print(pbmc[["pca"]], dims = 1:5, nfeatures = 5)
```

```r
VizDimLoadings(pbmc, dims = 1:2, reduction = "pca")
```
|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/pca_viz-1.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|

```r
DimPlot(pbmc, reduction = "pca")
```
|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/pca_viz-2.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|


```r
DimHeatmap(pbmc, dims = 1:15, cells = 500, balanced = TRUE)
```

|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/multi-heatmap-1.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|


## Determine the ‘dimensionality’ of the dataset

```r
# NOTE: This process can take a long time for big datasets, comment out for expediency. More
# approximate techniques such as those implemented in ElbowPlot() can be used to reduce
# computation time
pbmc <- JackStraw(pbmc, num.replicate = 100)
pbmc <- ScoreJackStraw(pbmc, dims = 1:20)
JackStrawPlot(pbmc, dims = 1:15)
```
|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/jsplots-1.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|

```r
ElbowPlot(pbmc)
```
|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/elbow_plot-1.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|


## Cluster the cells

```r
pbmc <- FindNeighbors(pbmc, dims = 1:10)
pbmc <- FindClusters(pbmc, resolution = 0.5)

# Look at cluster IDs of the first 5 cells
head(Idents(pbmc), 5)
```

## Run non-linear dimensional reduction (UMAP/tSNE)

```r
# If you haven't installed UMAP, you can do so via reticulate::py_install(packages =
# 'umap-learn')
pbmc <- RunUMAP(pbmc, dims = 1:10)
DimPlot(pbmc, reduction = "umap")
saveRDS(pbmc, file = "../output/pbmc_tutorial.rds")
```

|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/tsneplot-1.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|

## Finding differentially expressed features (cluster biomarkers)

```r
cluster2.markers <- FindMarkers(pbmc, ident.1 = 2, min.pct = 0.25)
head(cluster2.markers, n = 5)

# find all markers distinguishing cluster 5 from clusters 0 and 3
cluster5.markers <- FindMarkers(pbmc, ident.1 = 5, ident.2 = c(0, 3), min.pct = 0.25)
head(cluster5.markers, n = 5)

pbmc.markers <- FindAllMarkers(pbmc, only.pos = TRUE, min.pct = 0.25, logfc.threshold = 0.25)
pbmc.markers %>%
    group_by(cluster) %>%
    slice_max(n = 2, order_by = avg_log2FC)

cluster0.markers <- FindMarkers(pbmc, ident.1 = 0, logfc.threshold = 0.25, test.use = "roc", only.pos = TRUE)
VlnPlot(pbmc, features = c("MS4A1", "CD79A"))
```

|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/markerplots-1.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|

```r
# you can plot raw counts as well
VlnPlot(pbmc, features = c("NKG7", "PF4"), slot = "counts", log = TRUE)
```
|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/markerplots-2.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|

```r
FeaturePlot(pbmc, features = c("MS4A1", "GNLY", "CD3E", "CD14", "FCER1A", "FCGR3A", "LYZ", "PPBP",
    "CD8A"))
```

|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/markerplots-3.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|

```r
pbmc.markers %>%
    group_by(cluster) %>%
    top_n(n = 10, wt = avg_log2FC) -> top10
DoHeatmap(pbmc, features = top10$gene) + NoLegend()
```
|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/clusterHeatmap-1.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|


## Assigning cell type identity to clusters

```r
new.cluster.ids <- c("Naive CD4 T", "CD14+ Mono", "Memory CD4 T", "B", "CD8 T", "FCGR3A+ Mono",
    "NK", "DC", "Platelet")
names(new.cluster.ids) <- levels(pbmc)
pbmc <- RenameIdents(pbmc, new.cluster.ids)
DimPlot(pbmc, reduction = "umap", label = TRUE, pt.size = 0.5) + NoLegend()
saveRDS(pbmc, file = "../output/pbmc3k_final.rds")
```
|![Violine plot for QC](https://satijalab.org/seurat/articles/pbmc3k_tutorial_files/figure-html/labelplot-1.png)|
|:-:|
|[©Seurat 2021](https://satijalab.org/seurat/articles/pbmc3k_tutorial.html)|
