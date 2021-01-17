---
title: "Trinity"
description: "Trinity"
url: trinity
---

# Trinity

# Install

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

# Troubleshoot
## jellyfish
<pre>
Error, cannot find jellyfish installed on this system. Be sure to install it. You can get it here: http://www.genome.umd.edu/jellyfish.html at /home/ken/Bio/trinityrnaseq-v2.11.0/Trinity line 3935.
</pre>


```bash
sudo apt install jellyfish
```

## Salmon
<pre>
Trinity Trinity-v2.11.0 requires salmon to be installed.  Get it here: https://combine-lab.github.io/salmon/  at /home/ken/Bio/trinityrnaseq-v2.11.0/Trinity line 3973.
</pre>

```bash
sudo apt install salmon
```

# Quick start
```bash
~/Biosoft/trinityrnaseq-Trinity-v2.5.1/Trinity --seqType fq  --max_memory 50G  --single(--samples_file)  --CPU 8  --full_cleanup
~/Biosoft/trinityrnaseq-Trinity-v2.5.1/Analysis/DifferentialExpression/run_DE_analysis.pl --matrix MA-all-t0.01.matrix --method edgeR --samples sample
```

# Downstream Analysis

## Prerequisites
```R
BiocManager::install('edgeR')
BiocManager::install('limma')
BiocManager::install("qvalue")
BiocManager::install('DESeq2')
BiocManager::install('ctc')
BiocManager::install("Biobase")
install.packages('gplots')
install.packages('ape')
```

# Non-repeats Experiment (edgeR)
```bash
~/Biosoft/trinityrnaseq-Trinity-v2.8.4/Analysis/DifferentialExpression/run_DE_analysis.pl  --matrix Intest.table  --method edgeR  --dispersion 0.1
```

Beware that It can recognize ***tab-separated*** matrix only. if your count or expression matrix was coma-separated, your can run `sed -i s/,/\t/g ${your matrix file}` to change the separates.

After waiting, you are supposed have an `edger{*}.dir` directory and all DEGs among each groups are stored in it.

# Volcano Plot and Heatmap
After you finished with `run_DE_analysis.pl` process, `cd edger{*}.dir` and run codes below with your own args.
```bash
~/Biosoft/trinityrnaseq-Trinity-v2.8.4/Analysis/DifferentialExpression/analyze_diff_expr.pl --matrix ../Trinity_trans.TMM.EXPR.matrix -P 1e-3 -C 2
```

# Sample file
```bash
#      --samples_file <string>         tab-delimited text file indicating biological replicate relationships.
#                                   ex.
#                                        cond_A    cond_A_rep1    A_rep1_left.fq    A_rep1_right.fq
#                                        cond_A    cond_A_rep2    A_rep2_left.fq    A_rep2_right.fq
#                                        cond_B    cond_B_rep1    B_rep1_left.fq    B_rep1_right.fq
#                                        cond_B    cond_B_rep2    B_rep2_left.fq    B_rep2_right.fq
```

# Tricks
If you don't like the color of heatmap, you can can change the below lines in file:
`$TrinityFile/Analysis/DifferentialExpression/R/heatmap.3.R`

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
