---
title: "geom_boxplot | ggplot examples"
ytitle: "geom_boxplot | ggplot 箱型圖代碼實例"
description: "ggplot boxplot; 箱型图"
url: geom_boxplot
date: 2020/06/28
toc: true
excerpt: "R: ggplot, ggplot, boxplot"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://s1.ax1x.com/2020/06/28/NgVfWn.md.png'
thumbnail: 'https://s1.ax1x.com/2020/06/28/NgVfWn.md.png'
priority: 10000
---


## Quick Start
```r
library(ggplot2)
library(patchwork)

p1<- ggplot(ChickWeight,aes(x=Time,y=weight)) +
    geom_boxplot()+
    theme_light() + ggtitle("P1")

ChickWeight$Time <- factor(ChickWeight$Time)
p2<- ggplot(ChickWeight,aes(x=Time,y=weight)) +
    geom_boxplot()+
    theme_light() + ggtitle("P2")

ChickWeight$Diet <- factor(ChickWeight$Diet)

p3<- ggplot(ChickWeight,aes(x=Time,y=weight)) +
    geom_boxplot(aes(fill=Diet))+
    theme_light() + ggtitle("P3")


p4<- ggplot(ChickWeight,aes(x=Time,y=weight)) +
    geom_boxplot(aes(group=Diet, fill=Diet))+
    theme_light() + ggtitle("P4")

GGlay = 'ABBBB
CCCCD'

p1+p2+p3+p4 + plot_layout(design = GGlay)
##ggsave('box1.png')
```

![NgVfWn.md.png](https://s1.ax1x.com/2020/06/28/NgVfWn.md.png)

As you can see, we can separate the box by call the axis.x `Time` as factors (p2).

## Add smooth line

```r
ggplot(ChickWeight,aes(x=Time,y=weight)) +
        geom_boxplot(aes(fill=Diet),alpha=0.4)+
        theme_light() + ggtitle("P3")+ geom_smooth(aes(group=Diet),color='red')+
        facet_wrap(~Diet)
```
![NgesUg.md.png](https://s1.ax1x.com/2020/06/28/NgesUg.md.png)
