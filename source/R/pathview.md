---
title: "Pathview"
description: "Pathview"
url: pathview
---

# Pathview
An R package for mapping your genes and compounds to the KEGG pathways.

[Documentation](http://bioconductor.org/packages/release/bioc/vignettes/pathview/inst/doc/pathview.pdf)

# Install & Quick start
```R
#切换至国内镜像
options(BioC_mirror="https://mirrors.tuna.tsinghua.edu.cn/bioconductor")
BiocManager::install('pathview')
```

```R
library(pathview)
# Gene map
data(gse16873.d)
pv.out <- pathview(gene.data = gse16873.d[, 1], pathway.id = "04110",
	species = "hsa", out.suffix = "gse16873")

pv.out <- pathview(gene.data = gse16873.d[, 1], pathway.id = demo.paths$sel.paths[i],
	species = "hsa", out.suffix = "gse16873.2layer", kegg.native = T,
	same.layer = F)

# compound map
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
|[![tiZzjS.md.png](https://s1.ax1x.com/2020/05/26/tiZzjS.md.png)](https://imgchr.com/i/tiZzjS)|[![tieZcT.md.png](https://s1.ax1x.com/2020/05/26/tieZcT.md.png)](https://imgchr.com/i/tieZcT)|
## Multi group Date
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
[![tiZBlT.md.png](https://s1.ax1x.com/2020/05/26/tiZBlT.md.png)](https://imgchr.com/i/tiZBlT)

# Start with your data

## Genelist
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
[![tP9h8J.md.png](https://s1.ax1x.com/2020/05/26/tP9h8J.md.png)](https://imgchr.com/i/tP9h8J)


```R
```
## Genes & Compound

---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
