---
toc: true
url: nmf
covercopy: <a href="https://www.mdpi.com/1996-1073/12/19/3722/htm">© Li, X, et al</a>
priority: 10000
date: 2021-11-07 15:48:47
title: "NMF: Non-negtive matrix factorization"
ytitle: "NMF: Non-negtive matrix factorization"
description: "NMF: Non-negtive matrix factorization"
excerpt: "NMF: Non-negtive matrix factorization"
tags: [Statistic, Cluster]
category: [Notes, Statistic, Distribution]
cover: "https://www.mdpi.com/energies/energies-12-03722/article_deploy/html/images/energies-12-03722-g008.png"
thumbnail: "https://e7.pngegg.com/pngimages/339/67/png-clipart-science-technology-engineering-and-mathematics-logo-pi-math-white-text.png"
---


## NMF: Non-negtive matrix factorization

video instroctrions:
- [Non-Negative Matrix Factorization (NMF) | Multiplicative Update Rules By Lee And Seung; 2020; Youtube](https://www.youtube.com/watch?v=4pPTwsd-5M)
- [Non-negative Matrix Factorization (NMF) Implementation; 2020; Youtube](https://www.youtube.com/watch?v=dyuCcWzmssE)

Blog and Papers:

Github codes:
  - [ahmadvh; 2019](https://github.com/ahmadvh/Non-Negative-Matrix-factorization---Implemented-in-python)
  - [QColeman97; 2019](https://github.com/QColeman97/NMF-All-Stars)
Bacground
  - non-negtive matrix factorization (NMF) is an unsupervised machine learning technique created by Lee & Seung in 1999.
  - It is a verstile algorithm
    - Makes a parts-based-representation ofits input data
    - Non-nectivity of input data allows this

Uses
  - Dimensionality reduction
  - Data compression and approximation
  - Audio source separation
  - Text topic extraction

All input data should be positive numbers


## Nonnegative Matrix Factorization: An Analytical and Interpretive Tool in Computational Biology[^Devarajan_2008]


[^Devarajan_2008]: Devarajan, Karthik. "Nonnegative matrix factorization: an analytical and interpretive tool in computational biology." PLoS computational biology 4.7 (2008): e1000029.

This paper reviewed the principle algorithm of the NMF and both its advantage and disadvantage in the biology data.

- Molecular pattern discovery
  - In cell level:
    - In the gene and protein expresion profile → expressoin pattern
    - find functional biological groups
  - gene level
    - A group of functional gene: functional cell group
  -  Sequence level:
    - Sequence pattern among proteins.
  - Cancer type clustering, subclustering searching.
  - genomic hybridization data: patient subgroup


- Class comprision and prediction
  - Supevised learning framewaork
  - Identify differential expression gene with ANOVA.
  - Classification methods or protein folding recognision.

- Cross-Platform and Cross-Species Characterization
  - reduce noise
  - capturing invariant biological features
  - use of prior knowledge basd on existing datasets and generate new data

- Biomedical Information
  - NPL
  - PS: NPL: Topic modelling using NMF[^CHIRA_GOYAL_2021]

[^CHIRA_GOYAL_2021]: CHIRA GOYAL; Part 15: Step by Step Guide to Master NLP – Topic Modelling using NMF; 2021(https://www.analyticsvidhya.com/blog/2021/06/part-15-step-by-step-guide-to-master-nlp-topic-modelling-using-nmf/)

- Functional Characterization of Genes
  - find the homogeneous functional group by the Gene ontology batabase
  - This methodology is implemented in the program called GENERATOR (GENElist Aimed Theme- discovery execuTOR).
