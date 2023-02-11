---
title: "geom_rangeframe"
description: "geom_rangeframe"
url: geom_rangeframe2
date: 2020/06/19
toc: true
excerpt: "R: ggplot, ggplot, rangeframe"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://s1.ax1x.com/2020/06/19/NuYfQf.png'
thumbnail: 'https://s1.ax1x.com/2020/06/19/NuYfQf.png'
priority: 10000
---
## geom_rangeframe


```r
library(ggthemes)
library(patchwork)
library(ggplot2)

P1 <- ggplot(mtcars,aes(wt,mpg))+ ggtitle('Has rangeframe')+
      geom_point()+geom_rangeframe()+theme_tufte()+ theme(plot.title=element_text(hjust=0.5))
P2 <- ggplot(mtcars,aes(wt,mpg))+ ggtitle('No rangeframe')+
      geom_point()+theme_tufte()+ theme(plot.title=element_text(hjust=0.5))
P1|P2
```
![NuYfQf.png](https://s1.ax1x.com/2020/06/19/NuYfQf.png)

<a name="FG8Ad"></a>
## More






