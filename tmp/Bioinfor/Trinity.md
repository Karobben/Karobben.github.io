---
title: "Trinity"
description: "Trinity"
url: trinity
---

# Trinity

# Quick start
```bash
~/Biosoft/trinityrnaseq-Trinity-v2.5.1/Trinity --seqType fq  --max_memory 50G  --single(--samples_file)  --CPU 8  --full_cleanup
~/Biosoft/trinityrnaseq-Trinity-v2.5.1/Analysis/DifferentialExpression/run_DE_analysis.pl --matrix MA-all-t0.01.matrix --method edgeR --samples sample
```
# library R
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
~/Biosoft/trinityrnaseq-Trinity-v2.8.4/Analysis/DifferentialExpression/run_DE_analysis.pl  --matrix Intest.table  --method edgeR --min_reps_min_cpm --dispersion 0.1
```

# Volcano Plot and Heatmap
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
