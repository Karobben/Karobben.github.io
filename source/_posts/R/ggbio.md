---
toc: true
url: ggbio
covercopy: © Karobben
priority: 10000
date: 2022-07-23 15:03:12
title: "ggbio"
ytitle: "ggbio"
description: "ggbio, a powerful package to plot all kinds of sequence plot"
excerpt: "ggbio, a powerful package to plot all kinds of sequence plot"
tags: [R, Bioinformatics, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: "https://s1.ax1x.com/2022/07/24/jXXXef.png"
thumbnail: "https://s1.ax1x.com/2022/07/24/jXXXef.png"
---

## ggbio

### SNP plot from bam file

To plot this plot, you need the

By doing this, we need a genome vector we build by `BSgenome`. You can follow the instruction to build your own `BSgenome` library. Here what I use is pre-build and name as `BSgenome.dme.BDGP6.32`
Bam file was load by `Rsamtools`

```r
library(ggbio)
library(Rsamtools)
library(BSgenome.dme.BDGP6.32)

# define the regions you'd like to check
wh <- as(c("2R:24671294-24687896"), "GRanges")
bam<-BamFile(file="out.bam", index="out.bam.bai")

autoplot(bam, which =wh, bsgenome =BSgenome.dme.BDGP6.32, stat = "mismatch")
```

|![](https://s1.ax1x.com/2022/07/24/jXXQZ8.png)|
|:-:|

### GTF files

For this plot, some gtf files can not call gene names. So, I'll show an Alternative why to show symbols in the plot.

Reference: [girke.bioinformatics.ucr.edu; 2016](http://girke.bioinformatics.ucr.edu/CSHL_RNAseq/mydoc/mydoc_Rgraphics_7/ )

```r
library(ggbio)
library(rtracklayer)
library(GenomicFeatures)
library(clusterProfiler)
library(org.Dm.eg.db)

txdb <- makeTxDbFromGFF(file="genom.gtf", format="gtf")
Trans <- transcriptsBy(txdb, "gene")
tmp <- bitr(names(Trans), fromType="FLYBASE", toType="SYMBOL", OrgDb="org.Dm.eg.db")
names(Trans)[!is.na(tmp[[2]][match(names(Trans), tmp[[1]])])] <- tmp[[2]][match(names(Trans), tmp[[1]])][!is.na(tmp[[2]][match(names
    (Trans), tmp[[1]])])]

P1 <- autoplot(txdb, which= Trans$Mmp1)+ theme_bw()
tmp = range(Trans$Mmp1)
rg = c(tmp@ranges@start, tmp@ranges@start+tmp@ranges@width)
wh = as(c(paste(tmp@seqnames@values, ":", tmp@ranges@start, "-", tmp@ranges@start+tmp@ranges@width, sep ="")), "GRanges")
P2 <- autoplot(bam, which =wh, bsgenome =BSgenome.dme.BDGP6.32, stat = "mismatch") + theme_bw() + theme(legend.position="none")
tracks(Coverage=P2, Transcripts=P1, heights = c(0.2, 0.1)) + ylab("")
```

![](https://s1.ax1x.com/2022/07/24/jXX2sx.png)

### VCF file plot

```r
library(reshape2)
library(VariantAnnotation)

VCF <- read.table("out.vcf")
TB <- VCF[VCF$V1== as.character(tmp@seqnames@values),]
TB <- TB[TB$V2>=min(rg),]
TB <- TB[TB$V2<=max(rg),]
TB <- TB[c("V2", "V4", "V5")]
colnames(TB) <- c("x", "Ref", "Alt")
TB <- melt(TB, id.vars = "x" )
P1 <- autoplot(txdb, which= Trans$Mmp1, gap.geom = "chevron")+ theme_bw() +
    geom_text(aes(x=0, y=0, label=0,color="red"))+
    coord_cartesian(xlim =rg, expand = T)
P2 <- autoplot(bam, which =wh, bsgenome =BSgenome.dme.BDGP6.32, stat = "mismatch") + theme_bw()

P3 <- ggplot() + geom_tile(data=TB,aes(x= x, y= variable, label=value, fill= value), width=(rg[2]-rg[1])/300) +
    coord_cartesian(xlim =rg, expand = T) + theme_bw()
tracks(Coverage=P2, VCF = P3, Transcripts=P1, heights = c(0.2, 0.1, 0.2)) + ylab("")
```

![](https://s1.ax1x.com/2022/07/24/jXXjw8.png)

### 3 in 1 function

```r
library(ggbio)
library(reshape2)
library(Rsamtools)
library(rtracklayer)
library(org.Dm.eg.db)
library(GenomicFeatures)
library(clusterProfiler)
library(VariantAnnotation)
library(BSgenome.dme.BDGP6.32)


# read files: vcf, bam, gtf
VCF <- read.table("out.vcf")                            
bam<-BamFile(file="out.bam", index="out.bam.bai")
txdb <- makeTxDbFromGFF(file="genom.gtf", format="gtf")

# Change the name of the Trans into Sample
Trans <- transcriptsBy(txdb, "gene")
tmp <- bitr(names(Trans), fromType="FLYBASE", toType="SYMBOL", OrgDb="org.Dm.eg.db")
names(Trans)[!is.na(tmp[[2]][match(names(Trans), tmp[[1]])])] <- tmp[[2]][match(names(Trans), tmp[[1]])][!is.na(tmp[[2]][match(names
    (Trans), tmp[[1]])])]

PLOT_3 <- function(GENE){
    tmp = range(Trans[GENE])[[1]]
    rg = c(tmp@ranges@start, tmp@ranges@start+tmp@ranges@width)
    wh = as(c(paste(tmp@seqnames@values, ":", tmp@ranges@start, "-", tmp@ranges@start+tmp@ranges@width, sep ="")), "GRanges")

    TB <- VCF[VCF$V1== as.character(tmp@seqnames@values),]
    TB <- TB[TB$V2>=min(rg),]
    TB <- TB[TB$V2<=max(rg),]
    TB <- TB[c("V2", "V4", "V5")]
    colnames(TB) <- c("x", "Ref", "Alt")
    TB <- melt(TB, id.vars = "x" )
    P1 <- autoplot(txdb, which= Trans[GENE][[1]], gap.geom = "chevron")+ theme_bw() +
        geom_text(aes(x=0, y=0, label=0,color="red"))+
        coord_cartesian(xlim =rg, expand = T)
    P2 <- autoplot(bam, which =wh, bsgenome =BSgenome.dme.BDGP6.32, stat = "mismatch") + theme_bw()

    P3 <- ggplot() + geom_tile(data=TB,aes(x= x, y= variable, label=value, fill= value), width=(rg[2]-rg[1])/300) +
        coord_cartesian(xlim =rg, expand = T) + theme_bw()
    tracks(Coverage=P2, VCF = P3, Transcripts=P1, heights = c(0.2, 0.1, 0.2)) + ylab("")
}

PLOT_3("Sin3A")
```

![](https://s1.ax1x.com/2022/07/24/jXXXef.png)


## Multiplot

```r
library(ggbio)
library(stringr)
library(reshape2)
library(Rsamtools)
library(rtracklayer)
library(org.Dm.eg.db)
library(GenomicFeatures)
library(clusterProfiler)
library(VariantAnnotation)
library(BSgenome.dme.BDGP6.32)

GTF= "/media/ken/BackUP/Drosophila/Drosophila_melanogaster.BDGP6.32.104.chr.EGFP.GAL4.mCD8GFP.gtf"
txdb <- makeTxDbFromGFF(file=GTF, format="gtf")
# Change the name of the Trans into Sample
Trans <- transcriptsBy(txdb, "gene")
tmp <- bitr(names(Trans), fromType="FLYBASE", toType="SYMBOL", OrgDb="org.Dm.eg.db")
names(Trans)[!is.na(tmp[[2]][match(names(Trans), tmp[[1]])])] <- tmp[[2]][match(names(Trans), tmp[[1]])][!is.na(tmp[[2]][match(names
    (Trans), tmp[[1]])])]

BAM_Dir = "/run/user/1000/gvfs/sftp:host=cypress1.tulane.edu,user=wliu15/lustre/project/wdeng7/wliu15/Bam/"
VCF_Dir = "/run/user/1000/gvfs/sftp:host=cypress1.tulane.edu,user=wliu15/lustre/project/wdeng7/wliu15/vcf/"

Bam_list <- c("wt_10day_1_S27Aligned.sortedByCoord.out.bam",
    "G1F1_S31Aligned.sortedByCoord.out.bam",
    "G50-FE_TUMOR-a_S37Aligned.sortedByCoord.out.bam"
    )

GENE = "N"
RNA_plot <- function(GENE){
    tmp = range(Trans[GENE])[[1]]
    wh = as(c(paste(tmp@seqnames@values, ":", tmp@ranges@start, "-", tmp@ranges@start+tmp@ranges@width, sep ="")), "GRanges")
    rg = c(tmp@ranges@start, tmp@ranges@start+tmp@ranges@width)

    Result = c()
    Result2 = c()
    for (sample in Bam_list){
        # read files: vcf, bam, gtf
        VCF <- read.table(paste(VCF_Dir, sample, ".vcf", sep=''))

        bam<-BamFile(file=paste(BAM_Dir, sample, sep=""), index=paste(BAM_Dir, sample, ".bai", sep=""))

        P2 <- autoplot(bam, which =wh, bsgenome =BSgenome.dme.BDGP6.32, stat = "mismatch") + theme_bw()  +  guides(color=guide_legend(title=""))
        Result <- c(Result, P2)


        TB <- VCF[VCF$V1== as.character(tmp@seqnames@values),]
        TB <- TB[TB$V2>=min(rg),]
        TB <- TB[TB$V2<=max(rg),]
        TB <- TB[c("V2", "V4", "V5")]
        colnames(TB) <- c("x", "Ref", "Alt")
        TB <- melt(TB, id.vars = "x" )
        P3 <- ggplot() + geom_tile(data=TB,aes(x= x, y= variable, label=value, fill= value), width=(rg[2]-rg[1])/300) +
        coord_cartesian(xlim =rg, expand = T) + theme_bw()
        Result2 <- c(Result2, P3)

    }

    P1 <- autoplot(txdb, which= wh)+ theme_bw() +
    geom_text(aes(x=0, y=0, label=0,color="red"))+
    coord_cartesian(xlim =rg, expand = T)

    tracks( c(Result,P1))
    ggsave(paste("img/", GENE, '_RNA.png',sep= ""), w= 20 , h= 5.45)
}

ggsave("~/tmp/Mutation_GTF.png", w= 20 , h= 1.55)

```




































0
