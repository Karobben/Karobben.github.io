---
title: "Pathview"
description: "Pathview"
url: pathview
date: 2020/05/26
toc: true
excerpt: "The best way to draw kegg pathways in all platform!!! It is very friendly and powerful!!"
tags: [R, Plot, KEGG, KEGG pathway]
category: [R, Plot, VisuaProtocol]
cover: 'https://s1.ax1x.com/2020/05/26/tiZzjS.md.png'
thumbnail: 'https://s1.ax1x.com/2020/05/26/tiZzjS.md.png'
priority: 10000
---

## Pathview
An R package for mapping your genes and compounds to the KEGG pathways.

Documentation:
- [Bioconductor](http://bioconductor.org/packages/release/bioc/vignettes/pathview/inst/doc/pathview.pdf)
- [R Project](http://pathview.r-forge.r-project.org/pathview.pdf)
## Install & Quick start
```R
##切换至国内镜像
options(BioC_mirror="https://mirrors.tuna.tsinghua.edu.cn/bioconductor")
BiocManager::install('pathview')
```

```R
library(pathview)
## Gene map
data(gse16873.d)
pv.out <- pathview(gene.data = gse16873.d[, 1], pathway.id = "04110",
  species = "hsa", out.suffix = "gse16873")

pv.out <- pathview(gene.data = gse16873.d[, 1], pathway.id = demo.paths$sel.paths[i],
  species = "hsa", out.suffix = "gse16873.2layer", kegg.native = T,
  same.layer = F)

## compound map
data(demo.paths)
data(cpd.simtypes)
sim.cpd.data=sim.mol.data(mol.type="cpd", nmol=3000)
i <- 3
pv.out <- pathview(gene.data = gse16873.d[, 1], cpd.data = sim.cpd.data,
  pathway.id = demo.paths$sel.paths[i], species = "hsa", out.suffix = "gse16873.cpd",
  keys.align = "y", kegg.native = T, key.pos = demo.paths$kpos1[i])
```
|Gene map| Compound map|
|----|----|
|![tiZzjS.md.png](https://s1.ax1x.com/2020/05/26/tiZzjS.md.png)|![tieZcT.md.png](https://s1.ax1x.com/2020/05/26/tieZcT.md.png)|
### Multi group Date
```R
require(org.Hs.eg.db)
library(pathview)

data(gse16873.d)
data(demo.paths)
sim.cpd.data=sim.mol.data(mol.type="cpd", nmol=3000)

gse16873.t <- apply(gse16873.d, 1, function(x) t.test(x,
  alternative = "two.sided")$p.value)

i <- 3
sim.cpd.data2 = matrix(sample(sim.cpd.data, 18000, replace = T), ncol = 6)
rownames(sim.cpd.data2) = names(sim.cpd.data)
colnames(sim.cpd.data2) = paste("exp", 1:6, sep = "")

pv.out <- pathview(gene.data = gse16873.d[, 1:3],
  cpd.data = sim.cpd.data2[, 1:2], pathway.id = demo.paths$sel.paths[i],
  species = "hsa", out.suffix = "gse16873.cpd.3-2s.2layer",
  keys.align = "y", kegg.native = T, match.data = F, multi.state = T,
  same.layer = F)
```
![tiZBlT.md.png](https://s1.ax1x.com/2020/05/26/tiZBlT.md.png)

## Start with your data

### Genelist

!!! note Examples of acquire ko id through KGG API:

```bash
curl https://rest.kegg.jp/link/ko/dme:Dmel_CG7138+dme:Dmel_CG3936| sed 's/:/\t/g'| awk '{print $2,$4}'
```

```r
Anno_TB = data.frame()
for(i in c(1:(round(length(A)/200)+1)))
{
    AA <- paste("dme:Dmel_",A[c(((i-1)*200):(i*200))], sep = "", collapse = "+")
    Anno <- read.table( paste("https://rest.kegg.jp/link/ko/", AA, sep = ""))
    Anno_TB <- rbind(Anno_TB, Anno)
}

Anno_TB[[1]] <- as.data.frame(str_split_fixed(Anno_TB[[1]], "_", 2))[[2]]
Anno_TB[[2]] <- as.data.frame(str_split_fixed(Anno_TB[[2]], ":", 2))[[2]]
```


1. Make your gene list
```bash
echo "ID F
K18606 2
K00457 -1
K00815 -2"> gene.list
```


2. run in R
```R
library(pathview)
gene <- read.table('gene.list',header=T)
TB = matrix(gene[,2])
rownames(TB)= gene[,1]
pathview(gene.data = TB[, 1], pathway.id = "00130",
  species = "ko", out.suffix = "test")
```
![tP9h8J.md.png](https://s1.ax1x.com/2020/05/26/tP9h8J.md.png)


```R
```
### Genes & Compound
