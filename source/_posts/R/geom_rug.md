---
title: "geom_rug"
description: "geom_rug"
url: geom_rug
date: 2020/06/19
toc: true
excerpt: "R: ggplot, ggplot, rug plot"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://s1.ax1x.com/2020/06/19/Nut491.png'
thumbnail: 'https://s1.ax1x.com/2020/06/19/Nut491.png'
priority: 10000
---

## geom_rug

## Quick Inst
```r
library(ggplot2)
library(patchworks)

ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") +
  geom_rug() + theme_light()
```

<a name="njg2Q"></a>
## arguments

<a name="wBLEt"></a>
### outside

```r
 ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
geom_rug( outside = TRUE)+ coord_cartesian(clip = "off")
```
![NutfhR.png](https://s1.ax1x.com/2020/06/19/NutfhR.png)
![NuUnJA.png](https://s1.ax1x.com/2020/06/19/NuUnJA.png)

<a name="eA81n"></a>
### side

```r
library(patchwork)
P1 <- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
    geom_rug( sides='t', color='red') + ggtitle('t') +theme(plot.title = element_text(hjust = 0.5))
P2 <- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
    geom_rug( sides='r', color='red') + ggtitle('r') +theme(plot.title = element_text(hjust = 0.5))
P3 <- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
    geom_rug( sides='b', color='red') + ggtitle('b') +theme(plot.title = element_text(hjust = 0.5))
P4 <- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
    geom_rug( sides='l', color='red') + ggtitle('l') +theme(plot.title = element_text(hjust = 0.5))

(P1|P2)/(P3|P4)
```
![NutWN9.png](https://s1.ax1x.com/2020/06/19/NutWN9.png)

<a name="154js"></a>
### length


```r
P1<- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
    geom_rug()+ ggtitle('NA') + theme(plot.title = element_text(hjust = 0.5))
P2<- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
    geom_rug( length = unit(0.5, "npc"))+ ggtitle('0.5') + theme(plot.title = element_text(hjust = 0.5))
P3<- ggplot(mtcars,aes(wt,mpg))+ geom_point( color="grey50") + theme_light()+
    geom_rug( length = unit(1, "npc"))+ ggtitle('1') + theme(plot.title = element_text(hjust = 0.5))

P1/(P2|P3)
```

![Nut51x.png](https://s1.ax1x.com/2020/06/19/Nut51x.png)
![NuUuRI.png](https://s1.ax1x.com/2020/06/19/NuUuRI.png)




