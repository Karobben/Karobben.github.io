---
title: "geom_violin| ggplot examples"
ytitle: "geom_violin | ggplot 小提琴圖"
description: "geom_violin"
url: geom_violin2
date: 2020/08/13
toc: true
excerpt: "R: ggplot, ggplot, Violin plot"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://s1.ax1x.com/2020/08/13/dShnG6.png'
thumbnail: 'https://s1.ax1x.com/2020/08/13/dShnG6.png'
priority: 10000
---


## Quick Start

```r
library(ggplot2)

p <- ggplot(mtcars, aes(factor(cyl), mpg))
p + geom_violin()+ geom_point() + theme_light()
```

<a name="dw7gw"></a>
### scale
```r
p + geom_violin(scale = "width")+ theme_light()
```
![img](https://s1.ax1x.com/2020/08/13/dShmPx.png)

<a name="0p83A"></a>
### draw_quantiles
```r
p + geom_violin(aes(fill = factor(cyl)),draw_quantiles = c(0.25, 0.5, 0.75))
```
![img.png](https://s1.ax1x.com/2020/08/13/dShZI1.png)

<a name="FG8Ad"></a>
