---
title: "geom_segment"
description: "geom_segment"
url: geom_segment2
---
# geom_segment

![NuUOSI.png](https://s1.ax1x.com/2020/06/19/NuUOSI.png)

# Quick Start

```r
library(ggplot2)
library(ggtheme)

ggplot(seals, aes(long, lat)) + theme_map()
		geom_segment(aes(xend = long + delta_long, yend = lat + delta_lat),
    arrow = arrow(length = unit(0.1,"cm")))
```


<a name="L96t9"></a>
# length

```r
P1 <- ggplot(seals, aes(long, lat)) + theme_map()+ ggtitle('0.1')+
		geom_segment(aes(xend = long + delta_long, yend = lat + delta_lat),
    arrow = arrow(length = unit(0.1,"cm")))+
		theme(plot.title = element_text(hjust = 0.5))

P2 <- ggplot(seals, aes(long, lat)) + theme_map()+ ggtitle('0.3')+
    geom_segment(aes(xend = long + delta_long, yend = lat + delta_lat),
    arrow = arrow(length = unit(0.3,"cm")))+
		theme(plot.title = element_text(hjust = 0.5))

P1|P2
```
![NuUXlt.png](https://s1.ax1x.com/2020/06/19/NuUXlt.png)

<a name="odojW"></a>
# Bar

```r
counts <- as.data.frame(table(x = rpois(100,5)))
counts$x <- as.numeric(as.character(counts$x))

ggplot(counts, aes(x, Freq)) + theme_light()
  geom_segment(aes(xend = x, yend = 0), size = 10, lineend = "butt")
```
![NuUbYd.png](https://s1.ax1x.com/2020/06/19/NuUbYd.png)

<a name="jVgvF"></a>
# geom_spoke
<br />
```r
df <- expand.grid(x = 1:10, y=1:10)
df$angle <- runif(100, 0, 2*pi)
df$speed <- runif(100, 0, sqrt(0.1 * df$x))

ggplot(df, aes(x, y)) + geom_point() + theme_light()+
  geom_spoke(aes(angle = angle), radius = 0.5)
```
![NuUqfA.png](https://s1.ax1x.com/2020/06/19/NuUqfA.png)

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
