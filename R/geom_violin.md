---
url: geom_violin2
---
# geom_violin

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580050088677-c255a94b-5438-4d5d-951f-b0e9322a6970.png#align=left&display=inline&height=415&name=image.png&originHeight=415&originWidth=591&size=24972&status=done&style=none&width=591)
<a name="wGube"></a>
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
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580050217693-eee39f52-cdcc-472b-a8b5-d0b12e04e5ac.png#align=left&display=inline&height=357&name=image.png&originHeight=410&originWidth=590&size=23059&status=done&style=none&width=514)

<a name="0p83A"></a>
## draw_quantiles
```r
p + geom_violin(aes(fill = factor(cyl)),draw_quantiles = c(0.25, 0.5, 0.75))
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580050340691-cc8be8a1-32d1-490a-9775-b8d98fb36930.png#align=left&display=inline&height=410&name=image.png&originHeight=410&originWidth=585&size=23322&status=done&style=none&width=585)<br />
<br />

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)




--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
