---
toc: true
url: trinity_false
covercopy: © Trinity
priority: 10000
date: 2022-09-21 13:58:55
title: "False Positives Made by Trinity"
ytitle: "Trinity 的假陽性"
description: "False Positives Made by Trinity"
excerpt: "False Positives Made by Trinity"
tags: [Bioinformatics, Trinity]
category: [Biology, Bioinformatics, others]
cover: "https://opengraph.githubassets.com/a06b3cbd989a43741004aa11ea92c3411bca4242b57f6fbe7fa024af3a8d0427/trinityrnaseq/trinityrnaseq"
thumbnail: "https://opengraph.githubassets.com/a06b3cbd989a43741004aa11ea92c3411bca4242b57f6fbe7fa024af3a8d0427/trinityrnaseq/trinityrnaseq"
---

## Long repeat sequences

<pre>
Query_47  183       CATAAATAAATAAATATACATTTAAATGCAACTTAACGAATCGGCCCTCGACTTATATCC  242
X         13400713  ............................................................  13400654

Query_47  243       TACt<font color="salmon">atattatataatatatatatatatata</font>CACATTCGCACCAAACACCCACAATCACA  302
X         13400653  ...............................T.T...                         13400617
2R        16574732      ........................................................  16574677

Query_47  303       ACCACAAACACATCCTCGTAGATTAAGGCCCAAATGTTTGTTATGCCACTTGTTATCGCG  362
2R        16574676  ............................................................  16574617

Query_47  363       ACGTTTGATTAAAGCTAACAAAACTGAT  390
2R        16574616  ............................  16574589
</pre>













<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
