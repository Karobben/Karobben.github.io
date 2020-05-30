---
url: ggtree2
---
# ggtree

author's post:[https://cosx.org/2015/11/to-achieve-the-visualization-and-annotation-of-evolutionary-tree-using-ggtree](https://cosx.org/2015/11/to-achieve-the-visualization-and-annotation-of-evolutionary-tree-using-ggtree)

<a name="byfQw"></a>
# Quick Start

```r
library("ggtree")
tree <- read.tree("file")
ggplot(tree, aes(x, y)) + geom_tree() + theme_tree() + geom_tiplab(size=5, color="purple") +xlim(NA, 0.04)
```

<a name="PuN8f"></a>
# Installation

```r
source("https://bioconductor.org/biocLite.R")
# biocLite("BiocUpgrade") # you may need this
BiocManager::install('ggree')
```

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)






---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
