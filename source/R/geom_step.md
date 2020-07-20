---
title: "geom_step"
description: "geom_step"
url: geom_step2
---
# geom_step

<a name="HSJHQ"></a>
# Quick Start

```r
library(ggplot2)

d=data.frame(x=c(1,2,4,5,7,8,9), y=c(1,2,3,5,6,7,9))

ggplot() + theme_light()+ geom_step(data=d, mapping=aes(x=x, y=y)) +
geom_step(data=d, mapping=aes(x=x, y=y), direction="vh", linetype=3) +
geom_point(data=d, mapping=aes(x=x, y=y), color="red")
```
![Nuwmi4.png](https://s1.ax1x.com/2020/06/19/Nuwmi4.png)

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)




---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
