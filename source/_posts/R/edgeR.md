---
title: "Edger"
url: edger
date: 2019/08/13
toc: true
excerpt: "Codes for hot to running EdgeR to call differential Expression Genes from RSEM result. (More details you can find in Trinity wiki)"
tags: [R, Bioinformatics, RNA-Seq]
category: [R, Bio, DEG]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.hrqFhdEKQNHjEho5wb4tFQHaE8?pid=Api&rs=1'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.hrqFhdEKQNHjEho5wb4tFQHaE8?pid=Api&rs=1'
priority: 10000
---

## Edger


## Example form Trinity
### Expression Differential

Attention:
 - Make sure Trinity is installed because this scripts needs few functions from re-packaged scripts.
 - If you didn't install the Trinity, please download *heatmap.3.R* *misc_rnaseq_funcs* *pairs3.R* *vioplot2.R* from [Github](https://github.com/trinityrnaseq/trinityrnaseq/tree/master/Analysis/DifferentialExpression/R), or paste them to your codes instead of source them. (I paste this three codes at the end of the page)
 - This script is running the differential expression **counts**. So, make sure you are handling an appropriate matrix.

```R
library(cluster)
library(Biobase)
library(qvalue)
library(fastcluster)
options(stringsAsFactors = FALSE)
NO_REUSE = F

## try to reuse earlier-loaded data if possible
if (file.exists("diffExpr.P1e-5_C2.matrix.RData") && ! NO_REUSE) {
    print('RESTORING DATA FROM EARLIER ANALYSIS')
    load("diffExpr.P1e-5_C2.matrix.RData")
} else {
  # loading Count matrix
    print('Reading matrix file.')
    primary_data = read.table("diffExpr.P1e-5_C2.matrix", header=T, com='', row.names=1, check.names=F, sep='\t')
    primary_data = as.matrix(primary_data)
}

## reading repackaged R function from scripts
## similar like import File/lib.py in python
source("/home/ken/Biosoft/trinityrnaseq-Trinity-v2.8.4/Analysis/DifferentialExpression/R/heatmap.3.R")
source("/home/ken/Biosoft/trinityrnaseq-Trinity-v2.8.4/Analysis/DifferentialExpression/R/misc_rnaseq_funcs.R")
source("/home/ken/Biosoft/trinityrnaseq-Trinity-v2.8.4/Analysis/DifferentialExpression/R/pairs3.R")
source("/home/ken/Biosoft/trinityrnaseq-Trinity-v2.8.4/Analysis/DifferentialExpression/R/vioplot2.R")

data = primary_data
myheatcol = colorpanel(75, 'purple','black','yellow')
sample_types = colnames(data)
nsamples = length(sample_types)
sample_colors = rainbow(nsamples)
sample_type_list = list()
for (i in 1:nsamples) {
    sample_type_list[[sample_types[i]]] = sample_types[i]
}
sample_factoring = colnames(data)
for (i in 1:nsamples) {
    sample_type = sample_types[i]
    replicates_want = sample_type_list[[sample_type]]
    sample_factoring[ colnames(data) %in% replicates_want ] = sample_type
}
initial_matrix = data # store before doing various data transformations
data = log2(data+1)
sample_factoring = colnames(data)
for (i in 1:nsamples) {
    sample_type = sample_types[i]
    replicates_want = sample_type_list[[sample_type]]
    sample_factoring[ colnames(data) %in% replicates_want ] = sample_type
}
sampleAnnotations = matrix(ncol=ncol(data),nrow=nsamples)
for (i in 1:nsamples) {
  sampleAnnotations[i,] = colnames(data) %in% sample_type_list[[sample_types[i]]]
}
sampleAnnotations = apply(sampleAnnotations, 1:2, function(x) as.logical(x))
sampleAnnotations = sample_matrix_to_color_assignments(sampleAnnotations, col=sample_colors)
rownames(sampleAnnotations) = as.vector(sample_types)
colnames(sampleAnnotations) = colnames(data)
data = as.matrix(data) # convert to matrix

## Centering rows
data = t(scale(t(data), scale=F))

write.table(data, file="diffExpr.P1e-5_C2.matrix.log2.centered.dat", quote=F, sep='  ');
if (nrow(data) < 2) { stop("

**** Sorry, at least two rows are required for this matrix.

");}
if (ncol(data) < 2) { stop("

**** Sorry, at least two columns are required for this matrix.

");}
sample_cor = cor(data, method='pearson', use='pairwise.complete.obs')
write.table(sample_cor, file="diffExpr.P1e-5_C2.matrix.log2.centered.sample_cor.dat", quote=F, sep='  ')
sample_dist = dist(t(data), method='euclidean')
hc_samples = hclust(sample_dist, method='complete')
pdf("diffExpr.P1e-5_C2.matrix.log2.centered.sample_cor_matrix.pdf")
sample_cor_for_plot = sample_cor
heatmap.3(sample_cor_for_plot, dendrogram='both', Rowv=as.dendrogram(hc_samples), Colv=as.dendrogram(hc_samples), col = myheatcol, scale='none', symm=TRUE, key=TRUE,density.info='none', trace='none', symkey=FALSE, symbreaks=F, margins=c(10,10), cexCol=1, cexRow=1, cex.main=0.75, main=paste("sample correlation matrix
", "diffExpr.P1e-5_C2.matrix.log2.centered") )
dev.off()
gene_cor = NULL
gene_dist = dist(data, method='euclidean')
if (nrow(data) <= 1) { message('Too few genes to generate heatmap'); quit(status=0); }
hc_genes = hclust(gene_dist, method='complete')
heatmap_data = data
pdf("diffExpr.P1e-5_C2.matrix.log2.centered.genes_vs_samples_heatmap.pdf")
heatmap.3(heatmap_data, dendrogram='both', Rowv=as.dendrogram(hc_genes), Colv=as.dendrogram(hc_samples), col=myheatcol, scale="none", density.info="none", trace="none", key=TRUE, keysize=1.2, cexCol=1, margins=c(10,10), cex.main=0.75, main=paste("samples vs. features
", "diffExpr.P1e-5_C2.matrix.log2.centered" ) )
dev.off()
##save(list=ls(all=TRUE), file="diffExpr.P1e-5_C2.matrix.RData")
```


### Test

## edgeR(out of date)


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
##############################################
��Դ����������ģ�� edgeR�������裺https://www.tanboyu.com/edger-users-guide.html
######################################################################################

#####################################################################################
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


##########################################################

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


############################################################

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



#################################
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



---

## Attachment
### heatmap.3.R
```R
## From: https://github.com/trinityrnaseq/trinityrnaseq/blob/master/Analysis/DifferentialExpression/R/heatmap.3.R
### pulled from here, and then tweaked slightly: http://www.biostars.org/p/18211/
## CODE
heatmap.3 <- function(x,
                      Rowv = TRUE, Colv = if (symm) "Rowv" else TRUE,
                      distfun = dist,
                      hclustfun = hclust,
                      dendrogram = c("both","row", "column", "none"),
                      symm = FALSE,
                      scale = c("none","row", "column"),
                      na.rm = TRUE,
                      revC = identical(Colv,"Rowv"),
                      add.expr,
                      breaks,
                      symbreaks = max(x < 0, na.rm = TRUE) || scale != "none",
                      col = "heat.colors",
                      colsep,
                      rowsep,
                      sepcolor = "white",
                      sepwidth = c(0.05, 0.05),
                      cellnote,
                      notecex = 1,
                      notecol = "cyan",
                      na.color = par("bg"),
                      trace = c("none", "column","row", "both"),
                      tracecol = "cyan",
                      hline = median(breaks),
                      vline = median(breaks),
                      linecol = tracecol,
                      margins = c(5,5),
                      ColSideColors,
                      RowSideColors,
                      side.height.fraction=0.1,
                      #cexRow = 0.2 + 1/log10(max(nr,2)),
                      #cexCol = 0.2 + 1/log10(max(nc,2)),
        cexRow = 0.2,
        cexCol = 0.2,                  

        scaleRangeMin,
        scaleRangeMax,


    cex.main = 1,
                      labRow = NULL,
                      labCol = NULL,
                      key = TRUE,
                      keysize = 1.5,
                      density.info = c("none", "histogram", "density"),
                      denscol = tracecol,
                      symkey = max(x < 0, na.rm = TRUE) || symbreaks,
                      densadj = 0.25,
                      main = NULL,
                      xlab = NULL,
                      ylab = NULL,
                      lmat = NULL,
                      lhei = NULL,
                      lwid = NULL,
                      NumColSideColors = 1,
                      NumRowSideColors = 1,
                      KeyValueName="Value",...){

    invalid <- function (x) {
      if (missing(x) || is.null(x) || length(x) == 0)
          return(TRUE)
      if (is.list(x))
          return(all(sapply(x, invalid)))
      else if (is.vector(x))
          return(all(is.na(x)))
      else return(FALSE)
    }



    x <- as.matrix(x)
    scale01 <- function(x, low = min(x), high = max(x)) {
        x <- (x - low)/(high - low)
        x
    }

    retval <- list()


    scale <- if (symm && missing(scale))
        "none"
    else match.arg(scale)

    dendrogram <- match.arg(dendrogram)

    trace <- match.arg(trace)

    density.info <- match.arg(density.info)

    if (length(col) == 1 && is.character(col))
        col <- get(col, mode = "function")

    if (!missing(breaks) && (scale != "none"))
        warning("Using scale=\"row\" or scale=\"column\" when breaks are",
            "specified can produce unpredictable results.", "Please consider using only one or the other.")

    if (is.null(Rowv) || is.na(Rowv))
        Rowv <- FALSE

    if (is.null(Colv) || is.na(Colv))
        Colv <- FALSE
    else if (Colv == "Rowv" && !isTRUE(Rowv))
        Colv <- FALSE

    if (length(di <- dim(x)) != 2 || !is.numeric(x))
        stop("`x' must be a numeric matrix")

    nr <- di[1]
    nc <- di[2]

    if (nr <= 1 || nc <= 1)
        stop("`x' must have at least 2 rows and 2 columns")
    #print(paste("nr:", nr, "nc:", nc, "cexCol:", cexCol, "cexRow:", cexRow))
    #stop("debug")



    if (!is.numeric(margins) || length(margins) != 2)
        stop("`margins' must be a numeric vector of length 2")

    if (missing(cellnote))
        cellnote <- matrix("", ncol = ncol(x), nrow = nrow(x))

    if (!inherits(Rowv, "dendrogram")) {
        if (((!isTRUE(Rowv)) || (is.null(Rowv))) && (dendrogram %in% c("both", "row"))) {
            if (is.logical(Colv) && (Colv))
                dendrogram <- "column"
            else dedrogram <- "none"

            warning("Discrepancy: Rowv is FALSE, while dendrogram is `",
                dendrogram, "'. Omitting row dendogram.")
        }
    }

    if (!inherits(Colv, "dendrogram")) {
        if (((!isTRUE(Colv)) || (is.null(Colv))) && (dendrogram %in% c("both", "column"))) {
            if (is.logical(Rowv) && (Rowv))
                dendrogram <- "row"
            else dendrogram <- "none"

            warning("Discrepancy: Colv is FALSE, while dendrogram is `",
                dendrogram, "'. Omitting column dendogram.")
        }
    }

   if (inherits(Rowv, "dendrogram")) {
        ddr <- Rowv
        rowInd <- order.dendrogram(ddr)
    }
    else if (is.integer(Rowv)) {
        hcr <- hclustfun(distfun(x))
        ddr <- as.dendrogram(hcr)
        ddr <- reorder(ddr, Rowv)
        rowInd <- order.dendrogram(ddr)
        if (nr != length(rowInd))
            stop("row dendrogram ordering gave index of wrong length")
    }
    else if (isTRUE(Rowv)) {
        Rowv <- rowMeans(x, na.rm = na.rm)
        hcr <- hclustfun(distfun(x))
        ddr <- as.dendrogram(hcr)
        ddr <- reorder(ddr, Rowv)
        rowInd <- order.dendrogram(ddr)
        if (nr != length(rowInd))
            stop("row dendrogram ordering gave index of wrong length")
    }
    else {
        rowInd <- nr:1
    }

   if (inherits(Colv, "dendrogram")) {
        ddc <- Colv
        colInd <- order.dendrogram(ddc)
    }
    else if (identical(Colv, "Rowv")) {
        if (nr != nc)
            stop("Colv = \"Rowv\" but nrow(x) != ncol(x)")
        if (exists("ddr")) {
            ddc <- ddr
            colInd <- order.dendrogram(ddc)
        }
        else colInd <- rowInd
    }
    else if (is.integer(Colv)) {
        hcc <- hclustfun(distfun(if (symm)
            x
        else t(x)))
        ddc <- as.dendrogram(hcc)
        ddc <- reorder(ddc, Colv)
        colInd <- order.dendrogram(ddc)
        if (nc != length(colInd))
            stop("column dendrogram ordering gave index of wrong length")
    }
    else if (isTRUE(Colv)) {
        Colv <- colMeans(x, na.rm = na.rm)
        hcc <- hclustfun(distfun(if (symm)
            x
        else t(x)))
        ddc <- as.dendrogram(hcc)
        ddc <- reorder(ddc, Colv)
        colInd <- order.dendrogram(ddc)
        if (nc != length(colInd))
            stop("column dendrogram ordering gave index of wrong length")
    }
    else {
        colInd <- 1:nc
    }

    retval$rowInd <- rowInd
    retval$colInd <- colInd
    retval$call <- match.call()

    x <- x[rowInd, colInd]  # rearrange matrix according to dendrograms
    x.unscaled <- x

    cellnote <- cellnote[rowInd, colInd]  # also rearrange the cellnotes

    # get labels
    if (is.null(labRow))
        labRow <- if (is.null(rownames(x)))
            (1:nr)[rowInd]
        else rownames(x)
    else labRow <- labRow[rowInd]
    if (is.null(labCol))
        labCol <- if (is.null(colnames(x)))
            (1:nc)[colInd]
        else colnames(x)
    else labCol <- labCol[colInd]


    ## do scaling of matrix according to Z-scores
    if (scale == "row") {
        retval$rowMeans <- rm <- rowMeans(x, na.rm = na.rm)
        x <- sweep(x, 1, rm)
        retval$rowSDs <- sx <- apply(x, 1, sd, na.rm = na.rm)
        x <- sweep(x, 1, sx, "/")
    }
    else if (scale == "column") {
        retval$colMeans <- rm <- colMeans(x, na.rm = na.rm)
        x <- sweep(x, 2, rm)
        retval$colSDs <- sx <- apply(x, 2, sd, na.rm = na.rm)
        x <- sweep(x, 2, sx, "/")
    }

    # number of breaks
    if (missing(breaks) || is.null(breaks) || length(breaks) < 1) {
        if (missing(col) || is.function(col))
            breaks <- 16
        else breaks <- length(col) + 1
    }

    # set breakpoints
    if (length(breaks) == 1) {
        if (missing(scaleRangeMin))
            scaleRangeMin = min(x, na.rm=na.rm)

        if (missing(scaleRangeMax))
            scaleRangeMax = max(x, na.rm=na.rm)


        if (!symbreaks) {
            breaks <- seq(scaleRangeMin, scaleRangeMax, length=breaks);
        } else {
            #extreme <- max(abs(x), na.rm = TRUE)
            extreme = max(abs(c(scaleRangeMin,scaleRangeMax)), na.rm=na.rm)
            breaks <- seq(-extreme, extreme, length = breaks)
        }
    }

    nbr <- length(breaks)
    ncol <- length(breaks) - 1

    if (class(col) == "function")
        col <- col(ncol)

    min.breaks <- min(breaks)
    max.breaks <- max(breaks)

    # adjust for out-of-range given break settings
    x[x < min.breaks] <- min.breaks
    x[x > max.breaks] <- max.breaks

    # layout height
    if (missing(lhei) || is.null(lhei))
        lhei <- c(keysize, 4)

    # layout width
    if (missing(lwid) || is.null(lwid))
        lwid <- c(keysize, 4)

    # define the layout
    if (missing(lmat) || is.null(lmat)) {
        lmat <- rbind(4:3, 2:1)

        if (!missing(ColSideColors)) {
            if (!is.character(ColSideColors) || ncol(ColSideColors) != nc)
                stop("'ColSideColors' must be a matrix of ncol(x) ", nc, " columns")
            lmat <- rbind(lmat[1, ] + 1, c(NA, 1), lmat[2, ] + 1)
            #lhei=c(lhei[1], side.height.fraction*NumColSideColors, lhei[2])
            side_height = min(side.height.fraction*nrow(ColSideColors), 1);
            lhei=c(lhei[1], side_height, lhei[2])
        }

        if (!missing(RowSideColors)) {
            if (!is.character(RowSideColors) || nrow(RowSideColors) != nr)
                stop("'RowSideColors' must be a matrix of nrow(x) ", nr, " rows.  It currently has ", nrow(RowSideColors), " rows.")
            lmat <- cbind(lmat[, 1] + 1, c(rep(NA, nrow(lmat) - 1), 1), lmat[,2] + 1)
            #lwid <- c(lwid[1], side.height.fraction*NumRowSideColors, lwid[2])
            side_width = min(side.height.fraction*ncol(RowSideColors), 1);
      lwid <- c(lwid[1], side_width, lwid[2])
        }
        lmat[is.na(lmat)] <- 0
    }

    if (length(lhei) != nrow(lmat))
        stop("lhei must have length = nrow(lmat) = ", nrow(lmat))
    if (length(lwid) != ncol(lmat))
        stop("lwid must have length = ncol(lmat) =", ncol(lmat))


  op <- par(no.readonly = TRUE)
    on.exit(par(op))

    layout(lmat, widths = lwid, heights = lhei, respect = FALSE)

  ###########################################
  ## Draw the colorbars for the annotations:
  ###########################################

    if (!missing(RowSideColors)) {
        if (!is.matrix(RowSideColors)){
                par(mar = c(margins[1], 0, 0, 0.5))
                image(rbind(1:nr), col = RowSideColors[rowInd], axes = FALSE)
        } else {
            par(mar = c(margins[1], 0, 0, 0.5))
            rsc = t(RowSideColors[rowInd, , drop=F])
            rsc.colors = matrix()
            rsc.names = names(table(rsc))
            rsc.i = 1
            for (rsc.name in rsc.names) {
                rsc.colors[rsc.i] = rsc.name
                rsc[rsc == rsc.name] = rsc.i
                rsc.i = rsc.i + 1
            }
            # print(rsc)
            rsc = matrix(as.numeric(rsc), nrow = dim(rsc)[1])
            #print("RSC: ", rsc)
            #print(rsc.colors)    
            image(1:nrow(rsc), 1:ncol(rsc), rsc, col = as.vector(rsc.colors), axes = FALSE, xlab="", ylab="")

      # add labels
            if (length(colnames(RowSideColors)) > 0) {  
                #axis(1, 0:(dim(rsc)[2] - 1)/(dim(rsc)[2] - 1), rownames(RowSideColors), las = 2, tick = FALSE)
        #axis(1, 0:(nrow(rsc)-1), colnames(RowSideColors), las = 2, tick = T) # ncol because transposed
              axis(1, 1:ncol(RowSideColors), labels=colnames(RowSideColors), las=2, cex.axis=0.5, tick=F, xlab="", ylab="")

      }
        }
    }



    if (!missing(ColSideColors)) {

        if (!is.matrix(ColSideColors)){
            par(mar = c(0.5, 0, 0, margins[2]))
            image(cbind(1:nc), col = ColSideColors[colInd], axes = FALSE)
        } else {
            par(mar = c(0.5, 0, 0, margins[2]))
            csc = ColSideColors[, colInd, drop=F]
            csc.colors = matrix()
            csc.names = names(table(csc))
            csc.i = 1
            for (csc.name in csc.names) {
                csc.colors[csc.i] = csc.name
                csc[csc == csc.name] = csc.i
                csc.i = csc.i + 1
            }
            csc = matrix(as.numeric(csc), nrow = dim(csc)[1])
            #print(csc)
            image(1:nrow(t(csc)), 1:ncol(t(csc)), t(csc), col = as.vector(csc.colors), axes = FALSE, xlab="", ylab="")

      # add labels
            if (length(rownames(ColSideColors)) > 0) {
                #axis(2, 0:(dim(csc)[2] - 1)/max(1,(dim(csc)[2] - 1)), colnames(ColSideColors), las = 2, tick = FALSE)
        axis(2, 1:(nrow(ColSideColors)), labels=rownames(ColSideColors), las = 2, tick = FALSE, cex.axis=0.5)
            }
        }
    }



    par(mar = c(margins[1], 0, 0, margins[2]))
    x <- t(x)
    cellnote <- t(cellnote)
    if (revC) {
        iy <- nr:1
        if (exists("ddr"))
            ddr <- rev(ddr)
        x <- x[, iy]
        cellnote <- cellnote[, iy]
    }
    else iy <- 1:nr

  # draw the central heatmap
  image(1:nc, 1:nr, x, xlim = 0.5 + c(0, nc), ylim = 0.5 + c(0, nr), axes = FALSE, xlab = "", ylab = "", col = col, breaks = breaks, ...)

  # store the matrix drawn
  retval$carpet <- x

  # store the dendrograms
  if (exists("ddr"))
        retval$rowDendrogram <- ddr
    if (exists("ddc"))
        retval$colDendrogram <- ddc

  # store the breaks
  retval$breaks <- breaks

  # store the colormap used
  retval$col <- col

  # specially color in the na values
    if (!invalid(na.color) & any(is.na(x))) { # load library(gplots)
        mmat <- ifelse(is.na(x), 1, NA)
        image(1:nc, 1:nr, mmat, axes = FALSE, xlab = "", ylab = "", col = na.color, add = TRUE)
    }

  # X-axis column labels
    axis(1, 1:nc, labels = labCol, las = 2, line = -0.5, tick = 0, cex.axis = cexCol)

  # X-axis title
    if (!is.null(xlab))
        mtext(xlab, side = 1, line = margins[1] - 1.25)

  # Y-axis row labeling
    axis(4, iy, labels = labRow, las = 2, line = -0.5, tick = 0,
        cex.axis = cexRow)

  # Y-axis title
    if (!is.null(ylab))
        mtext(ylab, side = 4, line = margins[2] - 1.25)

     if (!missing(add.expr))
        eval(substitute(add.expr))
    if (!missing(colsep))
        for (csep in colsep) rect(xleft = csep + 0.5, ybottom = rep(0, length(csep)), xright = csep + 0.5 + sepwidth[1], ytop = rep(ncol(x) + 1, csep), lty = 1, lwd = 1, col = sepcolor, border = sepcolor)
    if (!missing(rowsep))
        for (rsep in rowsep) rect(xleft = 0, ybottom = (ncol(x) + 1 - rsep) - 0.5, xright = nrow(x) + 1, ytop = (ncol(x) + 1 - rsep) - 0.5 - sepwidth[2], lty = 1, lwd = 1, col = sepcolor, border = sepcolor)


  min.scale <- min(breaks)
    max.scale <- max(breaks)
    x.scaled <- scale01(t(x), min.scale, max.scale)

  # column trace
  if (trace %in% c("both", "column")) {
        retval$vline <- vline
        vline.vals <- scale01(vline, min.scale, max.scale)
        for (i in colInd) {
            if (!is.null(vline)) {
                abline(v = i - 0.5 + vline.vals, col = linecol, lty = 2)
            }
            xv <- rep(i, nrow(x.scaled)) + x.scaled[, i] - 0.5
            xv <- c(xv[1], xv)
            yv <- 1:length(xv) - 0.5
            lines(x = xv, y = yv, lwd = 1, col = tracecol, type = "s")
        }
    }

  # row trace
    if (trace %in% c("both", "row")) {
        retval$hline <- hline
        hline.vals <- scale01(hline, min.scale, max.scale)
        for (i in rowInd) {
            if (!is.null(hline)) {
                abline(h = i + hline, col = linecol, lty = 2)
            }
            yv <- rep(i, ncol(x.scaled)) + x.scaled[i, ] - 0.5
            yv <- rev(c(yv[1], yv))
            xv <- length(yv):1 - 0.5
            lines(x = xv, y = yv, lwd = 1, col = tracecol, type = "s")
        }
    }

  # add cell labels
    if (!missing(cellnote))
        text(x = c(row(cellnote)), y = c(col(cellnote)), labels = c(cellnote), col = notecol, cex = notecex)

  ###########################
  ## Plot the row dendrogram
  ###########################

    par(mar = c(margins[1], 0, 0, 0))
    if (dendrogram %in% c("both", "row")) {
        plot(ddr, horiz = TRUE, axes = FALSE, yaxs = "i", leaflab = "none")
    }
    else plot.new()

  #############################
  ## Plot the column dendrogram
  #############################

    par(mar = c(0, 0, if (!is.null(main)) 5 else 0, margins[2]))
    if (dendrogram %in% c("both", "column")) {
        plot(ddc, axes = FALSE, xaxs = "i", leaflab = "none")
    }
    else plot.new()

    if (!is.null(main))
        title(main, cex.main=cex.main) #cex.main = 1.5 * op[["cex.main"]])


  ############################
  ## Add the Color Chart
  ############################

    if (key) {
        par(mar = c(5, 4, 2, 1), cex = 0.75)
        tmpbreaks <- breaks
        if (symkey) {
            max.raw <- max(abs(c(x, breaks)), na.rm = TRUE)
            min.raw <- -max.raw
            tmpbreaks[1] <- -max(abs(x), na.rm = TRUE)
            tmpbreaks[length(tmpbreaks)] <- max(abs(x), na.rm = TRUE)
        }
        else {
            min.raw <- min(c(x,breaks), na.rm = TRUE)
            max.raw <- max(c(x,breaks), na.rm = TRUE)
        }

        message('for plotting:: min.raw: ', min.raw, ' max.raw: ', max.raw);

        z <- seq(min.raw, max.raw, length = length(col))
        image(z = matrix(z, ncol = 1), col = col, breaks = tmpbreaks,
            xaxt = "n", yaxt = "n")
        par(usr = c(0, 1, 0, 1))
        lv <- pretty(breaks)
        xv <- scale01(as.numeric(lv), min.raw, max.raw)
        axis(1, at = xv, labels = lv)
        if (scale == "row")
            mtext(side = 1, "Row Z-Score", line = 2)
        else if (scale == "column")
            mtext(side = 1, "Column Z-Score", line = 2)
        else mtext(side = 1, KeyValueName, line = 2)
        if (density.info == "density") {
            dens <- density(x, adjust = densadj, na.rm = TRUE)
            omit <- dens$x < min(breaks) | dens$x > max(breaks)
            dens$x <- dens$x[-omit]
            dens$y <- dens$y[-omit]
            dens$x <- scale01(dens$x, min.raw, max.raw)
            lines(dens$x, dens$y/max(dens$y) * 0.95, col = denscol,
                lwd = 1)
            axis(2, at = pretty(dens$y)/max(dens$y) * 0.95, pretty(dens$y))
            title("Color Key\nand Density Plot")
            par(cex = 0.5)
            mtext(side = 2, "Density", line = 2)
        }
        else if (density.info == "histogram") {
            h <- hist(x, plot = FALSE, breaks = breaks)
            hx <- scale01(breaks, min.raw, max.raw)
            hy <- c(h$counts, h$counts[length(h$counts)])
            lines(hx, hy/max(hy) * 0.95, lwd = 1, type = "s",
                col = denscol)
            axis(2, at = pretty(hy)/max(hy) * 0.95, pretty(hy))
            title("Color Key\nand Histogram")
            par(cex = 0.5)
            mtext(side = 2, "Count", line = 2)
        }
        else title("Color Key")
    }
    else plot.new()

    retval$colorTable <- data.frame(low = retval$breaks[-length(retval$breaks)], high = retval$breaks[-1], color = retval$col)

    invisible(retval)
}



## EXAMPLE USAGE

## example of colsidecolors rowsidecolors (single column, single row)
##mat <- matrix(1:100, byrow=T, nrow=10)
##column_annotation <- sample(c("red", "blue", "green"), 10, replace=T)
##column_annotation <- as.matrix(column_annotation)
##colnames(column_annotation) <- c("Variable X")

##row_annotation <- sample(c("red", "blue", "green"), 10, replace=T)
##row_annotation <- as.matrix(t(row_annotation))
##rownames(row_annotation) <- c("Variable Y")

##heatmap.3(mat, RowSideColors=row_annotation, ColSideColors=column_annotation)

## multiple column and row
##mat <- matrix(1:100, byrow=T, nrow=10)
##column_annotation <- matrix(sample(c("red", "blue", "green"), 20, replace=T), ncol=2)
##colnames(column_annotation) <- c("Variable X1", "Variable X2")

##row_annotation <- matrix(sample(c("red", "blue", "green"), 20, replace=T), nrow=2)
##rownames(row_annotation) <- c("Variable Y1", "Variable Y2")

##heatmap.3(mat, RowSideColors=row_annotation, ColSideColors=column_annotation)



##---------------------------------------------------------------------------------
##---------------------------------------------------------------------------------
##---------------------------------------------------------------------------------

## Borrowing the following from gplots  (gplots isn't compatible with R 3.0 (yet), and so bypassing it for now).

colorpanel = function (n, low, mid, high)
{
    if (missing(mid) || missing(high)) {
        low <- col2rgb(low)
        if (missing(high))
            high <- col2rgb(mid)
        else high <- col2rgb(high)
        red <- seq(low[1, 1], high[1, 1], length = n)/255
        green <- seq(low[3, 1], high[3, 1], length = n)/255
        blue <- seq(low[2, 1], high[2, 1], length = n)/255
    }
    else {
        isodd <- odd(n)
        if (isodd) {
            n <- n + 1
        }
        low <- col2rgb(low)
        mid <- col2rgb(mid)
        high <- col2rgb(high)
        lower <- floor(n/2)
        upper <- n - lower
        red <- c(seq(low[1, 1], mid[1, 1], length = lower), seq(mid[1,
            1], high[1, 1], length = upper))/255
        green <- c(seq(low[3, 1], mid[3, 1], length = lower),
            seq(mid[3, 1], high[3, 1], length = upper))/255
        blue <- c(seq(low[2, 1], mid[2, 1], length = lower),
            seq(mid[2, 1], high[2, 1], length = upper))/255
        if (isodd) {
            red <- red[-(lower + 1)]
            green <- green[-(lower + 1)]
            blue <- blue[-(lower + 1)]
        }
    }
    rgb(red, blue, green)
}


greenred = function (n)  {
    colorpanel(n, "green", "black", "red")
}

odd = function (x) {
    x%%2 == 1
}

even = function (x) {
    x%%2 == 0
}
```

### misc_rnaseq_funcs.R
```R
## from https://github.com/trinityrnaseq/trinityrnaseq/blob/master/Analysis/DifferentialExpression/R/misc_rnaseq_funcs.R

plot_counts_matrix_log2_dist = function(matrix_file) {


  data = read.table(file=matrix_file, com='', row.names=1, header=T)

  conditions = colnames(data)
  colors = rainbow(length(conditions))


  plot(density(log2(data[,1])), col=colors[1], main=matrix_file, xlab='log2(frag_counts)', ylab='density')

  for (i in 2:length(data[1,])) {

    points(density(log2(data[,i])), type='l', col=colors[i])

  }

  legend('topright', conditions, col=colors, pch=15)

}


matrix_to_color_assignments = function(matrix_m, col=NULL, by=c("matrix", "row", "col")) {

  if (! is.matrix(matrix_m))
    stop("Error, matrix_to_color_assignments() requires a matrix as parameter.")
  num_colors = 0

    if (is.null(col)) {
        num_colors = min(nrow(matrix_m), ncol(matrix_m))
        col = rainbow(num_colors)
    }
    else {
        num_colors = length(col)
    }

    by = match.arg(by)

    if (by == "matrix") {

        min_val = min(matrix_m, na.rm=T)
      matrix_m = matrix_m - min_val
      max_val = max(matrix_m, na.rm=T)
      matrix_m = matrix_m / max_val * num_colors
        #print(matrix_m)
         matrix_m = apply(matrix_m, 1:2, function(x) ifelse (x<1, as.character(col[1]), as.character(col[x])));

        matrix_m = matrix(as.character(matrix_m), nrow=dim(matrix_m)[1])
  }
  else {

    row_or_col_only_color_selector_func = function(x) {
        a = min(x, na.rm=T);
        b = max(x, na.rm=T);
        c = (x-a)/(b-a) * num_colors;
                c = round(c);
        c = ifelse (c<1, 1, c);
                #print(paste(c("color selection: (a)", a, " (b)", b, " (c)", paste(c, sep=','))));
                colors = as.character(col[c]);
                return(colors);
    }

    if (by == "row") {
            matrix_m = apply(matrix_m, 1, row_or_col_only_color_selector_func);
            print(matrix_m)
            print("dim matrix_m after apply"); print(dim(matrix_m))
            matrix_m = t(matrix_m);
            print("dim matrix_m after transpose: "); print(dim(matrix_m))
    }
    else {
      # by column
      matrix_m = apply(matrix_m, 2, row_or_col_only_color_selector_func);
    }
  }

  #print(matrix_m)
  return(matrix_m)
}

sample_matrix_to_color_assignments = function(sampleAnnotationsMatrix, colors) {

  if (missing(colors))
    colors = rainbow(nrow(sampleAnnotationsMatrix))

  nsamples = nrow(sampleAnnotationsMatrix);

  if (length(colors) < nrow(sampleAnnotationsMatrix))
    stop("Error, only ", length(colors), " colors specified, but have ", nsamples, " samples");

  for (i in 1:nrow(sampleAnnotationsMatrix)) {
    c = colors[i]
    sampleAnnotationsMatrix[i,] = sapply(sampleAnnotationsMatrix[i,], function(x) ifelse( x, as.character(c), 'white'))
  }

  return(sampleAnnotationsMatrix);

}
```
### pairs3.R
```R
## from: https://github.com/trinityrnaseq/trinityrnaseq/blob/master/Analysis/DifferentialExpression/R/pairs3.R
### snagged from: http://stackoverflow.com/questions/9680783/how-can-i-change-the-axis-position-for-pairs

## modified to include function for modifying X/Y values.


pairs3 <-
  function (x, labels, XY_convert_fun = NULL, CustomColorFun = NULL, panel = points, ..., lower.panel = panel,
            upper.panel = panel, diag.panel = NULL, text.panel = textPanel,
            label.pos = 0.5 + has.diag/3, cex.labels = NULL, font.labels = 1,
            row1attop = TRUE, gap = 1)
  {
    textPanel <- function(x = 0.5, y = 0.5, txt, cex, font) text(x,
                                                                 y, txt, cex = cex, font = font)
    localAxis <- function(side, x, y, xpd, bg, col = NULL, main,
                          oma, ...) {
      if (side%%2 == 1)
        Axis(x, side = side, xpd = NA, ...)
      else Axis(y, side = side, xpd = NA, ...)
    }
    localPlot <- function(..., main, oma, font.main, cex.main) {
        plot(...)
    }
    localLowerPanel <- function(..., main, oma, font.main, cex.main) lower.panel(...)
    localUpperPanel <- function(..., main, oma, font.main, cex.main) upper.panel(...)
    localDiagPanel <- function(..., main, oma, font.main, cex.main) diag.panel(...)
    dots <- list(...)
    nmdots <- names(dots)
    if (!is.matrix(x)) {
      x <- as.data.frame(x)
      for (i in seq_along(names(x))) {
        if (is.factor(x[[i]]) || is.logical(x[[i]]))
          x[[i]] <- as.numeric(x[[i]])
        if (!is.numeric(unclass(x[[i]])))
          stop("non-numeric argument to 'pairs'")
      }
    }
    else if (!is.numeric(x))
      stop("non-numeric argument to 'pairs'")
    panel <- match.fun(panel)
    if ((has.lower <- !is.null(lower.panel)) && !missing(lower.panel))
      lower.panel <- match.fun(lower.panel)
    if ((has.upper <- !is.null(upper.panel)) && !missing(upper.panel))
      upper.panel <- match.fun(upper.panel)
    if ((has.diag <- !is.null(diag.panel)) && !missing(diag.panel))
      diag.panel <- match.fun(diag.panel)
    if (row1attop) {
      tmp <- lower.panel
      lower.panel <- upper.panel
      upper.panel <- tmp
      tmp <- has.lower
      has.lower <- has.upper
      has.upper <- tmp
    }
    nc <- ncol(x)
    if (nc < 2)
      stop("only one column in the argument to 'pairs'")
    has.labs <- TRUE
    if (missing(labels)) {
      labels <- colnames(x)
      if (is.null(labels))
        labels <- paste("var", 1L:nc)
    }
    else if (is.null(labels))
      has.labs <- FALSE
    oma <- if ("oma" %in% nmdots)
      dots$oma
    else NULL
    main <- if ("main" %in% nmdots)
      dots$main
    else NULL
    if (is.null(oma)) {
      oma <- c(4, 4, 4, 4)
      if (!is.null(main))
        oma[3L] <- 6
    }
    opar <- par(mfrow = c(nc, nc), mar = rep.int(gap/2, 4), oma = oma)
    on.exit(par(opar))
    dev.hold()
    on.exit(dev.flush(), add = TRUE)
    for (i in if (row1attop)
      1L:nc
         else nc:1L) for (j in 1L:nc) {

      #print(paste(i,"vs", j));
      xvals = x[,j]
      yvals = x[,i]      

      if ( (i != j) && ! is.null(XY_convert_fun)) {

        res = XY_convert_fun(xvals, yvals);
        xvals = res[['x']]
        yvals = res[['y']]
      }

            col='black' # default
            if (! is.null(CustomColorFun))
                col=CustomColorFun(xvals,yvals)

       #     get_list_from_ellipsis2 <- function(...) as.list(substitute(list(...)))[-1L]
       # print(get_list_from_ellipsis2(...));stop();

           localPlot(xvals, yvals, xlab = "", ylab = "",axes = F, #col=ifelse(abs(xvals-yvals)>2, 'red', 'black'),
                     type = "n", ...)
           if (i == j || (i < j && has.lower) || (i > j && has.upper)) {
             box()
             # edited here...
             #           if (i == 1 && (!(j%%2) || !has.upper || !has.lower))
             #           localAxis(1 + 2 * row1attop, x[, j], x[, i],
             #                       ...)
             # draw x-axis
             if (i != j) #(i == nc & j != nc)
               localAxis(1, xvals, yvals,
                         ...)
             # draw y-axis
             if (j != i) #(j == 1 & i != 1)
               localAxis(2, xvals, yvals, ...)
             #           if (j == nc && (i%%2 || !has.upper || !has.lower))
             #             localAxis(4, x[, j], x[, i], ...)
             mfg <- par("mfg")
             if (i == j) {
               if (has.diag)
                 localDiagPanel(as.vector(yvals), ...)
               if (has.labs) {
                 par(usr = c(0, 1, 0, 1))
                 if (is.null(cex.labels)) {
                   l.wid <- strwidth(labels, "user")
                   cex.labels <- max(0.8, min(2, 0.9/max(l.wid)))
                 }
                 text.panel(0.5, label.pos, labels[i], cex = cex.labels,
                            font = font.labels)
               }
             }
             else if (i < j)
               localLowerPanel(as.vector(xvals), as.vector(yvals), col=col, ...)
             else localUpperPanel(as.vector(xvals), as.vector(yvals), col=col, ...)
             if (any(par("mfg") != mfg))
               stop("the 'panel' function made a new plot")
           }
           else par(new = FALSE)
         }
    if (!is.null(main)) {
      font.main <- if ("font.main" %in% nmdots)
        dots$font.main
      else par("font.main")
      cex.main <- if ("cex.main" %in% nmdots)
        dots$cex.main
      else par("cex.main")
      mtext(main, 3, 3, TRUE, 0.5, cex = cex.main, font = font.main)
    }
    invisible(NULL)
  }

### Demo it:
demo_pairs3 = function (custom_fun=F) {
    data(iris)

  xy_conv = function(x,y) {

    res = list();
    res[['x']] = (x+y)/2;
    res[['y']] = x - y;

    return(res);
  }

  if (custom_fun) {
    pairs3(iris[1:4], XY_convert_fun = xy_conv, main = "Anderson's Iris Data -- 3 species",pch = 21, bg = c("red", "green3", "blue")[unclass(iris$Species)])
  }
  else {
    pairs3(iris[1:4], main = "Anderson's Iris Data -- 3 species",pch = 21, bg = c("red", "green3", "blue")[unclass(iris$Species)])
  }
}
```
### vioplot2.R
```R
## from: https://github.com/trinityrnaseq/trinityrnaseq/blob/master/Analysis/DifferentialExpression/R/vioplot2.R

###################################################################################
### From:  https://stackoverflow.com/questions/22410606/violin-plot-with-list-input
### and slightly modified to my liking here.

vioplot2<-function (x, ..., range = 1.5, h = NULL, ylim = NULL, names = NULL,
                    horizontal = FALSE, col = c("magenta"), border = "black", lty = 1,
                    lwd = 1, rectCol = "black", colMed = "white", pchMed = 19,
                    at, add = FALSE, wex = 1, drawRect = TRUE)
{

    library(sm)


    if(!is.list(x)){
        datas <- list(x, ...)
    } else{
        datas<-x
    }
    n <- length(datas)
    if (missing(at))
        at <- 1:n
    upper <- vector(mode = "numeric", length = n)
    lower <- vector(mode = "numeric", length = n)
    q1 <- vector(mode = "numeric", length = n)
    q3 <- vector(mode = "numeric", length = n)
    med <- vector(mode = "numeric", length = n)
    base <- vector(mode = "list", length = n)
    height <- vector(mode = "list", length = n)
    baserange <- c(Inf, -Inf)
    args <- list(display = "none")
    if (!(is.null(h)))
        args <- c(args, h = h)
    for (i in 1:n) {
        data <- datas[[i]]
        data.min <- min(data)
        data.max <- max(data)
        q1[i] <- quantile(data, 0.25)
        q3[i] <- quantile(data, 0.75)
        med[i] <- median(data)
        iqd <- q3[i] - q1[i]
        upper[i] <- min(q3[i] + range * iqd, data.max)
        lower[i] <- max(q1[i] - range * iqd, data.min)
        est.xlim <- c(min(lower[i], data.min), max(upper[i],
                                                   data.max))
        smout <- do.call("sm.density", c(list(data, xlim = est.xlim),
                                         args))
        hscale <- 0.4/max(smout$estimate) * wex
        base[[i]] <- smout$eval.points
        height[[i]] <- smout$estimate * hscale
        t <- range(base[[i]])
        baserange[1] <- min(baserange[1], t[1])
        baserange[2] <- max(baserange[2], t[2])
    }
    if (!add) {
        xlim <- if (n == 1)
                    at + c(-0.5, 0.5)
                else range(at) + min(diff(at))/2 * c(-1, 1)
        if (is.null(ylim)) {
            ylim <- baserange
        }
    }
    if (is.null(names)) {
        label <- 1:n
    }
    else {
        label <- names
    }
    boxwidth <- 0.05 * wex
    if (!add)
        plot.new()
    if (!horizontal) {
        if (!add) {
            plot.window(xlim = xlim, ylim = ylim)
            axis(2)
            axis(1, at = at, label = label)
        }
        box()
        for (i in 1:n) {
            polygon(c(at[i] - height[[i]], rev(at[i] + height[[i]])),
                    c(base[[i]], rev(base[[i]])), col = col[i], border = border,
                    lty = lty, lwd = lwd)
            if (drawRect) {
                lines(at[c(i, i)], c(lower[i], upper[i]), lwd = lwd,
                      lty = lty)
                rect(at[i] - boxwidth/2, q1[i], at[i] + boxwidth/2,
                     q3[i], col = rectCol)
                points(at[i], med[i], pch = pchMed, col = colMed)
            }
        }
    }
    else {
        if (!add) {
            plot.window(xlim = ylim, ylim = xlim)
            axis(1)
            axis(2, at = at, label = label)
        }
        box()
        for (i in 1:n) {
            polygon(c(base[[i]], rev(base[[i]])), c(at[i] - height[[i]],
                                                    rev(at[i] + height[[i]])), col = col[i], border = border,
                    lty = lty, lwd = lwd)
            if (drawRect) {
                lines(c(lower[i], upper[i]), at[c(i, i)], lwd = lwd,
                      lty = lty)
                rect(q1[i], at[i] - boxwidth/2, q3[i], at[i] +
                                                       boxwidth/2, col = rectCol)
                points(med[i], at[i], pch = pchMed, col = colMed)
            }
        }
    }
    invisible(list(upper = upper, lower = lower, median = med,
                   q1 = q1, q3 = q3))
}
```
