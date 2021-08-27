---
title: "fastp"
description: "fastp| reads clean"
url: "fastp"
date: 2020/07/28
toc: true
excerpt: "Fastp, a fastq reads QC software"
tags: [Software, Bioinformatics, Fastq QC]
category: [Biology, Bioinformatics, Software, Fastq QC]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## Fastp

Location: [Github](https://github.com/OpenGene/fastp)

## Install

```bash
## get source (you can also use browser to download from master or releases)
git clone https://github.com/OpenGene/fastp.git
## build
cd fastp
make
## Install
sudo make install
```

## Usage

```bash
fastp -i in.fq -o out.fq
## for paired end data (gzip compressed)
fastp -i in.R1.fq.gz -I in.R2.fq.gz -o out.R1.fq.gz -O out.R2.fq.gz
```
