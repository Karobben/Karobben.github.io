---
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
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580047681259-546fc510-6151-49b2-afde-90e798c20f6e.png#align=left&display=inline&height=361&name=image.png&originHeight=361&originWidth=688&size=14730&status=done&style=none&width=688)<br />
<br />

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)




--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
