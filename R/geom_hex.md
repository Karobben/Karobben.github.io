---
url: geom_hex
---

# geom_hex

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580024777965-fe6628cf-fae8-43d6-9b6b-43a7c3b64867.png#align=left&display=inline&height=484&name=image.png&originHeight=484&originWidth=852&size=38431&status=done&style=none&width=852)
<a name="mLOtK"></a>
# Quick Start

```r
library(ggthemes)
library(ggplot2)
library(patchwork)
world <- map_data("world")

ggplot(world, aes(long, lat)) + geom_hex() + theme_map()  
```

<a name="RkQ0F"></a>
# Arguments
<a name="OnBpv"></a>
## bins

```r
ggplot(world, aes(long, lat)) + geom_hex(bins = 40) + theme_map()
P1 <-ggplot(world, aes(long, lat)) + geom_hex(bins = 20) + theme_map() + ggtitle('bins=20')          
P2 <-ggplot(world, aes(long, lat)) + geom_hex(bins = 80) + theme_map() + ggtitle('bins=80')          

P1|P2

```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580024981619-ab7bac11-af18-4e70-a5b7-387780e96471.png#align=left&display=inline&height=289&name=image.png&originHeight=212&originWidth=548&size=33344&status=done&style=none&width=746)

<a name="DivLR"></a>
## binwidth

```r
ggplot(world, aes(long, lat)) + geom_hex(binwidth = c(1, 10)) + theme_map()
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580025154102-3ffaa678-310a-4c9c-891d-48b453473e9a.png#align=left&display=inline&height=427&name=image.png&originHeight=427&originWidth=656&size=36894&status=done&style=none&width=656)<br />
<br />

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
