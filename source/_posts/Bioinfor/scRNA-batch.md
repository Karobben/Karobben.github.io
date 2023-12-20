---
toc: true
url: scRNA_batch
covercopy: <a href = 'https://www.10xgenomics.com/resources/analysis-guides/introduction-batch-effect-correction' >© X10 Genomics</a>
priority: 10000
date: 2023-10-03 11:39:22
title: "Understanding and Tackling Batch Effects in Single-Cell RNA-Seq Analysis"
ytitle: "Understanding and Tackling Batch Effects in Single-Cell RNA-Seq Analysis"
description:  "Remove Batch Effects in Single-Cell RNA-Seq"
excerpt: "In single-cell RNA sequencing (scRNA-seq) analysis, batch effects—non-biological variations from different sample processing—are pervasive challenges. Without correction, they can obscure genuine biological signals. This article elucidates the importance of batch effect removal and presents a comparative overview of three popular correction methods within Seurat: Harmony, fastMNN, and SCTransform. Choosing an apt method ensures accurate and unbiased biological insights, highlighting the significance of vigilant batch correction in scRNA-seq studies."
tags: [Bioinformatics, RNA-Seq, scRNA-Seq]
category: [Biology, Bioinformatics, Single Cell]
cover: "https://cdn.10xgenomics.com/image/upload/v1629241143/analysis-guides/BatchCorrection-Intro.png"
thumbnail: "https://d33wubrfki0l68.cloudfront.net/abc16e23a8293f1b0961651473861345c5a019b8/92ccd/img/icons/network.svg"
---

## The Challenge of Batch Effects

In the world of single-cell RNA sequencing (scRNA-seq), one of the most prevailing challenges is the presence of batch effects. These are technical non-biological variations that arise when samples are processed in separate runs or under slightly different conditions. If not accounted for, batch effects can overshadow true biological differences, leading to misinterpretations.

## Why Remove Batch Effects?

Imagine studying the effects of a drug on cell populations, with samples processed both before and after treatment. If the 'before' samples were processed in one batch and the 'after' samples in another, any difference you observe might be due to this batch variation rather than the drug effect.

Removing batch effects ensures that:

- Biological variations are distinguishable from technical variations.
- Combined data from multiple batches can be analyzed together without biases.
- Results are consistent, reproducible, and truly reflective of biological phenomena.

## Approaches to Counter Batch Effects

Several methods have been developed to correct for batch effects. Here, we'll delve into three popular methods used within the Seurat package: **Harmony**, **fastMNN**, and **SCTransform**.

## A Comparative Glimpse:

| Feature             | **Harmony**                                                                           | **fastMNN (batchelor)**                                                                                   | **SCTransform**                                                                   |
|---------------------|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Method              | Operates in PCA space to adjust principal components.                                 | Uses Mutual Nearest Neighbors to align cells.                                                             | Regresses out unwanted variation and stabilizes variance.                          |
| Use Cases           | Integrating datasets from different conditions, protocols, or platforms.              | Integrating datasets with batch effects. Faster than original MNN.                                         | Alternative to traditional normalization in Seurat. Prepares data for analysis.   |
| Advantages          | Preserves biological structures well; robust to complex batch effects.                | Designed for scRNA-seq batch correction; faster than original MNN; corrects severe batch effects.        | Stabilizes variance; can handle large datasets efficiently.                       |
| Disadvantages       | Can be computationally intensive with large datasets.                                 | Requires a good selection of mutual nearest neighbors.                                                     | Not specifically a batch correction method; often combined with other methods.    |

## Deep Dive into the Methods:

1. **Harmony:** Ideal for integrating multiple scRNA-seq datasets. Harmony adjusts the principal components of the data such that inter-batch differences are minimized while retaining biological variation.

2. **fastMNN (from the batchelor package):** This method identifies mutual nearest neighbors between batches, assuming that these pairs of cells represent the same cell type across batches. It's an optimized and faster variant of the original MNN algorithm.

3. **SCTransform:** More than a batch correction technique, SCTransform is a robust normalization method. It prepares the data for downstream analysis, including batch correction, by regressing out unwanted sources of variation.

## Final Thoughts:

Batch effect correction is a crucial step in scRNA-seq data processing. By choosing the right method tailored to your dataset's needs, you can unveil genuine biological insights without being misdirected by technical noises. Always visualize and interpret results at each step, ensuring that biological variation remains the highlight of your study.


## In Action

Seurat offers several methods to correct for batch effects, ensuring that variations across batches don't obscure the biological signals you're interested in. Here's a step-by-step guide to remove batch effects using Seurat:

1. **Install and Load Seurat:**

   First, ensure you've installed and loaded the Seurat package.

   ```R
   install.packages('Seurat')
   library(Seurat)
   ```

2. **Data Integration (Using Harmony, SCTransform, and others):**

   Seurat offers various integration methods like Harmony, fastMNN, and SCTransform. Here, I'll showcase using `SCTransform` followed by `RunPCA` and `Harmony`:

   ```R
   # List of Seurat Objects from different batches
   seurat_list <- list(batch1_seurat, batch2_seurat, ...)

   # SCTransform normalization
   seurat_list <- lapply(seurat_list, function(x) {
     x <- SCTransform(x, verbose = FALSE)
   })

   # Identify anchors for integration
   anchors <- FindIntegrationAnchors(object.list = seurat_list, normalization.method = "SCT", 
                                     anchor.features = 2000, verbose = FALSE)
   
   # Integrate data
   integrated_data <- IntegrateData(anchorset = anchors, normalization.method = "SCT", verbose = FALSE)
   ```

   If you prefer using `Harmony` specifically:

   ```R
   library(harmony)
   integrated_data <- RunPCA(integrated_data, features = VariableFeatures(object = integrated_data))
   integrated_data <- RunHarmony(integrated_data, group.by.vars = "batch")
   ```

3. **Scale and Run Linear Dimensional Reduction:**

   ```R
   integrated_data <- ScaleData(integrated_data, verbose = FALSE)
   integrated_data <- RunPCA(integrated_data, verbose = FALSE)
   ```

4. **Cluster and Visualize Integrated Data:**

   Using UMAP or t-SNE to visualize the integrated data is a great way to confirm if the batch effects have been mitigated.

   ```R
   integrated_data <- RunUMAP(integrated_data, reduction = "harmony", dims = 1:30)
   DimPlot(integrated_data, group.by = "batch")
   ```

5. **Optional - Regression of unwanted sources of variation:**

   If you are aware of specific unwanted sources of variation, you can regress them out using the `vars.to.regress` parameter in the `ScaleData` function.

   ```R
   seurat_object <- ScaleData(seurat_object, vars.to.regress = "batch")
   ```

Remember, the removal of batch effects should be done carefully. Overcorrection might lead to loss of genuine biological variation. It's always a good practice to visualize and interpret the results at each step, ensuring the intended correction.

Lastly, Seurat's integration methods and their parameters might evolve with time, so always consult the latest Seurat documentation or vignettes to ensure you're using the most effective and up-to-date approaches.

Harmony, fastMNN, and SCTransform are all methods to handle batch effects and data normalization in single-cell RNA-seq data, but they operate based on different principles and have distinct purposes.

**In summary:**
   
- **Harmony** and **fastMNN** are batch-correction methods that work to align datasets from different batches or conditions.
- **SCTransform** is a normalization method that prepares the data for further analysis, including batch correction.

When dealing with batch effects, researchers often first normalize the data using **SCTransform** and then apply batch correction methods like **Harmony** or **fastMNN** to the transformed data. This two-step approach ensures that the data is both normalized and free of batch effects, making downstream analyses like clustering and differential expression more reliable.


Other tutorial: 
- [2023; X10 Genomics: Batch Effect Correction](https://www.10xgenomics.com/resources/analysis-guides/introduction-batch-effect-correction)
- [2023; Seurat: Introduction to scRNA-seq integration
](https://satijalab.org/seurat/articles/integration_introduction.html)
<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
