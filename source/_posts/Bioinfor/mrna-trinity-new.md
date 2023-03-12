---
toc: true
url: mrna_trinity_new
covercopy: ©  Karobben
date: 2022-08-18 18:06:58
title: "Find novo transcripts based on Trinity de-nove assembly"
ytitle: "Find novo transcripts based on Trinity de-nove assembly"
description:
excerpt: "This post would show you a pipeline to find the new or abnormal transcript isoforms after de-novo by Trinity"
tags: [Software, Bioinformatics, NGS]
category: [Biology, Bioinformatics, Software, De nove]
cover: 'https://s1.ax1x.com/2022/09/04/vo2oRg.png'
thumbnail: 'https://s1.ax1x.com/2022/09/04/vo2oRg.png'
priority: 10000
---

## Why De novo?

Though we can get well quantified data by running alternative splicing processing. But the structure and the number of isoforms for each gene are kind of ambiguous. By de-novo transcripts assembling, we can technically get the full length of the transcripts and we may find some new transcripts and even new genes. Also, gene fusion could be easily told and illustrated. With some help from other tools, `blast+` for instance, we can visualize them very well when against them to a reference genome and other standard isoforms.

The bad side of the approach is that there is a high false positive rate. My previous sequencing experience tells me that some transcripts may never be detected even by PCR. And the transcripts could look weird because they might be fused with other genes, LncRNA, miRNA, etc., to form a very long and unreliable form. Also, you may never find a transcript from the standard isoform even from the control. And sometimes you can find the intron region is not appropriately spliced. But those are all normal and possible. Because the Trinity algorithm is not perfect. Those "abnormal" transcripts could be a false positive result or something different does happen here and have some biological meanings. But most of the time, I believe the first result.

As a result, though this tech might looks fancy and could get a very beautiful result, it is worthy to be verified by other means and be talked very carefully.

## Find novo transcripts based on Trinity de-nove assembly

This post is based on the Slurm system.
The main steps are included in:
  - De-novo Assembly by Trinity (Trinity)
  - Local align the Gene into the Trinscriptom (Biopython, blast+)
  - Align the Transcripts into the Genome (blast+)
  - Visualization (ggbio)



Prepare a file for the group and locations
<pre>
S39_	../../RNA_RAW/S39_L001_R1_001.fastq.gz
S39_	../../RNA_RAW/S39_L001_R2_001.fastq.gz
S39_	../../RNA_RAW/S39_L002_R1_001.fastq.gz
...
</pre>


## Pipeline

### Step 1: Assembly and Make Blast DB

```bash
module load trinity/2.8.5
module load jellyfish
module load ncbi-blast/2.12.0+

mkdir script
mkdir Transcirptons
mkdir LOG

for SAMPLE in $(awk '{print $1}' File.list | sort |uniq); do
    # if the result not exist:
    if [ -f Transcirptons/$SAMPLE.fa ]; then
        echo $SAMPLE
    else
        sed "s/--job-name=GATK/--job-name=$SAMPLE/;s/--output=Hi.out/--output=LOG\/$SAMPLE.out/;s/--error=Hi.err/--error=LOG\/$SAMPLE.err/" Model.sh > script/$SAMPLE.sh
        echo Trinity --seqType fq --CPU 64 --max_memory 60G  --output trinity_$SAMPLE --single $(grep $SAMPLE File.list| awk '{print $2}'| tr "\n" ","| sed 's/,$/ /')  >> script/$SAMPLE.sh
        echo cp trinity_$SAMPLE/Trinity.fasta Transcirptons/$SAMPLE.fa >> script/$SAMPLE.sh
        echo makeblastdb -in Transcirptons/$SAMPLE.fa  -dbtype nucl -parse_seqids -out Transcirptons/$SAMPLE  >> script/$SAMPLE.sh
        echo rm -rf trinity_$SAMPLE >> script/$SAMPLE.sh
        sbatch script/$SAMPLE.sh
    fi
done
```

### Step 1: Target Genes


```bash
mkdir Genes
mkdir Trans_anno
mkdir Genome_pos

GENOME=../DB/BDGP6.32
GTF=../DB/Drosophila_melanogaster.BDGP6.32.104.chr.EGFP.GAL4.mCD8GFP.gtf
GENE=Mmp1

CHROM=$(grep -w \"$GENE\" $GTF| awk '{print $1}'| head -n 1)
START=$(grep -w \"$GENE\" $GTF| awk '{print $4}'| sort -n | head -n 1)
TOEND=$(grep -w \"$GENE\" $GTF| awk '{print $5}'| sort -n | tail -n 1)

python GeneExtract.py -g $GENE -c $CHROM -s $START -e $TOEND -f $GENOME.fa -o Genes/$GENE.fa

for SAMPLE in $(ls Transcirptons| grep ".fa"| sed 's/.fa//'); do
    if [ -f  Genome_pos/$SAMPLE-$GENE.csv ]; then
        echo $SAMPLE is done
    else
        sed "s/Hi/$SAMPLE\_blt/" Model.sh > script/$SAMPLE\_$GENE\_blt.sh
        echo  "blastn -query Genes/$GENE.fa  -db Transcirptons/$SAMPLE -outfmt '6 qacc sacc evalue qstart qend sstart send' -evalue 1e-1 -max_target_seqs 1000 -num_threads 8 -max_hsps 10000 > Trans_anno/$SAMPLE-$GENE.csv" >> script/$SAMPLE\_$GENE\_blt.sh
        echo "grep -A 1 -wE \$(awk '{print \$2}' Trans_anno/$SAMPLE-$GENE.csv| sort | uniq| tr '\n' '|' | sed 's/|$/\n/') Transcirptons/$SAMPLE.fa| grep -v '^--' >  Trans_anno/$SAMPLE-$GENE.fa" >> script/$SAMPLE\_$GENE\_blt.sh
        echo "blastn -query Trans_anno/$SAMPLE-$GENE.fa  -db $GENOME -outfmt '6 qacc sacc evalue qstart qend sstart send' -evalue 1e-1 -max_target_seqs 1000 -num_threads 8 -max_hsps 10000 > Genome_pos/$SAMPLE-$GENE.csv"  >> script/$SAMPLE\_$GENE\_blt.sh
        sbatch script/$SAMPLE\_$GENE\_blt.sh
    fi
done
```

`grep .  Genome_pos/*Mmp1*| sed 's/:/\t/;s=Genome_pos/==;s/__Mmp1.csv//' > Mmp1.csv`


```r
library(ggplot2)
library(reshape2)
library(stringr)
library(GenomicFeatures)

GENE = "Mmp1"
GTF <- read.table("../DB/Drosophila_melanogaster.BDGP6.32.104.chr.EGFP.GAL4.mCD8GFP.gtf", sep ='\t')
GTF2 <- GTF[grep("transcript_id", GTF$V9),]
GTF2$TranID <- as.data.frame(str_split_fixed(as.data.frame(str_split_fixed(GTF2$V9, "transcript_id ", 2))[[2]], ";", 2))[[1]]
GTF2$GENE <- as.data.frame(str_split_fixed(as.data.frame(str_split_fixed(GTF2$V9, "gene_name ", 2))[[2]], ";", 2))[[1]]
GTF2 <- GTF2[GTF2$V3 %in% c("exon", "start_codon", "stop_codon"),]
wh = GTF2$V4[grep(GENE, GTF2$V9)]

TB <- read.table("Mmp1.csv")
TB$ID=paste(TB$V1, TB$V2)
TB$X1 = apply(TB[c("V7","V8")], 1, min)
TB$X2 = apply(TB[c("V7","V8")], 1, max)
TB$Y = as.numeric(as.factor(TB$ID))*-1 +1
#autoplot(txdb, which= Trans[GENE][[1]], gap.geom = "chevron")
#SAMPLE = c("CF-1_S1", "CF-2_S2", "CF-3_S3", "wt_10day_1_S27", "wt_10day_2_S28", "wt_10day_3_S29", "TF-1_S7", "TF-2_S8", "TF-3_S9", "TM-1_S10", "TM-2_S11", "TM-3_S12", "G15F_S46", "G15-M_TUMOR-a_S35", "G15-M_TUMOR-b_S36", "G17F_S51", "G17M_S32", "G1F1_S31", "G1F2_S47", "G1M1_S48", "G1M2_S49", "G2M_S50", "G50-FE_TUMOR-a_S37", "G50-FE_TUMOR-b_S38", "G5M_S45", "MG1T10-1_S32", "MG1T10-2_S33", "MG1T10-3_S34", "NICD_SxlRF1_S39", "NICD_SxlRF2_S40", "NICD_TraR2F1_S33", "NICD_TraR2F2_S34", "NICD_TraR2F3_S35", "NICD_TraR3F1_S36", "NICD_TraR3F2_S37", "NICD_TraR3F3_S38")
# TB <- TB[TB$V1 %in% SAMPLE,]
RegionPlot <- function(GENE){
    MAX = max(as.numeric(as.matrix(GTF2[GTF2$GENE==GENE,c("V4", "V5")])))
    MIN = min(as.numeric(as.matrix(GTF2[GTF2$GENE==GENE,c("V4", "V5")])))
    CHM = head(GTF2[GTF2$GENE==GENE,"V1"],1)
    tmp_GTF = GTF2[GTF2$V4 >= MIN,]
    tmp_GTF = tmp_GTF[tmp_GTF$V5 <= MAX,]
    tmp_GTF = tmp_GTF[tmp_GTF$V1 == CHM,]
    tmp_TB = TB[-c(17,27),]
    ggplot()+ theme_bw()+   
        geom_line(data=tmp_GTF, aes(x= V4, y=TranID, group=TranID))+
        geom_tile(data=tmp_GTF, aes(x=(V4+V5)/2, y=TranID, width= abs(V5-V4), height= .9, color=V3), fill='grey')+
        scale_color_manual(values = c("black","red","blue")) +
        geom_line(data=tmp_TB, aes(x= V7, y=ID, group=Y), size=1, alpha= .6)+
        geom_tile(data=tmp_TB, aes(x= (X1+X2)/2, width= abs(V8-V7),y=ID, height= .9,fill=V1), size=1, color="black")+ xlim(c(MIN, MAX))+
        facet_grid(V1~., space = 'free', scales = 'free')


}

RegionPlot_fact <- function(GENE){
    MAX = max(as.numeric(as.matrix(GTF2[GTF2$GENE==GENE,c("V4", "V5")])))
    MIN = min(as.numeric(as.matrix(GTF2[GTF2$GENE==GENE,c("V4", "V5")])))
    CHM = head(GTF2[GTF2$GENE==GENE,"V1"],1)
    tmp_GTF = GTF2[GTF2$V4 >= MIN,]
    tmp_GTF = tmp_GTF[tmp_GTF$V5 <= MAX,]
    tmp_GTF = tmp_GTF[tmp_GTF$V1 == CHM,]
    tmp_TB = TB[-c(17,27),]

    TRANS_list = list()
    for( TRANS in unique(tmp_GTF$TranID)){
        tmp_Tran_TB <- tmp_GTF[tmp_GTF$TranID == TRANS,c("V4","V5")]
        C_tmp = c()
        for(i in c(1:nrow(tmp_Tran_TB))){
            C_tmp = c(C_tmp, c(tmp_Tran_TB[i,1]:tmp_Tran_TB[i,2]))
        }
        tmp = list(C_tmp)
        names(tmp) = TRANS
        TRANS_list <- append(TRANS_list, tmp)
    }

    Seq_list = list()
    for( TRANS in unique(tmp_TB$ID)){
        tmp_Tran_TB <- tmp_TB[tmp_TB$ID == TRANS,c("X1","X2")]
        C_tmp = c()
        for(i in c(1:nrow(tmp_Tran_TB))){
            C_tmp = c(C_tmp, c(tmp_Tran_TB[i,1]:tmp_Tran_TB[i,2]))
        }
        tmp = list(C_tmp)
        names(tmp) = TRANS
        Seq_list <- append(Seq_list, tmp)
    }


    RESULT = data.frame()
    for(TRANS in names(TRANS_list)){
        for(Seq in names(Seq_list)){
            Cover1 = table(TRANS_list[[TRANS]] %in% Seq_list[[Seq]])['TRUE'][[1]]/ length(TRANS_list[[TRANS]])
            Cover2 =
            table(Seq_list[[Seq]] %in% TRANS_list[[TRANS]])['TRUE'][[1]]/ length(Seq_list[[Seq]])
            RESULT = rbind(RESULT, data.frame(TRANS=TRANS, Seq=Seq, Cover1= Cover1, Cover2 = Cover2))
        }
    }

    RESULT[is.na(RESULT)] <- 0
    RESULT$Cover = apply(RESULT[3:4], 1, sum)
    RESULT <- RESULT[order(RESULT$Cover,decreasing = T),]
    RESULT <- RESULT[!duplicated(RESULT$Seq),]

    LIST =c()
    for( i in unique(RESULT$TRANS)){
        LIST= c(LIST, c(i, as.character(RESULT$Seq[RESULT$TRANS == i])))
    }

    tmp_GTF$TranID <- factor(tmp_GTF$TranID, levels= unique(LIST))
    tmp_TB$ID <- factor(tmp_TB$ID, levels= LIST)

    tmp_GTF$TranID <- factor(tmp_GTF$TranID, levels= unique(LIST))
    colnames(tmp_GTF)[c(4,5,10)] <- c("X1", "X2", "ID")
    tmp_TB['V3'] <- "exon"


    TB_plot <- rbind(tmp_GTF[c("X1", "X2", "ID", "V3")], tmp_TB[c("X1", "X2", "ID", "V3")])
    TB_plot$ID <- factor(TB_plot$ID, levels=rev.default(LIST))
    TB_plot$TRANS <- RESULT$TRANS[match(TB_plot$ID, RESULT$Seq)]
    TB_plot$TRANS[is.na(TB_plot$TRANS)] <- TB_plot$ID[is.na(TB_plot$TRANS)]
    TB_plot$Cove = RESULT$Cover1[match(TB_plot$ID, RESULT$Seq)]
    TB_plot$Cove[is.na(TB_plot$Cove)] <- 1


    ggplot(TB_plot[TB_plot$Cove >=.5,], aes(fill=TRANS))+ theme_bw()+    
        geom_line(aes(x= X1, y=ID, group=ID))+
        geom_tile(aes(x=(X1+X2)/2, y=ID, width= abs(X2-X1), height= .9, color=V3), fill='grey')+
        scale_color_manual(values = c("black","red","blue")) + xlim(c(MIN, MAX)) +
        facet_grid(TRANS~., space = 'free', scales = 'free')
}


library(ggbio)
library(GenomicFeatures)
library(clusterProfiler)
library(org.Dm.eg.db)
library(Rsamtools)

txdb <- makeTxDbFromGFF(file="../DB/Drosophila_melanogaster.BDGP6.32.104.chr.EGFP.GAL4.mCD8GFP.gtf", format="gtf")
Trans <- transcriptsBy(txdb, "gene")
tmp <- bitr(names(Trans), fromType="FLYBASE", toType="SYMBOL", OrgDb="org.Dm.eg.db")
names(Trans)[!is.na(tmp[[2]][match(names(Trans), tmp[[1]])])] <- tmp[[2]][match(names(Trans), tmp[[1]])][!is.na(tmp[[2]][match(names
    (Trans), tmp[[1]])])]

bam<-BamFile(file="../Bam/G50-FE_TUMOR-a_S37Aligned.sortedByCoord.out.bam", index="../Bam/G50-FE_TUMOR-a_S37Aligned.sortedByCoord.out.bam.bai")
RegionPlot_ggbio <-function(GENE, SAMPLE="G50-FE_TUMOR-a_S37"){
    P1 <- autoplot(txdb, which= Trans[[GENE]])+ theme_bw()
    tmp = range(Trans[[GENE]])
    rg = c(tmp@ranges@start, tmp@ranges@start+tmp@ranges@width)
    wh = as(c(paste(tmp@seqnames@values, ":", tmp@ranges@start, "-", tmp@ranges@start+tmp@ranges@width, sep ="")), "GRanges")

    MAX = wh@ranges@start + wh@ranges@width
    MIN = wh@ranges@start
    CHM = wh@seqnames@values
    tmp_TB = TB[-c(17,27),]
    tmp_TB <- tmp_TB[tmp_TB$V1==SAMPLE,]
    tmp_TB$V2 <- factor(tmp_TB$V2, levels=unique(tmp_TB$V2))
    P_TRANS <- ggplot()+ theme_bw()+   
        scale_color_manual(values = c("black","red","blue")) +
        geom_line(data=tmp_TB, aes(x= V7, y=V2, group=Y), size=1, alpha= .6, show.legend = F)+
        geom_tile(data=tmp_TB, aes(x= (X1+X2)/2, width= abs(V8-V7),y=V2, height= .5,fill=V1), size=1, color="black", show.legend = F)+ xlim(c(MIN, MAX))+theme(axis.text.y = element_blank())+
        geom_text(data=tmp_TB, aes(x= MIN, y=as.numeric(V2)+.5, label=V2), vjust = .5, hjust =0, size = 3.5)

    P2 <- autoplot(bam, which =wh,  stat = "coverage") + theme_bw() + theme(legend.position="none") + coord_cartesian(xlim =c(wh@ranges@start, wh@ranges@start + wh@ranges@width))
    tracks(Coverage=P2, Transcripts=P1, Trans= P_TRANS, heights = c(0.4, Trans[[GENE]]@seqnames@lengths * .1, length(unique(tmp_TB$V2))*.1), title=SAMPLE) + ylab("")
    H = 2.58 + (Trans[[GENE]]@seqnames@lengths +length(unique(tmp_TB$V2))) *.48
    ggsave(paste('img/', SAMPLE,"_",GENE,".png",sep=""), w= 10, h = H)
}



# for loop

for(SAMPLE in unique(TB$V1)){
    print(SAMPLE)
    if(SAMPLE != "G50-FE_TUMOR-b_S38"){
        BAM = paste("../Bam/",SAMPLE,"Aligned.sortedByCoord.out.bam", sep="")
        BAI = paste("../Bam/",SAMPLE,"Aligned.sortedByCoord.out.bam.bai", sep="")
        bam<-BamFile(file= BAM, index= BAI)
        RegionPlot_ggbio(GENE, SAMPLE)
    }
}
```

|![](https://s1.ax1x.com/2022/09/03/vo6OZ6.png)|![](https://s1.ax1x.com/2022/09/03/vo6XdK.png)|
|:-:|:-:|


|![](https://s1.ax1x.com/2022/09/02/vICOX9.png)|
|:-:|
|Plot for single Sample with Depth|

## Add this to `GeneExtract.py`
```python
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument('-g','--gene')     
parser.add_argument('-o','--output')     
parser.add_argument('-c','--chrom')     
parser.add_argument('-s','--start', type =int)     
parser.add_argument('-e','--end', type=int)     
parser.add_argument('-f','--fasta')     

##获取参数
args = parser.parse_args()


GENE=   args.gene
CHROM=  args.chrom
START=  args.start
TOEND=  args.end
GENOME= args.fasta
OUT=    args.output

for seq_record in SeqIO.parse(GENOME, "fasta"):
    if seq_record.id == CHROM:
        F =open(OUT, 'w')
        F.write(">" + GENE+"\n")
        F.write(str(seq_record.seq[START-1:TOEND]) + "\n")
        F.close()
```
