---
toc: true
url: loc_gtf
covercopy: © Karobben
priority: 10000
date: 2022-12-15 15:25:44
title:
ytitle:
description:
excerpt:
tags:
category:
cover:
thumbnail:
---


A gtf file
<pre>
4	FlyBase	exon	213385	213449	.	+	.	gene_id "FBti0063548"; transcript_id "FBti0063548-RA"; exon_number "1"; gene_source "FlyBase"; gene_biotype "transposable_element"; transcript_source "FlyBase"; transcript_biotype "transposable_element"; exon_id "FBti0063548-RA-E1"; tag "Ensembl_canonical";
4	FlyBase	gene	1278430	1281474	.	-	.	gene_id "FBti0102121"; gene_source "FlyBase"; gene_biotype "transposable_element";
4	FlyBase	transcript	1278430	1281474	.	-	.	gene_id "FBti0102121"; transcript_id "FBti0102121-RA"; gene_source "FlyBase"; gene_biotype "transposable_element"; transcript_source "FlyBase"; transcript_biotype "transposable_element"; tag "Ensembl_canonical";
4	FlyBase	exon	1278430	1281474	.	-	.	gene_id "FBti0102121"; transcript_id "FBti0102121-RA"; exon_number "1"; gene_source "FlyBase"; gene_biotype "transposable_element"; transcript_source "FlyBase"; transcript_biotype "transposable_element"; exon_id "FBti0102121-RA-E1"; tag "Ensembl_canonical";
4	FlyBase	gene	629026	630613	.	+	.	gene_id "FBti0059980"; gene_source "FlyBase"; gene_biotype "transposable_element";
4	FlyBase	transcript	629026	630613	.	+	.	gene_id "FBti0059980"; transcript_id "FBti0059980-RA"; gene_source "FlyBase"; gene_biotype "transposable_element"; transcript_source "FlyBase"; transcript_biotype "transposable_element"; tag "Ensembl_canonical";
4	FlyBase	exon	629026	630613	.	+	.	gene_id "FBti0059980"; transcript_id "FBti0059980-RA"; exon_number "1"; gene_source "FlyBase"; gene_biotype "transposable_element"; transcript_source "FlyBase"; transcript_biotype "transposable_element"; exon_id "FBti0059980-RA-E1"; tag "Ensembl_canonical";
</pre>



```r
library(stringr)



GTF <- read.table("Drosophila_melanogaster.BDGP6.32.108.chr.gtf", sep = '\t')
TE_GTF <- GTF[grep("_element",GTF$V9),]

Chr='2L'
Pos = 5326506

Log_anno <- function(Chr, Pos, GTF){
    Pos = as.numeric(Pos)
    TMP <- GTF[GTF$V1 == Chr,]
    Hit <- TMP[(TMP$V4 - Pos) * (TMP$V5 - Pos)<=0,]
    if (nrow(Hit)==0){
        return ("Not Found")
    }else{
        if(length(Hit$V9[grep("gene_name",Hit$V9)]) != 0){
        return(str_split(str_split(Hit$V9[grep("gene_name",Hit$V9)][[1]], 'gene_name ')[[1]][2], ';')[[1]][1])
    }else{
        return(str_remove(str_split(Hit$V9[[1]], ' ')[[1]][2], ';'))
    }
    }
}


Loc <- read.table("Loc.csv")

List1 = c()
List2 = c()
for(i in c(1:nrow(Loc))){
    Chr = Loc$V2[i]
    Pos = Loc$V3[i]
    TMP1 <- Log_anno(Chr, Pos, TE_GTF)
    Chr = Loc$V4[i]
    Pos = Loc$V5[i]
    TMP2 <- Log_anno(Chr, Pos, TE_GTF)
    List1 = c(List1, TMP1)
    List2 = c(List2, TMP2)
}

Loc$Anno1=List1
Loc$Anno2=List2

Loc_hit <- Loc[(List1=="Not Found") + (List2=="Not Found")==1,]
TB <- as.data.frame(sort(table(Loc_hit$V1)))
TB$Var <- as.numeric(str_remove_all(TB$Var,"[A-Z]"))


```





<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
