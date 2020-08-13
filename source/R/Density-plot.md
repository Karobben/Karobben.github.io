---
title: "Density plot"
description: "Density plot"
url: density_plot2
---

# Density plot


![den1](https://s1.ax1x.com/2020/08/13/dS50Ej.png)

<a name="XxQSp"></a>
# Quick start
<a name="fXzqq"></a>
## geom_density_2d
```r
library(ggplot2)
world <- map_data("world")
ggplot(world,aes(long, lat)) +geom_density_2d(color='red') + theme_light()
```
![den2](https://s1.ax1x.com/2020/08/13/dS5dbQ.png)


<a name="tcYcw"></a>
## stat_density_2d
```r
ggplot(world,aes(long, lat)) + stat_density_2d(aes(fill = stat(level)), geom = "polygon") + theme_map()
```
![123](https://s1.ax1x.com/2020/08/13/dS5aDg.png)

```r
ggplot(world,aes(long, lat)) + stat_density_2d(aes(fill = stat(level),colour = region), geom = "polygon") + theme_map()+ theme(legend.position = 'none')
```
![den4](https://s1.ax1x.com/2020/08/13/dS5BUs.png)

<a name="OX1Ol"></a>
## geom_raster

```r
ggplot(faithfuld, aes(waiting, eruptions)) +
 geom_raster(aes(fill = density))+ theme_map()
```
![den5](https://s1.ax1x.com/2020/08/13/dS5UKS.png)

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)



---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
