---
title: "geom_tile"
description: "geom_tile"
url: geom_tile2
date: 2020/08/11
toc: true
excerpt: "R: ggplot, ggplot, geom_tile"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://s1.ax1x.com/2020/08/11/aXYd76.md.png'
thumbnail: 'https://s1.ax1x.com/2020/08/11/aXYd76.md.png'
priority: 10000
---

## Quick Start
```r
library(ggplot2)
df <- data.frame(
  x = rep(c(2, 5, 7, 9, 12), 2),
  y = rep(c(1, 2), each = 5),
  z = factor(rep(1:5, each = 2)),
  w = rep(diff(c(0, 4, 6, 8, 10, 14)), 2)
)

ggplot(df, aes(x, y)) + theme_light()+
  geom_tile(aes(fill = z), colour = "grey50")
```


```r
library(patchwork)

P1 <- ggplot(df, aes(x, y)) + theme_light()+ ggtitle('P1')+
  geom_tile(aes(fill = z), colour = "grey50")+
  theme(plot.title = element_text(hjust = 0.5))

P2 <- ggplot(df, aes(x, y, width = w)) + theme_light()+ ggtitle('P2')+
  theme(plot.title = element_text(hjust = 0.5))+
  geom_tile(aes(fill = z), colour = "grey50")

P3 <- ggplot(df, aes(x, y))+ geom_bar(aes(fill=z),stat='identity')+ theme_light()+
  ggtitle('bar plot')+ theme(plot.title = element_text(hjust = 0.5))

(P1|P2)/P3
```
![aXY0AK.md.png](https://s1.ax1x.com/2020/08/11/aXY0AK.md.png)

<a name="FG8Ad"></a>
## More
