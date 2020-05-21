---
url: geom_rect2
---
# geom_rect

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580038591063-d9ccb0dd-f5c4-4b56-88c9-38dd75cb2959.png#align=left&display=inline&height=317&name=image.png&originHeight=317&originWidth=355&size=5368&status=done&style=none&width=355)
<a name="Ktz7J"></a>
# Quick Start
```r
mydata <- data.frame(
  Lebal  = c("Point1","Point2","Point3","Point4","Point5"),
  xstart = c(5.5,15.7,19.5,37.2,36.9),
  xend   = c(9.7,28.1,24.6,44.6,47.1),
  ystart = c(9.6,23.1,2.3,33.2,9.2),
  yend   = c(16.1,36.2,11.7,38.5,15.3),
  size   = c(12,48,30,11.5,28),
  class  = c("A","A","A","C","C")
)

ggplot(mydata)+ geom_rect(aes(xmin = xstart,xmax = xend ,ymin = ystart ,
	ymax = yend , fill = class)) + scale_fill_wsj() + theme_map()
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580038623741-9c6222ad-6f00-456b-a601-97fe253b27d6.png#align=left&display=inline&height=354&name=image.png&originHeight=354&originWidth=469&size=4909&status=done&style=none&width=469)<br />
<br />

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)





--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
