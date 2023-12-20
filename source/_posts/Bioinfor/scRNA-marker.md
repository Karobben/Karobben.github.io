---
toc: true
url: scRNA_marker
covercopy: © Karobben
priority: 10000
date: 2023-10-04 13:16:57
title: "scRNA-Seq: makers explore"
ytitle: "scRNA-Seq: makers explore"
description: "scRNA-Seq: makers explore"
excerpt: "scRNA-Seq: makers explore"
tags: [Bioinformatics, RNA-Seq, NGS, scRNA-Seq]
category: [Biology, Bioinformatics, Single Cell]
cover: "https://z1.ax1x.com/2023/10/05/pPOzURU.png"
thumbnail: "https://z1.ax1x.com/2023/10/05/pPOzURU.png"
---

Seurat is a popular R package for single-cell RNA sequencing (scRNA-seq) data analysis. If you've already processed your data and assigned cell identities (classes), then finding differentially expressed genes (DEGs) between two different classes is a common next step.

Here's a brief step-by-step guide on how to identify DEGs between two cell types or classes using Seurat:

1. **Setup**:
   First, make sure you have the Seurat library loaded.
   ```R
   library(Seurat)
   ```

2. **Differential Expression**:
   Use the `FindMarkers` function in Seurat to identify DEGs. You can specify the two groups you are interested in by setting the `ident.1` and `ident.2` parameters.

   For example, if you have two classes named "ClassA" and "ClassB", you can identify DEGs between these two classes as follows:
   ```R
   de_genes <- FindMarkers(object = your_seurat_object, 
                ident.1 = "ClassA", 
                ident.2 = "ClassB", 
                min.pct = 0.25,
                logfc.threshold = 0.25,
                group.by = "Final_id")
   ```

   <pre>
    |++++++++++++++++++++++++++++++++++++++++++++++++++| 100% elapsed=29s  
   </pre>
   - `your_seurat_object` is your Seurat object.
   - `min.pct` is the minimum percentage of cells where the gene must be detected in either of the two groups.
   - `logfc.threshold` is the minimum log-fold change threshold.
   - `group.by` is the colname from `metadata`

3. **Inspect Results**:
   The resulting `de_genes` data frame will contain differentially expressed genes between "ClassA" and "ClassB". It will include columns for the average expression in each class, the percentage of cells expressing the gene in each class, the log fold-change, and the adjusted p-value (among other metrics).

4. **Filter Based on Significance**:
   You might want to filter out genes based on a significance threshold, for instance, an adjusted p-value less than 0.05:
   ```R
   significant_genes <- de_genes[de_genes$p_val_adj < 0.05, ]
   ```

5. **Visualize**:
   You can also visualize the expression of significant genes across different classes using feature plots or violin plots in Seurat.

Remember, the parameters like `min.pct`, `logfc.threshold`, and the p-value cutoff should be chosen based on your specific dataset and research questions. Adjust them as necessary to balance sensitivity and specificity.


## Violin Plot

```r
VlnPlot(OL3, 
  idents =  c("GMC1", "GMC2", "GMC3*"), 
  features = "N", 
  group.by = "Pred_cl")
```

|![Show apart of Cells](https://z1.ax1x.com/2023/10/05/pPOzURU.png)|
|:-:|

```r
VlnPlot(OL3, 
  idents =  c("GMC1", "GMC2", "GMC3*"), 
  features = row.names(de_genes), 
  group.by = "Pred_cl")
```

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
