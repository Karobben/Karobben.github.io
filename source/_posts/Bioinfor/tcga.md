---
toc: true
url: tcga
covercopy: <a href="https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga/studied-cancers">© NIH</a>
priority: 10000
date: 2022-12-06 13:02:44
title: TCGA Database
ytitle: TCGA Database
description: "TCGA Database usage. R packages, TCGA related API"
excerpt: "TCGA Database usage. R packages, TCGA related API"
tags: [TCGA, Bioinformatics, api]
category: [Biology, Bioinformatics, Database]
cover: "https://www.cancer.gov/sites/g/files/xnrzdm211/files/styles/cgov_article/public/cgov_image/media_image/100/700/5/files/Cancers%20selected%20labeled%20-%20article.jpg"
thumbnail: "https://www.cancer.gov/sites/g/files/xnrzdm211/files/styles/cgov_article/public/cgov_image/media_image/100/700/5/files/Cancers%20selected%20labeled%20-%20article.jpg"
---

## TCGA Database

Reference:
- [Documentation](https://bioconductor.org/packages/release/bioc/vignettes/TCGAbiolinks/inst/doc/download_prepare.html#Downloading_and_preparing_data_for_analysis)
- [Bioconductor](https://support.bioconductor.org/p/133576/)

```r
library(TCGAbiolinks)
library(SummarizedExperiment)
library(dplyr)
library(DT)

projects <- TCGAbiolinks:::getGDCprojects()$project_id
projects <- projects[grepl('^TCGA',projects,perl=T)]

query <- GDCquery(project = projects,
                  data.category = "Transcriptome Profiling",  
                  data.type = "Gene Expression Quantification",  
                  workflow.type = "STAR - Counts")
# counts <- GDCprepare(query,save = TRUE, save.filename = "all_tumor_htseq_raw_counts.rda")
data <- GDCprepare(query = query)

# download and fetch the data from local
GDCdownload(query = query,
              method = "api",
              files.per.chunk = 60,
              directory = "mRNA")

expdat <- GDCprepare(query = query,
                       directory = "mRNA")
```

If you download successfully, you would see the red codes below.

<code>
<pre style="background-color:white; color:red">
--------------------------------------
o GDCquery: Searching in GDC database
--------------------------------------
Genome of reference: hg38
--------------------------------------------
oo Accessing GDC. This might take a while...
--------------------------------------------
ooo Project: TCGA-ESCA
ooo Project: TCGA-SARC
ooo Project: TCGA-CESC
ooo Project: TCGA-UCEC
--------------------
oo Filtering results
--------------------
ooo By data.type
ooo By workflow.type
----------------
oo Checking data
----------------
ooo Checking if there are duplicated cases
ooo Checking if there are results for the query
-------------------
o Preparing output
-------------------
</pre>
</code>

!!! Note Check the group and counts information

```r
# Check the mate information
as.data.frame(colData(data))
# Check Exression counts
assay(data)[1:6,1:4]
```

<pre>
TCGA-DX-A6Z0-01A-13R-A36F-07 TCGA-X2-A95T-01A-11R-A37L-07 TCGA-DX-A6BF-01A-11R-A30C-07 TCGA-DX-A1L1-01A-11R-A24X-07
ENSG00000000003.15                         3415                          861                          316                         4004
ENSG00000000005.6                           340                            4                           14                            0
ENSG00000000419.13                         2296                          905                          938                         3935
ENSG00000000457.14                          594                          454                           85                          595
ENSG00000000460.17                          626                          318                           62                          458
ENSG00000000938.13                          259                          138                          271                          381
</pre>

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>


!!! note why download data

Sometimes, you may receive errors:
<pre>
Error in GDCquery(project = projects[3], data.category = "Transcriptome Profiling",  :
  Please set a valid workflow.type argument from the list below:
  => STAR - Counts
</pre>

You can't turn the "GDCprepare" results into data directly. You need to download it first and convert it by "GDCprepare". See details in [github](https://github.com/BioinformaticsFMRP/TCGAbiolinks/issues/153)


## Differential Expression Genes

Reference: [rdrr.io](https://rdrr.io/bioc/TCGAbiolinks/f/vignettes/analysis.Rmd)










```r

```
