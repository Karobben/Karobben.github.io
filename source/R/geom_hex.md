---
title: "geom_hex"
description: "geom_hex"
url: geom_hex
---

# geom_hex

![NuJMHH.png](https://s1.ax1x.com/2020/06/19/NuJMHH.png)
<a name="mLOtK"></a>
# Quick Start

```r
library(ggthemes)
library(ggplot2)
library(patchwork)
world <- map_data("world")

ggplot(world, aes(long, lat)) + geom_hex() + theme_map()  
```

<a name="RkQ0F"></a>
# Arguments
<a name="OnBpv"></a>
## bins

```r
ggplot(world, aes(long, lat)) + geom_hex(bins = 40) + theme_map()
P1 <-ggplot(world, aes(long, lat)) + geom_hex(bins = 20) + theme_map() + ggtitle('bins=20')          
P2 <-ggplot(world, aes(long, lat)) + geom_hex(bins = 80) + theme_map() + ggtitle('bins=80')          

P1|P2

```
![NuJ1UA.png](https://s1.ax1x.com/2020/06/19/NuJ1UA.png)

<a name="DivLR"></a>
## binwidth

```r
ggplot(world, aes(long, lat)) + geom_hex(binwidth = c(1, 10)) + theme_map()
```
![NuJlEd.png](https://s1.ax1x.com/2020/06/19/NuJlEd.png)

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
