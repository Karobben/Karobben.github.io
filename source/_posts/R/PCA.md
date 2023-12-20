---
title: "PCA and PCoA"
description: "PCA and PCoA in R"
url: pca2
date: 2020/06/23
toc: true
excerpt: "A few different ways to calculating PCA and draw plots!!"
tags: [R, Plot, PCA]
category: [R, Plot, VisuaProtocol]
cover: 'https://s1.ax1x.com/2020/06/23/NtRu8S.png'
thumbnail: 'https://s1.ax1x.com/2020/06/23/NtRu8S.png'
priority: 10000
---

## PCA


## PCA
![NtRu8S.png](https://s1.ax1x.com/2020/06/23/NtRu8S.png)

<a name="x3hBT"></a>
### 1 prcomp

```r
## install ggbioplot
## remotes::install_github("vqv/ggbiplot")
## install.packages('plyr')

library(plyr)
library(ggbiplot)

data(wine)
wine.pca <- prcomp(wine, scale. = TRUE)
## bioplot
ggbiplot(wine.pca, obs.scale = 1, var.scale = 1,
         groups = wine.class, ellipse = TRUE, circle = TRUE) +
  scale_color_discrete(name = '') +
  theme_light()+ theme(axis.title = element_text(size=10))


# var.axis = F to remove the varible axis on the center.
```

![NlbAKJ.png](https://s1.ax1x.com/2020/06/20/NlbAKJ.png)

<a name="duhUV"></a>
#### 1.1 Arguments

```r
ggbiplot(pcobj, choices = 1:2, scale = 1, pc.biplot =
TRUE, obs.scale = 1 - scale, var.scale = scale, groups =
NULL, ellipse = FALSE, ellipse.prob = 0.68, labels =
NULL, labels.size = 3, alpha = 1, var.axes = TRUE, circle
= FALSE, circle.prob = 0.69, varname.size = 3,
varname.adjust = 1.5, varname.abbrev = FALSE, ...)
pcobj # prcomp()或princomp()返回结果
choices # 选择轴，默认1：2
scale # covariance biplot (scale = 1), form biplot (scale = 0). When scale = 1, the inner product between the variables approximates the covariance and the distance between the points approximates the Mahalanobis distance.
obs.scale # 标准化观测值
var.scale # 标准化变异
pc.biplot # 兼容 biplot.princomp()
groups # 组信息，并按组上色
ellipse # 添加组椭圆
ellipse.prob # 置信区间
labels #向量名称
labels.size #名称大小
alpha  #点透明度 (0 = TRUEransparent, 1 = opaque)
circle #绘制相关环(only applies when prcomp was called with scale = TRUE and when var.scale = 1)
var.axes  #绘制变量线-菌相关
varname.size  #变量名大小
varname.adjust #标签与箭头距离 >= 1 means farther from the arrow
varname.abbrev # 标签是否缩写
```


<a name="j8UB2"></a>
### 2 Psych

```r
library(psych)
library(ggplot2)

# calculate PCA
PC <- principal(wine, nfactors=2, rotate ="none")
pc <- data.frame(PC$scores)

# calculate the location of labels
Label_pos <- aggregate(cbind(PC1, PC2) ~ wine.class, data=pc, FUN=median)

# Plot the PCA scatter graph
ggplot(pc, aes(x=PC1, y=PC2,color=wine.class )) + 
    geom_point(size=4,alpha=0.5)+ theme_light() +  
    geom_label(data = Label_pos, aes(label = wine.class), alpha = .3)+ 
    stat_ellipse(lwd=1,level = 0.95, alpha= .8, linetype = 4)
```


|![PCA plot](https://z1.ax1x.com/2023/10/05/pPOv6mR.png)|
|:-:|

<a name="wsYAL"></a>
### 3 qplot

```r
library(ggplot2)
qplot(x=PC1,y=PC2, data=pc,colour=factor(wine.class))+theme(legend.position="none")+stat_ellipse(lwd=1,level = 0.8)
```

![Nlbp5V.png](https://s1.ax1x.com/2020/06/20/Nlbp5V.png)


## More

```r
library(ggbiplot)
library(ggthemes)
library(patchwork)

data(wine)
wine.pca <- prcomp(wine, scale. = TRUE)
## bioplot
TB= data.frame(wine.pca$x)
TB$class = wine.class

p0 <- ggbiplot(wine.pca, obs.scale = 1, var.scale = 1,
        groups = wine.class, ellipse = TRUE, circle = TRUE) +
        scale_color_discrete(name = '') +
        theme_light()+theme(legend.position = 'none',
        axis.title=element_blank())

p1 <- ggplot() +
        geom_density(data=TB, aes(x=PC1,fill=class),alpha=0.5) +
        theme_map() +
        theme(legend.position = 'none')

p2 <- ggplot() +
        geom_density(data=TB, aes(x=PC2,fill=class),alpha=0.5)  +
        theme_map() +theme(legend.position = 'none') +
        coord_flip()  +  scale_y_reverse()

p3 <- ggplot(TB, aes(x=class,y=PC1)) +
        geom_tufteboxplot(aes(color=class),median.type = "line",
          hoffset = 0, width = 3) +
        coord_flip()+ theme_map()+
        theme(legend.position = 'none')

p4 <- ggplot(TB, aes(x=class,y=PC2)) +
        geom_tufteboxplot(aes(color=class),median.type = "line",
          hoffset = 0, width = 3) +
        theme_map()+
        theme(legend.position = 'none')


TB= data.frame(wine.pca$x)
TB$class = wine.class

GGlay <-
"#BBBBBB#
CAAAAAAE
CAAAAAAE
CAAAAAAE
CAAAAAAE
CAAAAAAE
CAAAAAAE
##DDDDDD#"
p0+p1+p2+p3+p4  +plot_layout(design = GGlay)
```
![NtRu8S.png](https://s1.ax1x.com/2020/06/23/NtRu8S.png)




## PCoA

!!! question What's different between PCA and PCoA?
        Principal Component Analysis (PCA) and Principal Coordinates Analysis (PCoA, also known as Multidimensional Scaling, MDS) are both techniques used for dimensionality reduction, which is the process of reducing the number of random variables under consideration by obtaining a set of principal variables. However, they are used in different contexts and have different underlying methodologies.

        PCA is a technique that is used when you have a multivariate data set and you want to identify new variables that will represent the variability of your entire data set as much as possible. The new variables, or principal components, are linear combinations of the original variables. PCA operates on a covariance (or correlation) matrix, which implies that it is a parametric method.

        On the other hand, PCoA is a method used in ecology and biology to transform a matrix of distances (or dissimilarities) between samples into a new set of orthogonal axes, the most important of which can be plotted against each other. PCoA can be applied to any symmetric distance or dissimilarity matrix. Unlike PCA, PCoA is non-parametric and makes no assumptions about the distribution of the original variables.

        So, the main difference lies in the type of data they work with: PCA works with the actual data matrix and is used when you have a set of observations and measurements, while PCoA works with a matrix of pairwise distances and is used when you have a set of pairwise dissimilarities (like geographical distances between cities or genetic distances between individuals or species).
        
        © ChatGPT4


Interesting