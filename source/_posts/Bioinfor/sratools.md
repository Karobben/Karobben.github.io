---
title: "sratools"
description: "sratools"
url: sratools
date: 2020/07/28
toc: true
excerpt: "sratools for manage SRA Files"
tags: [Software, Bioinformatics, MateGenome]
category: [Biology, Bioinformatics, Software, Download]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.pg0lLEEeNeiUp31DPMKtRwHaCY'
priority: 10000
---

## sratools

[GitHub](https://github.com/ncbi/sra-tools)

There are some dependency problems. So, conda would be the easist way to get this tool.

## Install

```bash
conda install -c bioconda sra-tools
```

Or download and configure

```bash
wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/3.0.0/sratoolkit.3.0.0-ubuntu64.tar.gz
tar -xvzf sratoolkit.3.0.0-ubuntu64.tar.gz

# if you are using bash environment rather than zsh, change zshrc tp bashrc
echo PATH=\$PATH:$(pwd)/sratoolkit.3.0.0-ubuntu64/bin >> ~/.zshrc
source ~/.zshrc

#configure sratools
vdb-config --interactive
```

After executing `vdb-config`, you can see an interactive environment board as below. You can input `c` to select `CACHE`. You can also select it by mouse and then input `enter`. Then, you need to give a directory for the category:

```diff
process-local location:
-[choose]
+[choose] /tmp
```

After that, save your change and you can use sratools, now.

|![](https://s1.ax1x.com/2022/09/14/vvC6IO.png)|
|:-:|


## SRA data download
```bash
prefetch  --ascp-path "/usr/bin/ascp|/home/ken/.aspera/connect/etc/asperaweb_id_dsa.putty" ERR02559
```
## For trinity
```bash
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files file.sra

Trinity --seqType fq --max_memory 55G --single Seq.fastq --CPU 8 --full_cleanup
```
