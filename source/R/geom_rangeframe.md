---
title: "geom_rangeframe"
description: "geom_rangeframe"
url: geom_rangeframe2
---
# geom_rangeframe


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
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
