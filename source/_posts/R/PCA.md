---
title: "PCA"
description: "PCA"
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
##install_github("vqv/ggbiplot")
##install.packages('plyr')
data(wine)
wine.pca <- prcomp(wine, scale. = TRUE)
## bioplot
ggbiplot(wine.pca, obs.scale = 1, var.scale = 1,
         groups = wine.class, ellipse = TRUE, circle = TRUE) +
  scale_color_discrete(name = '') +
  theme_light()
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
PC <- principal(wine, nfactors=2, rotate ="none")
pc <- data.frame(PC$scores)
p  <- ggplot(pc, aes(x=PC1, y=PC2,color=wine.class )) +
  geom_point(size=4,alpha=0.5)+
  theme(axis.text= element_text(size=20))+
  theme(panel.grid.major =element_blank(),
        panel.grid.minor = element_line(color="steelblue"),
        panel.background = element_blank(),
        axis.line = element_line(colour = "black"))+
  stat_ellipse(lwd=1,level = 0.8)
```


![Nlb7ZR.png](https://s1.ax1x.com/2020/06/20/Nlb7ZR.png)

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
