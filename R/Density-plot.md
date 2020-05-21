---
url: density_plot2
---

# Density plot

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580018385388-cbf761b1-dd32-41dc-b66c-bef05568a856.png#align=left&display=inline&height=469&name=image.png&originHeight=469&originWidth=730&size=94619&status=done&style=none&width=730)

<a name="XxQSp"></a>
# Quick start
<a name="fXzqq"></a>
## geom_density_2d
```r
library(ggplot2)

ggplot(world,aes(long, lat)) +geom_density_2d(color='red') + theme_light()
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580018504859-bb395bd4-87eb-4b97-955c-49409998ada3.png#align=left&display=inline&height=474&name=image.png&originHeight=474&originWidth=750&size=72932&status=done&style=none&width=750)<br />
<br />
<br />

<a name="tcYcw"></a>
## stat_density_2d
```r
ggplot(world,aes(long, lat)) + stat_density_2d(aes(fill = stat(level)), geom = "polygon") + theme_map()
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580018852015-7d07131f-f618-460d-a00e-fdc8ae2f89e5.png#align=left&display=inline&height=473&name=image.png&originHeight=473&originWidth=739&size=21923&status=done&style=none&width=739)<br />

```r
ggplot(world,aes(long, lat)) + stat_density_2d(aes(fill = stat(level),colour = region), geom = "polygon") + theme_map()+ theme(legend.position = 'none')
```

<br />
<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580020341585-cca27b54-dec8-4df6-a382-33d8a414a47a.png#align=left&display=inline&height=445&name=image.png&originHeight=445&originWidth=709&size=292493&status=done&style=none&width=709)<br />

<a name="OX1Ol"></a>
## geom_raster

```r
ggplot(faithfuld, aes(waiting, eruptions)) +
 geom_raster(aes(fill = density))+ theme_map()
```
![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580038000044-1955329a-6020-44eb-8581-670cc4ffe109.png#align=left&display=inline&height=320&name=image.png&originHeight=320&originWidth=471&size=14917&status=done&style=none&width=471)<br />
<br />

<a name="FG8Ad"></a>
# More
图片索引:[https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)



--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
