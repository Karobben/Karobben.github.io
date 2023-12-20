---
title: "ggtree | ggplot examples"
description: "ggtree | ggplot 畫進化樹； 擴展包"
url: ggtree2
date: 2020/08/13
toc: true
excerpt: "One of the best resolution to draw trees in R"
tags: [R, Plot, ggplot, Bioinformatics]
category: [R, Plot, GGPLOT]
cover: 'https://tse4-mm.cn.bing.net/th/id/OIP.Jc-GJ5WILwVMAaN1zqS25QHaIl?pid=Api&rs=1'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.Jc-GJ5WILwVMAaN1zqS25QHaIl?pid=Api&rs=1'
priority: 10000
---


author's post:[https://cosx.org/2015/11/to-achieve-the-visualization-and-annotation-of-evolutionary-tree-using-ggtree](https://cosx.org/2015/11/to-achieve-the-visualization-and-annotation-of-evolutionary-tree-using-ggtree)

## Quick Start

```r
library("ggtree")
tree <- read.tree("file")
ggplot(tree, aes(x, y)) + geom_tree() + theme_tree() + geom_tiplab(size=5, color="purple") +xlim(NA, 0.04)
```


## Installation

```r
source("https://bioconductor.org/biocLite.R")
## biocLite("BiocUpgrade") # you may need this
BiocManager::install('ggree')
```


