---
title: "CPAT"
description: "CPAT"
url: cpat
date: "2020/07/28"
toc: true
excerpt: "Capt to merger transcripts"
tags: [Software, Bioinformatics, RNA-Seq]
category: [Biology, Bioinformatics, Software, De nove]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## CPAT

## Quick start
```bash
cpat.py  -g Tinity.fna -d ~/Biosoft/CPAT-1.2.4/dat/Human_logitModel.RData -x ~/Biosoft/CPAT-1.2.4/dat/Human_Hexamer.tsv -o output
```
```
-r 指定参考基因组  
-g 输入的转录本序列。如果是BED格式，必须-r指定参考基因组；如果是FASTA格式，不需要指定参考基因组，即使使用-r参数也会被忽略。  
-d 预制好的模型（Prebuilt training model）（CPAT自带人、鼠、果蝇、斑马鱼的模型）  
-x 预制好的六聚体频率表（Prebuilt hexamer frequency table）（CPAT自带人、鼠、果蝇、斑马鱼的六聚体频率表）  
-o 输出
```
