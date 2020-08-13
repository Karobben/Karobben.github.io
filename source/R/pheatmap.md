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
![NlbFv4.png](https://s1.ax1x.com/2020/06/20/NlbFv4.png)

<a name="nU3ns"></a>
# Arguments

Quick View:
```r
pheatmap(mat, color = colorRampPalette(rev(brewer.pal(n = 7, name =
       "RdYlBu")))(100), kmeans_k = NA, breaks = NA, border_color = "grey60",
       cellwidth = NA, cellheight = NA, scale = "none", cluster_rows = TRUE,
       cluster_cols = TRUE, clustering_distance_rows = "euclidean",
       clustering_distance_cols = "euclidean", clustering_method = "complete",
       clustering_callback = identity2, cutree_rows = NA, cutree_cols = NA,
       treeheight_row = ifelse((class(cluster_rows) == "hclust") || cluster_rows,
       50, 0), treeheight_col = ifelse((class(cluster_cols) == "hclust") ||
       cluster_cols, 50, 0), legend = TRUE, legend_breaks = NA,
       legend_labels = NA, annotation_row = NA, annotation_col = NA,
       annotation = NA, annotation_colors = NA, annotation_legend = TRUE,
       annotation_names_row = TRUE, annotation_names_col = TRUE,
       drop_levels = TRUE, show_rownames = T, show_colnames = T, main = NA,
       fontsize = 10, fontsize_row = fontsize, fontsize_col = fontsize,
       angle_col = c("270", "0", "45", "90", "315"), display_numbers = F,
       number_format = "%.2f", number_color = "grey30", fontsize_number = 0.8
       * fontsize, gaps_row = NULL, gaps_col = NULL, labels_row = NULL,
       labels_col = NULL, filename = NA, width = NA, height = NA,
       silent = FALSE, na_col = "#DDDDDD", ...)
```

## Dendrogram

```r
cluster_rows = TRUE,
cluster_cols = TRUE,
clustering_distance_rows = "euclidean",
clustering_distance_cols = "euclidean",
clustering_method = "complete",
clustering_callback = identity2,
cutree_rows = NA,
cutree_cols = NA,
treeheight_row = ifelse((class(cluster_rows) == "hclust") || cluster_rows,50, 0),
treeheight_col = ifelse((class(cluster_cols) == "hclust") || cluster_cols, 50, 0),
```

### Disable dendrogram
```r
pheatmap(test, cluster_rows = F, cluster_cols = F)
```
![No Dendrogram](https://s1.ax1x.com/2020/08/13/dp4GrD.png)



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
