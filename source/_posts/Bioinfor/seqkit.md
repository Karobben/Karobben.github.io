---
toc: true
url: seqkit
covercopy: © Karobben
priority: 10000
date: 2024-02-05 15:00:06
title: "SeqKit: A Cross-Platform and Ultrafast Toolkit for FASTA/Q File Manipulation"
ytitle: "SeqKit - Your Swiss Army Knife for Sequence Data"
description: "SeqKit provides a comprehensive suite of utilities for the efficient and high-throughput processing of FASTA/Q files. This toolkit allows for format conversion, subsequence extraction, quality control, and much more."
excerpt: "Learn about SeqKit, a powerful command-line toolkit designed for handling high-throughput sequencing data with ease and efficiency."
tags: ["Bioinformatics", "Sequencing", "FASTA/Q", "SeqKit"]
category:
cover:
thumbnail:
---

## Install

GitHub: [shenwei356/seqkit](https://github.com/shenwei356/seqkit)

```bash
wget https://github.com/shenwei356/seqkit/releases/download/v2.7.0/seqkit_linux_amd64.tar.gz
tar -zxvf seqkit_linux_amd64.tar.gz
```

### Convert the Fastq to Fasta

```bash
seqkit fq2fa output_directory/output_prefix.extendedFrags.fastq -o output_directory/output_prefix.merged.fasta
```

### Remove Duplicated Sequence

```bash
```





<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
