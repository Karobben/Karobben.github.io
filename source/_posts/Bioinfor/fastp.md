---
title: "fastp"
description: "fastp| reads clean"
url: "fastp"
date: 2020/07/28
toc: true
excerpt: "fastp is a fast and efficient tool for quality control and preprocessing of high-throughput sequencing data. It can perform adapter trimming, quality filtering, and read correction in a single pass, and supports various sequencing platforms and data formats."
tags: [Software, Bioinformatics, NGS, QC]
category: [Biology, Bioinformatics, Software, Fasta/q]
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

Just download the build version:
```bash
wget http://opengene.org/fastp/fastp
chmod a+x fastp
```


!!! info Bioconda
    `conda install -c bioconda fastp`

## Usage

```bash
fastp -i in.fq -o out.fq
## for paired end data (gzip compressed)
fastp -i in.R1.fq.gz -I in.R2.fq.gz -o out.R1.fq.gz -O out.R2.fq.gz
```

## Some Examples

!!! note delete reads with mean score value >= 20
    - To remove reads with a mean quality score lower than 20 using fastp, you can use the -e option. This option sets the minimum mean quality score required for a read to be kept. If the mean quality score of a read is below this threshold, the read will be discarded.<br>
    - for single end: `fastp -i input.fq -o filtered_output.fq -e 20` <br>
    - for paired-ends: `fastp -i in1.fq -I in2.fq -o out1.fq -O out2.fq -e 20`
