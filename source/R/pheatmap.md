---
title: "Heatmap"
description: "Heatmap"
url: pheatmap2
---
# Heatmap

# pheatmap

[![NlbOJK.png](https://s1.ax1x.com/2020/06/20/NlbOJK.png)](https://imgchr.com/i/NlbOJK)
<a name="KbDPP"></a>
# Quick Start

```r
library(pheatmap )

test = matrix(rnorm(200), 20, 10)
test[1:10, seq(1, 10, 2)] = test[1:10, seq(1, 10, 2)] + 3
test[11:20, seq(2, 10, 2)] = test[11:20, seq(2, 10, 2)] + 2
test[15:20, seq(2, 10, 2)] = test[15:20, seq(2, 10, 2)] + 4
colnames(test) = paste("Test", 1:10, sep = "")
rownames(test) = paste("Gene", 1:20, sep = "")

# Draw heatmaps
pheatmap(t(test))
```
[NlbFv4.png](https://s1.ax1x.com/2020/06/20/NlbFv4.png)

<a name="nU3ns"></a>
# Arguments
```r
pheatmap(data, scale = "row", clustering_distance_row = "correlation", fontsize=9, fontsize_row=6) #改变排序算法

annotation<-data.frame(Var1=factor(patientcolors,labels=c("class1","class2")),Var2=groups)

pheatmap(data, annotation=annotation, fontsize=9, fontsize_row=6)

geom_texttmap(data, cluster_row=FALSE, fontsize=9, fontsize_row=6) #关闭按行排序(aes(label = B, vjust = 1.1, hjust = -0.5, angle = 45), show_guide = FALSE)
```


# Turn to ggplot

```r
install.packages('ggplotify')
library(ggplotify)

d <- matrix(rnorm(100), ncol=10)
library(pheatmap)
p <- pheatmap(d)
g = as.ggplot(p)
```

<a name="FG8Ad"></a>


# Heatmap for DEGs matrix

reference: Trinity
```r
primary_data = read.table("diffExpr.P1e-5_C2.matrix", header=T, com='', row.names=1, check.names=F, sep='\t')

primary_data = as.matrix(primary_data)

#transformations
data = log2(primary_data+1)
data = as.matrix(data) # convert to matrix
# Centering rows
data = data.frame(t(scale(t(data), scale=F)))
```








# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
