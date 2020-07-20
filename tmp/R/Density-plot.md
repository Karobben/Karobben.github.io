---
title: "Density plot"
description: "Density plot"
url: density_plot2
---

# Density plot


![den1](https://i.loli.net/2020/06/19/rOxBlm9cqaRzpwu.png)

<a name="XxQSp"></a>
# Quick start
<a name="fXzqq"></a>
## geom_density_2d
```r
library(ggplot2)
world <- map_data("world")
ggplot(world,aes(long, lat)) +geom_density_2d(color='red') + theme_light()
```
![den2](https://i.loli.net/2020/06/19/cyRwGV41PEIQWxz.png)


<a name="tcYcw"></a>
## stat_density_2d
```r
ggplot(world,aes(long, lat)) + stat_density_2d(aes(fill = stat(level)), geom = "polygon") + theme_map()
```
![123](https://i.loli.net/2020/06/19/quDabenCps8B4hj.png)

```r
ggplot(world,aes(long, lat)) + stat_density_2d(aes(fill = stat(level),colour = region), geom = "polygon") + theme_map()+ theme(legend.position = 'none')
```
![den4](https://i.loli.net/2020/06/19/k79MqaCDOlSUmwv.png)

<a name="OX1Ol"></a>
## geom_raster

```r
ggplot(faithfuld, aes(waiting, eruptions)) +
 geom_raster(aes(fill = density))+ theme_map()
```
![den5](https://i.loli.net/2020/06/19/xLcKEaleb6kofmq.png)

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)



---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
