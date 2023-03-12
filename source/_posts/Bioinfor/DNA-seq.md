---
toc: true
url: DNA_seq
covercopy: <a href="https://pixabay.com/illustrations/research-virus-corona-coronavirus-5297028/">© PixxlTeufel  </a>
date: 2022-08-26 13:36:01
title: "DNA Seq Pipeline and General Infor statistics"
ytitle: "DNA Seq Pipeline and General Infor statistics"
description: "DNA Seq Pipelines and tricks"
excerpt: "DNA Seq Pipelines and tricks"
tags: [Software, Bioinformatics, NGS]
category: [Biology, Bioinformatics, Software, De nove]
cover: 'https://cdn.pixabay.com/photo/2020/06/14/09/00/research-5297028_1280.jpg'
thumbnail: 'https://cdn.pixabay.com/photo/2020/06/14/09/00/research-5297028_1280.jpg'
priority: 10000
---


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>

## DNA seq Pipeline

## Quality Control

Quality control can use [fastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/). In DNA-seq data, we may find lots of overrepresented sequences from mitochondria and it is totally normal. Not like RNA-seq, we do not expect errors in GC content.

```bash
mkdir fastQC/
fastqc -o ./fastQC/ -t 7 reads.fq
```

for loop for slumn system
Example file:
<pre>
GFP-1_L1_1.fq.gz
GFP-1_L1_2.fq.gz
</pre>

```bash
FQ_DB={dir for fastq}

for i in $(ls $FQ_DB/* );
    do SAMPLE=$(echo $i|sed 's=FQ/==;s/.fq.gz//')
    sed "s/Hi/$SAMPLE\_fQC/" Model.sh > script/$SAMPLE\_fQC.sh
    echo fastqc -o fastQC   -t 7 $i  >> script/$SAMPLE\_fQC.sh
    sbatch script/$SAMPLE\_fQC.sh
done
```


## Align to the Genome

Choose appropriate short reads tools for your data. I heard that bwa was more suitable for short reads align, so it is frequently used in the miRNA-Seq pipeline. Bowtie is faster and can do better on longer reads alignment. According to this, if your reads are short like 50~70bp, you can choose bwa. If your reads are paired from 150~300bp, bowtie2 would work better.

In the post from [David, 2015](https://www.biostars.org/p/125020/); the best short-reads alignment tool is `segemehl`. Meanwhile, `bwa` was more sensitive than `bowtie2`. According to the  [Benchmark](https://www.ecseq.com/support/benchmark.html), the best tools for DNA-Seq is `segemehl` or `BWA-MEM`, the best tools for RNA-Seq is `segemehl`

|![](https://pbs.twimg.com/media/B537ZShCcAASTmY.jpg)|
|:-:|
|[© ecSeq Bioinformatics](https://www.ecseq.com/support/benchmark.html)|


### Scripts for align all your fq

#### Genome index

```bash
bwa index Genome.fa
```

#### Single end reads

In this Part, we will map all reads from the same directory to the reference genome by using `bwa`. Because programs would fail sometimes and we need to run them again. So, we can check and run only when the results don't exist.


```bash
FQ_DB={Your Directory}
DB={Your Reference Genome}

for SAMPLE in $(ls $FQ_DB/*L001*|awk -F/ '{print $NF}'| awk -F_ '{print $1"_"$2}'| sort |uniq); do
    if [ -f $SAMPLE.sorted.bam ]; then
        echo $SAMPLE is done
    else
        echo $SAMPLE can not be find
        sed "s/Hi/$SAMPLE/" Model.sh > script/$SAMPLE.sh
        echo cat $FQ_DB/$SAMPLE* \| bwa mem $DB -  -t 64 \|samtools view -S -b -\|samtools sort \> $SAMPLE.sorted.bam >> script/$SAMPLE.sh
        echo samtools index $SAMPLE.sorted.bam >> script/$SAMPLE.sh
        sbatch script/$SAMPLE.sh
    fi
done

## Check unexpected size of file
rm $(du   *.sorted.bam | awk '$1<=100'| awk '{print $2}')
## After removed failed files, we can excute the for loop again

for SAMPLE in $(ls $FQ_DB/*L001*|awk -F/ '{print $NF}'| awk -F_ '{print $1"_"$2}'| sort |uniq); do
    if [ -f $SAMPLE.sorted.bam ]; then
        echo $SAMPLE is done
    else
        echo $SAMPLE can not be find
        sed "s/Hi/$SAMPLE/" Model.sh > script/$SAMPLE.sh
        echo mv $SAMPLE.sorted.sam $SAMPLE.sorted.bam >> script/$SAMPLE.sh
        echo samtools index $SAMPLE.sorted.bam >> script/$SAMPLE.sh
        sbatch script/$SAMPLE.sh
    fi
done
```

Then, move every thing to one directory.
```bash
mkdir Bam
mv *bam* Bam
rm *.err *.out # Clear logs
```

#### Paired end reads

Name Example of my Paired multiple-lines reads:
<pre>
S40_L001_R1_001.fastq.gz
S40_L001_R2_001.fastq.gz
S40_L002_R1_001.fastq.gz
S40_L002_R2_001.fastq.gz
S41_L001_R1_001.fastq.gz
S41_L002_R1_001.fastq.gz
</pre>

`S40` is two lines paired-ends sample, `S41` is two lines single-ends sample.

```bash
module load samtools bwa

mkdir script
mkdir Log
mkdir Bam
mkdir tmp

FQ_DB={Your Directory}
DB={Your Reference Genome}
#FQ_DB="../../RNA_RAW/*/*/"
#DB=DB/Genome.fa

# Get the unique sample names:
# ls  $Directory/*.gz| awk -F"/" '{print $NF}'| sed 's/_L00[12]_R[12]_001.fastq.gz//'| sort |uniq

for SAMPLE in $(ls  $FQ_DB/*.gz| awk -F"/" '{print $NF}'| sed 's/_L00[12]_R[12]_001.fastq.gz//'| sort |uniq); do
    echo $SAMPLE;
    # check the exist of the result
    if [ -f Bam/$SAMPLE.sorted.bam ]; then
        echo $SAMPLE is done
    else
        # check the Number of the files. 4 means paired and 2 means unpaireds
        if [ $(ls $FQ_DB/$SAMPLE*|wc -l) -eq 4 ]; then
            echo Paired
            sed "s/Hi/$SAMPLE/" Model.sh > script/$SAMPLE.sh
            echo cat $FQ_DB/$SAMPLE*L00[12]_R1_* \> tmp/$SAMPLE.R1.fq.gz >> script/$SAMPLE.sh
            echo cat $FQ_DB/$SAMPLE*L00[12]_R2_* \> tmp/$SAMPLE.R2.fq.gz >> script/$SAMPLE.sh
            echo bwa mem $DB tmp/$SAMPLE.R[12].fq.gz  -t 64 \|samtools view -S -b -\|samtools sort \> $SAMPLE.sorted.bam >> script/$SAMPLE.sh
            echo samtools index $SAMPLE.sorted.bam >> script/$SAMPLE.sh
            echo mv $SAMPLE.sorted.bam $SAMPLE.sorted.bam.bai Bam >> script/$SAMPLE.sh
            echo rm tmp/$SAMPLE.R[12].fq.gz >> script/$SAMPLE.sh
        else
            echo Single
            sed "s/Hi/$SAMPLE/" Model.sh > script/$SAMPLE.sh
            echo cat $FQ_DB/$SAMPLE* \| bwa mem $DB - -t 64 \|samtools view -S -b -\|samtools sort \> $SAMPLE.sorted.bam >> script/$SAMPLE.sh
            echo samtools index $SAMPLE.sorted.bam >> script/$SAMPLE.sh
            echo mv $SAMPLE.sorted.sam $SAMPLE.sorted.bam >> script/$SAMPLE.sh
            echo samtools index $SAMPLE.sorted.bam >> script/$SAMPLE.sh
            echo mv $SAMPLE.sorted.bam $SAMPLE.sorted.bam.bai Bam >> script/$SAMPLE.sh
        fi
        sbatch script/$SAMPLE.sh
    fi
done
```


After checking the size of bam and re-run the failed files, each file has:
- Bam: all bam results and bam index
- Log: log files generated by sbatch. (Disposable)
- tmp： temporarily combined reads from different lines and should be cleaned. (Disposable)
- scripts: scripts for each sample from aligning to sort. (Disposable)

## Basic information Statistics

<pre>
.
└── Bam
│   ├── GFP-1.sorted.bam
│   └── GFP-2.sorted.bam
└── Model.sh
</pre>

```bash
mkdir Bam_stats script

for i in $(ls Bam/*.bam); do
    SAMPLE=$(echo $i| sed 's=Bam/==;s/.sorted.bam//');
    if [ -f Bam_stats/$SAMPLE.stats.csv ]; then
        echo $SAMPLE is done
    else
        sed "s/Hi/$SAMPLE\_BamStat/" Model.sh > script/$SAMPLE\_BamStat.sh
        echo samtools stats $i \> Bam_stats/$SAMPLE.stats.csv >> script/$SAMPLE\_BamStat.sh
        sbatch script/$SAMPLE\_BamStat.sh
    fi
done
```

After jobs are done, we can `grep` the SN infor from all samples into one:

```bash
grep ^SN Bam_stats/*| sed 's/.stats.csv:SN//;s=Bam_stats/==' | awk -F"\t" '{OFS="\t"; print $1,$2,$3}'| sed 's/://' > SN_infor.csv
```

### Insert size statistics

|What is insert size|
|:-:|
|![](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3906532/bin/fgene-05-00005-g001.jpg)|
|[© Frances S. Turner, 2014](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3906532/)|

!!! note Why there are negative insert sizes?
    Negative insert sizes can happen when the first read is mapped to the reverse strand. we can change it by using `awk '{print sqrt(\$0^2)}'`

Reference: [accio, 2020](https://accio.github.io/bioinformatics/2020/03/10/filter-bam-by-insert-size.html)
It might be help in ChIP-seq data.

```bash
for i in $(ls Bam/SJ_*.bam); do
    SAMPLE=$(echo $i| sed 's=Bam/==;s/.sorted.bam//');
    if [ -f Bam_stats/$SAMPLE.insert.csv ]; then
        echo $SAMPLE is done
    else
        sed "s/Hi/$SAMPLE\_BamStat/" Model.sh > script/$SAMPLE\_BamInser.sh
        echo samtools view -f66 $i \| cut -f9 \| awk "'{print sqrt(\$0^2)}'" \>  Bam_stats/$SAMPLE.insert.csv >> script/$SAMPLE\_BamInser.sh
        bash script/$SAMPLE\_BamInser.sh &
    fi
done
```

```bash
grep . Bam_stats/*.insert.csv| sed 's=Bam_stats/==;s/.insert.csv:/ /' > Insert.csv
```

Check the number of lines from each file and remove incorrect files.

### Visualization by ggplot2

Creat a directory, `img`, for storing the results.

```bash
mkdir img
```

```r
library(ggplot2)
library(stringr)
library(reshape2)
library(pheatmap)
library(ggplotify)

TB <- read.table("SN_infor.csv", sep = '\t')
Norm_list <- TB$V2[TB$V1==TB$V1[[1]]][TB$V3[TB$V1==TB$V1[[1]]] >= 1000]

## Bar plot 1: sort by total reads

TB$V1 <- factor(TB$V1, levels=as.character(na.omit(TB$V1[TB$V2=='raw total sequences'][order(TB$V3[TB$V2=='raw total sequences'])])))
ggplot(TB, aes(V1,V3)) + geom_bar(stat = 'identity') +
    facet_wrap(~V2, scales = 'free') + theme_bw()+theme(strip.background = element_rect(fill = 'white'), strip.text.x = element_text(size = 10))

ggsave("img/Stats_Sort_reads.png", w= 20, h= 10.9)

## Bar plot 2; sort by 'reads length'
TB$V1 <- factor(TB$V1, levels=as.character(na.omit(TB$V1[TB$V2=='raw total sequences'][order(TB$V3[TB$V2=='average length'])])))
ggplot(TB, aes(V1,V3)) + geom_bar(stat = 'identity') +
    facet_wrap(~V2, scales = 'free') + theme_bw()
ggsave("img/Stats_Sort_AL.png", w= 20, h= 10.9)

TB_w <- reshape(TB, timevar = "V1", idvar = "V2", direction = 'wide')
row.names(TB_w) <- TB_w[[1]]
TB_w <- TB_w[-1]
colnames(TB_w) <- str_replace(colnames(TB_w), "V3.", "")


# Corrolation Plot
List <- row.names(TB_w)[!is.na(data.frame(scale(t(TB_w)))[1,])]
TB_ww <- TB_w[row.names(TB_w)%in% List,]
ggpairs(as.data.frame(t(TB_ww)))
ggsave("123.png", w=30, h = 30)

TB_cor <- as.data.frame(cor(t(TB_ww)))
corPLOT <- function(COL, CUT=0.75){
    Cor_tmp = data.frame(
        X = row.names(TB_cor)[order(abs(TB_cor[COL]))],
        Y = TB_cor[COL][order(abs(TB_cor[COL])),]
    )
    Cor_tmp$X = factor(Cor_tmp$X, levels = Cor_tmp$X)
    ggplot(Cor_tmp, aes(Y, X, fill = Y)) + geom_bar( stat = 'identity') +
        geom_vline( xintercept = c(CUT, - CUT ), linetype = 2, color= 'grey') +
        geom_text(aes(x=CUT, y=1, label = CUT), hjust = -.1) + theme_bw() +
        ggtitle(COL) + theme(plot.title=element_text(hjust = .5))
    ggsave(paste('img/Cor_', str_replace_all(COL, " ", "_"), ".png", sep =""), w= 7, h= 7)
}


TB_w[row.names(TB_w) %in% Norm_list,]  <- TB_w[row.names(TB_w) %in% Norm_list,]/c(TB_w[1,])


TB_wS <- as.data.frame(t(scale(t(TB_w))))
TB_wS <- TB_wS[!is.na(TB_wS[[1]]),]
TB_w <- TB_w[!is.na(TB_wS[[1]]),]

TB_w[TB_w > 1] <- round(TB_w[TB_w > 1],2)
TB_w[TB_w < 1] <- paste(round(TB_w[TB_w < 1]*100,2), "%")
#TB_w[row.names(TB_w) %in% Norm_list,]  <- round(TB_w[row.names(TB_w) %in% Norm_list,]*100,2)

P <- pheatmap(as.data.frame(scale(t(TB_wS))), display_numbers = t(TB_w[row.names(TB_w) %in% row.names(TB_wS),]), fontsize_col= 15)
as.ggplot(P)
ggsave("img/Stat_Pheatmap.png", w= 20, h = 10.9)

```

|![](https://s1.ax1x.com/2022/09/07/vH0sXt.png)|
|:-:|
|Pheatmap|


### Align Depth Plot

Depth statistics are based on `samtools`: `samtools depth -r UAS:0-10000 sorted.bam`

```bash
mkdir Depth
for i in $(ls Bam/*.bam);
do SAMPLE=$(echo $i| sed 's=Bam/==;s/.sorted.bam//');
    if [ -f Depth/$SAMPLE.csv  ]; then
        echo $SAMPLE is done
    else
        sed "s/Hi/$SAMPLE/" Model.sh > script/Depth_$SAMPLE.sh
        echo samtools depth -r UAS:0-10000  $i \> Depth/$SAMPLE.csv >> script/Depth_$SAMPLE.sh
        sbatch script/Depth_$SAMPLE.sh
    fi

done

rm *.err  *.out
grep . Depth/*.csv| sed 's/.csv//;s/:/\t/;s=Depth/==' > Depth.csv
```


```r
library(ggplot2)
library(stringr)
library(reshape2)

TB <- read.table("Depth.csv")
TB$V1 <- as.character(TB$V1)


TB2 <- TB[TB$V3 %in% c(5300:5600),]

TB_w <- reshape(TB2[c(-2)], idvar = "V1", timevar = "V3", direction = 'wide')
TB_w[is.na(TB_w)] <- 0
row.names(TB_w)= TB_w[[1]]
TB_w = TB_w[-1]
#HCLUST = hclust(dist(TB_w))

TB$V1 <- factor(TB$V1, levels= row.names(TB_w)[order(TB_w$V4.5400)])

ggplot(TB, aes(V3, V4))+ geom_point() + facet_wrap(~V1) +
    xlim(5300,5500) + ylim(0, 100)+theme_bw() +
    theme(strip.text = element_text(size = 20), strip.background = element_rect(fill = 'white'))

ggsave('img/Depth_UAS.png', w= 20,, h = 10.9)
```




















































## `Model.sh`


```bash
#!/bin/sh
#SBATCH --qos=normal            # Quality of Service
#SBATCH --job-name=Hi       # Job Name
#SBATCH --time=1-0:00:00         # WallTime
#SBATCH --mem=256000
#SBATCH --mail-user=123@qq.com
#SBATCH --nodes=1               # Number of Nodes
#SBATCH --ntasks-per-node=1     # Number of tasks (MPI processes)
#SBATCH --cpus-per-task=1       # Number of threads per task (OMP threads)
#SBATCH --output=Log/Hi.out       ### File in which to store job output
#SBATCH --error=Log/Hi.err        ### File in which to store job error messages
```
