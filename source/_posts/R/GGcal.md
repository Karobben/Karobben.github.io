---
title: "GGcal | ggplot for Calendar"
ytitle: "GGcal | 用ggplot畫日曆圖"
description: "GGcal"
url: ggcal2
date: 2020/06/19
toc: true
excerpt: "Calendar plot solution package for ggplot"
tags: [R, Plot, ggplot]
category: [R, Plot, GGPLOT]
cover: 'https://s1.ax1x.com/2020/06/19/Nuh2QK.png'
thumbnail: 'https://s1.ax1x.com/2020/06/19/Nuh2QK.png'
priority: 10000
---

## Quick start:
The graph show ahead. 
```r
library(ggplot2)
library(ggcal)

mydate <- seq(as.Date("2017-02-01"), as.Date("2017-07-22"), by="1 day")
myfills <- rnorm(length(mydate))

print(ggcal(mydate, myfills))
```

<a name="LOqVj"></a>
## Installation

```r
devtools::install_github("jayjacobs/ggcal")
```


<a name="favorite"></a>
## Favorite theme

```r
gg <- ggcal(mydate, myfills) +
scale_fill_gradient2(low="#4575b4", mid="#ffffbf", high="#d73027", midpoint=0)
print(gg)
```

![Nuhcz6.png](https://s1.ax1x.com/2020/06/19/Nuhcz6.png)

<a name="FG8Ad"></a>
## More
