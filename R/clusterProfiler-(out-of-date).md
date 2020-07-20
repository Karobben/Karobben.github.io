---
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
