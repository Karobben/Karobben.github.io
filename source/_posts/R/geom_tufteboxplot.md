---
title: "geom_tufteboxplot | ggplot examples | Another boxplot "
ytitle: "geom_tufteboxplot | ggplot 另一種個箱線圖"
description: "geom_tufteboxplot | ggplot 另一種個箱線圖"
url: geom_tufteboxplot2
date: 2020/08/13
toc: true
excerpt: "R: ggplot, ggplot, tufteboxplot, stylized boxplot"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://s1.ax1x.com/2020/08/13/dSWoX4.png'
thumbnail: 'https://s1.ax1x.com/2020/08/13/dSWoX4.png'
priority: 10000
---


## Quick Start
```r
library(ggplot2)
library(patchwork)
p <- ggplot(mtcars, aes(factor(cyl), mpg))
### with a point for the median and lines for whiskers
P1 <- p + geom_tufteboxplot() + theme_light()+ ggtitle('P1')+
  theme(plot.title = element_text(hjust = 0.5))
### with a line for the interquartile range and points for whiskers
P2 <- p + geom_tufteboxplot(median.type = "line", whisker.type = "point", hoffset = 0)+
  theme_light()+ ggtitle('P2')+theme(plot.title = element_text(hjust = 0.5))
### with a wide line for the interquartile range and lines for whiskers
P3 <- p + geom_tufteboxplot(median.type = "line", hoffset = 0, width = 3) +
  theme_light()+ ggtitle('P3')+theme(plot.title = element_text(hjust = 0.5))
### with an offset line for the interquartile range and lines for whiskers
P4 <- p + geom_tufteboxplot(median.type = "line") + theme_light()+ ggtitle('P4')+
  theme(plot.title = element_text(hjust = 0.5))
P5 <- p + geom_point() + theme_light() + ggtitle('Scatter')+
  theme(plot.title = element_text(hjust = 0.5))
P6 <- p + geom_boxplot()+ theme_light()+ ggtitle('Boxplot')+
  theme(plot.title = element_text(hjust = 0.5))

(P1|P2|P3)/(P5|P4|P6)
```


![geom_tufteboxplot](https://s1.ax1x.com/2020/08/13/dSWoX4.png)
