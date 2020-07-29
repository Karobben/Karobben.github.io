---
title: "fastp"
description: "fastp| reads clean"
date: "2020/07/28"
url: "fastp"
---

# Fastp

Location: [Github](https://github.com/OpenGene/fastp)

# Install

```bash
# get source (you can also use browser to download from master or releases)
git clone https://github.com/OpenGene/fastp.git
# build
cd fastp
make
# Install
sudo make install
```

# Usage

```bash
fastp -i in.fq -o out.fq
# for paired end data (gzip compressed)
fastp -i in.R1.fq.gz -I in.R2.fq.gz -o out.R1.fq.gz -O out.R2.fq.gz
```
