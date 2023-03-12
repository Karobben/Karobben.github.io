---
title: "Trinity"
description: "Trinity"
url: trinity
date: 2020/07/28
covercopy:
toc: true
 trinityrnaseq
excerpt: "Trinity RNA-seq is a de novo transcriptome assembly software that uses RNA-seq data to reconstruct transcript sequences and estimate expression levels. It allows for comprehensive analysis of gene expression and isoform diversity in non-model organisms without a reference genome. <a title='ChatGPT'>Who said this?</a>"
tags: [Software, Bioinformatics, NGS]
category: [Biology, Bioinformatics, Software, De nove]
cover: 'https://raw.githubusercontent.com/wiki/trinityrnaseq/trinityrnaseq/images/TrinityCompositeLogo.png'
thumbnail: 'https://raw.githubusercontent.com/wiki/trinityrnaseq/trinityrnaseq/images/TrinityCompositeLogo.png'
priority: 10000
---

## Trinity

## Install

!!! info Prerequisite
    ```bash
    sudo apt install cmake
    sudo apt-get install autoconf
    ```

- [Rlease page](https://github.com/trinityrnaseq/trinityrnaseq/releases)

If you come with the error below as making, try the [full package](https://github.com/trinityrnaseq/trinityrnaseq/releases/download/v2.11.0/trinityrnaseq-v2.11.0.FULL.tar.gz). (See resolution at [GitHub issue](https://github.com/trinityrnaseq/trinityrnaseq/issues/870))
<pre>
Using gnu compiler for Inchworm and Chrysalis
cd Inchworm && make
make[1]: Entering directory '/home/ken/Bio/trinityrnaseq/Inchworm'
make[1]: *** No targets specified and no makefile found.  Stop.
make[1]: Leaving directory '/home/ken/Bio/trinityrnaseq/Inchworm'
make: *** [Makefile:32: inchworm_target] Error 2
</pre>

```bash
cd trinityrnaseq*
make
make test_all
```

### conda install
```bash
conda install trinity
conda install samtools bowtie bowtie2 bowtie rsem

```
## Troubleshoot
### jellyfish
<pre>
Error, cannot find jellyfish installed on this system. Be sure to install it. You can get it here: http://www.genome.umd.edu/jellyfish.html at /home/ken/Bio/trinityrnaseq-v2.11.0/Trinity line 3935.
</pre>


```bash
sudo apt install jellyfish
```

### Salmon
<pre>
Trinity Trinity-v2.11.0 requires salmon to be installed.  Get it here: https://combine-lab.github.io/salmon/  at /home/ken/Bio/trinityrnaseq-v2.11.0/Trinity line 3973.
</pre>

```bash
sudo apt install salmon
```

## Quick start
```bash
~/Biosoft/trinityrnaseq-Trinity-v2.5.1/Trinity --seqType fq  --max_memory 50G  --single(--samples_file)  --CPU 8  --full_cleanup
~/Biosoft/trinityrnaseq-Trinity-v2.5.1/Analysis/DifferentialExpression/run_DE_analysis.pl --matrix MA-all-t0.01.matrix --method edgeR --samples sample
```

## Downstream Analysis

### Prerequisites
```R
BiocManager::install('edgeR')
BiocManager::install('limma')
BiocManager::install("qvalue")
BiocManager::install('DESeq2')
BiocManager::install('ctc')
BiocManager::install("Biobase")
install.packages('gplots')
install.packages('ape')
install.packages("fastcluster")
```

## Non-repeats Experiment (edgeR)
```bash
~/Biosoft/trinityrnaseq-Trinity-v2.8.4/Analysis/DifferentialExpression/run_DE_analysis.pl  --matrix Intest.table  --method edgeR  --dispersion 0.1
```

Beware that It can recognize ***tab-separated*** matrix only. if your count or expression matrix was coma-separated, your can run `sed -i s/,/\t/g ${your matrix file}` to change the separates.

After waiting, you are supposed have an `edger{*}.dir` directory and all DEGs among each groups are stored in it.

## Volcano Plot and Heatmap
After you finished with `run_DE_analysis.pl` process, `cd edger{*}.dir` and run codes below with your own args.
```bash
~/Biosoft/trinityrnaseq-Trinity-v2.8.4/Analysis/DifferentialExpression/analyze_diff_expr.pl --matrix ../Trinity_trans.TMM.EXPR.matrix -P 1e-3 -C 2
```

## Sample file

<pre>
##      --samples_file <string>         tab-delimited text file indicating biological replicate relationships.
##                                   ex.
##                                        cond_A    cond_A_rep1    A_rep1_left.fq    A_rep1_right.fq
##                                        cond_A    cond_A_rep2    A_rep2_left.fq    A_rep2_right.fq
##                                        cond_B    cond_B_rep1    B_rep1_left.fq    B_rep1_right.fq
##                                        cond_B    cond_B_rep2    B_rep2_left.fq    B_rep2_right.fq
</pre>

## Group file

If you have the sample file, you can use the sample file as the group file since the first two columns are the same
<pre>
#  --samples <string>      tab-delimited text file indicating biological replicate relationships.
#                                   ex.
#                                        cond_A    cond_A_rep1
#                                        cond_A    cond_A_rep2
#                                        cond_B    cond_B_rep1
#                                        cond_B    cond_B_rep2
</pre>
## Tricks
If you don't like the color of heatmap, you can can change the below lines in file:
`$TrinityFile/Analysis/DifferentialExpression/R/heatmap.3.R`


## Errors

My environment:
<pre>
██████████████████  ████████     ken@manjaro
██████████████████  ████████     OS: Manjaro 21.0.7 Ornara
██████████████████  ████████     Kernel: x86_64 Linux 5.4.124-1-MANJARO
██████████████████  ████████     Uptime: 5m
████████            ████████     Packages: 1678
████████  ████████  ████████     Shell: zsh 5.8
████████  ████████  ████████     Resolution: 1920x1080
████████  ████████  ████████     DE: GNOME 3.38.5
████████  ████████  ████████     WM: Mutter
████████  ████████  ████████     WM Theme: Matcha-dark-sea
████████  ████████  ████████     GTK Theme: Matcha-sea [GTK2/3]
████████  ████████  ████████     Icon Theme: Papirus-Dark-Maia
████████  ████████  ████████     Font: Noto Sans 11
████████  ████████  ████████     Disk: 769G / 1.5T (54%)
                                 CPU: Intel Xeon E3-1535M v6 @ 8x 4.2GHz [51.0°C]
                                 GPU: NVIDIA Quadro M2200
                                 RAM: 3208MiB / 64042MiB
</pre>

Trinity version: `trinityrnaseq-v2.12.0`

Error code:
1. htslib
```
configure: error: cannot find required auxiliary files: config.guess config.sub
make[2]: *** [Makefile:10: htslib/version.h] Error 1
make[2]: Leaving directory '/home/ken/Bio/trinityrnaseq-v2.12.0/trinity-plugins/bamsifter'
make[1]: *** [Makefile:32: bamsifter_target] Error 2
make[1]: Leaving directory '/home/ken/Bio/trinityrnaseq-v2.12.0/trinity-plugins'
make: *** [Makefile:39: trinity_essentials] Error 2
```

`configure: error: cannot find required auxiliary files: config.guess config.sub`
This problem comes the version of `autoconf` (see [GitHub Issue](https://github.com/kerl/kerl/issues/359#issuecomment-799605467))
We can solve this by downgrade the version of `autoconf`. `2.69` works to me.

Install the autoconf: [andyguan01_2 2019](https://blog.csdn.net/andyguan01_2/article/details/89385120)
```bash
sudo pacman -R autoconf

wget ftp://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz
tar zxvf autoconf-2.69.tar.gz
cd autoconf-2.69
./configure --prefix=/usr/
make && make install
```
