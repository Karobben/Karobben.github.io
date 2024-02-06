---
toc: true
url: flash2
covercopy: © Karobben
priority: 10000
date: 2024-02-05 14:30:11
title: "FLASH2 (Fast Length Adjustment of SHort reads)"
ytitle: "FLASH2 (Fast Length Adjustment of SHort reads)"
description: "FLASH2 (Fast Length Adjustment of SHort reads), mearge paired-end reads"
excerpt: `FLASH2` (Fast Length Adjustment of SHort reads) is an improved version of the original `FLASH` tool. It is designed to merge pairs of reads from next-generation sequencing experiments when the original DNA fragments are shorter than twice the length of reads.
tags: [Bioinformatic, Software, fastq]
category: []
cover: ""
thumbnail: ""
---

## Install

GitHub: [dstreett/FLASH2](https://github.com/dstreett/FLASH2)

```bash
wget https://github.com/dstreett/FLASH2/archive/refs/tags/2.2.00.tar.gz
tar xzf FLASH-1.2.11.tar.gz
cd FLASH-1.2.11
make
```

The basic command structure to merge reads using `FLASH2` is as follows:

```bash
flash2 -d [output_directory] -o [output_prefix] [forward_reads.fastq] [reverse_reads.fastq]
```

Here's what the options mean:

- `-d` specifies the output directory for all the output files.
- `-o` specifies the prefix that will be prepended to all output files.
- The last two arguments are the paths to the FASTQ files containing the forward and reverse reads.

`FLASH2` outputs several files, including a file of merged reads (`[output_prefix].extendedFrags.fastq`), files for unmerged forward and reverse reads, and a histogram of read overlap sizes.

To run `FLASH2` and output the result as FASTA, you would first run the merging step as described, and then you can use `SeqKit` or any other FASTQ-to-FASTA converter to change the format. `FLASH2` itself does not directly output FASTA files.

Here's how you might run `FLASH2` followed by `SeqKit` to convert the merged FASTQ to FASTA:

```bash
# Merge reads with FLASH2
flash2 -d output_directory -o output_prefix forward_reads.fastq reverse_reads.fastq

# Convert merged reads to FASTA format with SeqKit
seqkit fq2fa output_directory/output_prefix.extendedFrags.fastq -o output_directory/output_prefix.merged.fasta
```

In this sequence of commands:

- First, `FLASH2` is used to merge the paired-end reads. Adjust `output_directory`, `output_prefix`, `forward_reads.fastq`, and `reverse_reads.fastq` according to your actual file names and desired output locations.
- Then, `SeqKit` is used to convert the resulting `output_prefix.extendedFrags.fastq` file to a FASTA format file named `output_prefix.merged.fasta`.

Make sure to replace `output_directory`, `output_prefix`, `forward_reads.fastq`, and `reverse_reads.fastq` with your actual directory, desired prefix, and file names.

Before running these commands, ensure that both `FLASH2` and `SeqKit` are installed in your environment. If you're using Conda, you can install both tools from the Bioconda channel.
<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
