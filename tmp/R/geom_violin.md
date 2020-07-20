---
title: "geom_violin"
description: "geom_violin"
url: geom_violin2
---
# geom_violin


![img](https://i.loli.net/2020/06/19/hbiwR31SFt46a9p.png)<a name="wGube"></a>
# Quick Start

```r
library(ggplot2)

p <- ggplot(mtcars, aes(factor(cyl), mpg))
p + geom_violin()+ geom_point() + theme_light()
```

<a name="dw7gw"></a>
## scale
```r
p + geom_violin(scale = "width")+ theme_light()
```
![img](https://i.loli.net/2020/06/19/x92jqz1ATVBp4tr.png)

<a name="0p83A"></a>
## draw_quantiles
```r
p + geom_violin(aes(fill = factor(cyl)),draw_quantiles = c(0.25, 0.5, 0.75))
```
![img.png](https://i.loli.net/2020/06/19/UqEZPzBosrVmDNT.png)

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)


---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
