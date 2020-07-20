---
title: "clusterProfiler"
description: "R package for Bioinformatics; made by Doc. Yu"
url: clusterprofiler2
---

# clusterProfiler (out of date)

Tutorial: [yulab](https://yulab-smu.github.io/clusterProfiler-book/)

# Install

```r
BiocManager::install("clusterProfiler")
```


# Go ontology

## GO_1. Supported Organism

For module species which added in `OrgDb`, we can turn the ID to GO_id;

For other species, you can build your own `OrgDb` database by following [GOSemSim](https://bioconductor.org/packages/devel/bioc/vignettes/GOSemSim/inst/doc/GOSemSim.html#supported-organisms).

If genes are already annotated (in `data.frame` witch gene ID column followed by GO ID), we can use `enricher()` and `geosGO()` function to perform over-representation test.  

## GO_2. Example for `OrgDb` species

```r
library(clusterProfiler)
library(org.Hs.eg.db)

data(geneList, package="DOSE")
gene <- names(geneList)[abs(geneList) > 2]
gene.df <- bitr(gene, fromType = "ENTREZID",
        toType = c("ENSEMBL", "SYMBOL"),
        OrgDb = org.Hs.eg.db)
head(gene.df)
```
```
ENTREZID         ENSEMBL SYMBOL
1     4312 ENSG00000196611   MMP1
2     8318 ENSG00000093009  CDC45
3    10874 ENSG00000109255    NMU
4    55143 ENSG00000134690  CDCA8
5    55388 ENSG00000065328  MCM10
6      991 ENSG00000117399  CDC20
```
```r
ggo <- groupGO(gene     = gene,
               OrgDb    = org.Hs.eg.db,
               ont      = "CC",
               level    = 3,
               readable = TRUE)

head(ggo)
barplot(ggo, showCategory = 20)
```
```
ID                    Description Count GeneRatio
GO:0005886 GO:0005886                plasma membrane    55    55/207
GO:0005628 GO:0005628              prospore membrane     0     0/207
GO:0005789 GO:0005789 endoplasmic reticulum membrane     8     8/207
...
```
![132](https://i.loli.net/2020/06/14/kLpExyf9lHI4FJc.png)



## GO_3. Over-Representation Test

```r
ego <- enrichGO(gene          = gene,
                universe      = names(geneList),
                OrgDb         = org.Hs.eg.db,
                ont           = "CC",
                pAdjustMethod = "BH",
                pvalueCutoff  = 0.01,
                qvalueCutoff  = 0.05,
        readable      = TRUE)
head(ego)
```
```r
ego2 <- enrichGO(gene         = gene.df$ENSEMBL,
                OrgDb         = org.Hs.eg.db,
                keyType       = 'ENSEMBL',
                ont           = "CC",
                pAdjustMethod = "BH",
                pvalueCutoff  = 0.01,
                qvalueCutoff  = 0.05)

# turn ENSEMBL ID to Samble
ego2_r <- setReadable(ego2, OrgDb = org.Hs.eg.db)
```
|ego|ego2|
|---|---|
|[![tzt3RK.md.png](https://s1.ax1x.com/2020/06/14/tzt3RK.md.png)](https://imgchr.com/i/tzt3RK)|[![tztDRf.png](https://s1.ax1x.com/2020/06/14/tztDRf.png)](https://imgchr.com/i/tztDRf)|


## GO_4 GO Gene Set Enrichment Analysis
```r
ego3 <- gseGO(geneList     = geneList,
              OrgDb        = org.Hs.eg.db,
              ont          = "CC",
              nPerm        = 1000,
              minGSSize    = 100,
              maxGSSize    = 500,
              pvalueCutoff = 0.05,
              verbose      = FALSE)
```
```
ID                              Description setSize enrichmentScore       NES      pvalue   p.adjust    qvalues rank                   leading_edge
GO:0031012 GO:0031012                     extracellular matrix     427      -0.4868578 -2.138854 0.001231527 0.03095063 0.02171974 1797 tags=37%, list=14%, signal=33%
GO:0099568 GO:0099568                       cytoplasmic region     368      -0.3426037 -1.488559 0.001259446 0.03095063 0.02171974 2613 tags=28%, list=21%, signal=23%
```
[![NSMQfg.png](https://s1.ax1x.com/2020/06/14/NSMQfg.png)](https://imgchr.com/i/NSMQfg)

# GO ontology for Non-module Species

```r

```

# KEGG Enrichment

## KE_1. Over-Representation Test  
```r
library(clusterProfiler)
search_kegg_organism('ece', by='kegg_code')

ecoli <- search_kegg_organism('Escherichia coli', by='scientific_name')
dim(ecoli)
```

```r
data(geneList, package="DOSE")
gene <- names(geneList)[abs(geneList) > 2]

kk <- enrichKEGG(gene         = gene,
                 organism     = 'hsa',
                 pvalueCutoff = 0.05)
head(kk)
```
```
ID                                                   Description GeneRatio  BgRatio       pvalue     p.adjust       qvalue                                             geneID Count
hsa04110 hsa04110                                                    Cell cycle     11/93 124/8031 1.590786e-07 3.213388e-05 3.148083e-05 8318/991/9133/890/983/4085/7272/1111/891/4174/9232    11
hsa04114 hsa04114                                                Oocyte meiosis     10/93 128/8031 1.960649e-06 1.980256e-04 1.940011e-04    991/9133/983/4085/51806/6790/891/9232/3708/5241    10
hsa04218 hsa04218                                           Cellular senescence     10/93 160/8031 1.450991e-05 9.375595e-04 9.185054e-04     2305/4605/9133/890/983/51806/1111/891/776/3708    10
hsa04061 hsa04061 Viral protein interaction with cytokine and cytokine receptor      8/93 100/8031 1.856553e-05 9.375595e-04 9.185054e-04           3627/10563/6373/4283/6362/6355/9547/1524     8
hsa03320 hsa03320                                        PPAR signaling pathway      7/93  77/8031 2.765640e-05 1.117319e-03 1.094611e-03                 4312/9415/9370/5105/2167/3158/5346     7
hsa04914 hsa04914                       Progesterone-mediated oocyte maturation      7/93  99/8031 1.392778e-04 4.689019e-03 4.593724e-03                    9133/890/983/4085/6790/891/5241     7
```
## KE_2. Gene Set Enrichment Analysis
```r
kk2 <- gseKEGG(geneList     = geneList,
               organism     = 'hsa',
               nPerm        = 1000,
               minGSSize    = 120,
               pvalueCutoff = 0.05,
               verbose      = FALSE)
head(kk2)
```
```
ID                 Description setSize enrichmentScore       NES      pvalue  p.adjust    qvalues rank                   leading_edge
hsa04510 hsa04510              Focal adhesion     190      -0.4169068 -1.697372 0.001418440 0.0241065 0.01552815 2183 tags=27%, list=17%, signal=22%
hsa03013 hsa03013               RNA transport     131       0.4116488  1.742019 0.003067485 0.0241065 0.01552815 3383 tags=40%, list=27%, signal=29%
hsa05152 hsa05152                Tuberculosis     162       0.3745153  1.628558 0.003164557 0.0241065 0.01552815 2823 tags=34%, list=23%, signal=27%
hsa04218 hsa04218         Cellular senescence     143       0.4153718  1.761689 0.003225806 0.0241065 0.01552815 1155  tags=17%, list=9%, signal=16%
hsa05203 hsa05203        Viral carcinogenesis     164       0.3523856  1.535177 0.003246753 0.0241065 0.01552815 3112 tags=35%, list=25%, signal=26%
hsa04062 hsa04062 Chemokine signaling pathway     165       0.3754101  1.632867 0.003300330 0.0241065 0.01552815 1298 tags=21%, list=10%, signal=19%
```

|kk|kk2|
|:---:|:---:|
|[![NSY9Rf.md.png](https://s1.ax1x.com/2020/06/14/NSY9Rf.md.png)](https://imgchr.com/i/NSY9Rf)|[![NSYpJP.md.png](https://s1.ax1x.com/2020/06/14/NSYpJP.md.png)](https://imgchr.com/i/NSYpJP)|
## KE_3. KEGG Module over-representation test

```r
mkk <- enrichMKEGG(gene = gene,
                   organism = 'hsa')
```

## KE_4. KEGG Module Gene Set Enrichment Analysis

```r
mkk2 <- gseMKEGG(geneList = geneList,
                 organism = 'hsa')
```
















---

```r
#############
###eg
############

eg = bitr(x, fromType="SYMBOL", toType="ENTREZID", OrgDb="org.Hs.eg.db")
eg = bitr(x, fromType="ENTREZID", toType="SYMBOL", OrgDb="org.Hs.eg.db")
head(eg)

gene <- eg[[2]]


barplot(ggio, drop=TRUE, showCategory=122)
####################################################################



##bitr_kegg: converting biological IDs using KEGG API

data(x)
hg <- x[[1]]
head(hg)
eg2np <- bitr_kegg(hg, fromType='kegg', toType='ncbi-proteinid', organism='hsa')
head(eg2np)
bitr_kegg("Z5100", fromType="kegg", toType='ncbi-geneid', organism='ece')
bitr_kegg("Z5100", fromType="kegg", toType='ncbi-proteinid', organism='ece')
bitr_kegg("Z5100", fromType="kegg", toType='uniprot', organism='ece')

###############################################################################
########### GO classification
###############################################################################
gene <- names(geneList)[abs(geneList) > 2]

gobp <- groupGO(gene     = gene,
               OrgDb    = org.Hs.eg.db,
               ont      = "BP",
               level    = 2,
               readable = TRUE)

head(ggo)

go <- groupGO(gene = gene, OrgDb = org.Hs.eg.db, ont = "BP", level = 2, readable = TRUE)
barplot(go, drop=TRUE, showCategory=122)
#############################
GO over-representation test
##############################
ego1 <- enrichGO(gene =gene, universe= names(geneList), ont = "CC",pAdjustMethod = "BH",pvalueCutoff  = 0.01,qvalueCutoff = 0.05,readable = TRUE)
ego2 <- enrichGO(gene =gene, universe= names(geneList), ont = "BP",pAdjustMethod = "BH",pvalueCutoff  = 0.01,qvalueCutoff = 0.05,readable = TRUE)
ego3 <- enrichGO(gene =gene, universe= names(geneList), ont = "MF",pAdjustMethod = "BH",pvalueCutoff  = 0.01,qvalueCutoff = 0.05,readable = TRUE)

head(ego)
##################################
#################################
#################################
source("http://bioconductor.org/biocLite.R")
library(clusterProfiler)
library(org.Hs.eg.db)
keytypes(org.Hs.eg.db)





KEGG
kk <- enrichKEGG(gene = gene, organism = 'human', pvalueCutoff = 0.05)

head(kk)
barplot(kk, drop=TRUE, showCategory=122)


kk2 <- gseKEGG(geneList = geneList, organism = 'hsa', nPerm = 1000, minGSSize = 120, pvalueCutoff = 100,verbose = FALSE)
ead(kk2)

###
kk2 <- gseKEGG(geneList = geneList, organism = 'hsa', nPerm = 10, minGSSize = 10, pvalueCutoff = 100,verbose = FALSE)

gseaplot(kk2, geneSetID = "hsa05200")

hsa05205
hsa05165
#################################################################
############pathview
#################################################################

library(clusterProfiler)
library(org.Hs.eg.db)
library("pathview")

hsa05418
 p  <- pathview(gene.data  = geneList,
                     pathway.id = "hsa04976",
                     species    = "hsa",
                     limit      = list(gene=max(abs(geneList)), cpd=1))

pathview(gene.data  = geneList, pathway.id = "hsa04976", species = "hsa", limit = list(gene=max(5), cpd=1))
pathview(gene.data  = geneList, pathway.id = i, species = "hsa", limit = list(gene=max(5), cpd=1))


###################################################################
###geneList
###################################################################


d = read.csv(your_csv_file)

d = read.table("geneList")
## assume 1st column is ID
## 2nd column is FC
## feature 1: numeric vector

geneList = d[,2]
names(geneList) = as.character(d[,1])  ## feature 2: named vector
geneList = sort(geneList, decreasing = TRUE)   ## feature 3: decreasing order
head(geneList)

eg = bitr(x, fromType="ENTREZID", toType="SYMBOL", annoDb="org.Hs.eg.db")

 p  <- pathview(gene.data  = geneList, pathway.id = "hsa04668", species    = "hsa", limit      = list(gene=max(abs(geneList)), cpd=1))


gene <- names(geneList)[abs(geneList) > 2]
gene.df <- bitr(gene, fromType = "ENTREZID",
        toType = c("ENSEMBL", "SYMBOL"),
        OrgDb = org.Hs.eg.db)
head(gene.df)




ego2 <- enrichGO(gene         = gene.df$ENSEMBL,
                OrgDb         = org.Hs.eg.db,
        keytype       = 'ENSEMBL',
                ont           = "CC",
                pAdjustMethod = "BH",
                pvalueCutoff  = 0.01,
                qvalueCutoff  = 0.05)
ego2 <- setReadable(ego2, OrgDb = org.Hs.eg.db)


biocLite("topGO")




barplot(ggo, drop=TRUE, showCategory=12)

##############################################################
#
##############################################################
geneList = d[,2]
names(geneList) = as.character(d[,1])  ## feature 2: named vector
geneList = sort(geneList, decreasing = TRUE)   ## feature 3: decreasing order
head(geneList)

kk2 <- gseKEGG(geneList     = geneList,
               organism     = 'hsa',
               nPerm        = 1000,
               minGSSize    = 120,
               pvalueCutoff = 0,
               verbose      = FALSE)
gseaplot(kk2, geneSetID = "hsa04668")


######################
###write the results
######################

write.csv(fortify(kk,showCategory=120),file="kk.matrix",quote=F,sep='\t')









#################################

a <- c("3","7","14","21")
b <- read.table("single_symol.matrix")

for(i in a)
 {
 x <- read.table("3")
 probes= x$V1
 probes1=match(probes,x$V1)
 probes2=match(probes,b$V1)
 sum(is.na(probes1))
 sum(is.na(probes1))
 List=data.frame(FC=(x$V4[probes1]* -1),S=b$V2[probes2],Co=b$V1[probes2])
 List=data.frame(Symbol=List$S, FC=List$FC )
 A<- List[order(List[,2],decreasing=F),]
 write.table(A,file=paste(i,"-tesst.txt",sep=''),sep='\t',quote=F,row.names=F)
 }

for (i in b[[1]])
 {
  probes= i
 probes1= match(probes,b$V1)
  c=b$V2[probes1]
 png(file=paste(i,"-",c,"-GSEA.png",sep=''),wi=400,he=400)
 gseaplot(kk2, geneSetID = i,title=paste(c,"0dpeVs7dpe"))
 dev.off()
 }


 for (i in b[[1]])
 {
 p  <- pathview(gene.data  = geneList,
 pathway.id = i,
  species    = "hsa",
                   limit      = list(gene=max(abs(geneList)), cpd=1))
 }


geneList=data.frame(List=List$Symbol,FC=List$FC* -1)


 png(file=paste(i,"-",title,".png",sep=''),wi=900,he=900)
 gseaplot(kk2, geneSetID = i,title= T)
 dev.off()}


a <- read.table("list")
 x <- a[[1]]
eg = bitr(x, fromType="ENTREZID", toType="SYMBOL", annoDb="org.Hs.eg.db")
dim(eg)
write.table(eg,file="",row.names=F,quote=F,sep='\t')

```
---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
