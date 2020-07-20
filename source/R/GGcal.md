---
title: "GGcal"
description: "GGcal"
url: ggcal2
---

# GGcal

![Nuh2QK.png](https://s1.ax1x.com/2020/06/19/Nuh2QK.png)


<a name="gCUUE"></a>
# Quick start:
The graph show ahead. 
```r
library(ggplot2)
library(ggcal)

mydate <- seq(as.Date("2017-02-01"), as.Date("2017-07-22"), by="1 day")
myfills <- rnorm(length(mydate))

print(ggcal(mydate, myfills))
```

<a name="LOqVj"></a>
# Installation

```r
devtools::install_github("jayjacobs/ggcal")
```


<a name="favorite"></a>
# Favorite theme

```r
gg <- ggcal(mydate, myfills) +
scale_fill_gradient2(low="#4575b4", mid="#ffffbf", high="#d73027", midpoint=0)
print(gg)
```

![Nuhcz6.png](https://s1.ax1x.com/2020/06/19/Nuhcz6.png)

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
