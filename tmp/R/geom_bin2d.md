---
title: "geom_bin2d"
description: "geom_bin2d"
url: geom_bin2d2
---
# geom_bin2d
![bin1](https://i.loli.net/2020/06/19/82lEc1uACRxOrGk.png)

<a name="4wGpq"></a>
# Quick Start
```r
library(ggplot2)
library(ggthemes)

world <- map_data("world")
ggplot(world, aes( long, lat)) +geom_bin2d()  + theme_map()
```

<a name="vmNgc"></a>
# Arguments
<a name="N6aE2"></a>
## bins
x=y=bins+1
```r
library(patchwork)

P1 <- ggplot(world, aes( long, lat)) +geom_bin2d(bins = 10)  + theme_map() +
			ggtitle('bins=10')+ theme(plot.title = element_text(hjust=0.5,size=20))
P2 <- ggplot(world, aes( long, lat)) +geom_bin2d(bins = 100)  + theme_map() +
			ggtitle('bins=100')+ theme(plot.title = element_text(hjust=0.5,size=20))

P1/P2
```

![Nu8yon.png](https://s1.ax1x.com/2020/06/19/Nu8yon.png)

<a name="pMKRk"></a>
## binwidth
```r
library(RColorBrewer)
colorRampPalette(rev(brewer.pal(n = 7,name = "RdYlBu"))) -> cc

P1 <- ggplot(world, aes( long, lat)) +geom_bin2d(binwidth = c(0.1, 0.1))+
		theme_map() +ggtitle('0.1 0.1')+ theme(plot.title = element_text(hjust=0.5,size=20))+
		scale_fill_gradientn(colors=cc(100))
P2 <- ggplot(world, aes( long, lat)) +geom_bin2d(binwidth = c(0.1, 10))+
		theme_map() +ggtitle('0.1 10')+ theme(plot.title = element_text(hjust=0.5,size=20))+
		scale_fill_gradientn(colors=cc(100))
P3 <- ggplot(world, aes( long, lat)) +geom_bin2d(binwidth = c(10, 0.1))+
		theme_map() +ggtitle('10 0.1')+ theme(plot.title = element_text(hjust=0.5,size=20))+
		scale_fill_gradientn(colors=cc(100))
P4 <- ggplot(world, aes( long, lat)) +geom_bin2d(binwidth = c(10, 10))+
		theme_map() +ggtitle('10 10')+ theme(plot.title = element_text(hjust=0.5,size=20))+
		scale_fill_gradientn(colors=cc(100))

(P1|P2)/(P4|P3)
```
![bin2](https://i.loli.net/2020/06/19/PR3sLuAMJ8HkFTN.png)


<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)




---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
