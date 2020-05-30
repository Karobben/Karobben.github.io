---
url: ggcal2
---

# GGcal

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579752304170-c61ee1c4-4fac-4dac-8419-7d18e45dac50.png#align=left&display=inline&height=491&name=image.png&originHeight=491&originWidth=834&size=20594&status=done&style=none&width=834)
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

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579752347484-ce2f1a96-b99a-44ab-81f8-83d9dfaf3e56.png#align=left&display=inline&height=484&name=image.png&originHeight=484&originWidth=834&size=20233&status=done&style=none&width=834)

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
