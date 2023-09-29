---
title: "Comprehensive Analysis of Large-Scale FastQC Results using Python"
ytitle: "用python收集FastaQC的结果"
description: "Comprehensive Analysis of Large-Scale FastQC Results using Python"
url: fastqc_crawl
date: 2022/07/20
toc: true
excerpt: "python"
tags: [Python, HTML, QC]
category: [Python, Data]
cover: 'https://s1.ax1x.com/2022/07/23/jXHAeg.png'
covercopy: '© Karobben'
thumbnail: 'https://s1.ax1x.com/2022/07/23/jXHAeg.png'
priority: 10000
---

## FastqQC

FastQC aims to provide a simple way to do some quality control checks on raw sequence data coming from high throughput sequencing pipelines. It provides a modular set of analyses which you can use to give a quick impression of whether your data has any problems of which you should be aware before doing any further analysis. [© illumina](https://www.illumina.com/products/by-type/informatics-products/basespace-sequence-hub/apps/fastqc.html)

When dealing with a large number of samples, it's crucial to conduct quality control (QC) and scrutinize the results to identify any outliers. Filtering out low-quality data can significantly influence subsequent processes. Below is an example illustrating how we use all QC results from FastQC for cluster analysis.

## Summary information collect

```python
import os
import pandas as pd
from bs4 import BeautifulSoup

def Tab_grep(Sample):
    html = open(Sample).read()
    soup = BeautifulSoup(html, features='lxml')
    Summary = soup.find_all('div',{"class":"summary"})[0]
    Reu_l = [Sample]
    Cla_l = ["Sample"]
    for line in Summary.find_all("li"):
        Cla_l += [line.get_text()]
        Reu_l += [str(line).split('"')[1]]
    Result_TB = pd.DataFrame([Reu_l], columns=Cla_l)
    return Result_TB

Result_TB = pd.DataFrame()
for Sample in [i for i in os.listdir() if "fastqc.html" in i]:
    Result_TB = pd.concat([Result_TB, Tab_grep(Sample)])

Result_TB.to_csv("QC.csv")
```

Plot in R

```r
library(ggplot2)
library(reshape2)

TB <- read.csv("QC.csv")[-1]
TB_P <- melt(TB, id.vars = "Sample")
ggplot() +   geom_tile(data= TB_P, aes(Sample,variable, fill= value))
```

|![](https://s1.ax1x.com/2022/07/24/jXH3mF.png)|
|:-:|

## Save the picutre in one file

```python

import os
import pandas as pd
from bs4 import BeautifulSoup

def Pic_save(Sample, OUT="/home/wliu15/OUT.md"):
    html = open(Sample).read()
    soup = BeautifulSoup(html, features='lxml')
    F = open(OUT,"a")
    F.write(Sample+"\n")
    F.write(str(soup.find('h2',{"id":"M5"})))
    F.write(str(soup.find('img',{"alt" : "Per base sequence content"})))
    F.close()

for Sample in [i for i in os.listdir() if "fastqc.html" in i]:
    Pic_save(Sample)
```

|![](https://s1.ax1x.com/2022/07/24/jXHGTJ.png)|
|:-:|

## Overrepresented Sequences

```python
import pandas as pd

TB = pd.DataFrame()
for Sample in [i for i in os.listdir() if "fastqc.html" in i]:
    if len(pd.read_html(Sample))!=1:
        TMP = pd.read_html(Sample)[1]
        TMP['Sample'] = Sample
        TB = pd.concat([TB, TMP])
```

||Sequence|Count|Percentage|Possible Source|Sample
|:-|:-|:-|:-|:-|:-
0|CCGGTAGTTATTAAAGAATTCTTTTCCATGCCCAAATGCGGCACGTACTC|33857|0.178685926|No Hit|S41_L002_R2_001_fastqc.html
1|CTTGATTATGTCTGTTTCTGATAACTACATTGAACACTTTAATGCTGTTA|26767|0.141267276|No Hit|S41_L002_R2_001_fastqc.html
2|GAAAGTGTCAACGATACACCCATGTGGATAAAGGAACCCATAGCCTTTAA|19126|0.100940633|No Hit|S41_L002_R2_001_fastqc.html
0|GTCCTTTCGTACTAAAATATCATAATTTTTTAAAGATAGAAACCAACCTG|24695|0.145008391|No Hit|S15_L002_R2_001_fastqc.html
1|CTCGTCTTTTAAATAAATTTTAGCTTTTTGACTAAAAAATAAAATTCTAT|17359|0.101931592|No Hit|S15_L002_R2_001_fastqc.html
0|CTCGTCTTTTAAATAAATTTTAGCTTTTTGACTAAAAAATAAAATTCTAT|19353|0.111227104|No Hit|S44_L002_R2_001_fastqc.html
1|GTCCTTTCGTACTAAAATATCACAATTTTTTAAAGATAGAAACCAACCTG|18903|0.108640828|No Hit|S44_L002_R2_001_fastqc.html
