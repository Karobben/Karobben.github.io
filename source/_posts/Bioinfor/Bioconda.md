---
title: "Bioconda"
description: "Bioconda"
url: bioconda
date: "2020/07/28"
toc: true
excerpt: "An Integrated Package for Bisulfite DNA Methylation Data Analysis with Indel-sensitive Mapping."
tags: [R, Bioinformatics]
category: [Biology, Bioinformatics, Software, Bioconda]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## Bioconda

## 1. Install
Location: [link](https://bioconda.github.io/user/install.html)
```bash
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
```

## 2. Setup Channels
You may need to add the bin file in your environment
```bash
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```


## Virtual Environment
```
## Create an environment
conda create -n Biostation python=3.7

## Check the env list
conda env list

## 激活工作环境，需要几十秒
source activate Biostation
##or
conda activate Biostation

## 关闭工作环境：不用时关闭，不然你其它程序可能会出错
source deactivate
## Or
conda deactivate
```

## Common Software for Bioinformatics

```bash
conda install fastqc
conda install fastp
conda install trimmomatic
conda install bowtie
conda install bowtie2
conda install samtools
```
## Error

<pre>
UnavailableInvalidChannel: The channel is not accessible or is invalid.
  channel name: miniconda/cloud/bioconda
  channel url: https://mirrors.bfsu.edu.cn/miniconda/cloud/bioconda
  error code: 404

You will need to adjust your conda configuration to proceed.
Use `conda config --show channels` to view your configuration's current state,
and use `conda config --show-sources` to view config file locations
</pre>

Soving his by run:
`conda config --remove-key channels`
