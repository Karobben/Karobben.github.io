---
title: "geom_curve"
description: "geom_curve"
url: geom_curve2
---
# geom_curve

<a name="EsYEd"></a>
# Quick Start

```r
ggplot() + geom_curve( aes(x = 1, y = 1, xend= 6, yend = 6))
```
![NuGc0H.png](https://s1.ax1x.com/2020/06/19/NuGc0H.png)

`geom_segment` draws a straight line between points (x, y) and (xend, yend).
`geom_curve` draws a curved line.

<a name="Mqwv9"></a>
# Arguments
<a name="fneug"></a>
## ncp

```r
p <- ggplot()
for(i in c(1:10)){
	p <- p+ geom_curve( aes(x = 1, y = 1, xend= 6, yend = 6),ncp = i)
}
p+ theme_light()
```

![NuGg7d.png](https://s1.ax1x.com/2020/06/19/NuGg7d.png)


<a name="NaZpK"></a>
## curvature

```r
p <- ggplot()
for(i in c(-10:10)){
    p <- p+ geom_curve( aes(x = 1, y = 1, xend= 6, yend = 6), curvature = i*0.1)
}
p+ theme_light()+ expand_limits(x=c(0,10),y=c(0,6))
```
![NuGRAA.png](https://s1.ax1x.com/2020/06/19/NuGRAA.png)

<a name="WHHOW"></a>
## angle

```r
p <- ggplot()
for(i in c(1:9)){
    p <- p+ geom_curve( aes(x = 1, y = 1, xend= 6, yend = 6), angle = i*10)
}
p+ theme_light()+ expand_limits(x=c(0,10),y=c(0,6))
```

![NuGWtI.png](https://s1.ax1x.com/2020/06/19/NuGWtI.png)


<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
