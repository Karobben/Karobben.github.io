---
url: edger
---

# edgeR(out of date)


```r
~/Biosoft/trinityrnaseq-Trinity-v2.8.4/Analysis/DifferentialExpression/run_DE_analysis.pl  --matrix Intest.table  --method edgeR --dispersion 0.1


source("http://bioconductor.org/biocLite.R")
library("limma")
library("edgeR")



x <- read.delim("3.isoforms.results")
y <- estimateCommonDisp(y)
y <- DGEList(counts=5,group=1)
y <- calcNormFactors(y)
y <- estimateTagwiseDisp(y)
y <- estimateCommonDisp(y)


source("http://bioconductor.org/biocLite.R")
library("limma")
library("edgeR")
rawdata <- read.delim("3.isoforms.results", check.names=FALSE, stringsAsFactors=FALSE)
y <- DGEList(counts=rawdata[,3:8], genes=rawdata[,1:2])
y$samples$lib.size <- colSums(y$counts)
y <- calcNormFactors(y)
Patient <- factor(c(8,8,33,33,51,51))
Tissue <- factor(c("N","T","N","T","N","T"))
data.frame(Sample=colnames(y),Patient,Tissue)
design <- model.matrix(~Patient+Tissue)
rownames(design) <- colnames(y)
y <- estimateGLMCommonDisp(y, design, verbose=TRUE)
y <- estimateGLMTrendedDisp(y, design)
y <- estimateGLMTagwiseDisp(y, design)
fit <- glmFit(y, design)
lrt <- glmLRT(fit); topTags(lrt)
topTags(lrt)
write.csv(topTags(lrt)$table, file="qqq")
#############################################
��Դ����������ģ�� edgeR�������裺https://www.tanboyu.com/edger-users-guide.html
#####################################################################################

####################################################################################
��׼��

source("http://bioconductor.org/biocLite.R")
library("limma")
library("edgeR")

rawdata <- read.delim("3.isoforms.results", check.names=FALSE, stringsAsFactors=FALSE)
y <- DGEList(counts=rawdata[,2:6], genes=rawdata[,1])
y$samples$lib.size <- colSums(y$counts)
y <- calcNormFactors(y)
Patient <- factor(c(8,8,51,51))
Tissue <- factor(c("N","T","N","T"))
data.frame(Sample=colnames(y),Patient,Tissue)
design <- model.matrix(~Patient+Tissue)
rownames(design) <- colnames(y)
y <- estimateGLMCommonDisp(y, design, verbose=TRUE)
y <- estimateGLMTrendedDisp(y, design)
y <- estimateGLMTagwiseDisp(y, design)
fit <- glmFit(y, design)
lrt <- glmLRT(fit); topTags(lrt)
topTags(lrt)


#########################################################

source("http://bioconductor.org/biocLite.R")
library("limma")
library("edgeR")

rawdata <- read.delim("3.isoforms.results", check.names=FALSE, stringsAsFactors=FALSE)
y <- DGEList(counts=rawdata[,5:8], genes=rawdata[,1])
y$samples$lib.size <- colSums(y$counts)
y <- calcNormFactors(y)
Patient <- factor(c(1,1,51,51))
Tissue <- factor(c("T","T","N","T"))
data.frame(Sample=colnames(y),Patient,Tissue)
design <- model.matrix(~Patient+Tissue)
rownames(design) <- colnames(y)
y <- estimateGLMCommonDisp(y, design, verbose=TRUE)
y <- estimateGLMTrendedDisp(y, design)
y <- estimateGLMTagwiseDisp(y, design)
fit <- glmFit(y, design)
lrt <- glmLRT(fit); topTags(lrt)
topTags(lrt)


###########################################################

source("http://bioconductor.org/biocLite.R")
library("limma")
library("edgeR")

rawdata <- read.delim("3.isoforms.results", check.names=FALSE, stringsAsFactors=FALSE)
y <- DGEList(counts=rawdata[,5], genes=rawdata[,1])
y$samples$lib.size <- colSums(y$counts)
y <- calcNormFactors(y)
Patient <- factor(c(1,2))
Tissue <- factor(c("T","T"))
data.frame(Sample=colnames(y),Patient,Tissue)
design <- model.matrix(~Patient+Tissue)
rownames(design) <- colnames(y)
y <- estimateGLMCommonDisp(y, design, verbose=TRUE)
y <- estimateGLMTrendedDisp(y, design)
y <- estimateGLMTagwiseDisp(y, design)
fit <- glmFit(y, design)
lrt <- glmLRT(fit); topTags(lrt)
topTags(lrt)

------------------

source("http://bioconductor.org/biocLite.R")
library("limma")
library("edgeR")
rawdata <- read.delim("6.matrix", check.names=FALSE, stringsAsFactors=FALSE)
y <- DGEList(counts=rawdata[,2:7], genes=rawdata[,1])
head(rawdata)
y$samples$lib.size <- colSums(y$counts)
y <- calcNormFactors(y)
Patient <- factor(c(1,1,2,2,3,3))
Tissue <- factor(c("N","T","N","T","N","T"))
data.frame(Sample=colnames(y),Patient,Tissue)
design <- model.matrix(~Patient+Tissue)
rownames(design) <- colnames(y)
y <- estimateGLMCommonDisp(y, design, verbose=TRUE)
y <- estimateGLMTrendedDisp(y, design)
y <- estimateGLMTagwiseDisp(y, design)
fit <- glmFit(y, design)
lrt <- glmLRT(fit); topTags(lrt)
topTags(lrt)
write.table(topTags(lrt), file = "6.txt",append =FALSE, quote = TRUE, sep = " ",eol = "\n", na = "NA", dec = ".",row.names = TRUE,col.names = TRUE, qmethod = c("escape", "double"),fileEncoding = "")

-------------------------------
10matrix


source("http://bioconductor.org/biocLite.R")
library("limma")
library("edgeR")
rawdata <- read.delim("Intest.table", check.names=FALSE, stringsAsFactors=FALSE)
y <- DGEList(counts=rawdata[,2:101], genes=rawdata[,1])
head(rawdata)
y$samples$lib.size <- colSums(y$counts)
y <- calcNormFactors(y)
Patient <- factor(c(1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27,27,28,28,29,29,30,30,31,31,32,32,33,33,34,34,35,35,36,36,37,37,38,38,39,39,40,40,41,41,42,42,43,43,44,44,45,45,46,46,47,47,48,48,49,49,50,50))
Tissue <- factor(c("N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T","N","T"))
data.frame(Sample=colnames(y),Patient,Tissue)
design <- model.matrix(~Patient+Tissue)
rownames(design) <- colnames(y)
y <- estimateGLMCommonDisp(y, design, verbose=TRUE)
y <- estimateGLMTrendedDisp(y, design)
y <- estimateGLMTagwiseDisp(y, design)
fit <- glmFit(y, design)
lrt <- glmLRT(fit); topTags(lrt)
topTags(lrt)
write.table(topTags(lrt), file = "a40.txt",append =FALSE, quote = TRUE, sep = " ",eol = "\n", na = "NA", dec = ".",row.names = TRUE,col.names = TRUE, qmethod = c("escape", "double"),fileEncoding = "")



################################
3line
source("http://bioconductor.org/biocLite.R")
library("limma")
library("edgeR")
rawdata <- read.delim("Intest.table", check.names=FALSE, stringsAsFactors=FALSE)
y <- DGEList(counts=rawdata[,2:4], genes=rawdata[,1])
head(rawdata)
y$samples$lib.size <- colSums(y$counts)
y <- calcNormFactors(y)
Patient <- factor(c(1,2,3))
Tissue <- factor(c("N","T","T2"))
data.frame(Sample=colnames(y),Patient,Tissue)
design <- model.matrix(~Patient+Tissue)
rownames(design) <- colnames(y)
y <- estimateGLMCommonDisp(y, design, verbose=TRUE)
y <- estimateGLMTrendedDisp(y, design)
y <- estimateGLMTagwiseDisp(y, design)
fit <- glmFit(y, design)
lrt <- glmLRT(fit); topTags(lrt)
topTags(lrt)
write.table(topTags(lrt), file = "a40.txt",append =FALSE, quote = TRUE, sep = " ",eol = "\n", na = "NA", dec = ".",row.names = TRUE,col.names = TRUE, qmethod = c("escape", "double"),fileEncoding = "")

```

