---
title: "clusterProfiler"
date: 2020/06/14
url: clusterprofiler2
toc: true
excerpt: "R package for Bioinformatics; made by Doc. Yu"
tags: [R, Bioinformatics, KEGG, GO]
category: [R, Bio, Anno/Enrich]
cover: 'https://s1.ax1x.com/2020/06/14/NSYpJP.md.png'
thumbnail: 'https://s1.ax1x.com/2020/06/14/NSYpJP.md.png'
priority: 10000
---

## clusterProfiler

Tutorial: [yulab](https://yulab-smu.github.io/clusterProfiler-book/)

## Install

```r
BiocManager::install("clusterProfiler")
```
## Enrichment analysis and GSEA

> Enrichment analysis is a computational method used in bioinformatics to determine whether a given set of genes or proteins is enriched for specific functions, pathways, or biological processes. It involves comparing the input gene set to a reference database, such as Gene Ontology, KEGG, or Reactome, and identifying the over-represented terms using statistical methods.
>
> Gene Set Enrichment Analysis (GSEA) is a type of enrichment analysis that determines whether a particular gene set shows statistically significant differences between two biological states. Unlike traditional enrichment analysis, GSEA considers the entire gene set, rather than individual genes, and evaluates whether the gene set is significantly enriched at the top or bottom of a ranked list of genes based on their differential expression or correlation with a phenotype. GSEA is commonly used in transcriptomics and genomics studies to identify pathways or biological processes that are differentially regulated between disease and control samples.
> © ChatGPT

## Go ontology

### GO_1. Supported Organism

For module species which added in `OrgDb`, we can turn the ID to GO_id;

For other species, you can build your own `OrgDb` database by following [GOSemSim](https://bioconductor.org/packages/devel/bioc/vignettes/GOSemSim/inst/doc/GOSemSim.html#supported-organisms).

If genes are already annotated (in `data.frame` witch gene ID column followed by GO ID), we can use `enricher()` and `geosGO()` function to perform over-representation test.  

### GO_2. Example for `OrgDb` species

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


|  | 4312     |8318|
| :------------- | :------------- |:-|
|ACCNUM|AAA35699|NP_001139410|
|ENTREZID |  ENSG00000196611|    ENSG00000093009|
|ENSEMBL SYMBOL| MMP1 |CDC45


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



### GO_3. Over-Representation Test

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

## turn ENSEMBL ID to Samble
ego2_r <- setReadable(ego2, OrgDb = org.Hs.eg.db)

dotplot(ego2)
```

|ego|ego2|
|---|---|
|![tzt3RK.md.png](https://s1.ax1x.com/2020/06/14/tzt3RK.md.png)|![tztDRf.png](https://s1.ax1x.com/2020/06/14/tztDRf.png)|


### GO_4 GO Gene Set Enrichment Analysis
```r
ego3 <- gseGO(geneList     = geneList,
              OrgDb        = org.Hs.eg.db,
              ont          = "CC",
              nPerm        = 1000,
              minGSSize    = 100,
              maxGSSize    = 500,
              pvalueCutoff = 0.05,
              verbose      = FALSE)

dotplot(ego3)
```

<pre>
ID                              Description setSize enrichmentScore       NES      pvalue   p.adjust    qvalues rank                   leading_edge
GO:0031012 GO:0031012                     extracellular matrix     427      -0.4868578 -2.138854 0.001231527 0.03095063 0.02171974 1797 tags=37%, list=14%, signal=33%
GO:0099568 GO:0099568                       cytoplasmic region     368      -0.3426037 -1.488559 0.001259446 0.03095063 0.02171974 2613 tags=28%, list=21%, signal=23%
</pre>

![NSMQfg.png](https://s1.ax1x.com/2020/06/14/NSMQfg.png)

## GO ontology for Non-module Species

```r

```

## KEGG Enrichment

### KE_1. Over-Representation Test  
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

<pre>
ID                                                   Description GeneRatio  BgRatio       pvalue     p.adjust       qvalue                                             geneID Count
hsa04110 hsa04110                                                    Cell cycle     11/93 124/8031 1.590786e-07 3.213388e-05 3.148083e-05 8318/991/9133/890/983/4085/7272/1111/891/4174/9232    11
hsa04114 hsa04114                                                Oocyte meiosis     10/93 128/8031 1.960649e-06 1.980256e-04 1.940011e-04    991/9133/983/4085/51806/6790/891/9232/3708/5241    10
hsa04218 hsa04218                                           Cellular senescence     10/93 160/8031 1.450991e-05 9.375595e-04 9.185054e-04     2305/4605/9133/890/983/51806/1111/891/776/3708    10
hsa04061 hsa04061 Viral protein interaction with cytokine and cytokine receptor      8/93 100/8031 1.856553e-05 9.375595e-04 9.185054e-04           3627/10563/6373/4283/6362/6355/9547/1524     8
hsa03320 hsa03320                                        PPAR signaling pathway      7/93  77/8031 2.765640e-05 1.117319e-03 1.094611e-03                 4312/9415/9370/5105/2167/3158/5346     7
hsa04914 hsa04914                       Progesterone-mediated oocyte maturation      7/93  99/8031 1.392778e-04 4.689019e-03 4.593724e-03                    9133/890/983/4085/6790/891/5241     7
</pre>


### KE_2. Gene Set Enrichment Analysis

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
|![NSY9Rf.md.png](https://s1.ax1x.com/2020/06/14/NSY9Rf.md.png)|![NSYpJP.md.png](https://s1.ax1x.com/2020/06/14/NSYpJP.md.png)|
### KE_3. KEGG Module over-representation test

```r
mkk <- enrichMKEGG(gene = gene,
                   organism = 'hsa')
```

### KE_4. KEGG Module Gene Set Enrichment Analysis

```r
mkk2 <- gseMKEGG(geneList = geneList,
                 organism = 'hsa')
```


## A Pipeline Example

Result from: edgeR
species: dme

```r
library(clusterProfiler)
library(org.Dm.eg.db)
library(pathview)
library(reshape2)
library(stringr)
library(ggplot2)
library(enrichplot)

args = commandArgs(trailingOnly=TRUE)

SampleA= args[1]#"G1F1"
SampleB= args[2]#"G50F"
Pvalue = 0.01
logFC= 2
C_cut = 10
Level= 2

Sample_Dir = paste(SampleA,"_VS_",SampleB,"/",sep="")
for(i in c("GO", "KEGG", "WIKI", "Reactome")){
    dir.create(i)
    dir.create(paste(i, Sample_Dir,sep='/'))
}

Gene_list <- read.table(paste("RSEM_transcript/transcript.isoform.counts.matrix.", SampleA, "_vs_", SampleB,".edgeR.DE_results", sep=""))


ENTREZID = bitr(row.names(Gene_list), fromType="FLYBASE", toType="ENTREZID", OrgDb="org.Dm.eg.db")
FLYBASECG = bitr(row.names(Gene_list), fromType="FLYBASE", toType="FLYBASECG", OrgDb="org.Dm.eg.db")
SYMBOL = bitr(row.names(Gene_list), fromType="FLYBASE", toType="SYMBOL", OrgDb="org.Dm.eg.db")


Gene_list$ENTREZID <- ENTREZID$ENTREZID[match(row.names(Gene_list), ENTREZID$FLYBASE)]
Gene_list$FLYBASECG <- FLYBASECG$FLYBASECG[match(row.names(Gene_list), FLYBASECG$FLYBASE)]
Gene_list$SYMBOL <- SYMBOL$SYMBOL[match(row.names(Gene_list), SYMBOL$FLYBASE)]

KE2SY <-function(kk_GSEA, COL){
    if( nrow(kk_GSEA@result) >0){
        for(i in c(1:nrow(kk_GSEA@result))){
            LIST <- kk_GSEA@result[[COL]][i]
            kk_GSEA@result[[COL]][i] <- paste(Gene_list$SYMBOL[match(str_remove(str_split(LIST, "/")[[1]], "Dmel_"),Gene_list$FLYBASECG )], collapse = "/")
        }        
    }
    return(kk_GSEA)
}

EN2SY <-function(WikiP_enrich, COL){
    if(length(WikiP_enrich@result[[COL]])>0){
        for(i in c(1:length(WikiP_enrich@result[[COL]]))){
            LIST <- WikiP_enrich@result[[COL]][i]
            WikiP_enrich@result[[COL]][i] <- paste(Gene_list$SYMBOL[match(str_remove(str_split(LIST, "/")[[1]], "Dmel_"),Gene_list$ENTREZID )], collapse = "/")
        }
    }
    return(WikiP_enrich)
}

ggsave_GO <- function(NAME, LEN){
    BASE = 3.8
    RATE = 0.125
    if (BASE + RATE*LEN <= 40){
        W = BASE + RATE*LEN
    }else{
        W = 40
    }
    ggsave(NAME , w = W, h = 8.35, limitsize = FALSE )
}

ggsave_GO_enrich <- function(NAME, LEN){
    BASE = 2
    RATE = 0.1114
    if (BASE + RATE*LEN <= 40){
        H = BASE + RATE*LEN
    }else{
        H = 40
    }
    ggsave(NAME , w = 10, h = H, limitsize = FALSE)
}

ridgeplot_save <- function(NAME,LEN){
    BASE = 1.02
    RATE = 0.2
    if (BASE + RATE*LEN <= 40){
        H = BASE + RATE*LEN
    }else{
        H = 40
    }
    ggsave(NAME , w = 10, h = H, limitsize = FALSE)
}

## GO ontology
TMP <- Gene_list[abs(Gene_list$logFC) >=2,]
TMP <- TMP[TMP$PValue <= Pvalue,]


sig_genes = TMP$ENTREZID

gooc <- groupGO(gene     = sig_genes,
               OrgDb    = org.Dm.eg.db,
               ont      = "CC",
               level    = Level,
               readable = TRUE)
goom <- groupGO(gene     = sig_genes,
              OrgDb    = org.Dm.eg.db,
              ont      = "MF",
              level    = Level,
              readable = TRUE)
goob <- groupGO(gene     = sig_genes,
             OrgDb    = org.Dm.eg.db,
             ont      = "BP",
             level    = Level,
             readable = TRUE)

gooc@result$Group = "CC"
goom@result$Group = "MF"
goob@result$Group = "BP"


GO_TB <- rbind(gooc@result, goom@result, goob@result)
GO_TB <- GO_TB[GO_TB$Count!=0,]
File_name = paste("Ontology", SampleA,SampleB,Pvalue, logFC, sep="_" )
write.csv(GO_TB, paste("GO/",Sample_Dir, File_name, ".csv", sep="" ), row.names=F)

# [GO ontology plot]
ggplot(GO_TB, aes(x=Description, y=Count, fill=Group)) +
    geom_bar(stat = 'identity') +
    facet_grid(~Group, scales = 'free', space = 'free') + theme_bw() +
    theme(axis.text.x = element_text(angle = 270, hjust = 0, vjust = .5), legend.position = 'none', panel.grid =  element_blank(), strip.background = element_rect(fill = 'white'))
ggsave_GO(paste("GO/", Sample_Dir, File_name, ".png", sep="" ), nrow(GO_TB))

## Overrepresentation
File_name = paste("Enrichment", SampleA,SampleB,Pvalue, logFC, sep="_" )


ego <- enrichGO(gene          = sig_genes,
                universe      = Gene_list$ENTREZID,
                OrgDb         = org.Dm.eg.db,
                ont           = "All",
                pAdjustMethod = "BH",
                pvalueCutoff  = 0.01,
                qvalueCutoff  = 0.05,
        readable      = TRUE)
head(ego)
SIZE = as.numeric(as.character(as.data.frame(str_split_fixed(ego@result$GeneRatio, "/",2))[[1]]))/
as.numeric(as.character(as.data.frame(str_split_fixed(ego@result$BgRatio, "/",2))[[1]]))
ego@result$size = SIZE
write.csv(ego, paste("GO/", Sample_Dir, File_name, ".csv", sep="" ), row.names=F)

# [GO Enrichment plot]
ggplot(ego@result, aes(x=Count, y=Description)) +
    geom_point(aes(size=size, color=pvalue)) + theme_bw() +
    facet_grid(ONTOLOGY~., space = 'free', scales = 'free')

ggsave_GO_enrich(paste("GO/", Sample_Dir, File_name, ".png", sep="" ), nrow(ego@result))

geneList <- Gene_list$logFC
names(geneList) <- Gene_list$ENTREZID
geneList <- sort(geneList, decreasing = T)

for(GROUP in c("CC", "BP", "MF")){
    egocc <- enrichGO(gene          = sig_genes,
            universe      = Gene_list$ENTREZID,
            OrgDb         = org.Dm.eg.db,
            ont           = GROUP,
            pAdjustMethod = "BH",
            pvalueCutoff  = 0.01,
            qvalueCutoff  = 0.05,
            readable      = TRUE)

    write.csv(egocc, paste("GO/",Sample_Dir, File_name, "_", GROUP, ".csv", sep="" ), row.names=F)
    # [GO Network category]
    Plot_and_Save <-function(){
        goplot(egocc)
        ggsave( paste("GO/",Sample_Dir, File_name,  "_", GROUP, "_category", ".png", sep="" ),
            w = 20, h = 10.9 )
    # [GO Network Genes]
        cnetplot(egocc, foldChange=geneList)
        ggsave( paste("GO/", Sample_Dir, File_name,  "_", GROUP, "_genes", ".png", sep="" ),
        w = 20, h = 10.9 )
    }
    try(Plot_and_Save(),silent=TRUE)

}


# GO Gene Set Enrichment Analysis
File_name = paste("GSEA",Pvalue, logFC, sep="_" )

for(GROUP in c("CC", "BP", "MF")){
    GOgse_CC <- gseGO(geneList     = geneList,
                  OrgDb        = org.Dm.eg.db,
                  ont          = GROUP,
                  minGSSize    = 100,
                  maxGSSize    = 500,
                  eps = 1e-10,
                  pvalueCutoff = 0.05,
                  verbose      = FALSE)
    write.csv(GOgse_CC, paste("GO/",Sample_Dir, File_name, "_", GROUP, ".csv", sep="" ), row.names=F)

    ridgeplot(GOgse_CC)
    ridgeplot_save(paste("GO/",Sample_Dir, File_name, "_", GROUP,"_ridgeplot.png", sep="" ), nrow(GOgse_CC@result))
    Plot_and_Save <-function(){
        goplot(GOgse_CC)
        ggsave( paste("GO/",Sample_Dir, File_name,  "_", GROUP, "_category", ".png", sep="" ),
        w = 20, h = 10.9 )
        cnetplot(GOgse_CC, foldChange=geneList)
        ggsave( paste("GO/",Sample_Dir, File_name,  "_", GROUP, "_genes", ".png", sep="" ),
        w = 20, h = 10.9 )
    }
    try(Plot_and_Save(),silent=TRUE)

    # [GO GSEA upsetplot]
    upsetplot(GOgse_CC)
    ggsave( paste("GO/",Sample_Dir, File_name,  "_", GROUP, "_upset", ".png", sep="" ),
        w = 20, h = 10.9 )
    # [GO GSEA Escore]
    for (i in c(1:nrow(GOgse_CC@result))){
        gseaplot2(GOgse_CC, geneSetID = i, title = GOgse_CC$Description[i], color = 'salmon', pvalue_table = TRUE)
        ggsave(paste("GO/",Sample_Dir, File_name,  "_", str_split(GOgse_CC@result$ID[i],":")[[1]][2], "_GSEA", ".png", sep="" ), w = 7.5, h = 5)
    }
}

#########################
## KEGG                 #
#########################

# gene set enrichment analysis
File_name = paste("GSEA",Pvalue, logFC, sep="_" )
geneList_kk <- Gene_list$logFC
names(geneList_kk) <- paste("Dmel", Gene_list$FLYBASECG, sep="_")
geneList_kk <- sort(geneList_kk, decreasing = T)

kk_GSEA <- gseKEGG(geneList     = geneList_kk,
               organism     = 'dme',
               minGSSize    = 10,
               pvalueCutoff = 0.05,
               verbose      = FALSE)

for (i in c(1:nrow(kk_GSEA@result))){
    gseaplot2(kk_GSEA, geneSetID = i, title = kk_GSEA$Description[i], color = 'salmon', pvalue_table = TRUE)
    ggsave(paste("KEGG/",Sample_Dir, File_name,  "_", kk_GSEA@result$ID[i], "_GSEA", ".png", sep="" ), w = 7.5, h = 5)
}


kk_GSEA2 <- KE2SY(kk_GSEA, "core_enrichment")

write.csv(kk_GSEA2, paste("KEGG/",Sample_Dir, File_name, ".csv", sep="" ), row.names=F)


geneList_smb <- Gene_list$logFC
names(geneList_smb) <-Gene_list$SYMBOL
geneList_smb <- sort(geneList_smb, decreasing = T)

Plot_and_Save <-function(){
    cnetplot(kk_GSEA2, foldChange=geneList_smb)
    ggsave( paste("KEGG/",Sample_Dir, File_name, "_genes", ".png", sep="" ), w = 20, h = 10.9 )
}
try(Plot_and_Save(),silent=TRUE)


sig_genes_kk =  paste("Dmel", TMP$FLYBASECG, sep="_")

# over-representation analysis
File_name = paste("Enrichment", Pvalue, logFC, sep="_" )
kk_Enrich <- enrichKEGG(gene = sig_genes_kk,
                   universe = names(geneList_kk),
                   organism = 'dme',
                   pvalueCutoff = 0.05)
write.csv(kk_Enrich, paste("KEGG/",Sample_Dir, File_name, ".csv", sep="" ), row.names=F)

ggplot(kk_Enrich@result, aes(x=Count, y=Description)) +
    geom_point(aes(size=GeneRatio, color=pvalue)) + theme_bw()
ggsave_GO_enrich(paste("KEGG/",Sample_Dir, File_name, ".png", sep="" ), nrow(kk_Enrich@result))


Plot_and_Save <-function(){
    cnetplot(kk_Enrich, foldChange=geneList_kk)
    ggsave( paste("KEGG/",Sample_Dir, File_name, "_genes", ".png", sep="" ), w = 20, h = 10.9 )
}
try(Plot_and_Save(),silent=TRUE)


neList_kk <- Gene_list$logFC
names(geneList_kk) <-Gene_list$ENTREZID
geneList_kk <- sort(geneList_kk, decreasing = T)

library("pathview")
#dme04624 <- pathview(gene.data  = geneList_kk,
#                        pathway.id = "04624",
#                        species    = "dme",
#                        out.prefix = paste("KEGG/",Sample_Dir, sep=""),
#                        limit      =2.5)

## WikiPathways
File_name = paste("Enrichment", Pvalue, logFC, sep="_" )
WikiP_enrich <- enrichWP(sig_genes, universe = names(geneList_kk), organism = "Drosophila melanogaster")
ggplot(WikiP_enrich@result, aes(x=Count, y=Description)) +
    geom_point(aes(size=GeneRatio, color=pvalue)) + theme_bw()
ggsave_GO_enrich(paste("WIKI/",Sample_Dir, File_name, ".png", sep="" ), nrow(kk_Enrich@result))

WikiP_enrich2 <- EN2SY(WikiP_enrich, "geneID")
write.csv(WikiP_enrich2@result, paste("WIKI/",Sample_Dir, File_name, ".csv", sep="" ), row.names=F)

Plot_and_Save <-function(){
    cnetplot(WikiP_enrich2, foldChange=geneList_smb)
    ggsave( paste("WIKI/",Sample_Dir, File_name, "_genes", ".png", sep="" ), w = 20, h = 10.9 )
}
try(Plot_and_Save(),silent=TRUE)


File_name = paste("GSEA",Pvalue, logFC, sep="_" )
WikiP_gse <- gseWP(geneList, organism = "Drosophila melanogaster")
WikiP_gse2 <- EN2SY(WikiP_gse, "core_enrichment")

if (nrow(WikiP_gse@result) >0 ){
    for (i in c(1:nrow(WikiP_gse@result))){
        gseaplot2(WikiP_gse, geneSetID = i, title = WikiP_gse$Description[i], color = 'salmon', pvalue_table = TRUE)
        ggsave(paste("WIKI/",Sample_Dir, File_name,  "_", WikiP_gse@result$ID[i], "_GSEA", ".png", sep="" ), w = 7.5, h = 5)
    }
}

write.csv(WikiP_gse2@result, paste("WIKI/",Sample_Dir, File_name, ".csv", sep="" ), row.names=F)

Plot_and_Save <-function(){
    ridgeplot(WikiP_gse)
    ridgeplot_save(paste("WIKI/",Sample_Dir, File_name, "_", GROUP,"_ridgeplot.png", sep="" ), nrow(WikiP_gse@result))
}
try(Plot_and_Save(),silent=TRUE)



## Reactome Pathway
library(ReactomePA)
File_name = paste("Enrichment", Pvalue, logFC, sep="_" )
Reactome_enrich <- enrichPathway(gene= sig_genes, pvalueCutoff = 0.05,
    readable=TRUE, organism ="fly", universe = names(geneList))
write.csv(Reactome_enrich, paste("Reactome/",Sample_Dir, File_name, ".csv", sep="" ), row.names=F)

Reactome_enrich@result <- Reactome_enrich@result[Reactome_enrich@result$pvalue<=0.05,]
ggplot(Reactome_enrich@result, aes(x=Count, y=Description)) +
    geom_point(aes(size=GeneRatio, color=pvalue)) + theme_bw()
ggsave_GO_enrich(paste("Reactome/",Sample_Dir, File_name, ".png", sep="" ), nrow(kk_Enrich@result))


File_name = paste("GSEA",Pvalue, logFC, sep="_" )
Reactome_gse <- gsePathway(geneList,
                pvalueCutoff = 0.05,
                organism = "fly",
                pAdjustMethod = "BH")
# [Reactome_gse ridgeplot]
ridgeplot(Reactome_gse)
ridgeplot_save(paste("Reactome/",Sample_Dir, File_name, "_", GROUP,"_ridgeplot.png", sep="" ), nrow(Reactome_gse@result))
write.csv(Reactome_gse, paste("Reactome/",Sample_Dir, File_name, ".csv", sep="" ), row.names=F)


for (i in c(1:nrow(Reactome_gse@result))){
    gseaplot2(Reactome_gse, geneSetID = i, title = Reactome_gse$Description[i], color = 'salmon', pvalue_table = TRUE)
    ggsave(paste("Reactome/",Sample_Dir, File_name,  "_", Reactome_gse@result$ID[i], "_GSEA", ".png", sep="" ), w = 7.5, h = 5)
}

```


[123](https://bioinformaticsbreakdown.com/how-to-gsea/)
[123](https://learn.gencore.bio.nyu.edu/rna-seq-analysis/gene-set-enrichment-analysis/)


||
|:-:|
|![](https://s1.ax1x.com/2022/10/07/x3Zf1g.png)|
|GO ontology plot|
|![](https://s1.ax1x.com/2022/10/07/x8d0hT.png)|
|GO Enrichment plot|
|![](https://s1.ax1x.com/2022/10/07/x8dqHI.png)|
|GO Network category|
|![](https://s1.ax1x.com/2022/10/07/x8dj4f.png)|
|GO Network Genes|
|![](https://s1.ax1x.com/2022/10/07/x8wpvQ.png)|
|GO GSEA upsetplot|
|![](https://s1.ax1x.com/2022/10/08/x8wibn.png)|
|GO GSEA Escore|
|![](https://s1.ax1x.com/2022/10/08/x80lQg.png)|
|pathview|
|![](https://s1.ax1x.com/2022/10/08/x8DMrQ.png)|
|Reactome_gse ridgeplot|


```r
##############
####eg
#############

eg = bitr(x, fromType="SYMBOL", toType="ENTREZID", OrgDb="org.Hs.eg.db")
eg = bitr(x, fromType="ENTREZID", toType="SYMBOL", OrgDb="org.Hs.eg.db")
head(eg)

gene <- eg[[2]]


barplot(ggio, drop=TRUE, showCategory=122)
#####################################################################



###bitr_kegg: converting biological IDs using KEGG API

data(x)
hg <- x[[1]]
head(hg)
eg2np <- bitr_kegg(hg, fromType='kegg', toType='ncbi-proteinid', organism='hsa')
head(eg2np)
bitr_kegg("Z5100", fromType="kegg", toType='ncbi-geneid', organism='ece')
bitr_kegg("Z5100", fromType="kegg", toType='ncbi-proteinid', organism='ece')
bitr_kegg("Z5100", fromType="kegg", toType='uniprot', organism='ece')

################################################################################
############ GO classification
################################################################################
gene <- names(geneList)[abs(geneList) > 2]

gobp <- groupGO(gene     = gene,
               OrgDb    = org.Hs.eg.db,
               ont      = "BP",
               level    = 2,
               readable = TRUE)

head(ggo)

go <- groupGO(gene = gene, OrgDb = org.Hs.eg.db, ont = "BP", level = 2, readable = TRUE)
barplot(go, drop=TRUE, showCategory=122)
##############################
GO over-representation test
###############################
ego1 <- enrichGO(gene =gene, universe= names(geneList), ont = "CC",pAdjustMethod = "BH",pvalueCutoff  = 0.01,qvalueCutoff = 0.05,readable = TRUE)
ego2 <- enrichGO(gene =gene, universe= names(geneList), ont = "BP",pAdjustMethod = "BH",pvalueCutoff  = 0.01,qvalueCutoff = 0.05,readable = TRUE)
ego3 <- enrichGO(gene =gene, universe= names(geneList), ont = "MF",pAdjustMethod = "BH",pvalueCutoff  = 0.01,qvalueCutoff = 0.05,readable = TRUE)

head(ego)
###################################
##################################
##################################
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

####
kk2 <- gseKEGG(geneList = geneList, organism = 'hsa', nPerm = 10, minGSSize = 10, pvalueCutoff = 100,verbose = FALSE)

gseaplot(kk2, geneSetID = "hsa05200")

hsa05205
hsa05165
##################################################################
#############pathview
##################################################################

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


####################################################################
####geneList
####################################################################


d = read.csv(your_csv_file)

d = read.table("geneList")
### assume 1st column is ID
### 2nd column is FC
### feature 1: numeric vector

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

###############################################################
##
###############################################################
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


#######################
####write the results
#######################

write.csv(fortify(kk,showCategory=120),file="kk.matrix",quote=F,sep='\t')









##################################

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

## Error in installation

<pre>
config.status: creating src/Makevars.tmp
config.status: creating src/Makevars
config.status: creating src/config.h
** libs
gfortran -fno-optimize-sibling-calls  -fpic  -g -O2  -c AMD/Source/amd.f -o AMD/Source/amd.o
make: gfortran: No such file or directory
make: *** [/usr/lib64/R/etc/Makeconf:195: AMD/Source/amd.o] Error 127
ERROR: compilation failed for package 'igraph'
* removing '/home/karobben/R/x86_64-pc-linux-gnu-library/4.0/igraph'
During startup - Warning message:
</pre>

problem: lack of gcc-fortran

```bash
sudo pacman -S gcc-fortran
```

## Error in using

<pre>
fail to download KEGG data...
Error in download.KEGG.Path(species) : 
  'species' should be one of organisms listed in 'http://www.genome.jp/kegg/catalog/org_list.html'...
Calls: gseKEGG ... prepare_KEGG -> download_KEGG -> download.KEGG.Path
In addition: Warning message:
In download.file(url, method = method, ...) :
  URL 'https://rest.kegg.jp/link/hsa/pathway': status was 'Failure when receiving data from the peer'
Execution halted
</pre>

This is such an annoying issue. The weird thing is that everything works fine when I use the code in the terminal, but as soon as I write the code into a script, it just doesn't seem to work. The author suggests that the issue could be resolved by updating to the latest version. However, this would mean that I would also need to update either the Bioconductor or R base. I don't want to update anything, I just want the job to be done. Thankfully, [Slohr](https://github.com/YuLab-SMU/clusterProfiler/issues/256)'s answer in 2022 provided a perfect solution to this problem.



```r
## https://www.genome.jp/kegg/rest/keggapi.html
## kegg_link('hsa', 'pathway')
ttp_kegg_link <- function(target_db, source_db) {
    url <- paste0("https://rest.kegg.jp/link/", target_db, "/", source_db, collapse="")
    local_mydownload <- function (url, method, quiet = TRUE, ...) 
    {
        if (capabilities("libcurl")) {
            dl <- tryCatch(utils::download.file(url, quiet = quiet, 
                method = "libcurl", ...), error = function(e) NULL)
        }
        else {
            dl <- tryCatch(downloader::download(url, quiet = TRUE, 
                method = method, ...), error = function(e) NULL)
        }
        return(dl)
    }
    local_kegg_rest <- function (rest_url) 
    {
        message("Reading KEGG annotation online:\n")
        f <- tempfile()
        dl <- local_mydownload(rest_url, destfile = f)
        if (is.null(dl)) {
            message("fail to download KEGG data...")
            return(NULL)
        }
        content <- readLines(f)
        content %<>% strsplit(., "\t") %>% do.call("rbind", .)
        res <- data.frame(from = content[, 1], to = content[, 2])
        return(res)
    }
    local_kegg_rest(url)
}

ttp_kegg_list <- function(db) {
    url <- paste0("https://rest.kegg.jp/list/", db, collapse="")
    local_mydownload <- function (url, method, quiet = TRUE, ...) 
    {
        if (capabilities("libcurl")) {
            dl <- tryCatch(utils::download.file(url, quiet = quiet, 
                method = "libcurl", ...), error = function(e) NULL)
        }
        else {
            dl <- tryCatch(downloader::download(url, quiet = TRUE, 
                method = method, ...), error = function(e) NULL)
        }
        return(dl)
    }
    local_kegg_rest <- function (rest_url) 
    {
        message("Reading KEGG annotation online:\n")
        f <- tempfile()
        dl <- local_mydownload(rest_url, destfile = f)
        if (is.null(dl)) {
            message("fail to download KEGG data...")
            return(NULL)
        }
        content <- readLines(f)
        content %<>% strsplit(., "\t") %>% do.call("rbind", .)
        res <- data.frame(from = content[, 1], to = content[, 2])
        return(res)
    }
    local_kegg_rest(url)
}

rlang::env_unlock(env = asNamespace('clusterProfiler'))
rlang::env_binding_unlock(env = asNamespace('clusterProfiler'))
assign('kegg_link', ttp_kegg_link, envir = asNamespace('clusterProfiler'))
assign('kegg_list', ttp_kegg_list, envir = asNamespace('clusterProfiler'))
rlang::env_binding_lock(env = asNamespace('clusterProfiler'))
rlang::env_lock(asNamespace('clusterProfiler'))
```

