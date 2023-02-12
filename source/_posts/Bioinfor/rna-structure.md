---
toc: true
url: rna_structure
covercopy: © Karobben
priority: 10000
date: 2022-11-15 10:16:46
title: "RNA-structure and Prediction"
ytitle: "RNA-structure and Prediction"
description: "RNA-structure and Prediction"
excerpt: "RNA structure research is important for understanding RNA function and regulation, as the structure of RNA molecules can impact their interactions with other molecules, such as proteins and small molecules, and influence gene expression and protein synthesis. <a title='ChatGPT'>Who sad this?</a>"
tags: [Software, miRNA-Seq, Protocol]
category: [Biology, Bioinformatics, Protocol, miRNA]
cover: "https://s1.ax1x.com/2022/11/16/zVg3Sf.png"
thumbnail: "https://s1.ax1x.com/2022/11/16/zVg3Sf.png"
---


## RNA Structure and Prediction

|      |      |
| :------------- | :--: |
| Like protein, RNA also has secondary structure, tertiary structure, and quaternary stricture, too.    | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/DNA_RNA_structure_%28full%29.png/540px-DNA_RNA_structure_%28full%29.png)<br>[© wiki](https://en.wikipedia.org/wiki/Nucleic_acid_sequence)]       |


In Secondary Structure, it could form:
- Double helix
- Stem-loop structure
- Pseudoknots

[wikipedia](https://en.wikipedia.org/wiki/List_of_RNA_structure_prediction_software) listed a bunch of tools for RNA secondary structure prediction.


Online structure prediction servers:

- [Mathews Lab](https://rna.urmc.rochester.edu/RNAstructureWeb/Servers/Predict1/ResultsPages/20221115.114114-7c052f9f/Results.html)
- [RNAfold](http://rna.tbi.univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi)


## RAN Secondary Structure Format.

- DB format (Dot bracket)
    - Unpaired nucleotides are indicated with the . or : characters.
    - Matching pairs of parentheses indicate base pairs.
    - To indicate non-nested base pairs (pseudoknots), additional brackets may be used: [], {}, or <>.
Example:

<pre>
GGUGCAUGCCGAGGGGCGGUUGGCCUCGUAAAAAGCCGCAAAAAAUAGCAUGUAGUACC
((((((((((((((.[[[[[[..))))).....]]]]]]........)))))...))))
</pre>


## Secondary Structure Predict


Seq:
```
UGAGUGGUGUUGUUGGCUGCAUUAUGAUGUUGGUUAUAUUCUGGUUUUCUUCCACUCAACAACAACAACAACACGCAGUAGUAGAAGCAACAACAAGCAUAUAACCAACAUCAUAAUGCAGCCAACAACACCACUCA
```

Website: [RANfold](http://rna.tbi.univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi)
Result:
![](https://s1.ax1x.com/2022/11/16/zVgb0H.png)

## RNA Secondary Structure Plot

### RNAplot from ViennaRNA

```bash
RNAplot tmp.db # RNAfold results
```
![](https://s1.ax1x.com/2022/11/16/zV2KuF.png)


### RRNA in R


```r
install.package("RRNA")
library(RRNA)
coord=ct2coord(ct)
ct=makeCt( "(((((((((((((((((((((((((((((((((((((((.((.(((((((((.(((..((.................))))).)))).)).))).)).)))))))))))))))))))))))))))))))))))))))", "UGAGUGGUGUUGUUGGCUGCAUUAUGAUGUUGGUUAUAUUCUGGUUUUCUUCCACUCAACAACAACAACAACACGCAGUAGUAGAAGCAACAACAAGCAUAUAACCAACAUCAUAAUGCAGCCAACAACACCACUCA")
RNAPlot(coord,hl=c("GGGUUU","AAAUUU"),seqcols=c(2,4),labTF=F)
```
![](https://s1.ax1x.com/2022/11/16/zVg3Sf.png)




## Python

```bash
pip install RNA forgi
```
















<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
