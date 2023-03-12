---
title: "fastp"
description: "fastp| reads clean"
url: "fastp"
date: 2020/07/28
toc: true
excerpt: "fastp is a fast and efficient tool for quality control and preprocessing of high-throughput sequencing data. It can perform adapter trimming, quality filtering, and read correction in a single pass, and supports various sequencing platforms and data formats."
tags: [Software, Bioinformatics, NGS, QC]
category: [Biology, Bioinformatics, Software, FastQC]
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

!!! info Bioconda
    `conda install -c bioconda fastp`

## Usage

```bash
fastp -i in.fq -o out.fq
## for paired end data (gzip compressed)
fastp -i in.R1.fq.gz -I in.R2.fq.gz -o out.R1.fq.gz -O out.R2.fq.gz
```
