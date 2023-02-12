---
toc: true
url: tcga
covercopy: <a href="https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga/studied-cancers">© NIH</a>
priority: 10000
date: 2022-12-06 13:02:44
title: TCGA Database with R
ytitle: TCGA Database with R
description: "TCGA Database usage. R packages, TCGA related API"
excerpt: "TCGAbiolinks is an R package that provides an easy-to-use interface to access and analyze data from The Cancer Genome Atlas (TCGA) project. It allows users to download TCGA data, perform quality control, differential expression analysis, and data visualization. TCGAbiolinks has contributed to a better understanding of the molecular basis of cancer and identified new potential biomarkers and therapeutic targets. <a title='ChatGPT'>Who sad this?</a>"
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


I am failed to get the expression matrix by using `GDCprepare`. According to [© g27182818, 2022], it caused by STAR-Count files has more infor than `GDCprepare` need. What ever, a modified solution could be like codes below:

```r
library('TCGAbiolinks')
library(stringr)

project_name <- "TCGA-CHOL"

# Defines the query to the GDC
query <- GDCquery(project = project_name,
                  data.category = "Transcriptome Profiling",
                  data.type = "Gene Expression Quantification",
                  experimental.strategy = "RNA-Seq",
                  workflow.type = "STAR - Counts")

# Get metadata matrix
metadata <- query[[1]][[1]]

# Get main directory where data is stored
main_dir <- file.path("mRNA", project_name)
# Get file list of downloaded files
file_list <- file.path("mRNA", project_name,list.files(main_dir,recursive = TRUE)) 

# Read first downloaded to get gene names
test_tab <- read.table(file = file_list[1], sep = '\t', header = TRUE)
# Delete header lines that don't contain usefull information
test_tab <- test_tab[-c(1:4),]
# STAR counts and tpm datasets
tpm_data_frame <- data.frame(test_tab[,1])
count_data_frame <- data.frame(test_tab[,1])

# Append cycle to get the complete matrix
for (i in c(1:length(file_list))) {
  # Read table
  test_tab <- read.table(file = file_list[i], sep = '\t', header = TRUE)
  # Delete not useful lines
  test_tab <- test_tab[-c(1:4),]
  # Column bind of tpm and counts data
  tpm_data_frame <- cbind(tpm_data_frame, test_tab[,7])
  count_data_frame <- cbind(count_data_frame, test_tab[,4])
  # Print progres from 0 to 1
  print(i/length(file_list))
}

ID_list <- as.data.frame(str_split_fixed(file_list, '/', 7))[[6]]

row.names(count_data_frame) <- count_data_frame[[1]]
count_data_frame <- count_data_frame[-1]
colnames(count_data_frame) <- metadata$cases[match(ID_list, metadata$id)]

N_control = length(which(as.numeric(gsub("[^0-9.-]", "", as.data.frame(str_split_fixed(metadata$cases, '-', 5))[[4]])) >= 10))

```

## The meaning of the barcode

|![](https://docs.gdc.cancer.gov/Encyclopedia/pages/images/barcode.png)|
|:-:|
|[© NIH, GDC](https://docs.gdc.cancer.gov/Encyclopedia/pages/TCGA_Barcode/)|


Label| Identifier for| Value | Value Description |Possible Values
:-|:-|:-|:-|:-|
Analyte| Molecular type of analyte for analysis| D| The analyte is a DNA sample| See Code Tables Report|
Plate| Order of plate in a sequence of 96-well plates| 182| The 182nd plate |4-digit alphanumeric value
Portion| Order of portion in a sequence of 100 - 120 mg sample portions | 1| The first portion of the sample| 01-99
Vial| Order of sample in a sequence of samples| C| The third vial| A to Z
Project |Project name| TCGA| TCGA project |TCGA
Sample| Sample type| 1| A solid tumor| Tumor types range from 01 - 09, normal types from 10 - 19 and control samples from 20 - 29. See Code Tables Report for a complete list of sample codes
Center| Sequencing or characterization center that will receive the aliquot for analysis| 1| The Broad InstituteGCC| See Code Tables Report
Participant| Study participant| 1| The first participant from MD Anderson for GBM study | Any alpha-numeric value
TSS| Tissue source site| 2| GBM (brain tumor) sample from MD Anderson |See Code Tables Report


So, the most important information for us is the sample type: ==Tumor types range from 01 - 09, normal types from 10 - 19 and control samples from 20 - 29. See Code Tables Report for a complete list of sample codes==



## Abbreviations of projects


|Study Abbreviation | Study Name|
|:-|:-|
LAML|Acute Myeloid Leukemia
ACC|Adrenocortical carcinoma
BLCA|Bladder Urothelial Carcinoma
LGG|Brain Lower Grade Glioma
BRCA|Breast invasive carcinoma
CESC|Cervical squamous cell carcinoma and endocervical adenocarcinoma
CHOL|Cholangiocarcinoma
LCML|Chronic Myelogenous Leukemia
COAD|Colon adenocarcinoma
CNTL|Controls
ESCA|Esophageal carcinoma
FPPP|FFPE Pilot Phase II
GBM|Glioblastoma multiforme
HNSC|Head and Neck squamous cell carcinoma
KICH|Kidney Chromophobe
KIRC|Kidney renal clear cell carcinoma
KIRP|Kidney renal papillary cell carcinoma
LIHC|Liver hepatocellular carcinoma
LUAD|Lung adenocarcinoma
LUSC|Lung squamous cell carcinoma
DLBC|Lymphoid Neoplasm Diffuse Large B-cell Lymphoma
MESO|Mesothelioma
MISC|Miscellaneous
OV|Ovarian serous cystadenocarcinoma
PAAD|Pancreatic adenocarcinoma
PCPG|Pheochromocytoma and Paraganglioma
PRAD|Prostate adenocarcinoma
READ|Rectum adenocarcinoma
SARC|Sarcoma
SKCM|Skin Cutaneous Melanoma
STAD|Stomach adenocarcinoma
TGCT|Testicular Germ Cell Tumors
THYM|Thymoma
THCA|Thyroid carcinoma
UCS|Uterine Carcinosarcoma
UCEC|Uterine Corpus Endometrial Carcinoma
UVM|Uveal Melanoma